import tkinter as tk
from PIL import Image



racine = tk.Tk()
label = tk.Label(racine, text="J'adore Python !")
bouton = tk.Button(racine, text="Quitter", command=racine.quit)
bouton["fg"] = "red"
label.pack()
bouton.pack()
racine.mainloop()
print("C'est fini !")




import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


def encrypt_message (key, message):
    print ("hello")




def button_encrypt_pressed():
    key = entry_key.get()
    message = text_message.get("1.0", tk.END)
    print("key=" + key)
    print("message=" + message)
    encrypt_message (key, message)


def button_download_pressed():
    print("download")





window = tk.Tk()


label_key = tk.Label(text="Key :")
label_key.pack()
entry_key = tk.Entry()
entry_key.insert(0, "MySecretKey")
entry_key.pack()

label_msg = tk.Label(text="Message :")
label_msg.pack()
text_message = tk.Text()
text_message.insert("1.0", "My\nmessage\nto\nencrypt")
text_message.pack()

button_encrypt = tk.Button(text="Encrypt", command=button_encrypt_pressed)
button_encrypt.pack()

img = PhotoImage(file='./sasuke.png')
label_image = tk.Label(image=img, height=100)
label_image.pack()

button_download = tk.Button(text="Download", command=button_download_pressed)
button_download.pack()

window.mainloop()

