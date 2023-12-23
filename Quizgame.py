print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0

# First Question
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("You are correct!")
    score = score + 1
else: 
    print("Incorrect!")

# Second Question    
answer = input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("You are correct!")
    score = score + 1
else: 
    print("Incorrect!")

# Third Question
answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("You are correct!")
    score = score + 1
else: 
    print("Incorrect!")
    
# Fourth Question
answer = input("What does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("You are correct!")
    score = score + 1
else: 
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + " questions correct!")