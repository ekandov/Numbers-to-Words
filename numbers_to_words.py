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
        halfNum = (targetVal - (wholeNum * divisor))

        thousands:str = typeRes("thousands", targetVal, divisor, wholeNum, halfNum)
        hundreds:str = typeRes("hundreds", targetVal, divisor, wholeNum, halfNum)
        digits:str = typeRes("digits", targetVal, divisor, wholeNum, halfNum)
        tens:str = typeRes("tens", targetVal, divisor, wholeNum, halfNum)

        print(f"wholeNum: {wholeNum}")
        print(f"halfNum: {halfNum}")
        print(f"thousandNum: {thousands[0]}")
        print(f"hundNum: {hundreds[1]}")
        print(f"tenNum: {tens[0]}")
        print(f"digits: {digits[0]}")

        result = (numDict[wholeNum] + cardDict[divisor] + cardDict[thousands[0]] + 
        numDict[hundreds[0]] + cardDict[hundreds[1]] + cardDict[tens[0]] + numDict[digits[0]])

        search_res += (result)
        targetVal = math.floor(targetVal % divisor)
        divisor /= 10
        return search_res

def typeRes(typeVal: str, targetVal: int, divisor: int, wholeNum: int, halfNum: int):

    trillions, billions, millions, thousands, hundreds, tens, digits = [], [], [], [], [], [], []

    #Needs work - Currently works for numbers up to 19,999
    thousandNum = (halfNum // 1000) * 1000
    thousands.append(round(calcDiv(thousandNum))) #Thousands calculation for numbers over 10000
    
    hundNum = (halfNum // 100) * 100
    hundreds.append(hundNum // (divisor/10)) #Digit calculation for hundreds.
    hundreds.append(round(calcDiv(hundNum))) #Divisor calculation for hundreds. For numbers over 1000

    tens.append(((targetVal - (wholeNum * divisor) - hundNum) // 10) * 10) # Isolates tens from numbers 100 and over.

    digits.append((targetVal - (wholeNum * divisor) - hundNum) - tens[0]) # Digits calculation

    match typeVal:
        case "trillions":
            return trillions
        case "billions":
            return billions
        case "millions":
            return millions
        case "thousands":
            return thousands
        case "hundreds":
            return hundreds
        case "tens":
            return tens
        case "digits":
            return digits
        case _:
            return trillions, billions, millions, thousands, hundreds, tens, digits


def calcDiv(targetVal):
    
    divisor = 1
    while targetVal >= divisor:
        divisor *= 10
    
    match len(str(targetVal)):
        case 5 | 8 | 11 | 14: #Special treatment for ten thousands, millions, billions, and trillions.
            divisor //= 100
        case 9 | 12 | 15: #Special treatment for hundreds of millions, billions, and trillions.
            divisor //= 1000
        case _:
            divisor //= 10
    return divisor

main()
