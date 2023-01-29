from art import logo

print(logo)

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def div(x, y):
  return x / y

def mult(x, y):
  return x * y


dic_op = {
  "+" : add,
  "-" : sub,
  "/" : div,
  "*" : mult
}

def calculator():
  num1 = float(input("What's the first number?: "))
  
  should_cont = True
  while should_cont:
    
    for key in dic_op:
      print(key)
  
    op_symbol = input("Pick an operation from the above line: ")
  
    num2 = float(input("What's the second number?: "))
  
    function = dic_op[op_symbol]
  
    answer = function(num1, num2)
    
    print(f"{num1} {op_symbol} {num2} = {answer}")
  
    want_to_continue = input("'yes' for continue in this operation, 'no' for create a new one? ")
  
    if want_to_continue == "yes":
      num1 = answer
    
    else:
      should_cont = False
      calculator()

calculator()

