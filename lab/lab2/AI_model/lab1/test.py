import torchvision.models as models
import torch
# A simple example in PyTorch is available below. This simple example shows how to take a pre-trained
# PyTorch model(a weights object and network class object)
# and convert it to ONNX format(that contains the weights and net structure).


# Use an existing model from Torchvision, note it
# will download this if not already on your computer (might take time)
model = models.alexnet(pretrained=True)

# Create some sample input in the shape this model expects
dummy_input = torch.randn(10, 3, 224, 224)

# It's optional to label the input and output layers
input_names = ["actual_input_1"] + ["learned_%d" % i for i in range(16)]
output_names = ["output1"]

# Use the exporter from torch to convert to onnx
# model (that has the weights and net arch)
torch.onnx.export(model, dummy_input, "alexnet.onnx", verbose=True,
                  input_names=input_names, output_names=output_names)
