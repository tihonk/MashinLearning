import cv2 as cv
from time import sleep

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

from scit import threshold, whatNumIsThis


def saveAssociation(img_count, action):
    numberArrayExamples = open('data.txt', 'a')
    imgFilePath = 'mediaFiles/view/' + str(img_count-1) + '.png'
    img = Image.open(imgFilePath)
    new_image = img.resize((8, 8))
    img_array = np.array(new_image)
    b_w_img_array = threshold(img_array)
    lineToWrite = action.lower() + '::' + str(b_w_img_array.tolist()) + '\n'
    numberArrayExamples.write(lineToWrite)
    fig = plt.figure()
    ax = plt.subplot2grid((8, 6), (0, 0), rowspan=4, colspan=3)
    ax.title.set_text(action)
    ax.imshow(b_w_img_array)
    plt.show()


def getAssociation(img_count):
    imgFilePath = 'mediaFiles/view/' + str(img_count - 1) + '.png'
    img = Image.open(imgFilePath)
    new_image = img.resize((8, 8))
    img_array = np.array(new_image)
    b_w_img_array = threshold(img_array)
    whatNumIsThis(b_w_img_array)
    pass


class View:

    makePhoto = False
    img_counter = 0

    def startView(self=None):
        capture = cv.VideoCapture(0)
        capture.set(cv.CAP_PROP_FRAME_WIDTH, 140)
        capture.set(cv.CAP_PROP_FRAME_HEIGHT, 180)
        while True:
            ret, frame = capture.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            (thresh, blackAndWhiteImage) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
            cv.imshow('frame', blackAndWhiteImage)
            if cv.waitKey(1) == ord('q'):
                break

            if View.makePhoto:
                View.makePhoto = False
                img_name = "mediaFiles/view/{}.png".format(View.img_counter)
                cv.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                View.img_counter += 1
        capture.release()
        cv.destroyAllWindows()

    @classmethod
    def saveAction(cls, action):
        img_count = View.img_counter + 1
        View.makePhoto = True
        sleep(0.33)
        saveAssociation(img_count, action)

    @classmethod
    def determinateView(cls):
        img_count = View.img_counter + 1
        View.makePhoto = True
        sleep(0.33)
        getAssociation(img_count)
