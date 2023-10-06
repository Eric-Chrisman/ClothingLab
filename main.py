# gets hat size
def getHatSize(weight, height):
  hatSize = (weight * 2.9) / height
  
  return hatSize


# gets jacket size
def getJacketSize(weight, height, age):
  jacketSize = (weight * height) / 288

  #every 10 years above 30 (starting at 30), add (1/8) to our jacket size total
  if age > 30:
    decadesOldFromThirdy = (30 - age) // 10
    jacketSize += decadesOldFromThirdy * (1/8)
  
  return jacketSize


# gets waist size
def getWaistSize(weight, age):
  waistSize = weight / 5.7

  #every two years above 28 (starting at 28), add (1/10) to our waist size total
  if age > 28:
    amountOfTwoYearsFromTwentyEight = (28 - age) // 2
    waistSize += amountOfTwoYearsFromTwentyEight * (1/10)
  
  return waistSize


# repeats to test out the functions / calls the other functions and is the main logic of the program
def printProgram():
  print("This Program will allow a gentlman to determine his hat size, jacket size and waist size from his age, height and weight.\n")

  age = int(input("What is your age?  "))

  print("\nWhat is your height in feet and inches?")
  heightFeet = int(input("Feet:  "))
  heightInches = int(input("Inches:  "))
  height = (heightFeet * 12) + heightInches

  weight = float(input("\nHow much do you weigh (in pounds)?  "))

  hatSize = getHatSize(weight, height)
  jacketSize = getJacketSize(weight, height, age)
  waistSize = getWaistSize(weight, age)

  print("\nAccording to our calculations, your sizes are as follows:")
  print(f"Hat Size:  {hatSize:.2f}\nJacket Size:  {jacketSize:.2f}\nWaist Size:  {waistSize:.2f}\n\n\n")
  print("\n///////////////////////////////////////////////\n")

#test cases to try out
#feet 5; inches 7; age 30; weight 167
#hatsize:  7.23  jacketsize:  38.35  waistsize:  29.40

#feet 5; inches 7; age 35; weight 167
#hatsize:  7.23  jacketsize:  38.85  waistsize:  29.60

#feet 5; inches 7; age 40; weight 167
#hatsize:  7.23  jacketsize:  38.98  waistsize:  29.90

#don't use the while statment for any of your works yet until it is covered in class; this just repeats our program
while True:
  printProgram()
