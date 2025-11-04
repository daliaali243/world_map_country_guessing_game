import turtle,pandas

from score import Score

screen = turtle.Screen()
screen.bgpic('map.gif')
screen.title("map game")
screen.setup(width=700, height=400)
screen.bgpic('map.gif')
data = pandas.read_csv('coordinates.csv')
locations=data['country'].to_list()
guessed=[]
missed=[]

while len(guessed)< len(locations):
    answer = screen.textinput(title=f'{len(guessed)}/22 guessed', prompt='Enter a country: ').title()
    if answer in locations:
        guessed.append(answer)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_location=float(data[data.country == answer]['x'].item())
        y_location=float(data[data.country==answer]['y'].item())
        t.goto(x_location,y_location)
        t.hideturtle()
        t.fillcolor('red')
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.write(answer,font=('Arial',10,'bold'))

    elif answer == 'Exit':
        for country in locations:
            if country not in guessed:
                missed.append(country)
        fincal_csv =pandas.DataFrame(missed).to_csv('missed.csv')
        break



