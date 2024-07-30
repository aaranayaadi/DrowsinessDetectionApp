#These are the important lines of codes from DrowsinessDetector.ipynb file. I have provided this file to provide faster
#access to the code. Please do not run this file directly. Copy blocks of codes in separate cells in a jupyter notebook
#to run this model.

pip install torch torchvision torchaudio

!git clone https://github.com/ultralytics/yolov5

!cd yolov5 & pip install -r requirements.txt

import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

"""2. Loading model"""

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

model

"""3. Training from Scratch"""

import uuid #unique identifier
import os
import time

IMAGES_PATH = os.path.join('data', 'images')
labels = ['awake', 'drowsy']
number_imgs = 20

for label in labels:
    print(label)

cap = cv2.VideoCapture(0)
#Loop through labels
for label in labels:
    print('Collecting images for {}'.format(labels))
    time.sleep(5)

    #loop through number of images
    for img_num in range(number_imgs):
        print('Collecting images for {}, image number {}'.format(label, img_num))

        #webcam feed
        ret, frame = cap.read()

        #Naming the image path
        img_name = os.path.join(IMAGES_PATH, label + '.' + str(uuid.uuid1())+'.jpg')

        #writes out image to file
        cv2.imwrite(img_name, frame)

        #Render to the screen
        cv2.imshow('Image Collection', frame)

        #2 second delay between captures
        time.sleep(2)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

!git clone https://github.com/HumanSignal/labelImg

!pip install pyqt5 lxml --upgrade
!cd labelImg && pyrcc5 -o libs/resources.py resources.qrc

!cd yolov5 && python train.py --img 320 --batch 16 --epochs 420 --data dataset.yaml --weights yolov5s.pt

"""4. Loading Models"""

model = torch.hub.load('ultralytics/yolov5', 'custom', path = 'yolov5/runs/train/exp3/weights/best.pt', force_reload=True)


# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.imshow(np.squeeze(results.render()))
plt.show()

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    results = model(frame)
    cv2.imshow('YOLO', np.squeeze(results.render()))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

