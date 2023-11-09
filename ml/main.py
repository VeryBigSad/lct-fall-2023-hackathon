import os
import cv2
import random
import torch
from torch import nn
import torchvision
import torchvision.transforms as transforms
import json
from ultralytics import YOLO
from PIL import Image
import tqdm
from catboost import CatBoostRegressor
import pandas as pd
from transformers import ViTImageProcessor, ViTForImageClassification
import matplotlib.pyplot as plt

device = 'cuda' if torch.cuda.is_available() else 'cpu'


class WeaponDetectModel():
    def __init__(self, model_people, model_vit, processor_vit, model_cb):
        self.model_people = model_people
        self.model_vit = model_vit
        self.model_cb = model_cb
        self.processor = processor_vit

    def predict_frame(self, frame, treshold=0.75):
        results = self.model_people(frame, show_conf=True)
        for i in range(len(results)):
            if (results[i].boxes.cls.cpu().size()[0] != 0):
                x1, y1, x2, y2 = results[i].boxes.xyxy[0]
                image = results[i].orig_img
                image_pers = Image.fromarray(image)
                person_image = image_pers.crop((x1.item(), y1.item(), x2.item(), y2.item()))
                # plt.imshow(person_image)

                inputs = self.processor(images=person_image, return_tensors="pt").to(device)
                outputs = self.model_vit(**inputs)
                pred = self.model_cb.predict(outputs.logits.cpu().detach().numpy())

                if pred > treshold:
                    print(pred)
                    label = f'{round(float(pred), 2)} human_with_weapon'
                    color = (0, 0, 255)
                else:
                    label = f'{round(float(1 - pred), 2)} human'
                    color = (255, 0, 0)

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color,
                              3)  # (0, 255, 0) - цвет прямоугольника (здесь зеленый), 2 - толщина линии
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, label, (int(x1), int(y1) - 10), font, 1.5, color, 2,
                            cv2.LINE_AA)  # (x1, y1 - 10) - координаты для текста, (0, 255, 0) - цвет текста
        return frame

    def predict_video(self, video_path, output_path="results/out_video.avi", fps=30, treshold=0.75):

        cap = cv2.VideoCapture(video_path)

        frame_width = int(cap.get(3))  # Ширина кадра, берем из исходного видео
        frame_height = int(cap.get(4))  # Высота кадра, берем из исходного видео

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

        # Loop through the video frames
        while cap.isOpened():
            # Read a frame from the video
            success, frame = cap.read()
            if success:
                frame = self.predict_frame(frame, treshold=treshold)
                out.write(frame)
            else:
                break

        cap.release()
        out.release()


model_people = YOLO("weights/best_yolo_people.pt")
model_vit = ViTForImageClassification.from_pretrained("weights/model_vit", ignore_mismatched_sizes=True)
processor_vit = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224')
model_cb = CatBoostRegressor()
model_cb.load_model("weights/cb_v1")

model = WeaponDetectModel(model_people, model_vit, processor_vit, model_cb)


