# 4.0 Jedi Training (40pts)  Name:Logan Mills
# Below each program list the mistakes found in comments.

# 1. Make the following program work. (3 mistakes)  (3pts)

midichlorians = float(input("Enter midichlorian count: "))  # Indentation, missing parenthesis

if midichlorians > 10000:  # Missing colon
    print("You have serious Jedi potential")
else:  # Elif requires a condition
    print("Jedi, you will never be.")


# 2. Make the following program work. (3 mistakes)  (3pts)
     
x = int(input("Enter a number: "))  # Missing int statement, indentation
if x == 3:  # Missing colon, double equals sign
    print("You entered 3")


# 3. Make the following program work. (4 mistakes)  (4pts)
     
answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":  # Double equals, wrong variable, a is not defined
    print("Correct!")
else:  # Indent and colon
    print("Incorrect! It is BB8.")


# 4. Make the following program work. (4 mistakes) (4pts)
     
jedi = input("Name one of the top 3 greatest Jedi.")  # Defined x but used variable jedi later
if jedi == "Yoda" or jedi == "Luke Skywalker" or jedi == "Obi-Wan Kenobi":  # Has to be jedi == for each, quotes around strings
    print("That is correct!")  # Missing quotes

# 5. Make the following program work whether they enter a, A, Jedi Master or jedi master
#    Print "Not a choice!" if they don't choose any of the three and set sensitivity to blank text.  (6pts)
     
print("Welcome to the Jedi Academy!")

print("A. Jedi Master")
print("B. Sith Lord")
print("C. Droid")

user_input = input("Choose a character?")
sensitivity = 0

if user_input.lower() == "a":  # .lower() to get both a and A, strings need quotes, double quotes
    sensitivity = 1000
elif user_input.lower() == "b":  # elif not else if
    sensitivity = 900
elif user_input.lower() == "c":
    sensitivity = 0
else:
    print("Not a choice")  # Added error catch

print("Sensitivity: ", sensitivity)  # Add , sensitivity to print sensitivity, define sensitivity earlier to prevent undefined errors

'''
6. NUMBER ANALYSIS PROGRAM  (10pts)
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''

number = int(input("Choose a number: "))

# Test 1
if number % 2 == 1:
    print("Test 1: Odd")
else:
    print("Test 1: Even")

# Test 2
if number > 0:
    print("Test 2: Positive")
elif number < 0:
    print("Test 2: Negative")
else:
    print("Test 2: Zero")

# Test 3
if -100 <= number <= 100:
    print("Test 3: Inclusive")
else:
    print("Test 3: Exclusive")

'''
GRADING 2.0    (10pts)
-------------------
Copy your Grading 1.0 program below and then modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

sem = float(input("What is your semester grade? "))
fin = float(input("What is your final exam grade? "))
wor = float(input("How much is your final worth? "))

semwor = 100 - wor
semwor /= 100
sem *= semwor
wor /= 100
fin *= wor
overall = fin + sem

print("Your overall grade is", overall)

if overall >= 90:
    print("Your letter grade is A")
elif overall >= 80:
    print("Your letter grade is B")
elif overall >= 70:
    print("Your letter grade is C")
elif overall >= 60:
    print("Your letter grade is D")
else:
    print("Your letter grade if F, you should transfer to Johnston")
