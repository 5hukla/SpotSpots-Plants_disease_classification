import cv2
import os
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm
import pickle
import random


# preparing training model
DATADIR = "./Data"

CATEGORIES = ["Black spot", "Healthy"]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        """plt.imshow(img_array, cmap='gray')
        plt.show()"""
        break
    break

IMG_SIZE = 256

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
"""plt.imshow(new_array, cmap='gray')
plt.show()"""

training_data = []


def create_training_data():
    for category in CATEGORIES:

        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)

        for img in tqdm(os.listdir(path)):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass


create_training_data()

print(len(training_data))

random.shuffle(training_data)

'''for sample in training_data[:10]:
    print(sample[1])'''

X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)

"print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))"

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()