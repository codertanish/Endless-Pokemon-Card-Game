from tkinter import*
from PIL import ImageTk, Image
import random
root = Tk()
root.title("Endless Pokemon Game")
root.configure(bg = "lightgreen")
root.geometry("800x400")

player1_score = 0
player2_score = 0


charizard = ImageTk.PhotoImage(Image.open("Charizard_Pokemon_Card.png").resize((200,250)))
gengar = ImageTk.PhotoImage(Image.open("Gengar_Pokemon_Card.png").resize((200,250)))
pikachu = ImageTk.PhotoImage(Image.open("Pikachu_Pokemon_Card.png").resize((200,250)))
pikachuVMAX = ImageTk.PhotoImage(Image.open("PikachuVMAX_Pokemon_Card.png").resize((300,250)))
regieleki = ImageTk.PhotoImage(Image.open("RegielekiVMAX_Pokemon_Card.png").resize((200,250)))
snorlax = ImageTk.PhotoImage(Image.open("Snorlax_Pokemon_Card.png").resize((200,250)))
charizardVMAX = ImageTk.PhotoImage(Image.open("CharizardVMAX_Pokemon_Card.png").resize((200,250)))
mew = ImageTk.PhotoImage(Image.open("MewVMAX_Pokemon_Card.png").resize((200,250)))
snorlaxVMAX = ImageTk.PhotoImage(Image.open("SnorlaxVMAX_Pokemon_Card.png").resize((200,250)))
urshifu = ImageTk.PhotoImage(Image.open("UrshifuVMAX_Pokemon_Card.png").resize((250,250)))
venusaur = ImageTk.PhotoImage(Image.open("Venusaur_Pokemon_Card.png").resize((200,250)))
wailord = ImageTk.PhotoImage(Image.open("Wailord_Pokemon_Card.png").resize((200,250)))
pokeball = ImageTk.PhotoImage(Image.open("Pokeball_Button.jpg").resize((100,100)))

pokemon_list = [charizard, gengar, pikachu, pikachuVMAX, regieleki, snorlax, charizardVMAX, mew, snorlaxVMAX, urshifu, venusaur, wailord]
pokemon_HP_list = [270, 240, 240, 310, 310, 270, 330, 310, 340, 330, 270, 300]


header = Label(root, text = "Endless Pokemon Card Game", fg = "black", font = ("Comic Sans MS", 20, "bold"), bg = "lightgreen")
header.place(relx = 0.5, rely = 0.1, anchor = CENTER)

player1 = Label(root, text = "Player 1", fg = "black", bg = "lightblue", font = ("Comic Sans MS", 16, "bold"))
player1.place(relx = 0.15, rely = 0.3, anchor = CENTER)

score1 = Label(root, fg = "black", bg = "lightblue", font = ("Comic Sans MS", 12, "bold"))
score1.place(relx = 0.15, rely = 0.4, anchor = CENTER)

player2 = Label(root, text = "Player 2", fg = "black", bg = "lightblue", font = ("Comic Sans MS", 16, "bold"))
player2.place(relx = 0.85, rely = 0.3, anchor = CENTER)

score2 = Label(root, fg = "black", bg = "lightblue", font = ("Comic Sans MS", 12, "bold"))
score2.place(relx = 0.85, rely = 0.4, anchor = CENTER)

pokemon_card = Label(root, bg = "lightgreen")
pokemon_card.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def p1_attack():
    global player1_score
    pokemon_card_position1 = random.randint(0,11)
    pokemon_card_image1 = pokemon_list[pokemon_card_position1]
    pokemon_card["image"] = pokemon_card_image1
    player1_score += pokemon_HP_list[pokemon_card_position1]
    score1["text"] = player1_score
    
player1_button = Button(root, image = pokeball, relief = RAISED, command = p1_attack)
player1_button.place(relx = 0.15, rely = 0.6, anchor = CENTER)

def p2_attack():
    global player2_score
    pokemon_card_position2 = random.randint(0,11)
    pokemon_card_image2 = pokemon_list[pokemon_card_position2]
    pokemon_card["image"] = pokemon_card_image2
    player2_score += pokemon_HP_list[pokemon_card_position2]
    score2["text"] = player2_score


player2_button = Button(root, image = pokeball, relief = RAISED, command = p2_attack)
player2_button.place(relx = 0.85, rely = 0.6, anchor = CENTER)

root.mainloop()