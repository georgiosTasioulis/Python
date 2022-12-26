import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# Load image on screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_states = set()

# Read data from csv
data = pandas.read_csv("50_states.csv")

while True:
    # Prompt user to type answer in a textbox
    user_answer = screen.textinput(title=f"Guessed: {len(correct_states)}/50", prompt="What's the state?")
    user_answer = user_answer.title().strip()

    # If user writes "Exit" game finishes
    if user_answer == "Exit":
        break

    # Check if user typed an existing state
    for line in data.state:
        if user_answer == line:
            state_found = True
            correct_states.add(user_answer)
            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.goto(int(data[data.state == line].x), int(data[data.state == line].y))
            state_name.write(user_answer)

missed_states = {"Missed States": []}

for line in data.state:
    if line not in correct_states:
        missed_states["Missed States"].append(line)

# Create a csv file with missing states
df = pandas.DataFrame(missed_states)
df.to_csv("missed_states.csv")

df.to_csv("missed_states.csv")

