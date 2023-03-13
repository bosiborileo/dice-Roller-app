import os
import tensorflow as tf


import random
import tkinter as tk
from tkinter import *
from chat import get_response

root = tk.Tk()
root.title(f"Chatbot")
root.geometry('600x500' )
root.resizable(True, True)
message = tk.StringVar()

chat_win=Frame(root, bd=1, bg='black', width= 70, height=4)
chat_win.place(x=6, y=6, height=300, width=488)

textcon= tk.Text(chat_win, bd=1, bg='white', width=50, height=8)
textcon.pack(fill="both", expand=True)

mes_win= Entry(root, width=30, xscrollcommand=True, textvariable=message)
mes_win.place(x=6, y=310, height=90, width=450)
mes_win.focus()

textcon.config(fg='black')
textcon.tag_config('usr', foreground='Black')
textcon.insert(END, "Bot: CHUKA BOT! Your University Assistant. \n\n")
msg=mes_win.get()

exit_list = ["Thanks", "Thank you", "That's helpful"]

def greet_res(text):
    text=text.lower()
    bot_greet= ["hello", "hi", "good day", "greetings", "how is it going?"]
    usr_greet= ["hello", "hi", "good day", "greetings", "how is it going?"]
    for word in text.split():
        if word in usr_greet:
            return random.choice(bot_greet)

def send_msz(event=None):
    usr_input = message.get()
    usr_input = usr_input.lower()
    textcon.insert(END, f'You: {usr_input}'+'\n', 'usr')
    if usr_input in exit_list:
        textcon.config(fg='black')
        textcon.insert(END, "Bot: Ok bye! Chat with you later \n")
        return root.destroy()
    else:
        textcon.config(fg='black')
        if greet_res(usr_input) != None:
            lab= f"Bot: {greet_res(usr_input)}"+ '\n'
            textcon.insert(END,lab)
            mes_win.delete(0,END)
        else:
            lab= f"Bot: {get_response(usr_input)}"+'\n'
            textcon.insert(END,lab)
            mes_win.delete(0,END)

button_send=Button(root,text='Send', bg='orange', activebackground='white', command=send_msz, width=12, height=5, font=('Arial'))
button_send.place(x=376, y=310, height=60, width=110)
root.bind('<Return>', send_msz, button_send)
root.mainloop()

