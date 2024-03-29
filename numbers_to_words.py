def main():
    userInput = input("Please enter an integer: ")
    checkInput(userInput)

def checkInput(userInput):
    numDict = {
        "0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four",
        "5": "Five", "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine",
        "10": "Ten", "11": "Eleven", "12": "Twelve", "13": "Thirteen",
        "14": "Fourteen", "15": "Fifteen", "16": "Sixteen", "17": "Seventeen",
        "18": "Eighteen", "19": "Nineteen"
    }

    tenList = ["Twenty", "Thirty", "Fourty", "Fifty", 
               "Sixty", "Seventy", "Eighty", "Ninety"]

    cardinals = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]
    if float(userInput) < 20:
        return print(f"{numDict[userInput]}")
    if float(userInput) >= 20 and float(userInput) < 100:
        pass

main()
