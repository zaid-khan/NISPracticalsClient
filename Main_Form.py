import tkinter as tk
from SymmetricCiphers.caesar import caesar_encryption
from SymmetricCiphers.hillcipher import HillCipherEncryptWrapper
from SymmetricCiphers.playfair import PlayFairEncrypt
from SymmetricCiphers.sdes import SDESEncrypt

from client import send_data_to_server

from tkinter.font import Font
import tkinter.ttk as ttk
from tkinter import messagebox

import tkinter as tk
from tkinter.font import Font



root = tk.Tk()
text = tk.Text(root)
myFont = Font(family="FreeSans", size=10, weight="bold")








root.title("NIS Practicals Client")
v = tk.IntVar()
v.set(0)  # initializing the choice, i.e. Symmetric

languages = [
    "Symmetric",
    "Asymmetric"
]
def Pass_Text():
    print(ent.get())
    if v.get() == 0:
        if tkvarsymmetric.get() == "Caesar":
            try:
                key_value = int(ent2.get())
                key_value = key_value % 26
            except ValueError:
                messagebox.showerror("Error", "Please enter a number")
                return

            cipher = caesar_encryption(ent.get(), key_value)
            send_data_to_server(cipher)

        elif tkvarsymmetric.get() == "Hill":
            try:
                key_value = ent2.get()
                plaintxt = ent.get().replace(' ', '')
                if len(key_value) != 9:
                    raise ValueError("Key Length is not equal to 6") 
            except ValueError:
                messagebox.showerror("Error", "Please enter a key of length : 6")
                return

            cipher = HillCipherEncryptWrapper(plaintxt, key_value)
            send_data_to_server(cipher)        

        elif tkvarsymmetric.get() == "Playfair":
            try:
                key_value = ent2.get()
                plaintxt = ent.get().replace(' ', '')
                if len(key_value) == 0:
                    raise ValueError("Key Length should not be equal to Zero") 
            except ValueError:
                messagebox.showerror("Error", "Key Length should not be equal to Zero")
                return

            cipher = PlayFairEncrypt(plaintxt, key_value)
            send_data_to_server(cipher)

        elif tkvarsymmetric.get() == "S-DES":
            try:
                key_value = ent2.get()
                plaintxt = ent.get().replace(' ', '')
                
                if len(key_value) != 10:
                    raise ValueError("Key is invalid")
                
                if len(plaintxt) != 1:
                    raise ValueError("Plaintext is invalid")
                 
            except ValueError:
                messagebox.showerror("Error", "Key/Plaintext is invalid")
                return

            cipher = SDESEncrypt(key_value, plaintxt)
            send_data_to_server(cipher)        
        


mainFrame = tk.Frame(root)
mainFrame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)
mainFrame2 = tk.Frame(root)
mainFrame2.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)
optionFrame = tk.Frame(root)
optionFrame.pack(side=tk.BOTTOM, fill=tk.X, padx=20, pady=20)

tkvarsymmetric = tk.StringVar()
# List with options
choicessy = {'Caesar', 'Hill', 'Playfair', 'S-DES'}
tkvarsymmetric.set('Caesar')
popupMenuSy = tk.OptionMenu(optionFrame, tkvarsymmetric, *choicessy)
popupMenuSy.pack(side=tk.TOP, padx=20, pady=20)
popupMenuSy.configure(font=myFont)


tkvarasy = tk.StringVar()
# List with options
choicesasy = {'Diffie Hellman', 'xyz'}
tkvarasy.set('Diffie Hellman')
popupMenuAsy = tk.OptionMenu(optionFrame, tkvarasy, *choicesasy)
popupMenuAsy.pack(side=tk.TOP, padx=20, pady=20)
popupMenuAsy.configure(font=myFont)
popupMenuAsy.pack_forget()
# popupMenuSy.pack_forget()

lab = tk.Label(mainFrame, width=15, text="Plain Text: ", anchor='w')
lab.configure(font=myFont)
ent = tk.Entry(mainFrame)
lab.pack(side=tk.LEFT)
ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
ent.configure(font=myFont)

lab2 = tk.Label(mainFrame2, width=15, text="Key: ", anchor='w')
lab2.configure(font=myFont)
ent2 = tk.Entry(mainFrame2)
ent2.configure(font=myFont)
lab2.pack(side=tk.LEFT)
ent2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

# ent.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)
# ent2 = tk.Entry(mainFrame)
# ent2.pack(side=tk.BOTTOM, expand=tk.YES, fill=tk.X)

buttonFrame = tk.Frame(root)
buttonFrame.pack(side=tk.RIGHT, fill=tk.X, padx=20, pady=20)

b1 = tk.Button(buttonFrame, text='Quit', command=root.quit)
b1.pack(side=tk.LEFT, padx=5, pady=5)    
b1.configure(font=myFont)
b2 = tk.Button(root, text='Encrypt',
          command=(Pass_Text))
b2.pack(side=tk.RIGHT, padx=5, pady=5)
b2.configure(font=myFont)

def ShowChoice():
    print(v.get())
    if v.get() == 0:
        popupMenuAsy.pack_forget()
        popupMenuSy.pack(side=tk.TOP, padx=20, pady=20)
    elif v.get() == 1:
        popupMenuSy.pack_forget()
        popupMenuAsy.pack(side=tk.TOP, padx=20, pady=20)
    

        

row = tk.Frame(root)

for val, language in enumerate(languages):
    tk.Radiobutton(row, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val,font=myFont).pack(side=tk.LEFT)

row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)


root.mainloop()