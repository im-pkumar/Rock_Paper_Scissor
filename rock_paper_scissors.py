from tkinter import *
from tkinter import messagebox
import os
import threading
from PIL import Image, ImageTk
import random as rdm

color = {'rock': "#A90404", 'paper':"#0CB7E2", 'scissors':"#E8001B"}
boy = ['B1.png']
girl = ['G1.png']
options = ["ROCK", "PAPER", "SCISSORS", "PAPER", "SCISSORS", "ROCK", "SCISSORS", "PAPER", "ROCK" ]
opt = []
pname = ["Player 1", "Player 2"]

win = Tk()
win.configure(bg = "#2B2B2B")
win.state("zoomed")
win.resizable(False, False)
win.title("Rock Paper Scissors Game")
icon = PhotoImage(file = f"{os.getcwd()}/images/logo.png")
win.iconphoto(False, icon)

root = Frame(bg = "#2b2b2b")
root.place(relx =0 , rely =0 , relheight=1, relwidth=1)

middle_image = PhotoImage(file = f"{os.getcwd()}/images/RPS.png")
middle_l = Label(root, text = "Middle Logo Image", image = middle_image, bg = "#2B2B2B", fg = "Black", font = ("Sans Serif", 28, "bold"))
middle_l.image = middle_image
middle_l.place(relx = 0.175, rely = 0.1)

bottom_image = PhotoImage(file = f"{os.getcwd()}/images/bottom.png")
bottom_l = Label(root, text = "Bottom Children Image", image = bottom_image, bg = "#2b2b2b", fg = "Black", font = ("Sans Serif", 28, "bold"))
bottom_l.image = bottom_image
bottom_l.place(relx = 0.05, rely = 0.7)
bottom_image = PhotoImage(file = f"{os.getcwd()}/images/bottom.png")
bottom_l = Label(root, text = "Bottom Children Image", image = bottom_image, bg = "#2b2b2b", fg = "Black", font = ("Sans Serif", 28, "bold"))
bottom_l.image = bottom_image
bottom_l.place(relx = 0.5, rely = 0.7)

def get_result(pname):
    global opt

    if opt[0] == "PAPER" and opt[1] ==  "SCISSORS":
        result = pname[0]
    elif opt[0] == "PAPER" and opt[1] == "ROCK":
        result = pname[1]
    elif opt[0] == "SCISSORS" and opt[1] == "ROCK":
        result = pname[1]
    elif opt[0] == "SCISSORS" and opt[1] == "PAPER":
        result = pname[0]
    elif opt[0] == "ROCK" and opt[1] == "PAPER":
        result = pname[1]
    elif opt[0] == "ROCK" and opt[1] == "SCISSORS":
        result = pname[0]
    elif opt[0] == opt[1]:
        result = "Tie"

    return result


def mainscreen():
    root.destroy()
    banner_image = PhotoImage(file = f"{os.getcwd()}/images/banner.png")
    banner_l = Label(win, text = "ROCK PAPER SCISSORS - GAME", image = banner_image, bg = "#2B2B2B", fg = "Black", font = ("Sans Serif", 28, "bold"))
    banner_l.image = banner_image
    banner_l.place(relx = 0.3, rely = 0.0)

    changing_f = Frame(win, bg = "#2B2B2B")
    changing_f.place(relx =0 , rely =0.2 , relheight=0.8, relwidth=1)

    def show_winner(winner):
        if winner != "Tie":
            winner_img = PhotoImage(file = f"{os.getcwd()}/images/winner.png")
        else:
            winner_img = PhotoImage(file = f"{os.getcwd()}/images/tie.png")

        win_l = Label(changing_f, text = "Winner", image = winner_img, bg = "#2b2b2b", fg = "white", font = ("Sans Serif", 18, "normal"))
        win_l.image = winner_img
        win_l.place(relx = 0.415, rely = 0.1)

        win_player = Label(changing_f, text = winner, bg = "#2b2b2b", fg = "white", font = ("Sans Serif", 18, "bold"), width = 34)
        win_player.place(relx = 0.3, rely = 0.5)

        global options, opt
        rdm.shuffle(options)
        opt = []
        t2 = threading.Timer(5, mainscreen)
        t2.start()

