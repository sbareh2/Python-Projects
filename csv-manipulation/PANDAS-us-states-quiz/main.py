import turtle as t
import pandas

screen = t.Screen()
screen.title('U.S. States Game')
screen.addshape('blank_states_img.gif')

t.shape('blank_states_img.gif')

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# t.onscreenclick(get_mouse_click_coor)
#
# t.mainloop()

data = pandas.read_csv('50_states.csv')

states_list = data.state.to_list()
guessd_states = []

while len(guessd_states) < 50:

    answer_state = screen.textinput(title=f'{len(guessd_states)}/50 States Correct', prompt='What\'s another state\'s name?')
    new_input = answer_state.title()
    if new_input == 'Exit':
        missing_states = []
        for state in states_list:
            if state not in guessd_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn')
        break
    if new_input in states_list:
        if new_input not in guessd_states:
            guessd_states.append(new_input)
        answer = t.Turtle()
        answer.hideturtle()
        answer.penup()
        state_data = data[data.state == new_input]
        answer.goto(int(state_data.x), int(state_data.y))
        answer.write(state_data.state.item())





screen.exitonclick()
