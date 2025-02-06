from fetch import *
import customtkinter
import tkinter
import random
face_var = "ฅ^._.^ฅ"
face_list = [
    "(ෆ˙ᵕ˙ෆ)♡", "(⸝⸝ᵕᴗᵕ⸝⸝)", "(⸝⸝> ᴗ•⸝⸝)", "(๑¯◡¯๑)", "(＾∇＾)", "(─‿‿─)",  
    "٩( ๑╹ ꇴ╹)۶", "(๑˘︶˘๑)", "( ˶ˆ꒳ˆ˵ )", "(๑˃ᴗ˂)ﻭ", "(๑˃ᴗ˂)♡", 
    "(⁎˃ᴗ˂⁎)", "(๑•ᴗ•๑)♡", "( •⌄• ू )✧",  
    "(｡• ᵕ •｡)", "(♡⸝⸝•ᴗ•⸝⸝)", "(ฅ́ ˘ ฅ̀)", "(ˊᵕˋ)♡", "(๑´ლ`๑)", "(｡•̀ᴗ-)✧"
]



def button_callback():
    if entry.get() != "":
        face.configure(text=random.choice(face_list))

app = customtkinter.CTk()
app.title("S.P.A.R.K")
app.geometry("1400x800")
customtkinter.set_appearance_mode("light")

text_var1 = tkinter.StringVar(value="S.P.A.R.K")
text_var2 = tkinter.StringVar(value="Spotify Playlist and Audio Retrieval Kit")


label1 = customtkinter.CTkLabel(master=app,
                                textvariable=text_var1,
                                text_color="black",
                                font=("Tuffy", 128),
                                width=120,
                                height=25)
label1.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0))

label2 = customtkinter.CTkLabel(master=app,
                                textvariable=text_var2,
                                text_color="gray",
                                font=("Tuffy", 24),
                                width=120,
                                height=25)
label2.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20))

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=0)

label3 = customtkinter.CTkLabel(master=app,
                                text="Enter spotify link here:",
                                text_color="black",
                                font=("Manrope", 32),
                                width=120,
                                height=25)
label3.grid(row=9, column=0, padx=(60, 5), pady=(140, 0), sticky="w")

face = customtkinter.CTkLabel(master=app,
                                text=face_var,
                                text_color="black",
                                font=("Manrope", 48),
                                width=120,
                                height=25)
face.grid(row=9, column=0, padx=(60, 5), pady=(140, 0), sticky="e")

entry = customtkinter.CTkEntry(master=app,
                               width=800,
                               height=92,
                               fg_color="black",
                               font=("Manrope", 24),
                               text_color="#1ED760",
                               border_width=2,
                               corner_radius=35)
entry.grid(row=10, column=0, padx=(40, 5), pady=20, sticky="w")

button = customtkinter.CTkButton(master=app,
                                 width=250,
                                 height=92,
                                 border_width=2,
                                 border_color="black",
                                 corner_radius=35,
                                 text="Submit",
                                 font=("Manrope", 32),
                                 text_color="white",
                                 fg_color="black",
                                 hover_color="white",
                                 command=button_callback)
button.grid(row=10, column=1, padx=(0, 0), pady=20, sticky="w")

button.bind("<Enter>", lambda event: button.configure(text_color="black", fg_color="white"))
button.bind("<Leave>", lambda event: button.configure(text_color="white", fg_color="black"))

app.mainloop()