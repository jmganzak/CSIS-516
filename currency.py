curr = int(input("Enter the currency in knuts\n"))
def convert():
    knuts = curr % 29
    temp = int(curr / 29)
    sickles = temp % 17
    galleon = int(temp / 17)

    print(curr, "knuts =" , galleon ,  "galleons" , sickles ,  "sickles and" , knuts , "knuts." )
    print("--------------------------------------------------------")
convert()

