from replit import clear
#HINT: You can call clear() to clear the output in the console.

dict = {}

while True:
  print("Welcome to the secret auction program.") 
  
  name = input("What is your name?")
  
  if name not in dict.keys():
    bid = int(input("What's your bid?"))
    
    dict[name] = bid

    thereAreOthers = input("Are there any other bidders? Type 'yes' or 'no'.")

    if thereAreOthers == 'no':
      maxValue = max(dict.values())
  
      key = [k for k, v in dict.items() if v == maxValue][0]
  
      #print(key, dict[key])
      print(f"The winner is {key} with a bid of ${dict[key]}")
      
      break
      
    else:
      clear()

  else:
    clear()
    print("User already exist!")
    
      

      



  
 
  

  