import cv2
import os

def detectFace(img,name):
    gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray_image,1.4)#could be 1.5. Depend on images

    for(x,y,w,h) in faces:
        center = (x+w//2,y+h//2)
        gray_image = cv2.ellipse(gray_image,center,(w//2,h//2),0,0,360,(255,255,255),4)
        img = cv2.circle(img,center,w//2,(255,0,255),4)

    cv2.imshow(name,img)
    return img

if not os.path.exists("new_folder"):
    os.makedirs("new_folder")

for filename in os.listdir("."):
    if (filename.endswith(".jpg")) or (filename.endswith(".png")):
        print(filename)

        im = cv2.imread(filename)
        new_im = detectFace(im,filename)
        cv2.imwrite(os.path.join("new_folder","New"+filename),new_im)


cv2.waitKey(0)
cv2.destroyAllWindows()

