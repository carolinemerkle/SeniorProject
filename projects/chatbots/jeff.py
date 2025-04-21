

print('hello there! my name is jeff')
userName = input('what is your name?')

print(userName + " wow thats a stupid name")

userAge = input('how old are you?')

print(userAge + " wow you are old thats embarassing")

print("do you want me to tell you when and how you will die?")
perdictDeath = input("type yes or no")

while perdictDeath == "yes":
  favNumber = input("whats your favorite number")
  favNumber = float(favNumber)
  if favNumber >= 100.0 :
    print("ur dumb")
    print("you will die on march 16 2053 at 2pm")
    break
  elif favNumber <100 :
    print("thats a really stupid number")
    print("you will die in 7 days ")
    break
  elif favNumber == 69.0 :
    print("nice")
    print("you will die in 2 days")  
    break
  elif favNumber <=69.0 :
    print("ok wierdo")
    print("you gonna die never")
    break
while perdictDeath == "no":
  print("ur lame")  
  print("ima kill you now ")
