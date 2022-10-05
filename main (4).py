print("Let's guess the area of your rectangle")

L =int(input("What is the length of your rectangle?: "))
# This line asks for the length of their rectangle
W =int(input("What is the width of your rectangle?: ")) 
# This line asks for the width of their rectangle
guess = int(input("What is the area of this rectangle?: "))  
# This line asks for their guess of the area
a = L * W
# This line calculates the correct answer

if guess == a :
  print("Good job, that is correct")
# This line tell the user their guess is correct
else:
  print("Incorrect, the answer was " + str(a))
# This line tell the user their guess is incorrect and gives them the real answer
          