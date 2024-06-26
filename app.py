# Importing the requirements
import numpy as np
import gradio as gr
import torch
from PIL import Image
from transformers import DPTImageProcessor, DPTForDepthEstimation


# Load the model and feature extractor
feature_extractor = DPTImageProcessor.from_pretrained("Intel/dpt-beit-large-512")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-beit-large-512")


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


# Image input for the interface
image = gr.Image(type="pil", label="Image")

# Output for the interface
answer = gr.Image(type="pil", label="Depth Map")

# Examples for the interface
examples = [
    ["cat.jpg"],
    ["dog.jpg"],
    ["bird.jpg"],
]

# Title, description, and article for the interface
title = "Zero Shot Depth Estimation"
description = "Gradio Demo for the Intel/DPT Beit-Large-512 Depth Estimation model. This model can estimate the depth of objects in images. To use it, upload your photo and click 'submit', or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://arxiv.org/pdf/2307.14460' target='_blank'>MiDaS v3.1 – A Model Zoo for Robust Monocular Relative Depth Estimation</a> | <a href='https://huggingface.co/Intel/dpt-beit-large-512' target='_blank'>Model Page</a></p>"


# Launch the interface
interface = gr.Interface(
    fn=process_image,
    inputs=[image],
    outputs=answer,
    examples=examples,
    title=title,
    description=description,
    article=article,
    theme="Soft",
    allow_flagging="never",
)
interface.launch(debug=False)
