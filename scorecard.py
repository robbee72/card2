# Program make a simple calculator
# This function adds two numbers
print("Enter par:")
a = int(input())
print("Enter score:")
b = int(input())


def main():
    par, score = (a, b)

    if(par - 1 == score):
        st = "Birdie"
    elif (par - 2 == score):
        st = "Eagle"
    elif (par - 3 == score):
        st = "Double Eagle"
    elif (par == score):
        st = "Nice Par"
    elif (par + 1 == score):
        st = "Bogey"
    elif (par + 2 == score):
        st = "Double Bogey"
    else:
        st = "Oops Big Number"
    print(st)


if __name__ == "__main__":
    main()
