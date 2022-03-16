from functools import reduce

import numpy as np
from PIL import Image
from collections import Counter

def createExamples():
    numberArrayExamples = open('data.txt', 'a')
    numbersWeHave = range(0, 2)
    versionsWeHave = range(0, 3)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            print(str(eachNum) + '.' + str(eachVer))
            imgFilePath = 'mediaFiles/pixels/' + str(eachNum) + '.' + str(eachVer) + '.png'
            img = Image.open(imgFilePath)
            img_array = np.array(img)
            string_array = str(img_array.tolist())

            lineToWrite = str(eachNum)+'::'+string_array+'\n'
            numberArrayExamples.write(lineToWrite)


def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRaw in imageArray:
        for eachPix in eachRaw:
            avgNum = reduce(lambda x, y: x + y, eachPix[:3]/len(eachPix[:3]))
            balanceAr.append(avgNum)
    balance = reduce(lambda x, y: x + y, balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3]/len(eachPix[:3])) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
    return newAr


def whatNumIsThis(img_array):
    matchedArray = []
    loadExamples = open('data.txt', 'r').read()
    loadExamples = loadExamples.split('\n')
    img_array_list = img_array.tolist()

    inQuestion = str(img_array_list)
    for eachExample in loadExamples:
        if len(eachExample) > 3:
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentArr = splitEx[1]
            eachPixEx = currentArr.split('],')
            eachPixInQ = inQuestion.split('],')
            x = 0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedArray.append(int(currentNum))
                x += 1

    x = Counter(matchedArray)
    print([(i, x[i] / len(matchedArray) * 100.0) for i in x])

if __name__ == '__main__':
    # whatNumIsThis('mediaFiles/test1.png')
    createExamples()
