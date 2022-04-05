## Various types of Neural Networks ##

### Lets define some of the common neural networks and create them ###

![A group of most used neural networks](https://github.com/prodramp/python-projects/blob/main/images/neural-networks-small.png?raw=true)

At higher level:
- Single Layer Network - Perceptron - Input + Output
- Multiple Layer Perceptron: (Regular neural network) - Input + Layers + Output

### Regular Neural Network (Multiple Layer Perceptron) ###
A neural network (Multiple Layer Perceptron: Regular neural network ): It does a linear combination (a mathematical operation) between the previous layer's output and the current layer's weights(vectors) and then it passes data to the next layer by passing through an activation function. The picture shows a unit of a layer.
![](https://github.com/prodramp/python-projects/blob/main/images/mlp-reg-nn.png?raw=true)


### CNN - Convolution Neural Network ###
The convolutional-neural-network is a subclass of neural-networks which have at least one convolution layer. 
- They are great for capturing local information (e.g. neighbor pixels in an image or surrounding words in a text)
- Reducing the complexity of the model - faster training, needs fewer samples, reduces the chance of overfitting)
- Convolutional Neural Networks have three important architectural features.
  - **Local Connectivity:** Neurons in one layer are only connected to neurons in the next layer that are spatially close to them. This design trims the vast majority of connections between consecutive layers, but keeps the ones that carry the most useful information. The assumption made here is that the input data has spatial significance, or in the example of computer vision, the relationship between two distant pixels is probably less significant than two close neighbors.

  - **Shared Weights:** This is the concept that makes CNNs "convolutional." By forcing the neurons of one layer to share weights, the forward pass (feeding data through the network) becomes the equivalent of convolving a filter over the image to produce a new image. The training of CNNs then becomes the task of learning filters (deciding what features you should look for in the data.)

  - **Pooling and ReLU:** CNNs have two non-linearities: pooling layers and ReLU functions. Pooling layers consider a block of input data and simply pass on the maximum value. Doing this reduces the size of the output and requires no added parameters to learn, so pooling layers are often used to regulate the size of the network and keep the system below a computational limit. The ReLU function takes one input, x, and returns the maximum of {0, x}. ReLU(x) = argmax(x, 0). This introduces a similar effect to tanh(x) or sigmoid(x) as non-linearities to increase the model's expressive power.


### What is convolution? ###
The everyday definition of convolution comes from the Latin convolutus meaning 'to roll together'. Hence the meaning twisted or complicated.

The mathematical definition comes from the same root, with the interpretation of taking a "rolling average".
Hence in Machine Learning, a convolution is a sliding window across an input creating one averaged output for each stride the window takes. I.e. the values covered by the window are convoluted to create one convoluted output. This is best demonstrated with an a diagram:
![](https://github.com/prodramp/python-projects/blob/main/images/cnn-conv-ani2.gif?raw=true)

A neural network (Convolutional Neural Network): It does convolution (In signal processing it's known as Correlation) (Its a mathematical operation) between the previous layer's output and the current layer's kernel ( a small matrix ) and then it passes data to the next layer by passing through an activation function. The picture shows a Convolution operation. Each layer may have many convolution operation

![](https://github.com/prodramp/python-projects/blob/main/images/cnn-conv-ani.gif?raw=true)

### Resources ###
- https://ai.stackexchange.com/questions/5546/what-is-the-difference-between-a-convolutional-neural-network-and-a-regular-neur
- https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6
- https://medium.com/aiguys/deep-convolutional-neural-networks-dcnns-explained-in-layman-terms-b990b2818061
- https://medium.com/mlearning-ai/basic-concepts-in-machine-learning-a20de41137cc (TLDR)
