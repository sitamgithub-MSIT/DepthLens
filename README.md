# DepthLens

Depth Estimation is the task of predicting the depth of each pixel in an image. This project uses one of the popular models, [dpt-beit-large-512](https://huggingface.co/Intel/dpt-beit-large-512) for depth estimation from the Hugging Face model hub. The used model can be run on CPUs.

## Project Structure

The project is structured as follows:

- `app.py`: The main file that contains the Gradio application for depth estimation.
- `depth_estimation.py`: The file that contains the depth estimation model and functions.
- `requirements.txt`: The file that contains the required dependencies for the project.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `assets`: The folder that contains the screenshots for working on the application.
- `images`: The folder that contains the images for testing the application.

## Tech Stack

- Python (for the programming language)
- Hugging Face Transformers Library (for the visual question-answering model)
- Gradio (for the web application)
- Hugging Face Spaces (for hosting the gradio application)

## Getting Started

To get started with this project, follow the steps below:

1. Clone the repository: `git clone https://github.com/sitamgithub-MSIT/DepthLens.git`
2. Create a virtual environment: `python -m venv tutorial-env`
3. Activate the virtual environment: `tutorial-env\Scripts\activate`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Run the Gradio application: `python app.py`

Now, open up your local host and you should see the web application running. For more information, refer to the Gradio documentation [here](https://www.gradio.app/docs/interface). Also, a live version of the application can be found [here](https://huggingface.co/spaces/sitammeur/DepthLens).

## Usage

The web application allows you to input an image, and the model will generate a depth map of the image. This can be useful in various applications such as autonomous driving, 3D modeling, augmented reality, and more. The depth estimation model provides a detailed understanding of the spatial structure of the scene in the image, enhancing the capabilities of computer vision systems.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you would like to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to me on my GitHub profile.

Happy coding! 🚀
