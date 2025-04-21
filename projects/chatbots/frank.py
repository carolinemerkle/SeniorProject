hoursInDay= 24
goalHoursOutside = 6


print("Hello! My name is Frank.")
userName = input("Whats your name?")
print("Nice to meet you " + userName)

print("Did you go outside today?")
didYouGoOutside = input("Yes or No?")

while didYouGoOutside.lower() == "yes":
  print("thats great!")
  hoursOutside = input("How many hours did you go outside?")
  hoursOutside = int(hoursOutside)
  if hoursOutside >= goalHoursOutside:
    print("Thats great! You went outside for " + str(hoursOutside) + " hours! You are doing great!")
    break
  else:
    print("go outside")
    break

while didYouGoOutside.lower() == "no":
  print("\nyou are a failure")
  print("\ndishonor on you, dishonor on your family,\n dishonor on your cow")
  print("\nGo outside right now and think about what you have done " + userName)
  break
