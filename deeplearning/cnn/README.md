# Convolutional Neural Network (CNN) #

### CNN Architecture ###
![](https://github.com/prodramp/python-projects/blob/main/images/cnn-arch.png?raw=true)

<hr>

## Convolution ##
- This layer is the first layer that is used to extract the various features from the input images. 
- In this layer, the mathematical operation of convolution is performed between the input image and a filter of a particular size MxM. By sliding the filter over the input image, the dot product is taken between the filter and the parts of the input image with respect to the size of the filter (MxM).
- The output is termed as the Feature map which gives us information about the image such as the corners and edges. Later, this feature map is fed to other layers to learn several other features of the input image.

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
- Two main elements 
  - (a). Pooling size (x,y ) 
  - (b). Stride
- The primary aim of this layer is to decrease the size of the convolved feature map to reduce computational costs. 
- This is performed by decreasing the connections between layers and independently operating on each feature map.
- It is a downsampling operation executed over each feature map. 
- It extracts receptive fields from the feature map and replaces it with a single value. 
- This single value can be obtained by different aggregation criteria, such as maximum value, average, or weighted average according to the distance from the centre of the receptive field.

- In Max Pooling, the largest element is taken from the feature map. 
- Average Pooling calculates the average of the elements in a predefined sized Image section. 
- The total sum of the elements in the predefined section is computed in Sum Pooling. 
- The Pooling Layer usually serves as a bridge between the Convolutional Layer and the FC Layer
- 
<div align="center" background-color='white'>
  <img src="https://github.com/prodramp/python-projects/blob/main/images/pooling-3by3with-Stride2-white.png">
</div>
<div>
  Propagation of values through pooling layers with pooling size 3x3 and stride of 2. In this example, the convolutional layers were omitted for clarity.
</div>

<hr>

## Flatten ##
- Take x,y,z dimension and convert them to x*y*z
- Convert (10,10,2) => 200

<hr>

## Dropout ##

- Usage - Dropout(0.2) - 20% of the values randomly set to 0
- The Dropout layer randomly sets input units to 0 with a frequency of rate at each step during training time, which helps prevent overfitting. 
- Dropout is commonly used to regularize deep neural networks; however, applying dropout on fully-connected layers and applying dropout on convolutional layers are fundamentally different operations.
- The Dropout layer randomly sets input units to 0 with a frequency of rate at each step during training time, which helps prevent overfitting.
- Dropout(0.5) means - creating a dropout layer with a 50% chance of setting inputs to zero.

<div align="center">
  <img src="https://github.com/prodramp/python-projects/blob/main/images/dropout-view.png?raw=true" />
</div>
<div align="center">
Srivastava, Nitish, et al. ”Dropout: a simple way to prevent neural networks from
overfitting”, JMLR 2014
</div>
  
<hr>

### References ###
Note: Full Credits to the following content creators for the above images and text content 
- https://towardsdatascience.com/visualizing-the-fundamentals-of-convolutional-neural-networks-6021e5b07f69
- https://medium.com/aiguys/deep-convolutional-neural-networks-dcnns-explained-in-layman-terms-b990b2818061
- https://towardsdatascience.com/dropout-on-convolutional-layers-is-weird-5c6ab14f19b2
- https://medium.com/@amarbudhiraja/https-medium-com-amarbudhiraja-learning-less-to-learn-better-dropout-in-deep-machine-learning-74334da4bfc5
- https://github.com/christianversloot/machine-learning-articles/blob/main/how-to-predict-new-samples-with-your-keras-model.md
- https://www.cs.ryerson.ca/~aharley/vis/conv/flat.html
