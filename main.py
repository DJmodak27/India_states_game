import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "blank_india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("data.csv")
all_states = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title =f"{len(guess_state)}/31 States Correct",
                                    prompt="What's the another name?").title()

    if answer_state == 'Exit':
        missing_sate = []
        for state in all_states:
            if state not in answer_state:
                missing_sate.append(state)
        new_data = pandas.DataFrame(missing_sate)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)



