""" Using the TensorDataset class
In practice, loading your data into a PyTorch dataset will be one of the first steps you take in order to create and train a neural network with PyTorch.

The TensorDataset class is very helpful when your dataset can be loaded directly as a NumPy array. Recall that TensorDataset() can take one or more NumPy arrays as input.

In this exercise, you'll practice creating a PyTorch dataset using the TensorDataset class.

torch and numpy have already been imported for you, along with the TensorDataset class.

Instructions
Create a TensorDataset using the torch_features and the torch_target tensors provided (in this order).
Return the last element of the dataset.
"""

import numpy as np
import torch
from torch.utils.data import TensorDataset

np_features = np.array(np.random.rand(12, 8))
np_target = np.array(np.random.rand(12, 1))

torch_features = torch.tensor(np_features)
torch_target = torch.tensor(np_target)

# Create a TensorDataset from two tensors
dataset = TensorDataset(torch.tensor(np_features).double(), torch.tensor(np_target).double())

# Return the last element of this dataset
print(dataset[-1])


""" From data loading to running a forward pass
In this exercise, you'll create a PyTorch DataLoader from a pandas DataFrame and call a model on this dataset. Specifically, you'll run a forward pass on a neural network. You'll continue working with fully connected neural networks, as you have done so far.

You'll begin by subsetting a loaded DataFrame called dataframe, converting features and targets NumPy arrays, and converting to PyTorch tensors in order to create a PyTorch dataset.

This dataset can be loaded into a PyTorch DataLoader, batched, shuffled, and used to run a forward pass on a custom fully connected neural network.

NumPy as np, pandas as pd, torch, TensorDataset(), and DataLoader() have been imported for you.

Instructions 1/3
Extract the features (ph, Sulfate, Conductivity, Organic_carbon) and target (Potability) values and load them into tensors to represent features and targets.
Use both tensors to generate a PyTorch dataset using the tensor dataset class.
Instructions 2/3
Create a PyTorch DataLoader from the created TensorDataset; this DataLoader should use a batch_size of two and shuffle the dataset.
Instructions 3/3
Implement a small, fully connected neural network using exactly two linear layers and the nn.Sequential() API, where the final output size is 1.
"""

# Load the different columns into two PyTorch tensors
features = torch.tensor(dataframe[["ph", "Sulfate", "Conductivity", "Organic_carbon"]].values).float()
target = torch.tensor(dataframe["Potability"]).float()

# Create a dataset from the two generated tensors
dataset = TensorDataset(features, target)


# Load the different columns into two PyTorch tensors
features = torch.tensor(dataframe[['ph', 'Sulfate', 'Conductivity', 'Organic_carbon']].to_numpy()).float()
target = torch.tensor(dataframe['Potability'].to_numpy()).float()

# Create a dataset from the two generated tensors
dataset = TensorDataset(features, target)

# Create a dataloader using the above dataset
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)
x, y = next(iter(dataloader))



# Load the different columns into two PyTorch tensors
features = torch.tensor(dataframe[['ph', 'Sulfate', 'Conductivity', 'Organic_carbon']].to_numpy()).float()
target = torch.tensor(dataframe['Potability'].to_numpy()).float()

# Create a dataset from the two generated tensors
dataset = TensorDataset(features, target)

# Create a dataloader using the above dataset
dataloader = DataLoader(dataset, shuffle=True, batch_size=2)
x, y = next(iter(dataloader))

# Create a model using the nn.Sequential API
model = nn.Sequential(
    nn.Linear(features.shape[1], 4),
    nn.Linear(4, 1)
)
output = model(features)
print(output)



""" Writing the evaluation loop
In this exercise, you will practice writing the evaluation loop. Recall that the evaluation loop is similar to the training loop, except that you will not perform the gradient calculation and the optimizer step.

The model has already been defined for you, along with the object validationloader, which is a dataset.

Instructions 1/2
Set the model to evaluation mode.
Sum the current batch loss to the validation_loss variable.
Instructions 2/2
Calculate the mean loss value for the epoch.
Set the model back to training mode.
"""
# Set the model to evaluation mode
model.eval()
validation_loss = 0.0

