
from ultralytics import YOLO
import cv2




model_det = YOLO(r'runs\detect\train11\weights\best.pt')


yolo_result_list = []

def trayclf():
        try:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            results1 = model_det(frame,verbose = False)
            pred_labels = []
            for data in results1[0].boxes.data.tolist():
                xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
                cv2.rectangle(frame, (xmin, ymin) , (xmax, ymax), (0,255,0), 2)
                pred_labels.append(results1[0].boxes.cls.data.tolist())


            return [frame,pred_labels]
        except Exception as e:
            print(f"An exception occurred: {e}")
        cap.release()
        cv2.destroyAllWindows()
        raise 



