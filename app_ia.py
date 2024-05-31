import cv2

# Upload image
image = cv2.imread('assets/1.jpg')

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# detection face in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30,30))

# draw rectangles around the detected faces
for (x, y, w, h) in faces:
    face = image[y:y+h, x:x+w]
    blurred_face = cv2.resize(cv2.resize(face,(w//10, h//10)), (w,h))
    image[y:y+h, x:x+w] = blurred_face
    
# show the image with the detected faces
cv2.imshow('Faces detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()