#   ******************************************* PLAYER - 1  ********************************************************

    def player1_option():
        global opt
        o = rdm.choice(options)
        opt.append(o)
        print(opt[0])
        choice_l = Label(player1_f, text = opt[0], bg = "#2b2b2b", fg = "white", font = ("Sans Serif", 18, "normal"))
        choice_l.grid(row = 3, column = 0, padx = 5, pady = 5)

        choice_img = PhotoImage(file = f"{os.getcwd()}/images/{opt[0].lower()}.png")
        choice = Label(changing_f, image = choice_img, bg = "#2b2b2b", fg = "white", font = ("Sans Serif", 18, "normal"))
        choice.image = choice_img
        choice.place(relx = 0.31, rely = 0.65)

    player1_f = Frame(changing_f, bg = "#2b2b2b")
    player1_f.place(relx = 0.05, rely = 0.075, relheight = 0.75, relwidth = 0.25)

    p1 = PhotoImage(file = f"{os.getcwd()}/images/{boy[0]}")
    p1_profile = Label(player1_f, image = p1)
    p1_profile.image = p1
    p1_profile.grid(row = 0, column = 0, padx=5, pady=8)
   
    p1_name = Entry(player1_f, font = ("Sans Serif", 20, "bold"), fg = "white", bg = color["paper"], width = 22, bd = 0, justify = 'center')
    p1_name.grid(row = 1, column = 0,padx = 4)
    p1_name.insert(0, pname[0])

    p1_b = Button(player1_f, text = "Click For Response", command = player1_option, font = ("Sans Serif", 16, "bold"), bg = "white", fg = color["paper"], width = 25, bd = 2)
    p1_b.grid(row = 2, column = 0, padx = 4, pady = (5,0))

#   ******************************************* PLAYER - 2  ********************************************************

    def player2_option():
        global opt
        o = rdm.choice(options)
        opt.append(o)
        print(opt[1])
        choice_l = Label(player2_f, text = opt[1], bg = "#2b2b2b", fg = "white", font = ("Sans Serif", 18, "normal"))
        choice_l.grid(row = 3, column = 0, padx = 5, pady = 5)

        choice_img = PhotoImage(file = f"{os.getcwd()}/images/{opt[1].lower()}.png")
        choice = Label(changing_f, image = choice_img, bg = "#2b2b2b", fg = "white", font = ("Sans Serif", 18, "normal"))
        choice.image = choice_img
        choice.place(relx = 0.56, rely = 0.65)
        global pname
        pname = [p1_name.get(), p2_name.get()]
        res = get_result(pname)
        show_winner(res)

    player2_f = Frame(changing_f, bg = "#2b2b2b")
    player2_f.place(relx = 0.675, rely = 0.075, relheight = 0.75, relwidth = 0.25)

    p2 = PhotoImage(file = f"{os.getcwd()}/images/{girl[0]}")
    p2_profile = Label(player2_f, image = p2)
    p2_profile.image = p2
    p2_profile.grid(row = 0, column = 0, padx=5, pady=8)

    p2_name = Entry(player2_f, font = ("Sans Serif", 20, "bold"), fg = "white", bg = color["scissors"], width = 22, bd = 0, justify = 'center')
    p2_name.grid(row = 1, column = 0,padx = 4)
    p2_name.insert(0, pname[1])

    p2_b = Button(player2_f, text = "Click For Response", command = player2_option, font = ("Sans Serif", 16, "bold"), bg = "white", fg = color["scissors"], width = 25, bd = 2)
    p2_b.grid(row = 2, column = 0, padx = 4, pady = (5,0))


t = threading.Timer(2, mainscreen)
t.start()

win.mainloop()