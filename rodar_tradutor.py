import subprocess
import sys

def instalar_dependencias():
    libs = ["mss", "pytesseract", "pillow", "googletrans==4.0.0-rc1", "legacy-cgi"]
    for lib in libs:
        try:
            if "googletrans" in lib:
                __import__("googletrans")
            else:
                __import__(lib)
        except ImportError:
            if lib == "legacy-cgi":
                subprocess.check_call([sys.executable, "-m", "pip", "install", "legacy-cgi"])
            elif "googletrans" in lib:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "googletrans==4.0.0-rc1"])
            else:
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

instalar_dependencias()

import time
import threading
import tkinter as tk
from PIL import Image, ImageOps, ImageEnhance
import mss
import pytesseract
import os
import re
from googletrans import Translator

possible_paths = [
    r'C:\Program Files\Tesseract-OCR\tesseract.exe',
    r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
    os.path.expanduser('~') + r'\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
]
for path in possible_paths:
    if os.path.exists(path):
        pytesseract.pytesseract.tesseract_cmd = path
        break

class SelectorApp:
    def __init__(self, master):
        self.root = tk.Toplevel(master)
        self.root.attributes("-alpha", 0.3, "-fullscreen", True)
        self.root.config(cursor="cross")
        self.canvas = tk.Canvas(self.root, cursor="cross", bg="grey")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.start_x = self.start_y = self.rect = self.region = None

    def on_press(self, event):
        self.start_x, self.start_y = event.x, event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1, outline='red', width=2)

    def on_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        x1, x2 = min(self.start_x, event.x), max(self.start_x, event.x)
        y1, y2 = min(self.start_y, event.y), max(self.start_y, event.y)
        self.region = {'top': y1, 'left': x1, 'width': x2 - x1, 'height': y2 - y1}
        self.root.destroy()

def selecionar_regiao(master):
    app = SelectorApp(master)
    master.wait_window(app.root)
    return app.region

def limpar_texto(texto):
    texto = re.sub(r'\d+:\d+', '', texto)
    texto = re.sub(r'Playback|Play|Next|Prev|hide|capti', '', texto, flags=re.IGNORECASE)
    texto = re.sub(r'[|\[\]{}]', '', texto)
    return " ".join(texto.split()).lower()

def iniciar_traducao(menu_root, region):
    menu_root.withdraw()
    
    trans_root = tk.Toplevel(menu_root)
    trans_root.title("Tradutor PT-PT")
    trans_root.overrideredirect(True)
    trans_root.attributes('-topmost', True)
    trans_root.attributes('-alpha', 0.85)
    
    sw, sh = trans_root.winfo_screenwidth(), trans_root.winfo_screenheight()
    trans_root.geometry(f"1000x60+{(sw - 1000)//2}+{sh - 120}")

    label = tk.Label(trans_root, text="A iniciar tradução... (Clica aqui para voltar ao menu)", font=("Arial", 14, "bold"), fg="yellow", bg="black", wraplength=980, justify="center")
    label.pack(fill=tk.BOTH, expand=True)
    
    ativo = True

    def fechar_tradutor(event=None):
        nonlocal ativo
        ativo = False
        try:
            trans_root.destroy()
        except:
            pass
        try:
            menu_root.deiconify()
        except:
            pass

    trans_root.bind("<Button-1>", fechar_tradutor)

    translator = Translator()
    cache_local = {}

    def worker():
        nonlocal ativo
        last_text = ""
        with mss.MSS() as sct:
            while ativo:
                try:
                    screenshot = sct.grab(region)
                    img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
                    img = ImageOps.grayscale(img)
                    img = ImageEnhance.Contrast(img).enhance(2.0)
                    
                    raw = pytesseract.image_to_string(img, config='--psm 6').strip()
                    text = limpar_texto(raw)

                    if text and len(text) > 4 and text != last_text:
                        last_text = text
                        
                        if text in cache_local:
                            translated = cache_local[text]
                        else:
                            try:
                                res = translator.translate(text, dest='pt')
                                translated = res.text
                                cache_local[text] = translated
                            except:
                                translated = f"[Erro]: {text}"

                        try:
                            trans_root.after(0, lambda t=translated: label.config(text=t.capitalize()))
                        except:
                            break
                    
                    time.sleep(0.4)
                except:
                    time.sleep(0.5)

    threading.Thread(target=worker, daemon=True).start()

def criar_menu():
    menu_root = tk.Tk()
    menu_root.title("Tradutor de Legendas - Menu")
    menu_root.geometry("380x240")
    menu_root.resizable(False, False)
    menu_root.attributes('-topmost', True)
    
    sw, sh = menu_root.winfo_screenwidth(), menu_root.winfo_screenheight()
    menu_root.geometry(f"380x240+{(sw - 380)//2}+{(sh - 240)//2}")
    menu_root.config(bg="#1e1e1e")

    titulo = tk.Label(menu_root, text="Tradutor de Legendas OCR", font=("Arial", 14, "bold"), fg="#ffffff", bg="#1e1e1e")
    titulo.pack(pady=20)

    def acao_selecionar():
        region = selecionar_regiao(menu_root)
        if not region or region['width'] < 10 or region['height'] < 10:
            return
        iniciar_traducao(menu_root, region)

    btn_inciar = tk.Button(menu_root, text="Selecionar Área e Traduzir", font=("Arial", 11, "bold"), bg="#007acc", fg="white", width=26, height=2, bd=0, command=acao_selecionar)
    btn_inciar.pack(pady=10)

    btn_sair = tk.Button(menu_root, text="Sair", font=("Arial", 11, "bold"), bg="#cc3333", fg="white", width=26, height=2, bd=0, command=menu_root.destroy)
    btn_sair.pack(pady=5)

    menu_root.mainloop()

if __name__ == "__main__":
    criar_menu()