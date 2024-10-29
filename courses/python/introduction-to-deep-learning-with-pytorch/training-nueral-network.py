""" Building a binary classifier in PyTorch
Recall that a small neural network with a single linear layer followed by a sigmoid function is a binary classifier. It acts just like a logistic regression.

In this exercise, you'll practice building this small network and interpreting the output of the classifier.

The torch package and the torch.nn package have already been imported for you.

Instructions
Create a neural network that takes a tensor of dimensions 1x8 as input, and returns an output of the correct shape for binary classification.
Pass the output of the linear layer to a sigmoid, which both takes in and return a single float.
"""

import torch
import torch.nn as nn

input_tensor = torch.Tensor([[3, 4, 6, 2, 3, 6, 8, 9]])

# Implement a small neural network for binary classification
model = nn.Sequential(
  nn.Linear(8, 1),
  nn.Sigmoid()
)

output = model(input_tensor)
print(output)



""" From regression to multi-class classification
Recall that the models we have seen for binary classification, multi-class classification and regression have all been similar, barring a few tweaks to the model.

In this exercise, you'll start by building a model for regression, and then tweak the model to perform a multi-class classification.

Instructions 1/2
Create a 4-layer linear neural network compatible with input_tensor as the input, and a regression value as output.
Instructions 2/2
Update the network provided to perform a multi-class classification with four outputs.
"""

import torch
import torch.nn as nn

input_tensor = torch.Tensor([[3, 4, 6, 7, 10, 12, 2, 3, 6, 8, 9]])

# Implement a neural network with exactly four linear layers
model = nn.Sequential(
    nn.Linear(len(input_tensor[0]), 64),
    nn.Linear(64, 32),
    nn.Linear(32, 16),
    nn.Linear(16, 1),
)

output = model(input_tensor)
print(output)



import torch
import torch.nn as nn

input_tensor = torch.Tensor([[3, 4, 6, 7, 10, 12, 2, 3, 6, 8, 9]])

# Update network below to perform a multi-class classification with four labels
model = nn.Sequential(
  nn.Linear(11, 20),
  nn.Linear(20, 12),
  nn.Linear(12, 6),
  nn.Linear(6, 4), 
  nn.Softmax(dim=-1)
)

output = model(input_tensor)
print(output)



""" Creating one-hot encoded labels
One-hot encoding is a technique that turns a single integer label into a vector of N elements, where N is the number of classes in your dataset. This vector only contains zeros and ones. In this exercise, you'll create the one-hot encoded vector of the label y provided.

You'll practice doing this manually, and then make your life easier by leveraging the help of PyTorch! Your dataset contains three classes, and the class labels range from 0 to 2 (e.g., 0, 1, 2).

NumPy is already imported as np, and torch.nn.functional as F. The torch package is also imported.

Instructions
Manually create a one-hot encoded vector of the ground truth label y by filling in the NumPy array provided.
Create a one-hot encoded vector of the ground truth label y using PyTorch.
"""

y = 1
num_classes = 3

# Create the one-hot encoded vector using NumPy
one_hot_numpy = np.array([0, 1, 0])

# Create the one-hot encoded vector using PyTorch
one_hot_pytorch = F.one_hot(torch.tensor(y), num_classes=num_classes)



""" Calculating cross entropy loss
Cross entropy loss is one of the most common ways to measure loss for classification problems. In this exercise, you will calculate cross entropy loss in PyTorch for a vector of predicted scores and a ground truth label. You are provided with the ground truth label y and the scores vector, a vector of model predictions before the final softmax function.

You'll start by creating a one-hot encoded vector of the ground truth label y. Next, you'll instantiate a cross entropy loss function. Last, you'll call the loss function, which takes scores, and the one-hot encoded ground truth label, as inputs. Its output will be a single float, the loss of that sample.

torch, CrossEntropyLoss, and torch.nn.functional as F have already been imported for you.

Instructions 1/3
Create the one-hot encoded vector of the ground truth label y, with 4 features (one for each class), and assign it to one_hot_label.
Instructions 2/3
Create the cross entropy loss function and store it as criterion.
Instructions 3/3
Calculate the cross entropy loss using the one_hot_label vector and the scores vector, by calling the loss_function you created.
"""

import torch
import torch.nn.functional as F
from torch.nn import CrossEntropyLoss

y = [2]
scores = torch.tensor([[0.1, 6.0, -2.0, 3.2]])

# Create a one-hot encoded vector of the label y
one_hot_label = F.one_hot(torch.tensor(y), num_classes=len(scores[0]))


import torch
import torch.nn.functional as F
from torch.nn import CrossEntropyLoss

y = [2]
scores = torch.tensor([[0.1, 6.0, -2.0, 3.2]])

# Create a one-hot encoded vector of the label y
one_hot_label = F.one_hot(torch.tensor(y), num_classes = scores.shape[1])

# Create the cross entropy loss function
criterion = CrossEntropyLoss()


import torch
import torch.nn.functional as F
from torch.nn import CrossEntropyLoss

y = [2]
scores = torch.tensor([[0.1, 6.0, -2.0, 3.2]])

# Create a one-hot encoded vector of the label y
one_hot_label = F.one_hot(torch.tensor(y), scores.shape[1])

# Create the cross entropy loss function
criterion = CrossEntropyLoss()

# Calculate the cross entropy loss
loss = criterion(scores.double(), one_hot_label.double())
print(loss)



