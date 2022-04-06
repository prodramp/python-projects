# Convolutional Neural Network (CNN) #

### CNN Architecture ###
![](https://github.com/prodramp/python-projects/blob/main/images/cnn-arch.png?raw=true)

<hr>

## Convolution ##
### Step-by-step of the convolution of a 5x5 image with a 3x3 kernel ###
![](https://github.com/prodramp/python-projects/blob/main/images/5x5-img-conv-3x3kernel.png?raw=true)

### Convolution of a 5x5 input with a 3x3 kernel ###
![](https://github.com/prodramp/python-projects/blob/main/images/5x5-cov.png?raw=true)

### ReLU function applied after the convolution ###
![](https://github.com/prodramp/python-projects/blob/main/images/conv-added-relu.png?raw=true)

### Visual representation of the ReLU function applied after the convolution ###
![](https://github.com/prodramp/python-projects/blob/main/images/conv-added-relu-img.png?raw=true)

<hr>

## Pooling ##
- Pooling size = (x,y)
- Stride = n
<div align="center" background-color='white'>
  <img src="https://github.com/prodramp/python-projects/blob/main/images/pooling-3by3with-Stride2-white.png">
</div>
![](https://github.com/prodramp/python-projects/blob/main/images/pooling-3by3with-Stride2-white.png?raw=true)

<div>
  Propagation of values through pooling layers with pooling size 3x3 and stride of 2. In this example, the convolutional layers were omitted for clarity.
</div>

<hr>

### References ###
- Full Credits to the following content creators for the above images and text content 
- https://towardsdatascience.com/visualizing-the-fundamentals-of-convolutional-neural-networks-6021e5b07f69
- https://medium.com/aiguys/deep-convolutional-neural-networks-dcnns-explained-in-layman-terms-b990b2818061
