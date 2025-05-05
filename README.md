Stable Bud

Stable Bud is a simple desktop app to generate AI images from text prompts using the stabilityai/sd-turbo model from Hugging Face.

Built with:

Python

CustomTkinter (for modern GUI)

Hugging Face Diffusers

Stable Diffusion Turbo

✨ Features

Text prompt input.

Choose from different artistic styles (Realistic, Anime, Cyberpunk, Fantasy, Oil Painting).

Generates and displays the image inside the app.

Saves the generated image automatically as generated.png.

Lightweight and runs on CPU/MPS.

🛠 Installation

Clone the repository:

git clone https://github.com/your-username/stable-bud.git
cd stable-bud

Install required libraries:

pip install torch diffusers transformers accelerate customtkinter pillow

(Mac Only):If you are using Apple Silicon (M1/M2) and want to use MPS backend:

pip install torch torchvision torchaudio

Run the app:

python app.py

📸 Screenshots

Prompt Entry

Style Dropdown

Generated Image







🚀 How It Works

Uses Hugging Face's StableDiffusionPipeline to load the stabilityai/sd-turbo model.

Adds optional style-specific suffixes to prompts.

Applies negative prompts for better image quality.

Resizes and displays the generated image using Pillow (PIL).

📚 Learning Outcomes

How to use pretrained models from Hugging Face (diffusers library).

How to create modern GUI applications using customtkinter.

How to combine text prompt engineering + AI models.

Managing device compatibility (cpu vs mps).
