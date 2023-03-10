from flask import request
import cv2
import os

def resized_image(path):
    if request.method == 'POST':
        img = cv2.imread(path ,cv2.IMREAD_GRAYSCALE)  
        resized_img = cv2.resize(img, (200, 200))
        cv2.imwrite(r'static\uploads\1.jpg', resized_img) 
        return 
    return ''

def resize(path):
    img=cv2.imread(path)
    #reading test image
    #img = cv2.imread("p 159.jpg") #image name

    #reading label name from obj.names file
    with open(os.path.join(r"C:\Users\Ahmed\Downloads\New folder (10)\pothole-detection-main\project_files",'obj.names'), 'r') as f:
        classes = f.read().splitlines()

    #importing model weights and config file
    net = cv2.dnn.readNet(r'C:\\Users\\Ahmed\\Downloads\\New folder (10)\\pothole-detection-main\\project_files\\yolov4_tiny.weights', r'C:\Users\Ahmed\Downloads\New folder (10)\pothole-detection-main\project_files\yolov4_tiny.cfg')
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
    classIds, scores, boxes = model.detect(img, confThreshold=0.1, nmsThreshold=0.1)

    count=0
    #detection 
    for (classId, score, box) in zip(classIds, scores, boxes):
        cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),color=(0,255,0), thickness=2)
        cv2.putText(img, "%" + str(round(scores[0]*100,2)) + " " + "pothole", (box[0], box[1]-10),cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
        count+=1
        
        
    print(f"number of potholes = {count}")

    number_of_potholes = count

    #cv2.imshow("pothole",img)
    cv2.imwrite(r'static\uploads\2.jpg',img) #result name
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return number_of_potholes