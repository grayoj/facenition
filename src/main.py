# Gerald Maduabuchi, 2023

# Import Open CV module.
import cv2

# Define cascade classifer variable.
cascade_image = cv2.CascadeClassifier(
    '/Users/gerald/documents/facenition/src/cascade/haarcascade_frontalface_default.xml')

# Return video from the first webcam on your computer.
capture = cv2.VideoCapture(0)

# Function to execute recognition
while True:
    ret, img = capture.read()
    print(ret)
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detects objects in the input image
    f = cascade_image.detectMultiScale(g, 1.3, 5)

    for (x, y, w, h) in f:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 225), 4)

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff

        if k == 27:
            break

        capture.release()
        # Close any gui windows
        cv2.destroyAllWindows()
