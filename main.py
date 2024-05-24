import cv2  ## open cv
import os   ## help with file paths - accessing them
import time ## helper for sign langueg - used to manage time taken to move the hand - to get proper angles
import uuid ## for naming image files -> unique name

print("Hi testing")

IMAGES_PATH = "Tensorflow\workspace\images\collectedImages"

labels = ["hello", "thankyou", "yes", "no", "iloveyou"]   ## only these five gesturs to be detected
no_imgs = 15

## getting the images
for label in labels:
    ## creating directory for each labels
    label_dir = "Tensorflow/workspace/images/collectedImages/" + label
    os.makedirs(label_dir, exist_ok=True)

    capture = cv2.VideoCapture(0)   ## start video capture
    print("Collecting images for {}".format(label))

    time.sleep(5)   ## 5sec sleep - time to position oneself to capture the gsters

    for imgNo in range(no_imgs):
        ret, frame= capture.read()  ## setting up capture
        imgName = os.path.join(IMAGES_PATH, label, label+"."+"{}.jpg".format(str(uuid.uuid1())))  ## image name each image captured
        cv2.imwrite(imgName, frame) ## to write in directory
        cv2.imshow("Frame", frame)  ## to show on screen
        time.sleep(2)

        ## 'q' keystroke to stop the video
        if cv2.waitKey(1) & 0xff == ord("q"):
            break

    capture.release()