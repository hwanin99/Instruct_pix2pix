#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import hashlib
import os
import requests

def download_model(model_name, filename, file_url, file_md5):
#     print(f"Downloading the sketch simplification {model_name} model...")
    print("Downloading the sketch simplification {} model...".format(model_name))


    # 파일 다운로드
    response = requests.get(file_url, stream=True)
    response.raise_for_status()  # 다운로드가 실패한 경우 예외 발생

    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192): 
            file.write(chunk)

    # MD5 체크섬 확인
    print("Checking integrity (md5sum)...")
    checksum = calculate_md5(filename)

    if checksum != file_md5:
        print("failed")
        print("Integrity check failed. File is corrupt!")
#         print(f"Try running this script again and if it fails remove '{filename}' before trying again.")
        print("Try running this script again and if it fails remove '{}' before trying again.".format(filename))
        raise ValueError("File integrity check failed.")

    print("ok")

def calculate_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# 모델 다운로드
def select_model (model_name):
    if model_name == 'MSE':
        download_model("MSE", "model_mse.t7", "https://esslab.jp/~ess/data/sketch_mse.t7", "12317df9a0a2a7220629f5f361b45b82")
    elif model_name == 'GAN':
        download_model("GAN", "model_gan.t7", "https://esslab.jp/~ess/data/sketch_gan.t7", "3a5b4088f2490ca4b8140a374e80c878")
    elif model_name == 'PENCIL(1)':
        download_model("PENCIL(1)", "model_pencil1.t7", "https://esslab.jp/~ess/data/pencil_artist1.t7", "33d553ff3a50d6522e79a73002b0025c")
    elif model_name == 'PENCIL(2)':
        download_model("PENCIL(2)", "model_pencil2.t7", "https://esslab.jp/~ess/data/pencil_artist2.t7", "537b3ad9d46b2a82b65883be747a7ba9")

    print("Downloads finished successfully!")

