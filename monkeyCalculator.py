def calculateTime():
    
    # This first line is provided for you
    monkey_one = input("Is the first monkey smiling?:  ")
    monkey_two = input("Is the second monkey smiling?: ")

    y = 1
    n = 2

    if monkey_one == monkey_two:
        print("Uh Oh! We're in trouble!")
    
    elif monkey_one != monkey_two:
        print("Yay! We're going to have a good day!")

    # end assignment


## If you want to test locally run > python monkeyCalculator.py

if __name__ == "__main__":
    calculateTime()
    