with torch.no_grad():
  
  for data in validationloader:
    
      outputs = model(data[0])
      loss = criterion(outputs, data[1])

      # Sum the current loss to the validation_loss variable
      validation_loss += loss.item()




# Set the model to evaluation mode
model.eval()
validation_loss = 0.0

with torch.no_grad():
  
  for data in validationloader:
    
      outputs = model(data[0])
      loss = criterion(outputs, data[1])
      
      # Sum the current loss to the validation_loss variable
      validation_loss += loss.item()
      
# Calculate the mean loss value
validation_loss_epoch = validation_loss / len(validationloader)
print(validation_loss_epoch)

# Set the model back to training mode
model.train()


""" Calculating accuracy using torchmetrics
In addition to the losses, you should also be keeping track of the accuracy during training. By doing so, you will be able to select the epoch when the model performed the best.

In this exercise, you will practice using the torchmetrics package to calculate the accuracy. You will be using a sample of the facemask dataset. This dataset contains three different classes. The plot_errors function will display samples where the model predictions do not match the ground truth. Performing such error analysis will help you understand your model failure modes.

The torchmetrics package is already imported. The model outputs are the probabilities returned by a softmax as the last step of the model. The labels tensor contains the labels as one-hot encoded vectors.

Instructions 1/2
Create an accuracy metric for a "multiclass" problem with three classes.
Calculate the accuracy for each batch of the dataloader.
Instructions 2/2
Calculate accuracy for the epoch.
Reset the metric for the next epoch.
"""

# Create accuracy metric using torch metrics
metric = torchmetrics.Accuracy(task="multiclass", num_classes=3)
for data in dataloader:
    features, labels = data
    outputs = model(features)
    
    # Calculate accuracy over the batch
    acc = metric(outputs, labels.argmax(dim=-1))



# Create accuracy metric using torch metrics
metric = torchmetrics.Accuracy(task="multiclass", num_classes=3)
for data in dataloader:
    features, labels = data
    outputs = model(features)
    
    # Calculate accuracy over the batch
    acc = metric(outputs, labels.argmax(dim=-1))
    
# Calculate accuracy over the whole epoch
acc = metric.compute()

# Reset the metric for the next epoch 
metric.reset()
plot_errors(model, dataloader)



""" Experimenting with dropout
The dropout layer randomly zeroes out elements of the input tensor. Doing so helps fight overfitting. In this exercise, you'll create a small neural network with one linear layer, one dropout layer, and one activation function.

The torch.nn package has already been imported as nn. An input_tensor of dimensions 
 has been created for you.

Instructions 1/2
Create a neural network with a linear, a ReLU, and a dropout layer, using input_tensor as input and a size 16 output.
Using the same neural network, set the probability of zeroing out elements in the dropout layer to 0.8.
Instructions 2/2
Create a neural network with a linear, a ReLU, and a dropout layer, using input_tensor as input and a size 16 output.
Using the same neural network, set the probability of zeroing out elements in the dropout layer to 0.8.
"""
# Create a small neural network
model = nn.Sequential(
    nn.Linear(3072, 16),
    nn.ReLU(),
    nn.Dropout()
)
model(input_tensor)

# Using the same model, set the dropout probability to 0.8
model = nn.Sequential(
    nn.Linear(3072, 16),
    nn.ReLU(),
    nn.Dropout(p=0.8)
)
model(input_tensor)



""" Implementing random search
Hyperparameter search is a computationally costly approach to experiment with different hyperparameter values. However, it can lead to performance improvements. In this exercise, you will implement a random search algorithm.

You will randomly sample 10 values of the learning rate and momentum from the uniform distribution. To do so, you will use the np.random.uniform() function.

The numpy package has already been imported as np.

Instructions
Randomly sample a learning rate factor between 2 and 4 so that the learning rate (lr) is bounded between 10^-2
 and 10^-4.

Randomly sample a momentum between 0.85 and 0.99.
"""

values = []
for idx in range(10):
    # Randomly sample a learning rate factor between 2 and 4
    factor = np.random.uniform(2, 4)
    lr = 10 ** -factor
    
    # Randomly select a momentum between 0.85 and 0.99
    momentum = np.random.uniform(0.85, 0.99)
    
    values.append((lr, momentum))