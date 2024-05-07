import math

numDict = {
    0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
    5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
    10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
    14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
    18: "Eighteen", 19: "Nineteen", 
}

cardDict = {
    0: "", 20: "Twenty", 30: "Thirty",40: "Fourty", 50: "Fifty", 
    60: "Sixty", 70: "Seventy",80: "Eighty", 90: "Ninety", 
    100: "Hundred", 1000: "Thousand",1000000: "Million", 
    10000000: "Billion", 100000000: "Trillion"
}

def main():
    userInput = int(input("Please type a number: "))
    checkInput(userInput)

def checkInput(userInput):
    #if userInput < 20:
    #return print(f"{numDict[userInput]}")
    if search(userInput).endswith("Zero") != False:
        return print(search(userInput).strip("Zero"))
    if search(userInput).rfind("Dot") != True:
        return print(search(userInput).replace("Zero", ""))
    return print(search(userInput))

"""
    tenCard = {"2": "Twenty", "3": "Thirty", "4": "Fourty","5": "Fifty", 
               "6": "Sixty","7": "Seventy","8": "Eighty","9": "Ninety"}

    cardinals = ["Hundred", "Thousand", "Million", "Billion", "Trillion"]

    if float(userInput) < 20:
        return print(f"{numDict[userInput]}")
"""


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
       se return print(f"{numDict[userInput[:1]]} {cardinals[0]} {tenCard[userInput[1]]} {numDict[userInput[2:]]}")
"""



def search(targetVal):
    
    divisor = calcDiv(targetVal)
    print(f"Divisor: {divisor}")
    search_res = ""
    while targetVal:

        wholeNum = targetVal // divisor
        thousandNum = ((targetVal - (wholeNum * divisor)) // 1000) * 1000
        hundNum = ((targetVal - (wholeNum * divisor)) // 100) * 100 # Checks if user inputted 100 value, works only for numbers above 1000.
        hunDigit = hundNum // (divisor/10)
        digits = targetVal - divisor - hundNum
        hundNum = round(calcDiv(hundNum))
        tenNum = (digits // 10) * 10
        digits -= abs(tenNum)

        lastNum = wholeNum * divisor
        print(f"wholeNum: {wholeNum}")
        print(f"lastNum: {lastNum}")
        print(f"thousandNum: {thousandNum}")
        print(f"hundNum: {hundNum}")
        print(f"tenNum: {tenNum}")
        print(f"digits: {digits}")
        #if targetVal < 100:
        #search_res += (cardDict[lastNum] + numDict[digits])
            #print(search_res)
        #targetVal = math.floor(targetVal % divisor)
        #divisor /= 10
        #return search_res
        search_res += (numDict[wholeNum] + cardDict[thousandNum] + numDict[hunDigit] + cardDict[hundNum] + cardDict[tenNum] + numDict[digits])
        targetVal = math.floor(targetVal % divisor)
        divisor /= 10
        return search_res

def typeRes(value):
    pass


def calcDiv(targetVal):

    divisor = 1
    while targetVal >= divisor:
        divisor *= 10
    if len(str(targetVal)) == 2:
        divisor /= 10
        return divisor
    lastNum = int(targetVal / divisor)
    divisor = (divisor-lastNum)/10
    return divisor

main()
