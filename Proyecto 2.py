from tkinter import *
import tkinter as tk
import winsound
import random

class Home_Window:

    def __init__(self,master):

        #Main Window
        self.canvas = Canvas(master, width = 800, height = 600,
                             highlightthickness = 0, relief='ridge')
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        #Title "Clash Rooks"
        self.clash = Label(self.canvas, text= "CLASH", font=("padauk book",46),fg="white",bg="black")
        self.clash.place(x=300,y=50,width=197,height=47)

        self.rooks = Label(self.canvas, text= "ROOKS", font=("padauk book",46),fg="royalblue2",bg="black")
        self.rooks.place(x=295,y=110,width=214,height=47)

        #Buttons
        self.play = Button(self.canvas, text = "NEW GAME", font=("padauk book",28),fg="white",bg="black",borderwidth=0)
        self.play.place(x=285,y=200,width=230,height=50)

        self.load = Button(self.canvas, text = "LOAD GAME", font=("padauk book",28),fg="white",bg="black",borderwidth=0)
        self.load.place(x=280,y=260,width=240,height=50)

        self.instructions = Button(self.canvas, text = "INSTRUCTIONS", font=("padauk book",28),fg="white",bg="black",borderwidth=0)
        self.instructions.place(x=260,y=320,width=290,height=50)

        self.highscores = Button(self.canvas, text = "HIGHSCORES", font=("padauk book",28),fg="white",bg="black",borderwidth=0)
        self.highscores.place(x=275,y=380,width=260,height=50)

        self.credits = Button(self.canvas, text = "CREDITS", font=("padauk book",28),fg="white",bg="black",borderwidth=0,command= self.credits)
        self.credits.place(x=310,y=440,width=180,height=50)

    #Buttons Pressed
    def credits(self):
        Credits_Win()
        


class Credits_Win:

    def __init__(self):

        self.canvas = Canvas(window, width = 800, height = 600,
                             highlightthickness = 0, relief='ridge')
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        #All the credits
        self.country = Label(self.canvas,text = "COSTA RICA", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.country.place(x=10,y=10,width=244,height=30)       

        self.university = Label(self.canvas,text = "ITCR", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.university.place(x=10,y=50,width=100,height=30)
        
        self.career = Label(self.canvas,text = "COMPUTER ENGINEERING", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.career.place(x=10,y=90,width=520,height=30)

        self.professor = Label(self.canvas,text = "PROF. LUIS BARBOZA ARTAVIA", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.professor.place(x=10,y=130,width=610,height=30)

        self.version = Label(self.canvas,text = "CLASH ROOKS V1", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.version.place(x=10,y=170,width=350,height=30)

        self.author = Label(self.canvas,text = "GONZALO ACUÑA MADRIGAL", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.author.place(x=10,y=210,width=570,height=30)

        self.author1 = Label(self.canvas,text = "FRANCISCO CORRALEZ ZAMORA", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.author1.place(x=10,y=250,width=650,height=30)

        self.year = Label(self.canvas,text = "2020", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.year.place(x=10,y=290,width=90,height=30)

        self.credits = Label(self.canvas,text = "-------------------------CREDITS-------------------------", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
        self.credits.place(x=0,y=370,width=800,height=30)

        #Back Button
        self.backbutton = Button(self.canvas, text = "BACK", font=("padauk book",30),fg="white",bg="black",borderwidth=0,command=self.backbutton)
        self.backbutton.place(x=340,y=450,width=120,height=50)

    def backbutton(self):
        self.canvas.destroy()



if __name__ == "__main__":
    window = Tk()
    home_window = Home_Window(window)
    window.title("Clash Rooks")
    window.minsize(800,600)
 
    window.mainloop()
