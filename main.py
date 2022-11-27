from datetime import date
from tkinter import *

window = Tk()
window.title("Age Calculator")
window.geometry("800x600")
window.resizable(False, False)


def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    # Label(text=f"{nameValue.get()}, your age is  {age}", font=("Helvetica", 23, "bold")).place(x=300, y=520)
    output.insert(END, f"{nameValue.get()}, your age is  {age}")


def close_window():
    window.destroy()
    exit()


photo_one = PhotoImage(file="Age calculator  .png")
myPhoto = Label(image=photo_one)
myPhoto.pack(padx=15, pady=15)

Label(text="Name", font=('arial', 20)).place(x=200, y=250)
Label(text="Day", font=('arial', 20)).place(x=200, y=300)
Label(text="Month", font=('arial', 20)).place(x=200, y=350)
Label(text="Year", font=('arial', 20)).place(x=200, y=400)

nameValue = StringVar()
dayValue = StringVar()
monthValue = StringVar()
yearValue = StringVar()

nameEntry = Entry(window, textvariable=nameValue, width=30, bd=10, bg="white", fg="black", font=('arial', 16, 'bold'))
nameEntry.place(x=300, y=250)
dayEntry = Entry(window, textvariable=dayValue, width=30, bd=10, bg="white", fg="black", font=('arial', 16, 'bold'))
dayEntry.place(x=300, y=300)
monthEntry = Entry(window, textvariable=monthValue, width=30, bd=10, bg="white", fg="black", font=('arial', 16, 'bold'))
monthEntry.place(x=300, y=350)
yearEntry = Entry(window, textvariable=yearValue, width=30, bd=10, bg="white", fg="black", font=('arial', 16, 'bold'))
yearEntry.place(x=300, y=400)
# As bd is higher, border is getting thicker

Button(window, text="Calculate Age", font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="black",
       command=calculateAge).place(x=300, y=470)

Button(window, text="Exit", font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="black",
       command=close_window).place(x=500, y=470)

output = Text(window, width=35, height=2, wrap=WORD, bg="white", fg="black", font=('arial', 16, 'bold'))
output.place(x=300, y=520)

if __name__ == "__main__":
    mainloop()

