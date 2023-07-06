print("welcome to the game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()

print("Let's begin!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else: 
    print("wrong")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else: 
    print("wrong")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct")
    score += 1
else: 
    print("wrong")


print("you got " + str(score))