
import os
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import torch
from diffusers import StableDiffusionPipeline


os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"

# Create the app using CTk
app = ctk.CTk()
app.geometry("532x700")  # increased height for dropdown
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

# Prompt entry field
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.pack(pady=(20, 10))

# Style dropdown
style_var = tk.StringVar(value="None")  # default style
style_options = ["None", "Realistic", "Anime", "Cyberpunk", "Fantasy", "Oil Painting"]
style_menu = ctk.CTkOptionMenu(master=app, variable=style_var, values=style_options, width=200)
style_menu.pack(pady=(0, 10))

# Output label for image
lmain = ctk.CTkLabel(master=app, height=512, width=512)
lmain.place(x=10, y=150)

# Load SD-Turbo pipeline
model_id = "stabilityai/sd-turbo"
device = "mps" if torch.backends.mps.is_available() else "cpu"

pipeline = StableDiffusionPipeline.from_pretrained(model_id)
pipeline.to(device)

# Style prompt additions
style_prompts = {
    "None": "",
    "Realistic": "photo-realistic, 4K, ultra-detailed",
    "Anime": "anime style, cel-shaded, vibrant colors",
    "Cyberpunk": "cyberpunk, neon lights, futuristic city",
    "Fantasy": "epic fantasy, magical atmosphere, cinematic lighting",
    "Oil Painting": "oil painting, brush strokes, canvas texture"
}

# Generate image function
def generate():
    prompt_text = prompt.get()
    if not prompt_text.strip():
        return  # Prevent empty prompt

    style_choice = style_var.get()
    style_suffix = style_prompts.get(style_choice, "")

    final_prompt = prompt_text + ", " + style_suffix if style_suffix else prompt_text
    print(f"Generating image for prompt: {final_prompt} [style: {style_choice}]")

    image = pipeline(
        final_prompt,
        guidance_scale=2.0,
        negative_prompt="blurry, low quality, cropped, close-up, distorted face, bad anatomy"
    ).images[0]

    image = image.resize((512, 512), resample=Image.BICUBIC)
    image.save("generated.png")
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)
    lmain.image = img  # Prevent garbage collection

# Generate button
trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 20),
                        text_color="white", fg_color="blue", text="Generate", command=generate)
trigger.place(x=210, y=100)

app.mainloop()
