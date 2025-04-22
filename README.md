# <p align = "center">Instruct Pix2Pix </p>  
<p align = "center"><img src="https://github.com/user-attachments/assets/22ad3d24-4591-49da-8140-c5f5b54e122b" width="700" height="350"></p>

> 1. RGB 이미지를 스케치 형태의 이미지로 변환  
> (1) CV2를 사용해 이미지를 RGB -> Gray로 변환  
> (2) 저장된 Gray 이미지를 Gaussian Blur를 통해 Sketch 이미지로 변환 후 저장  
> (3) Gausssian Blur로 만들어진 Sketch 이미지를 GAN을 통해 더욱 깔끔한 스케치 형태로 변환 후 저장

> 2. RGB 이미지에서 caption을 생성  
> (1) CLIP + BLIP으로 이미지에 대한 caption을 생성  
> (2) ChatGPT를 사용해 생성된 caption을 정제
---
<p align = "center"><img src="https://github.com/user-attachments/assets/02677b1b-9ef9-41b0-84c4-31e1277d958a" width="800" height="260"></p>

> * 1번과 2번으로 만들어진 결과를 아래와 같이 Instruct Pix2Pix에 들어갈 데이터셋으로 구성
>   * Dataset{1번: Original Image, 2번: Edit Prompt, RGB 이미지: Edited Image}
---
# <p align = "center">Result </p>  
<p align = "center"><img src="https://github.com/user-attachments/assets/d13a036d-9eda-41d0-8427-2bf56c9d52c5" width="800" height="260"></p>
