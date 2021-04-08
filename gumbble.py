from tkinter import *
from tkinter import messagebox
import random

answer = [
	"css",
	"php",
	"html",
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
	"scs",
	"pph",
	"hltm",
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]


num=random.randrange(0,len(words),1)

def auto():
	global words, answer, num
	label.config(text=words[num])
	
def res():
    global words,answers,num
    num = random.randrange(0, len(words), 1)
    label.config(text = words[num])
    etn.delete(0, END)


def chkans():
    global words,answer,num
    var = etn.get()
    if var == answer[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        res()
    else:
       	messagebox.showerror("Error", "This is a wrong answer")
       	etn.delete(0, END)



root=Tk()
root.title("Gumble Words")
root.config(bg="#2f3542")

label=Label(root,
text="Your Text", 
font=("Verdana" , 18), 
bg="#2f3542",
fg="#ced6e0"
)

label.pack(pady=30)

etnv= StringVar

etn=Entry(root,
font=("Verdana", 16),
textvariable=etnv
)

etn.pack()

btnchk=Button(root,
text="Check",
font=("Comic sans ms", 16),
width=10,
bg="#57606f",
fg="#a4b0be",
command=chkans
)

btnchk.pack(pady=40)

rstbtn=Button(root,
text="Reset",
font=("Comic sans ms", 16),
bg="#57606f",
fg="#ff6b81",
width=10,
command=res
)

rstbtn.pack()

auto()

root.mainloop()