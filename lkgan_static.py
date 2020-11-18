import os
import time
import tensorflow as tf
from tensorflow.keras.initializers import RandomNormal
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, \
    LeakyReLU, Conv2DTranspose, Conv2D, Dropout, Flatten, Reshape
import scipy as sp
import numpy as np

from LkGAN import LkGAN

k, version, trial_number, seed_num = 1, 1, 1, 1
if int(version) == 1:
    alpha = 0.6
    beta = 0.4
elif int(version) == 2:
    alpha = 1
    beta = 0
else:
    alpha = 0
    beta = 1
if int(version) == 3:
    gamma = 1
else:
    gamma = (alpha + beta)/2.0
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
np.random.seed(int(seed_num))
tf.random.set_random_seed(int(seed_num))

model = LkGAN(round(float(k), 1), int(version), int(alpha), int(beta), int(gamma), int(trial_number))
model.build()
model.train(n_epochs=100)
