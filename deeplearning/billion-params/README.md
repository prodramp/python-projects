# Your very first Billon Params Neural Network ##


![](https://github.com/prodramp/python-projects/blob/main/images/billion-code-1.png?raw=true)


![](https://github.com/prodramp/python-projects/blob/main/images/billion-code-2.png?raw=true)


Code First Example

```
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Dropout 
from keras.models import Sequential, Model


model_cnn = Sequential([
    Conv2D(128, 3, input_shape=(256,256,1), use_bias=True ),
    # 3*3 * 128 + 1*128 =  Parameters = 1280
    MaxPooling2D(pool_size=2),
    #  output = 127, 127, 128

    Conv2D(256, 3, use_bias=True ),
    # 3 * 3 * 256 + 128 * 256 = 295168
    MaxPooling2D(pool_size=2),
    # 62, 62, 256
    Flatten(),
    # 62 * 62 * 256 = 984064
    Dropout(0.5),
    # 984064
    Dense(1000, activation='softmax')
    # 984064 * 1 = 984,064,000
])

model_cnn.summary()
```

## First Example Output ##

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 254, 254, 128)     1280      
                                                                 
 max_pooling2d (MaxPooling2D  (None, 127, 127, 128)    0         
 )                                                               
                                                                 
 conv2d_1 (Conv2D)           (None, 125, 125, 256)     295168    
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 62, 62, 256)      0         
 2D)                                                             
                                                                 
 flatten (Flatten)           (None, 984064)            0         
                                                                 
 dropout (Dropout)           (None, 984064)            0         
                                                                 
 dense (Dense)               (None, 1000)              984065000 
                                                                 
=================================================================
Total params: 984,361,448
Trainable params: 984,361,448
Non-trainable params: 0
_________________________________________________________________
```

## Code Second Example: ##

```
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Dropout 
from keras.models import Sequential, Model


model_cnn = Sequential([
    Conv2D(1024, 3, input_shape=(128,128,1), use_bias=True ),
    # 3*3 * 1024 + 1*1024 =  Parameters = 10240
    MaxPooling2D(pool_size=4),
    # Input size = 31,31,1024
    Flatten(),
    # Params = 31*31*1024 = 984064
    Dropout(0.5),
    # 984064
    Dense(1000, activation='softmax')
    # 984064 * 1000 =  984,075,240 Parameters
])

model_cnn.summary()
```

## Second Example Output ##

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 126, 126, 1024)    10240     
                                                                 
 max_pooling2d (MaxPooling2D  (None, 31, 31, 1024)     0         
 )                                                               
                                                                 
 flatten (Flatten)           (None, 984064)            0         
                                                                 
 dropout (Dropout)           (None, 984064)            0         
                                                                 
 dense (Dense)               (None, 1000)              984065000 
                                                                 
=================================================================
Total params: 984,075,240
Trainable params: 984,075,240
Non-trainable params: 0
_________________________________________________________________

```