""" Accessing the model parameters
A PyTorch model created with the nn.Sequential() is a module that contains the different layers of your network. Recall that each layer parameter can be accessed by indexing the created model directly. In this exercise, you will practice accessing the parameters of different linear layers of a neural network.

Instructions
Access the weight parameter of the first linear layer.
Access the bias parameter of the second linear layer.
"""

model = nn.Sequential(nn.Linear(16, 8),
                      nn.Linear(8, 2)
                     )

# Access the weight of the first linear layer
weight_0 = model[0].weight

# Access the bias of the second linear layer
bias_1 = model[1].bias



""" Updating the weights manually
Now that you know how to access weights and biases, you will manually perform the job of the PyTorch optimizer. PyTorch functions can do what you're about to do, but it's helpful to do the work manually at least once, to understand what's going on under the hood.

A neural network of three layers has been created and stored as the model variable. This network has been used for a forward pass and the loss and its derivatives have been calculated. A default learning rate, lr, has been chosen to scale the gradients when performing the update.

Instructions 1/2
Create the gradient variables by accessing the local gradients of each weight tensor.
Instructions 2/2
Update the weights using the gradients scaled by the learning rate.
"""

weight0 = model[0].weight
weight1 = model[1].weight
weight2 = model[2].weight

# Access the gradients of the weight of each linear layer
grads0 = weight0.grad
grads1 = weight1.grad
grads2 = weight2.grad



weight0 = model[0].weight
weight1 = model[1].weight
weight2 = model[2].weight

# Access the gradients of the weight of each linear layer
grads0 = weight0.grad
grads1 = weight1.grad
grads2 = weight2.grad

# Update the weights using the learning rate and the gradients
weight0 = weight0 - lr * grads0
weight1 = weight1 - lr * grads1
weight2 = weight2 - lr * grads2



""" Using the PyTorch optimizer
In the previous exercise, you manually updated the weight of a network. You now know what's going on under the hood, but this approach is not scalable to a network of many layers.

Thankfully, the PyTorch SGD optimizer does a similar job in a handful of lines of code. In this exercise, you will practice the last step to complete the training loop: updating the weights using a PyTorch optimizer.

A neural network has been created and provided as the model variable. This model was used to run a forward pass and create the tensor of predictions pred. The one-hot encoded tensor is named target and the cross entropy loss function is stored as criterion.

torch.optim as optim, and torch.nn as nn have already been loaded for you.

Instructions 1/2
Use optim to create an SGD optimizer with a learning rate of your choice (must be less than one) for the model provided.
Instructions 2/2
Update the model's parameters using the optimizer.
"""

# Create the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001)


# Create the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001)

loss = criterion(pred, target)
loss.backward()

# Update the model's parameters using the optimizer
optimizer.step()



""" Using the MSELoss
For regression problems, we often use Mean Squared Error (MSE) as a loss function instead of cross-entropy. MSE calculates the squared difference between predicted values (y_pred) and actual values (y). In this exercise, you'll compute MSE loss using both NumPy and PyTorch.

The torch package has been imported, along with numpy as np and torch.nn as nn.

Instructions
Calculate the MSE loss using NumPy.
Create a MSE loss function using PyTorch.
Convert y_pred and y to tensors and then float data types, and then use them to calculate MSELoss using PyTorch as mse_pytorch.
"""

y_pred = np.array(10)
y = np.array(1)

# Calculate the MSELoss using NumPy
mse_numpy = (y_pred - y) ** 2

# Create the MSELoss function
criterion = nn.MSELoss()

# Calculate the MSELoss using the created loss function
mse_pytorch = criterion(torch.tensor(y_pred).float(), torch.tensor(y).float())
print(mse_pytorch)



""" Writing a training loop
In scikit-learn, the training loop is wrapped in the .fit() method, while in PyTorch, it's set up manually. While this adds flexibility, it requires a custom implementation.

In this exercise, you'll create a loop to train a model for salary prediction.

The show_results() function is provided to help you visualize some sample predictions.

The package imports provided are: pandas as pd, torch, torch.nn as nn, torch.optim as optim, as well as DataLoader and TensorDataset from torch.utils.data.

The following variables have been created: num_epochs, containing the number of epochs (set to 5); dataloader, containing the dataloader; model, containing the neural network; criterion, containing the loss function, nn.MSELoss(); optimizer, containing the SGD optimizer.

Instructions 1/3
Write a for loop that iterates over the dataloader; this should be nested within a for loop that iterates over a range equal to the number of epochs.
Set the gradients of the optimizer to zero.
Instructions 2/3
Write the forward pass.
Compute the MSE loss value using the criterion() function provided.
Compute the gradients.
"""

# Loop over the number of epochs and then the dataloader
for i in range(num_epochs):
  for data in dataloader:
    # Set the gradients to zero
    optimizer.zero_grad()


# Loop over the number of epochs and the dataloader
for i in range(num_epochs):
  for data in dataloader:
    # Set the gradients to zero
    optimizer.zero_grad()
    # Run a forward pass
    feature, target = data
    prediction = model(feature)
    # Calculate the loss
    loss = criterion(prediction, target)
    # Compute the gradients
    loss.backward()


# Loop over the number of epochs and the dataloader
for i in range(num_epochs):
  for data in dataloader:
    # Set the gradients to zero
    optimizer.zero_grad()
    # Run a forward pass
    feature, target = data
    prediction = model(feature)    
    # Calculate the loss
    loss = criterion(prediction, target)    
    # Compute the gradients
    loss.backward()
    # Update the model's parameters
    optimizer.step()
show_results(model, dataloader)