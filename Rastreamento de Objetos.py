import cv2

'''
NOTA:
A biblioteca opencv-python não possui o atributo TrackerCSRT_create, portanto, é necessário desinstalar
e instalar a biblioteca opencv-contrib-python
'''

cap = cv2.VideoCapture(0)

tracker = cv2.TrackerCSRT_create()

success, img = cap.read()
bbox = cv2.selectROI("Seguindo", img, False)
tracker.init(img,bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x,y), ((x+w), (y+h)), (255,0,0),3, 1)
    cv2.putText(img, "Seguindo", (75,75), cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255), 1)
    
    
while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    
    success, bbox = tracker.update(img)
    
    
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Perdeu o rastro", (75,75), cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255), 1)
        
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)), (75,50), cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255), 1)
    cv2.imshow("Seguindo", img)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
