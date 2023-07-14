import customtkinter as ctk
import time

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.geometry('500x600')
app.resizable(False, False)
app.title('Pomodoro APP')
frame_1 = ctk.CTkFrame(app, 200, 600)




app.mainloop()