#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import time
import json
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from PIL import Image
from IPython.display import clear_output, display

import torch
import torchfile
from torchvision import transforms
from torchvision.utils import save_image
from torch.utils.serialization import load_lua

from PIL import Image
import argparse
import cv2


# In[ ]:


def make_gray_img(img_paths):
    # Output 디렉토리 만들기
    if not os.path.exists('./gray'):  # 디렉토리가 없으면
        os.makedirs('./gray')
        print('Successfully created the gray directory.')
    else:
        print('The gray directory already exists.') # 디렉토리가 있으면
    
    # img_paths가 단일 경로(str)인 경우
    if isinstance(img_paths, str):
        img_paths = [img_paths]  # 단일 경로를 리스트로 변환
        
    img_paths = [img_path.replace('\\', '/') for img_path in img_paths]  # 슬래시 통일
    img_paths = sorted(img_paths, key=lambda x: int(x.split('/')[-1].split('.')[0]))  # 이미지 경로/{index}.jpg인 경우 정렬
    for img_path in img_paths:
        name = img_path.split('/')[-1].split('.')[0] # 이미지 경로/{이름}.jpg인 경우에 이름만 출력
        img = cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
        if img is None:
            print("Error: {} not found.".format(img_path))

        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(gray_image)
        img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
        final_img = cv2.divide(gray_image, 255 - img_smoothing, scale=256)
        
        if os.path.exists('./gray/{}.jpg'.format(name)):  # gray 디렉토리에 이미지가 이미 존재하면 저장안함.
            print("{}.jpg is alreay exists.".format(name))
        else:
            cv2.imwrite('./gray/{}.jpg'.format(name), final_img)
            print("Saved image to: ./gray/{}.jpg".format(name)) 

    return final_img


# In[ ]:


def make_pencil_img(gray_img_paths,model):
    use_cuda = torch.cuda.device_count() > 0
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    cache  = load_lua(model,long_size=8)
    # cache = torchfile.load('./model_gan.t7')
    model  = cache.model
    immean = cache.mean
    imstd  = cache.std
    model.evaluate()
    
    # Ouput 디렉토리 만들기
    if not os.path.exists('./sketch'):  # 디렉토리가 없으면
        os.makedirs('./sketch')
        print('Successfully created the sketch directory.')
    else: # 디렉토리가 있으면
        print('The sketch directory already exists.')
        
    # gray_img_paths가 단일 경로(str)인 경우
    if isinstance(gray_img_paths, str):
        gray_img_paths = [gray_img_paths]  # 단일 경로를 리스트로 변환
    
    gray_img_paths = [gray_img_path.replace('\\', '/') for gray_img_path in gray_img_paths]  # 슬래시 통일    
    gray_img_paths = sorted(gray_img_paths, key=lambda x: int(x.split('/')[-1].split('.')[0]))  # 파일명 기준 정렬
    for gray_img_path in gray_img_paths:
        gray_img_path = gray_img_path.replace('\\','/')
        name = gray_img_path.split('/')[-1].split('.')[0]
        data = Image.open(gray_img_path).convert('L')

        w, h = data.size[0], data.size[1]
        pw = 8-(w%8) if w%8!=0 else 0
        ph = 8-(h%8) if h%8!=0 else 0

        print('start unsqueeze()')

        data = ((transforms.ToTensor()(data)-immean)/imstd).unsqueeze(0)
        if pw != 0 or ph != 0:
            data = torch.nn.ReplicationPad2d( (0,pw,0,ph) )( data ).data

        print('start ReplicationPad2d()')
        if use_cuda:
            print(' use cuda')
            pred = model.cuda().forward(data.cuda()).float()
        else:
            print('don\'t use cuda')
            pred = model.forward(data)
        
        if os.path.exists('./sketch/{}.jpg'.format(name)):
            print("{}.jpg is alreay exists.".format(name))
        else:
            save_image(pred[0], './sketch/{}.jpg'.format(name))
            print("Saved image to: ./sketch/{}.jpg".format(name)) 

