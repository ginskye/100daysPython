from turtle import Turtle, Screen
# import prettytable
# cat = Turtle()
#
# print(cat)
# cat.shape('turtle')
# cat.color('green')
# cat.forward(100)
# cat.pencolor('red')

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable, from_csv
table = PrettyTable()
print(table)
table.add_column("Pokemon Name",["pikachu","squirtle", "charmander"])
table.add_column("Type", ["Electric", "water", "fire"])

from prettytable import from_csv 
fp = open("pokedex.csv", "r") 
poketable = from_csv(fp) 
fp.close()

#with open('pokedex.csv', ) as fp:
#    poketable = from_csv(fp)
print(poketable)
