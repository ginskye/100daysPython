import art
from replit import clear
print(art.calc_logo)

#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
keep_going ="no"
while keep_going== "no":
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)


  operation_symbol = input("Pick an operation: ") 
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {first_answer}")

#Here we select "*" which overides the "+" we selected on line 26.

  keep_going = input("fContinue with {first_answer}? \n  Type yes, or no to start again: \n") 
  if keep_going=="yes":
    operation_symbol = input("Choose your operation: ")
    num3 = float(input("What's the next number?: "))

#Here the calculation_function selected will be the multiply() function
    calculation_function = operations[operation_symbol] 

#Here the code will be:
#second_answer = multiply(multiply(num1, num2), num3)
    second_answer = calculation_function(calculation_function(num1, num2), num3)

    second_answer = calculation_function(first_answer, num3)

    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
  else:
    clear()
