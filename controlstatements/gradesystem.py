grades =[int(score) for score in input("Enter scores for math, physics, and chemistry separated by space: ").split()]

for grade in grades:
    if grade < 35:
        print("You did not pass.")
        exit()

average = (grades[0] + grades[1] + grades[2])/3

if average <= 59:
    print("You earned a C.")
elif average <= 69:
    print("You earned a B.")
else:
    print("You earned an A.")