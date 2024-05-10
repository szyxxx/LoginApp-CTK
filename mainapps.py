import customtkinter as ctk
from PIL import Image

lebar = 1280
tinggi = 720
mainapp = ctk.CTk(fg_color='grey')
mainapp.geometry(f'{lebar}x{tinggi}')
mainapp.title('Dashboard')

mainapp.mainloop()