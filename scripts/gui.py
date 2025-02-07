from fetch import *
import customtkinter
import tkinter
import random
import time

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

# Animation parameters for the button.
initial_width = 250
initial_height = 92
size_increase = 20  # How much bigger the button gets on hover

# Create a container frame for the button.
# This container will have a fixed size (the maximum expected size)
# so that when the button inside grows, it doesn't push other widgets.
max_width = initial_width + size_increase
max_height = initial_height + size_increase
button_frame = customtkinter.CTkFrame(master=app, width=max_width, height=max_height, fg_color="transparent")
button_frame.grid(row=10, column=1, padx=(0, 0), pady=20, sticky="w")
button_frame.grid_propagate(False)  # Lock the frame size

# Create the button inside the fixed container.
# Use .place() to position it so that when its size changes, its container remains fixed.
button = customtkinter.CTkButton(master=button_frame,
                                 width=initial_width,
                                 height=initial_height,
                                 border_width=2,
                                 border_color="black",
                                 corner_radius=35,
                                 text="Submit",
                                 font=("Manrope", 32),
                                 text_color="white",
                                 fg_color="black",
                                 hover_color="white",
                                 command=button_callback)
button.place(relx=0.5, rely=0.5, anchor="center")

# Function to animate the button size with easing.
def animate_size(widget, target_width, target_height):
    if hasattr(widget, "animation_id") and widget.animation_id is not None:
        app.after_cancel(widget.animation_id)
        widget.animation_id = None

    current_width = float(widget.cget("width"))
    current_height = float(widget.cget("height"))
    easing_factor = 0.2  # Adjust this factor for smoother or faster animation.
    new_width = current_width + (target_width - current_width) * easing_factor
    new_height = current_height + (target_height - current_height) * easing_factor

    if abs(target_width - new_width) > 1 or abs(target_height - new_height) > 1:
        widget.configure(width=int(new_width), height=int(new_height))
        widget.animation_id = app.after(10, animate_size, widget, target_width, target_height)
    else:
        widget.configure(width=target_width, height=target_height)
        widget.animation_id = None

# Hover event functions to trigger the animation.
def on_enter(event):
    if hasattr(button, "animation_id") and button.animation_id is not None:
        app.after_cancel(button.animation_id)
        button.animation_id = None
    target_width = initial_width + size_increase
    target_height = initial_height + size_increase
    animate_size(button, target_width, target_height)
    button.configure(text_color="black", fg_color="white")

def on_leave(event):
    if hasattr(button, "animation_id") and button.animation_id is not None:
        app.after_cancel(button.animation_id)
        button.animation_id = None
    animate_size(button, initial_width, initial_height)
    button.configure(text_color="white", fg_color="black")

# Bind hover events to the button.
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

app.mainloop()
