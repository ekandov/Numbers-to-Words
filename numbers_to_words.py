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
    
    tenCard = {"2": "Twenty", "3": "Thirty", "4": "Fourty","5": "Fifty", 
               "6": "Sixty","7": "Seventy","8": "Eighty","9": "Ninety"}

    cardinals = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]

    if float(userInput) < 20:
        return print(f"{numDict[userInput]}")



"""
    if float(userInput) < 20:
    return print(f"{result}")
    if float(userInput) >= 20 and float(userInput) < 100:
        return print(f"{tenCard[userInput[:1]]} {numDict[userInput[1:]]}")
    if float(userInput) >= 100 and float(userInput) < 110:
        return print(f"{numDict[userInput[:1]]} {cardinals[0]} {numDict[userInput[2:]]}")
    if float(userInput) >= 110 and float(userInput) < 120:
        return print(f"{numDict[userInput[:1]]} {cardinals[0]} {tenDict[userInput[1:]]}")
    if float(userInput) >= 120 and float(userInput) < 1000:
        return print(f"{numDict[userInput[:1]]} {cardinals[0]} {tenCard[userInput[1]]} {numDict[userInput[2:]]}")
"""



def search(values, targetVal):
    search_at = 0
    search_res = False
    
    while search_at < len(values) and search_res is False:
        if values[search_at] == targetVal:
            search_res = True
        else:
            search_at = search_at + 1
    return search_res



main()
