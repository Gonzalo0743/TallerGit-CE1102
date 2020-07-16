from tkinter import *
import tkinter as tk
import winsound
import random
import pickle


class Open_Window:
    def __init__(self, master):
        self.open(Home_Window)
    def open(self, Twindow):
        Twindow(self)
    def switch_frame(self, Twindow, saved):
        print(saved)
        Twindow(self, saved)
        
        
class Home_Window:

    def __init__(self, inself):
        #Main Window
        self.canvas = Canvas( width = 800, height = 700,
                             highlightthickness = 0, relief='ridge')
        self.canvas.place(x=0,y=0)

        self.canvas.configure(bg='black')

        #Title "Clash Rooks"
        self.clash = Label(self.canvas, text= "CLASH", font=("padauk book",46),fg="white",bg="black")
        self.clash.place(x=315,y=50,width=197,height=47)

        self.rooks = Label(self.canvas, text= "ROOKS", font=("padauk book",46),fg="royalblue2",bg="black")
        self.rooks.place(x=310,y=110,width=214,height=47)

        #Buttons
        self.play = Button(self.canvas, text = "NEW GAME", font=("padauk book",28),fg="white",bg="black",borderwidth=0, command =lambda: [self.del_win(), inself.switch_frame(Game_Win, "new")])
        self.play.place(x=300,y=200,width=240,height=50)

        self.load = Button(self.canvas, text = "LOAD GAME", font=("padauk book",28),fg="white",bg="black",borderwidth=0, command = lambda: [self.del_win(), inself.switch_frame(Game_Win, "load")])
        self.load.place(x=295,y=260,width=250,height=50)

        self.instructions = Button(self.canvas, text = "INSTRUCTIONS", font=("padauk book",28),fg="white",bg="black",borderwidth=0)
        self.instructions.place(x=275,y=330,width=290,height=50)

        self.highscores = Button(self.canvas, text = "HIGHSCORES", font=("padauk book",28),fg="white",bg="black",borderwidth=0)
        self.highscores.place(x=280,y=390,width=260,height=50)

        self.credits = Button(self.canvas, text = "CREDITS", font=("padauk book",28),fg="white",bg="black",borderwidth=0,command= self.credits)
        self.credits.place(x=325,y=450,width=180,height=50)

    #Buttons Pressed
    def game(self):
        Game_Win(inself)
    def credits(self):
        Credits_Win()
    def del_win(self):
        self.canvas.destroy()
        
