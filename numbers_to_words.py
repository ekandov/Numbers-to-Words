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
    100: "Hundred", 1000: "Thousand", 100000: "Hundred Thousand", 
    1000000: "Million", 1000000000: "Billion", 1000000000000: "Trillion"
}

def main():
    userInput = int(input("Please type a number: "))
    checkInput(userInput)

def checkInput(userInput):
    if search(userInput).startswith("Zero") != True:
        return print(search(userInput).replace("Zero", ""))
    if search(userInput).rfind("Dot") != True:
        return print(search(userInput).replace("Zero", ""))
    return print(search(userInput))

def search(targetVal):
    
    divisor = calcDiv(targetVal)
    print(f"Divisor: {divisor}")
    search_res = ""
    while targetVal:

        wholeNum = targetVal // divisor 
        thousandNum = ((targetVal - (wholeNum * divisor)) // 1000) * 1000
        hundNum = ((targetVal - (wholeNum * divisor)) // 100) * 100 # Checks if user inputted 100 value, works only for numbers above 1000.
        hunDigit = hundNum // (divisor/10)
        digits = targetVal - (wholeNum * divisor) - hundNum
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


        search_res += (numDict[wholeNum] + cardDict[divisor] + numDict[hunDigit] + cardDict[hundNum] + cardDict[tenNum] + numDict[digits])
        targetVal = math.floor(targetVal % divisor)
        divisor /= 10
        return search_res

def typeRes(value):
    pass


def calcDiv(targetVal):

    divisor = 1
    while targetVal >= divisor:
        divisor *= 10
    match len(str(targetVal)):
        case 5 | 8 | 11 | 14: #Special treatment for ten thousands, millions, billions, and trillions.
            divisor /= 100
            return divisor
        case 9 | 12 | 15: #Special treatment for hundreds of millions, billions, and trillions.
            divisor /= 1000
            return divisor
    divisor /= 10
    print(f"calcDiv div: {divisor}")
    return divisor

main()
