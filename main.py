import os
from threading import Thread

import cv2 as cv

import numpy as np
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf


from hormones.serotonin import Serotonin
from view.View import View


def kissOrKick():
    action = input("")
    Serotonin.levelUp(1)
    if action != '':
        View.saveAction(action)
    else:
        View.determinateView()
    kissOrKick()


if __name__ == '__main__':
    print("Sigma started work")
    thread = Thread(target=Serotonin.selfControl, args=(0.001,))
    thread.start()
    thread1 = Thread(target=View.startView)
    thread1.start()
    thread = Thread(target=kissOrKick())
    thread.start()


    # train = ImageDataGenerator(rescale=1/255)
    # validation = ImageDataGenerator(rescale=1/255)
    # train_dataset = train.flow_from_directory('mediaFiles',
    #                                           target_size=(200, 200),
    #                                           batch_size=3,
    #                                           class_mode='binary')
    #
    # validation_dataset = train.flow_from_directory('validationMediaFiles',
    #                                           target_size=(200, 200),
    #                                           batch_size=3,
    #                                           class_mode='binary')
    # model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(200, 200, 3)),
    #                                     tf.keras.layers.MaxPool2D(2, 2),
    #                                     tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    #                                     tf.keras.layers.MaxPool2D(2, 2),
    #                                     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    #                                     tf.keras.layers.MaxPool2D(2, 2),
    #                                     tf.keras.layers.Flatten(),
    #                                     tf.keras.layers.Dense(512, activation='relu'),
    #                                     tf.keras.layers.Dense(1, activation='sigmoid')
    #                                     ])
    #
    # model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.RMSprop(lr=0.001), metrics=['accuracy'])
    # model_fit = model.fit(train_dataset, steps_per_epoch=3, epochs=10, validation_data=validation_dataset)
    #
    # dir_path = 'test'
    # for i in os.listdir(dir_path):
    #     img = image.load_img(dir_path + '//' + i, target_size=(200, 200))
    #     X = image.img_to_array(img)
    #     X = np.expand_dims(X, axis=0)
    #     images = np.vstack([X])
    #     val = model.predict(images)
    #     if val == 0:
    #         print('It\'s a cat' + i)
    #     else:
    #         print('It\'s a dog: ' + i)