class Game_Win:
    def __init__(self, inself, saved):
        print (saved + " 2")
        self.can = Canvas( width = 800, height = 675, highlightthickness = 0, relief='ridge', bg= "black")
        self.can.place(x=0,y=0)

        self.save = Button(self.can, text = "Save Game", font=("padauk book",20),fg="white",bg="black",borderwidth=0,command= self.load)
        self.save.place(x=20, y=600)
        #self.canvas = Canvas( width = 375, height = 675, highlightthickness = 0, relief='ridge')
        #self.canvas.place(x=300,y=0)
        

        positions = (((300,0, 375,75),(375,0, 450,75),(450,0, 525,75),(525,0, 600,75),(600,0, 675,75)),
                     ((300,75, 375,150),(375,75, 450,150),(450,75, 525,150),(525,75, 600,150),(600,75, 675,150)),
                     ((300,150, 375,225),(375,150, 450,225),(450,150, 525,225),(525,150, 600,225),(600,150, 675,225)),
                     ((300,225, 375,300),(375,225, 450,300),(450,225, 525,300),(525,225, 600,300),(600,225, 675,300)),
                     ((300,300, 375,375),(375,300, 450,375),(450,300, 525,375),(525,300, 600,375),(600,300, 675,375)),
                     ((300,375, 375,450),(375,375, 450,450),(450,375, 525,450),(525,375, 600,450),(600,375, 675,450)),
                     ((300,450, 375,525),(375,450, 450,525),(450,450, 525,525),(525,450, 600,525),(600,450, 675,525)),
                     ((300,525, 375,600),(375,525, 450,600),(450,525, 525,600),(525,525, 600,600),(600,525, 675,600)),
                     ((300,600, 375,675),(375,600, 450,675),(450,600, 525,675),(525,600, 600,675),(600,600, 675,675)))

        self.table(positions, len(positions), len(positions[0])-1, 0, "C0L0", 0,0, saved)
    def table(self, positions, columm, lines, color, name, contli, contco, saved):
        
        #self.identi= self.can.find_overlapping(0, 0, 55, 200)
        if contco==columm:
            if saved == "load":
                #try:
                pickle_file=open('data.pickle', 'rb')
                rooks =pickle.load(pickle_file)
                print (saved + " 3")
                    
                self.load_game(rooks, 0, 1)
                #except:
                #    nothing=0

                
            self.can.create_rectangle(0,0, 55,55, fill='red')
            self.can.create_rectangle(0,100, 55,155, fill='yellow')
            self.identi0= self.can.find_overlapping(0, 0, 55, 55)
            self.identi1= self.can.find_overlapping(0, 57, 55, 100)
            #self.can.tag_raise(self.identi[0])
            
            self.can.tag_bind(self.identi0[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi0[0]))
            self.can.tag_bind(self.identi0[0], "<Button1-Motion>", self.move)
            self.can.tag_bind(self.identi0[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"one"))
            self.can.tag_bind(self.identi1[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi1[0]))
            self.can.tag_bind(self.identi1[0], "<Button1-Motion>", self.move)
            self.can.tag_bind(self.identi1[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"two"))
            
            self.object_mo = None
        elif contli<=lines and color==0 and contco<=columm:
            self.can.create_rectangle(positions[contco][contli][0], positions[contco][contli][1],
                                         positions[contco][contli][2], positions[contco][contli][3],
                                         width=1, fill='green',tags=name)
            return self.table(positions, columm, lines, 1, name[:-1] + str(int(name[3])+ 1), contli+1, contco, saved)
        elif contli<=lines and color==1 and contco<=columm:
            self.can.create_rectangle(positions[contco][contli][0], positions[contco][contli][1],
                                         positions[contco][contli][2], positions[contco][contli][3],
                                         width=1, fill='blue',tags=name)
            return self.table(positions, columm, lines, 0, name[:-1] + str(int(name[3])+ 1), contli+1, contco, saved)
        elif contco<columm:
            return self.table(positions, columm, 4, color, "C"+str(int(name[1])+1)+"L0", 0, contco+1, saved)
        
    def load_game(self, rooks, rook, place):
        #print (rooks[rook])
        #print (rook)
        #print (len(rooks)-2)
        if rook == len(rooks)-2:
            self.create(rooks[rook], rooks[place], (rooks, rook, place, False))
            
        else:
            self.create(rooks[rook], rooks[place], (rooks, rook, place, True))
            #self.load_game(rooks, rook+2, place+2)
            
        
    def press_boton(self, event, ID):
        rook = ID
        self.selected_rook = (rook, event.x, event.y)
    def move(self,event):
        self.squads = ("C0L0", "C0L1", "C0L2", "C0L3", "C0L4", "C1L0", "C1L1", "C1L2", "C1L3", "C1L4",
                  "C2L0", "C2L1", "C2L2", "C2L3", "C2L4", "C3L0", "C3L1", "C3L2", "C3L3", "C3L4",
                  "C4L0", "C4L1", "C4L2", "C4L3", "C4L4", "C5L0", "C5L1", "C5L2", "C5L3", "C5L4",
                  "C6L0", "C6L1", "C6L2", "C6L3", "C6L4", "C7L0", "C7L1", "C7L2", "C7L3", "C7L4",
                  "C8L0", "C8L1", "C8L2", "C8L3", "C8L4", "C9L0", "C9L1", "C9L2", "C9L3", "C9L4")
        x, y = event.x, event.y
        rook, x1, y1 = self.selected_rook
        self.can.move(rook, x-x1, y-y1)
        self.selected_rook = (rook, x, y)
        
        #self.new_position(squads, 0, x, y, rook)
    def load (self):
        pickle_file = open('data.pickle', 'wb')
        pickle.dump(self.data, pickle_file)
        pickle_file.close()
        pickle_file=open('data.pickle', 'rb')
        data= pickle.load(pickle_file)
        print(data)
    def create(self, rook, place, info):
        if rook == "one":
            self.object = Label (self.can,  bg="red")
            self.object.place(x=place[0], y=place[1], width=55,height=55)
        elif rook == "two":
            self.object = Label (self.can,  bg="yellow")
            self.object.place(x=place[0], y=place[1], width=55,height=55)
        data = (rook, place)
        try:
            self.data= self.data + data
        except:
            self.data= data
        if info ==  "gaming":
            self.rooks(rook)
        else:
            if info[3] == True:
                self.load_game(info[0], info[1]+2, info[2]+2)
        
    def rooks(self, rook):
        
        if rook == "one":
            #self.can.addtag_withtag("run", self.identi0[0] )
            self.can.create_rectangle(0,0, 55,55, fill='red')
        elif rook == "two":
            self.can.create_rectangle(0,100, 55,155, fill='yellow')
        self.identi0= self.can.find_overlapping(0, 0, 55, 55)
        self.identi1= self.can.find_overlapping(0, 100, 55, 155)
        
            #print((self.can.gettags(self.identi0[0])))
        self.can.tag_bind(self.identi0[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi0[0]))
        self.can.tag_bind(self.identi0[0], "<Button1-Motion>", self.move)
        self.can.tag_bind(self.identi0[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"one"))
        self.can.tag_bind(self.identi1[0], "<ButtonPress-1>", lambda event: self.press_boton(event,self.identi1[0]))
        self.can.tag_bind(self.identi1[0], "<Button1-Motion>", self.move)
        self.can.tag_bind(self.identi1[0], "<ButtonRelease-1>", lambda event: self.new_position(event,"two"))
        

    def new_position(self, event ,rook):
        
        if rook=="one":
            ID=self.identi0[0]
        elif rook == "two":
            ID=self.identi1[0]
        over=self.can.coords(ID)
        #print(self.identi)
        #print(ID)
        #print(len(self.can.find_overlapping(over[0], over[1], over[2], over[3])))
        if self.can.coords(self.squads[0])[0]-10<=over[2]<=self.can.coords(self.squads[0])[2] and self.can.coords(self.squads[0])[1]<=over[3]<=self.can.coords(self.squads[0])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(310,10, 365,65)
            self.create(rook, lis, "gaming")
            #self.can.coords(ID, 310,10, 365,65)
            #print((self.can.gettags(self.identi0[0])))
            
                
        elif self.can.coords(self.squads[1])[0]-10<=over[2]<=self.can.coords(self.squads[1])[2]and self.can.coords(self.squads[0])[1]<=over[3]<=self.can.coords(self.squads[0])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis = (385,10, 440,65)
            self.create(rook, lis, "gaming")

        elif self.can.coords(self.squads[2])[0]-10<=over[2]<=self.can.coords(self.squads[2])[2]and self.can.coords(self.squads[0])[1]<=over[3]<=self.can.coords(self.squads[0])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(460,10, 515,65)
            self.create(rook, lis, "gaming")

        elif self.can.coords(self.squads[3])[0]-10<=over[2]<=self.can.coords(self.squads[3])[2]and self.can.coords(self.squads[0])[1]<=over[3]<=self.can.coords(self.squads[0])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(535,10, 590,65)
            self.create(rook, lis, "gaming")

        elif self.can.coords(self.squads[4])[0]-10<=over[2]<=self.can.coords(self.squads[4])[2]and self.can.coords(self.squads[0])[1]<=over[3]<=self.can.coords(self.squads[0])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(610,10, 665,65)
            self.create(rook, lis, "gaming")
            
        elif self.can.coords(self.squads[5])[0]-10<=over[2]<=self.can.coords(self.squads[5])[2]and self.can.coords(self.squads[5])[1]<=over[3]<=self.can.coords(self.squads[5])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(310,85, 365,140)
            self.create(rook, lis, "gaming")
        elif self.can.coords(self.squads[6])[0]-10<=over[2]<=self.can.coords(self.squads[6])[2]and self.can.coords(self.squads[5])[1]<=over[3]<=self.can.coords(self.squads[5])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(385,85, 440,140)
            self.create(rook, lis, "gaming")
        elif self.can.coords(self.squads[7])[0]-10<=over[2]<=self.can.coords(self.squads[7])[2]and self.can.coords(self.squads[5])[1]<=over[3]<=self.can.coords(self.squads[5])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(460,85, 515,140)
            self.create(rook, lis, "gaming")
        elif self.can.coords(self.squads[8])[0]-10<=over[2]<=self.can.coords(self.squads[8])[2]and self.can.coords(self.squads[5])[1]<=over[3]<=self.can.coords(self.squads[5])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(535,85, 590,140)
            self.create(rook, lis, "gaming")
        elif self.can.coords(self.squads[9])[0]-10<=over[2]<=self.can.coords(self.squads[9])[2]and self.can.coords(self.squads[5])[1]<=over[3]<=self.can.coords(self.squads[5])[3]and len(self.can.find_overlapping(over[0], over[1], over[2], over[3]))<=2:
            self.can.delete(ID)
            lis=(610,85, 665,140)
            self.create(rook, lis, "gaming")

        else:
            if rook == "one":
                self.can.coords(ID, 0,0, 55,55)  
            elif rook == "two":
                self.can.coords(ID, 0,100, 55,155)
        
            
        
        #over=self.can.coords(squads[i])
        #touch=self.can.find_overlapping(over[0], over[1], over[2], over[3])
        
        #touch[6]
        #self.selected_rook = (rook, x, y)
        #self.new_position (squads, i+1, x, y, rook)
            
             

        

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

        self.author1 = Label(self.canvas,text = "FRANCISCO ZAMORA CORRALES", font=("padauk book",30),fg="white",bg="black",borderwidth=0)
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
    home_window = Open_Window(window)
    window.title("Clash Rooks")
    window.minsize(800,700)

