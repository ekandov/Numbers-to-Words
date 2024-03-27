def main:
    userInput = input("Please enter an integer: ")
    checkInput(userInput)
    pass

def checkInput(userInput):
    numDict = {
        "0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
        "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"
    }

    tenList = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", 
               "Fifteen", "Nineteen", "Twenty", "Thirty", "Fourty", 
               "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    cardinals = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]

    match userInput:
        case userInput == 0:
            return print(f"{numDict["0"]}")
        case userInput >= 1 and userInput < 10:
            pass
    pass

main()
