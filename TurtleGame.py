from turtle import Turtle, Screen
import random

# Configurazione iniziale dello schermo
is_race_on = False
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)

# Prompt per l'input dell'utente con un messaggio più chiaro
user_bet = screen.textinput(title="Fai la tua scommessa!", prompt="Quale tartaruga vincerà la gara? Scegli un colore tra: rosso, arancione, giallo, verde, blu o viola:")

# Lista di colori e posizioni delle tartarughe
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Creazione delle tartarughe e posizionamento iniziale
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtles.append(new_turtle)

# Avvia la gara se l'utente ha inserito una scommessa
if user_bet:
    is_race_on = True

# Loop della gara
while is_race_on:
    for turtle in all_turtles:
        # Controllo se una tartaruga ha raggiunto il traguardo
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Messaggio di vittoria o sconfitta migliorato
            if winning_color == user_bet.lower():
                print(f"Congratulazioni! Hai vinto! La tartaruga {winning_color} ha vinto la gara!")
            else:
                print(f"Peccato, hai perso. La tartaruga vincente è {winning_color}. Meglio fortuna la prossima volta!")

        # Movimento casuale per ogni tartaruga
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Chiudi la finestra con un clic
screen.exitonclick()
