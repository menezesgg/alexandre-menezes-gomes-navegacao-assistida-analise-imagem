import cv2
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path
import google.generativeai as genai
import pyttsx3

# Configurar a API do Gemini Pro Vision
genai.configure(api_key="CHAVE-DA-API")

# Configurações do modelo Gemini Pro Vision
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Inicializar o motor de síntese de voz
engine = pyttsx3.init()

class App:
    def __init__(self, root, window_title="Assistente de Navegação"):
        self.root = root
        self.root.title(window_title)

        self.cap = cv2.VideoCapture(0)
        _, self.frame = self.cap.read()

        # Adicionando um canvas para exibir a imagem
        self.canvas = tk.Canvas(root, width=self.frame.shape[1], height=self.frame.shape[0])
        self.canvas.pack()

        self.btn_analyze = tk.Button(root, text="Analisar", command=self.analyze_image)
        self.btn_analyze.pack()

        self.analysis_label = tk.Label(root, text="")
        self.analysis_label.pack()

        self.root.after(10, self.update)

    def update(self):
        _, self.frame = self.cap.read()
        self.photo = self.convert_frame_to_photo()
        
        # Atualizando o canvas com a nova imagem
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
        self.root.after(10, self.update)

    def convert_frame_to_photo(self):
        frame_rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        photo = ImageTk.PhotoImage(image=img)
        return photo

    def analyze_image(self):
        cv2.imwrite('temp_image.jpg', self.frame)
        description = self.perform_analysis('temp_image.jpg')
        self.update_analysis_label(description)

    def perform_analysis(self, image_path):
        image_parts = [
            {
                "mime_type": "image/jpeg",
                "data": Path(image_path).read_bytes()
            },
        ]

        prompt_parts = [
            image_parts[0],
            "DESCREVER A IMAGEM PRA UMA PESSOA QUE NÃO ENXERGA NADA, ELA É 100% DEFICIENTE VISUAL DE NASCENÇA",
        ]

        response = model.generate_content(prompt_parts)
        return response.text

    def update_analysis_label(self, description):
        current_text = self.analysis_label.cget("text")
        if current_text:
            current_text += "\n"  # Adiciona uma quebra de linha
        updated_text = current_text + description
        self.analysis_label.config(text=updated_text)
        
        # Falar a análise em voz alta
        self.speak(description)

    def speak(self, text):
        engine.say(text)
        engine.runAndWait()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
