# %%
from ultralytics import YOLO
import numpy as np
import cv2
from datetime import datetime
import os
import csv



model_det = YOLO(r'runs\detect\train11\weights\best.pt')
# %%
def pass_to_csv(labels):


    headers = list(set([0,1,2]))
    data = []

    for row_index in range(len(labels)):
        row_data = [1 if i in labels else 0 for i in headers]
        data.append(row_data)
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        writer.writerows(data)
                

# %%

def trayclf():
    cap = cv2.VideoCapture(0)
    while True:

        ret, frame = cap.read()
        
        results1 = model_det(frame)
        for data in results1[0].boxes.data.tolist():
            xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            cv2.rectangle(frame, (xmin, ymin) , (xmax, ymax), (0,255,0), 2)
        pred_labels = results1[0].boxes.cls.data.tolist()
        cv2.imshow("Image Classification", frame)
        if (cv2.waitKey(1) & 0xFF == ord('p')):
            if any((0 == sublist) or(1 == sublist) or (2 == sublist) for sublist in pred_labels):
                cv2.putText(frame,'transfered_to_csv', (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                pass_to_csv(sorted(set(pred_labels)))

 
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()
    return
trayclf()


