""" Getting started with PyTorch tensors
Tensors are the primary data structure in PyTorch and will be the building blocks for our deep learning models. They share many similarities with NumPy arrays but have some unique attributes too.

In this exercise, you'll practice creating a tensor from a Python list of temperature data from two weather stations. The Python list is named temperatures and has two sublists whose elements represent a different day each, with columns for readings from two stations.

Instructions
Begin by importing PyTorch.
Create a tensor from the Python list temperatures.
"""

# Import PyTorch
import torch

temperatures = [[72, 75, 78], [70, 73, 76]]

# Create a tensor from temperatures
temp_tensor = torch.tensor(temperatures)


""" Checking and adding tensors
While continuing your temperature data collection, you realize that the recorded temperatures are off by 2 degrees, so you need to add 2 degrees to the tensor of temperatures. Before adjusting the data, you want to verify the shape and type of the tensor, to make sure they are compatible to be added together. The torch library has been pre-imported.

Instructions
Check the shape of the temperatures tensor.
Check the type of the temperatures tensor.
Add the temperatures and adjustment tensors.
"""

temperatures = torch.tensor([[72, 75, 78], [70, 73, 76]])
adjustment = torch.tensor([[2, 2, 2], [2, 2, 2]])

# Check the shape of the temperatures tensor
temp_shape = temperatures.shape
print("Shape of temperatures:", temp_shape)

# Check the type of the temperatures tensor
temp_type = temperatures.dtype
print("Data type of temperatures:", temp_type)

# Adjust the temperatures by adding the adjustment tensor
corrected_temperatures = temperatures + adjustment

print("Corrected temperatures:", corrected_temperatures)



""" Your first neural network
In this exercise, you will implement a small neural network containing two linear layers. The first layer takes an eight-dimensional input, and the last layer outputs a one-dimensional tensor.

The torch package and the torch.nn package have already been imported for you.

Instructions
100 XP
Create a neural network of two linear layers that takes a tensor of dimensions 
    as input, representing 8 features, and outputs a tensor of dimensions .
Use any output dimension for the first layer you want.
"""

import torch
import torch.nn as nn

input_tensor = torch.Tensor([[2, 3, 6, 7, 9, 3, 2, 1]])

# Implement a small neural network with two linear layers
model = nn.Sequential(nn.Linear(8, 8),
                      nn.Linear(8, 1)
                     )

output = model(input_tensor)
print(output)



""" The sigmoid and softmax functions
The sigmoid and softmax functions are two of the most popular activation functions in deep learning. They are both usually used as the last step of a neural network. Sigmoid functions are used for binary classification problems, whereas softmax functions are often used for multiclass classification problems.

Let's say that you have a neural network that returns the values contained in the score tensor as a pre-activation output. Apply the activation function corresponding to the use cases described to get the output.

torch.nn is already imported as nn.

Instructions 1/2
Create a sigmoid function and apply it on input_tensor to generate a probability for a binary classification task.
Instructions 2/2
Create a softmax function and apply it on input_tensor to generate a probability for a multiclass classification task.
"""

input_tensor = torch.tensor([[0.8]])

# Create a sigmoid function and apply it on input_tensor
sigmoid = nn.Sigmoid()
probability = sigmoid(input_tensor)
print(probability)



input_tensor = torch.tensor([[1.0, -6.0, 2.5, -0.3, 1.2, 0.8]])

# Create a softmax function and apply it on input_tensor
softmax = nn.Softmax(dim=-1)
probabilities = softmax(input_tensor)
print(probabilities)