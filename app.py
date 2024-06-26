# Importing the requirements
import gradio as gr
from depth_estimation import process_image  # Import the depth estimation function


# Image input for the interface
image = gr.Image(type="pil", label="Image")

# Output for the interface
answer = gr.Image(type="pil", label="Depth Map")

# Examples for the interface
examples = [
    ["images/cat.jpg"],
    ["images/dog.jpg"],
    ["images/bird.jpg"],
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
