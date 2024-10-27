""" Implementing ReLU
The rectified linear unit (or ReLU) function is one of the most common activation functions in deep learning.

It overcomes the training problems linked with the sigmoid function you learned, such as the vanishing gradients problem.

In this exercise, you'll begin with a ReLU implementation in PyTorch. Next, you'll calculate the gradients of the function.

The nn module has already been imported for you.

Instructions 1/2
Create a ReLU function in PyTorch.
Instructions 2/2
Calculate the gradient of the ReLU function for x using the relu_pytorch() function you defined, then running a backward pass.
Find the gradient at x.
"""

# Create a ReLU function with PyTorch
relu_pytorch = nn.ReLU()


# Create a ReLU function with PyTorch
relu_pytorch = nn.ReLU()

# Apply your ReLU function on x, and calculate gradients
x = torch.tensor(-1.0, requires_grad=True)
y = relu_pytorch(x)
y.backward()

# Print the gradient of the ReLU function for x
gradient = x.grad
print(gradient)



""" Implementing leaky ReLU
You've learned that ReLU is one of the most used activation functions in deep learning. You will find it in modern architecture. However, it does have the inconvenience of outputting null values for negative inputs and therefore, having null gradients. Once an element of the input is negative, it will be set to zero for the rest of the training. Leaky ReLU overcomes this challenge by using a multiplying factor for negative inputs.

In this exercise, you will implement the leaky ReLU function in NumPy and PyTorch and practice using it. The numpy as np package, the torch package as well as the torch.nn as nn have already been imported.

Instructions
Create a leaky ReLU function in PyTorch with a negative slope of 0.05.
Call the function on the tensor x, which has already been defined for you.
"""

# Create a leaky relu function in PyTorch
leaky_relu_pytorch = nn.LeakyReLU(negative_slope=0.05)

x = torch.tensor(-2.0)
# Call the above function on the tensor x
output = leaky_relu_pytorch(x)
print(output)



""" Counting the number of parameters
Deep learning models are famous for having a lot of parameters. Recent language models have billions of parameters. With more parameters comes more computational complexity and longer training times, and a deep learning practitioner must know how many parameters their model has.

In this exercise, you will calculate the number of parameters in your model, first manually, and then using PyTorch.

The torch.nn package has been imported as nn.

Instructions
Now, confirm your manual calculation by iterating through the model's parameters to update the total variable with the total number of parameters in the model.
"""

model = nn.Sequential(nn.Linear(16, 4),
                      nn.Linear(4, 2),
                      nn.Linear(2, 1))

total = 0

# Calculate the number of parameters in the model
for parameter in model.parameters():
  total += parameter.numel()
  
print(f"The number of parameters in the model is {total}")



""" Manipulating the capacity of a network
In this exercise, you will practice creating neural networks with different capacities. The capacity of a network reflects the number of parameters in said network. To help you, a calculate_capacity() function has been implemented, as follows:

def calculate_capacity(model):
  total = 0
  for p in model.parameters():
    total += p.numel()
  return total
This function returns the number of parameters in your model.

The dataset you are training this network on has n_features features and n_classes classes. The torch.nn package has been imported as nn.

Instructions 1/2
Create a 3-layer linear neural network with <120 parameters, using n_features as input and n_classes as output sizes.
Instructions 2/2
Create a 4-layer linear neural network with >120 parameters, using n_features as input and n_classes as output sizes.
"""

n_features = 8
n_classes = 2

input_tensor = torch.Tensor([[3, 4, 6, 2, 3, 6, 8, 9]])

# Create a neural network with less than 120 parameters
model = nn.Sequential(
    nn.Linear(n_features,6),
    nn.Linear(6, 4),
    nn.Linear(4, n_classes),
)
output = model(input_tensor)

print(calculate_capacity(model))




n_features = 8
n_classes = 2

input_tensor = torch.Tensor([[3, 4, 6, 2, 3, 6, 8, 9]])

# Create a neural network with more than 120 parameters
model = nn.Sequential(
    nn.Linear(n_features, 7),
    nn.Linear(7, 6),
    nn.Linear(6, 4),
    nn.Linear(4, 2),
)

output = model(input_tensor)

print(calculate_capacity(model))



""" Experimenting with learning rate
In this exercise, your goal is to find the optimal learning rate such that the optimizer can find the minimum of the non-convex function 
 in ten steps.

You will experiment with three different learning rate values. For this problem, try learning rate values between 0.001 to 0.1.

You are provided with the optimize_and_plot() function that takes the learning rate for the first argument. This function will run 10 steps of the SGD optimizer and display the results.

Instructions 1/3
Try a small learning rate value such that the optimizer isn't able to get past the first minimum on the right.
Instructions 2/3
Try a large learning rate value such that the optimizer skips past the global minimum at -2.
Instructions 3/3
Based on the previous results, try a better learning rate value.
"""

# Try a first learning rate value
lr0 = 0.00001
optimize_and_plot(lr=lr0)

# Try a second learning rate value
lr1 = 0.1
optimize_and_plot(lr=lr1)

# Try a third learning rate value
lr2 = 0.09
optimize_and_plot(lr=lr2)



""" Experimenting with momentum
In this exercise, your goal is to find the optimal momentum such that the optimizer can find the minimum of the following non-convex function 
 in 20 steps. You will experiment with two different momentum values. For this problem, the learning rate is fixed at 0.01.

You are provided with the optimize_and_plot() function that accepts as input the momentum parameter. This function will run 20 steps of the SGD optimizer and display the results.

Instructions 1/2
Try a first value for the momentum such that the optimizer gets stuck in the first minimum.
Instructions 2/2
Try a second value for the momentum such that the optimizer finds the global optimum.
"""

# Try a first value for momentum
mom0 = 0
optimize_and_plot(momentum=mom0)

# Try a second value for momentum
mom1 = 0.94
optimize_and_plot(momentum=mom1)



""" Freeze layers of a model
You are about to fine-tune a model on a new task after loading pre-trained weights. The model contains three linear layers. However, because your dataset is small, you only want to train the last linear layer of this model and freeze the first two linear layers.

The model has already been created and exists under the variable model. You will be using the named_parameters method of the model to list the parameters of the model. Each parameter is described by a name. This name is a string with the following naming convention: x.name where x is the index of the layer.

Remember that a linear layer has two parameters: the weight and the bias.

Instructions
Use an if statement to determine if the parameter should be frozen or not based on its name.
Freeze the parameters of the first two layers of this model.
"""

for name, param in model.named_parameters():    
    # Check if the parameters belong to the first layer
    if name == '0.weight' or name == '0.bias':
        # Freeze the parameters
        param.requires_grad = False
    # Check if the parameters belong to the second layer
    if name == '1.weight' or name == '1.bias':
        # Freeze the parameters
        param.requires_grad = False


""" Layer initialization
The initialization of the weights of a neural network has been the focus of researchers for many years. When training a network, the method used to initialize the weights has a direct impact on the final performance of the network.

As a machine learning practitioner, you should be able to experiment with different initialization strategies. In this exercise, you are creating a small neural network made of two layers and you are deciding to initialize each layer's weights with the uniform method.

Instructions
For each layer (layer0 and layer1), use the uniform initialization method to initialize the weights.
"""

layer0 = nn.Linear(16, 32)
layer1 = nn.Linear(32, 64)

# Use uniform initialization for layer0 and layer1 weights
nn.init.uniform_(layer0.weight)
nn.init.uniform_(layer1.weight)

model = nn.Sequential(layer0, layer1)