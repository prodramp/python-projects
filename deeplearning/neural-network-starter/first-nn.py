## Create 
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
input = Input(shape=(512,512,1))
layer1 = Dense(10, use_bias=False, activation=tf.nn.relu)(input)
layer2 = Dense(5, use_bias=False)(layer1)
layer3 = Dense(15, use_bias=False)(layer2)
output = Dense(1, use_bias=True, activation=tf.nn.softmax)(layer3)
model = tf.keras.Model(inputs=input, outputs=output)
model.compile(optimizer="adam", loss="mse", metrics=['mae'])
model.summary()
model_name = 'simple_model.h5'
model.save(model_name)

## Visualize
import netron
netron.start(model_name, 8081)
netron.stop()
