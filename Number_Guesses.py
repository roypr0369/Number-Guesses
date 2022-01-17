import random
x = random.randint(0 , 100000)
random_num = random.randint(x , x + 20)
ask = input("Are you Ready to Play? (y/n) ").lower()
if ask == "y":
  print("Rules of the Game: \n")
  print("You got 5 attempts to guess the and you have 3 hints to use. You can type end anytime to end the game \n")
  prev = -1
  chance = 5
  hint = 3
  while (chance > 0) & (hint > 0):
    n = input("")
    if (prev == -1) & (n == "hint"):
      print("Idiot!!! First guess the number...lol!!!")
    elif (prev >= 0) & (n == "hint"):
      if(prev < random_num):
        print("Your Number is Too Low!!!")
      else:
        print("Your Number is Too High!!!")
      hint -= 1
    elif n == "end":
      print("You ended the game!!!")
      quit()
    else:
      flag = True
      for j in range(0 ,len(n)):
        if ((n[j] >= "a") & (n[j] <= "z")) | ((n[j] >= "A") & (n[j] <= "Z")):
          print("Idiot!!! Type a Number")
          flag = False
          break
      if flag:
        n = int(n) 
        if(n == random_num):
          print("Right Guess. You win the Game!!!")
          quit()
        prev = n
      chance -= 1
    print("You have got " + str(chance) + " chances left and " + str(hint) + " left")
  print("You lost the game (:  Better luck next time , I was thinking of " + str(random_num))      
elif ask =="n":
  print("You ended the game!!!")
  quit()
else:
  print("Idiot!!! Answer only in (y/n)")
