from tkinter import *
# from tkinter import Label
from tkinter import  messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters =[choice(letters) for _ in range(randint(8, 10)) ]

    password_symbols =[choice(symbols) for _ in range(randint(2, 4)) ]

    password_numbers =[choice(numbers) for _ in range(randint(2, 4)) ]

    password_list = password_letters +password_symbols +password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    password_entery.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = webite_entery.get()
    email = email_entery.get()
    password = password_entery.get()
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="opps",message="please make sure you haven't empty. ")

    else:

        is_ok= messagebox.askokcancel(title=website,message=f"these are the details entered:\n Email:{email}"
                                     f"\n password:{password}\n is it ok to save?")
        if is_ok:

            with open("data.txt","a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                webite_entery.delete(0,END)
                password_entery.delete(0,END)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image= logo_img)
canvas.grid(row=0,column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password :")
password_label.grid(row=3,column=0)
# entery
webite_entery = Entry(width=35)
webite_entery.grid(row=1,column=1,columnspan=2)
webite_entery.focus()
email_entery = Entry(width=35)
email_entery.grid(row=2,column=1,columnspan=2)
email_entery.insert(0,"user@gmail.com")
password_entery = Entry(width=21)
password_entery.grid(row=3,column=1)
# buttons
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button =Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
