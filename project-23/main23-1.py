# 사진 속에서 얼굴 찾기
import numpy as np
import cv2

#얼굴과 눈을 찾기 위한 OpenCV 알고리즘 적용된 파일 불러오기
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_casecade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# numpy로 불러오는 이유는 한글경로의 파일을 읽기 위해서라고 함. 난 영어 경로인디
ff=np.fromfile(r'project-23\sample_img.jpg',np.uint8)
# imdecode하여 numpy의 이미지 파일을 OpenCV 이미지로 불러온다
# IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽음
img=cv2.imdecode(ff,cv2.IMREAD_UNCHANGED)
# 이미지의 크기 조절. fx, fy의 비율로 조절할 수 있음. 코드에서는 원래의 비율을 사용
img=cv2.resize(img,dsize=(0,0),fx=1.0,fy=1.0,interpolation=cv2.INTER_LINEAR)

# 이미지에서 얼굴을 찾기 위해 회색조 처리
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 여러개의 얼굴을 찾기. 
# 1.2 = ScaleFactor
# 5 = minNeighbot 
#얼굴 찾아서 파란색 네모 표시
faces=face_cascade.detectMultiScale(gray,1.2,5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h),(255,0,0),2)
    
    roi_gray=gray[y:y+h,x:x+w]
    roi_color=img[y:y+h,x:x+w]
    eyes=eye_casecade.detectMultiScale(roi_gray)
    
    #눈을 찾아서 녹색 네모 표시
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        
cv2.imshow('face find',img)
cv2.waitKey(0)
cv2.destroyWindow()