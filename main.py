#Program Written by Dillon Porter
# Just a simple Trivia game wrapped in a while loop to ensure asking users to play again
while True:
  print("Hello, welcome to the Toronto Maple Leafs Trivia game!")
  print("\n")
  answer = input("Are you ready to play (yes/no): ")
  score = 0
  total_q = 10
  print("\n")
  if answer.lower() == "yes":
    answer = input("1. What is Auston Matthew's nickname? ")
  else:
    answer.lower() == "no"
    print("Okay, goodbye")
    break
  if answer == "Papi":
    score += 1
    print("Correct!")
  elif answer == "papi":
    score +=1
    print("Correct")
  else:
    print("Incorrect!")

  print("\n")

  answer = input("2. What is Auston Matthew's jersey number? ")
  if answer == "34":
    score += 1
    print("Correct!")
  else:
    print("Incorrect!")

  print("\n")

  answer = input("3. Which Toronto Maple Leaf player had to most penalty minutes? ")
  if answer == "Tie Domi":
    score += 1
    print("Correct!")
  elif answer == "Domi":
    score += 1
    print("Correct")
  elif answer == "28":
    score += 1
    print("Correct")
  elif answer == "domi":
    score += 1
    print("Correct")
  elif answer == "tie domi":
    score += 1
    print("Correct")
  elif answer == "Tie domi":
    score += 1
    print("Correct")
  else:
    print("Incorrect!")

  print("\n")

  answer = input("4. Which player of the Toronto Maple Leafs scored the most goals? ")
  if answer == "Mats Sundin":
    score += 1
    print("Correct")
  elif answer == "Sundin":
    score += 1
    print("Correct")
  elif answer == "13":
    score += 1
    print("Correct")
  elif answer == "sundin":
    score += 1
    print("Correct")
  elif answer == "Mats sundin":
    score += 1
    print("Correct")
  else:
    print("Incorrect")
  
  print("\n")

  answer = input("5. What year was it when the Toronto Maple Leafs last won the Stanley Cup? ")
  if answer == "1967":
    score += 1
    print("Correct!")
  elif answer == "67":
    score += 1
    print("Correct!")
  else:
    print("Incorrect!")

  print("\n")

  answer = input("6. What number did Curtis Joseph (Cujo) wear? ")
  if answer == "31":
    score += 1
    print("Correct!")
  else:
    print("Incorrect!")

  print("\n")

  answer = input("7. What team did the Leafs lose to against a zamboni driver who worked for them? ")
  if answer == "Carolina Hurricanes":
    score += 1
    print("Correct!")
  elif answer == "Hurricanes":
    score += 1
    print("Correct")
  elif answer == "hurricanes":
    score += 1
    print("Correct!")
  elif answer == "carolina":
    score += 1
    print("Correct!")
  elif answer == "carolina hurricanes":
    score += 1
    print("Correct!")
  else:
    print("Incorrect!")

  print("\n")

  answer = input("8. Who was the first Leaf to score 100 points in a season? ")
  if answer == "Darryl Sittler ":
    score += 1
    print("Correct!")
  elif answer == "Sittler": 
    score += 1
    print("Correct!")
  elif answer == "sittler": 
    score += 1
    print("Correct!")
  elif answer == "darryl sittler": 
    score += 1
    print("Correct!")
  elif answer == "27": 
    score += 1
    print("Correct!")
  else:
    print("Incorrect!")
  
  print("\n")

  answer = input("9. Who was the goalie when the leafs won the cup in 1967? ")
  if answer == "Terry Sawchuk":
    score += 1
    print("Correct!")
  elif answer == "Sawchuk":
    score += 1
    print("Correct!")
  elif answer == "sawchuk":
    score += 1
    print("Correct!")
  elif answer == "terry sawchuk":
    score += 1
    print("Correct!")
  elif answer == "30":
    score += 1
    print("Correct!")
  else:
    print("Incorrect!")

  print("\n")

  answer = input("10. How many goals did Auston Matthews score during his NHL debut? ")
  if answer == "4":
    score += 1
    print("Correct!")
  else:
    print("Incorrect!")

  print("You got", score, "questions correct!");
  mark = (score/total_q) * 100
  print("\n")
  print("Mark: ", str(mark) + "%") ##Converting number to a string
  print("\n")
  print ("Thank-you for playing!")
  print("\n")
  try_again = int(input("Press 1 to try again, 0 to exit. "))
  if try_again == 0:
    break