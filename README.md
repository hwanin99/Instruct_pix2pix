# <p align = "center">Instruct Pix2Pix </p>  
<p align = "center"><img src="https://github.com/user-attachments/assets/0b203565-369f-40e5-9487-57dc2e253b42" width="900" height="220"></p>

> 1. RGB 이미지를 스케치 형태의 이미지로 변환  
> (1) CV2를 사용해 이미지를 RGB -> Gray로 변환  
> (2) 저장된 Gray 이미지를 Gaussian Blur를 통해 Sketch 이미지로 변환 후 저장  
> (3) Gausssian Blur로 만들어진 Sketch 이미지를 GAN을 통해 더욱 깔끔한 스케치 형태로 변환 후 저장

> 2. RGB 이미지에서 caption을 생성  
> (1) CLIP + BLIP으로 이미지에 대한 caption을 생성  
> (2) ChatGPT를 사용해 생성된 caption을 정제

> * Dataset{1번: Original Image, 2번: Edit Prompt, RGB 이미지: Edited Image}
---
## <p align = "center">Result </p>  
<p align = "center"><img src="https://github.com/user-attachments/assets/997101c4-a6ff-4004-b17d-85bab10e96e4" width="800" height="260"></p>
