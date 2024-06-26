# Importing the requirements
import numpy as np
import torch
from PIL import Image
from transformers import DPTImageProcessor, DPTForDepthEstimation


# Load the model and feature extractor
feature_extractor = DPTImageProcessor.from_pretrained("Intel/dpt-beit-large-512")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-beit-large-512")


# Function to process an image and return the formatted depth map as an image
def process_image(image):
    """
    Preprocesses an image, passes it through a model, and returns the formatted depth map as an image.

    Args:
        image (PIL.Image.Image): The input image.

    Returns:
        PIL.Image.Image: The formatted depth map as an image.
    """

    # Preprocess the image for the model
    encoding = feature_extractor(image, return_tensors="pt")

    # Forward pass through the model
    with torch.no_grad():
        outputs = model(**encoding)
        predicted_depth = outputs.predicted_depth

    # Interpolate the predicted depth map to the original image size
    prediction = torch.nn.functional.interpolate(
        predicted_depth.unsqueeze(1),
        size=image.size[::-1],
        mode="bicubic",
        align_corners=False,
    ).squeeze()
    output = prediction.cpu().numpy()
    formatted = (output * 255 / np.max(output)).astype("uint8")

    # Return the formatted depth map as an image
    return Image.fromarray(formatted)
