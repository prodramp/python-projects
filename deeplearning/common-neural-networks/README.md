## Various types of Neural Networks ##

### Lets define some of the common neural networks and create them ###

![A group of most used neural networks](https://github.com/prodramp/python-projects/blob/main/images/neural-networks-small.png?raw=true)

### CNN - Convolution Neural Network ###
The convolutional-neural-network is a subclass of neural-networks which have at least one convolution layer. 
- They are great for capturing local information (e.g. neighbor pixels in an image or surrounding words in a text)
- Reducing the complexity of the model - faster training, needs fewer samples, reduces the chance of overfitting)
- Convolutional Neural Networks have three important architectural features.
  - **Local Connectivity:** Neurons in one layer are only connected to neurons in the next layer that are spatially close to them. This design trims the vast majority of connections between consecutive layers, but keeps the ones that carry the most useful information. The assumption made here is that the input data has spatial significance, or in the example of computer vision, the relationship between two distant pixels is probably less significant than two close neighbors.

  - **Shared Weights:** This is the concept that makes CNNs "convolutional." By forcing the neurons of one layer to share weights, the forward pass (feeding data through the network) becomes the equivalent of convolving a filter over the image to produce a new image. The training of CNNs then becomes the task of learning filters (deciding what features you should look for in the data.)

  - **Pooling and ReLU:** CNNs have two non-linearities: pooling layers and ReLU functions. Pooling layers consider a block of input data and simply pass on the maximum value. Doing this reduces the size of the output and requires no added parameters to learn, so pooling layers are often used to regulate the size of the network and keep the system below a computational limit. The ReLU function takes one input, x, and returns the maximum of {0, x}. ReLU(x) = argmax(x, 0). This introduces a similar effect to tanh(x) or sigmoid(x) as non-linearities to increase the model's expressive power.



### Resources ###
- https://ai.stackexchange.com/questions/5546/what-is-the-difference-between-a-convolutional-neural-network-and-a-regular-neur
- 
