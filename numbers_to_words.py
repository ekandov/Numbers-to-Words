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
    100: "Hundred", 1000: "Thousand", 10000: "Thousand", 
    100000: "Hundred Thousand", 1000000: "Million", 
    100000000: "Hundred Million", 1000000000: "Billion", 
    100000000000: "Hundred Billion", 1000000000000: "Trillion",
    100000000000000: "Hundred Trillion"
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
        
        thousands:str = typeRes("thousands", targetVal, divisor)
        hundreds:str = typeRes("hundreds", targetVal, divisor)
        digits:str = typeRes("digits", targetVal, divisor)
        tens:str = typeRes("tens", targetVal, divisor)

        print(f"Hundreds0: {hundreds[0]}, Tens0: {tens[0]}, Digits0: {digits[0]}")

        result = (numDict[digits[0]] + cardDict[hundreds[0]] + cardDict[tens[0]] + cardDict[divisor])
        #result += (cardDict[hundreds[3]])
        search_res += (result)
        targetVal = math.floor(targetVal % divisor)
        divisor /= 10
        return search_res

def typeRes(typeVal: str, targetVal: int, divisor: int):

    thousands, hundreds, tens, digits = [], [], [], [] 

    #Calculations that separates numbers before divisor
    wholeNum = targetVal // divisor

    hundreds.append(calcDiv(wholeNum)) #Calculates hundred divisor of wholeNum

    tenNum = (wholeNum // calcDiv(wholeNum)) * calcDiv(wholeNum) #Separates tens from wholeNum 
    tens.append(tenNum)

    digits.append(wholeNum // calcDiv(wholeNum)) #Separates wholeNum as a single digit from hundreds.

    match typeVal:
        case "thousands":
            return thousands
        case "hundreds":
            if hundreds[0] < 100:
                hundreds[0] = 0
            return hundreds
        case "tens":
            if wholeNum > 100:
                tens[0] = ((wholeNum - tenNum) // 10) * 10
            if tens[0] < 20:
                tens[0] = 0
            return tens
        case "digits":
            if wholeNum < 100 and wholeNum >= 10:
                digits[0] = 0
            if wholeNum < 10:
                digits[0] = wholeNum
            return digits
        case _:
            return print("No input given.")

def calcDiv(targetVal):
    
    divisor = 1
    while targetVal >= divisor:
        divisor *= 10
    
    match len(str(targetVal)):
        case 5 | 8 | 11 | 14: #Special treatment for ten thousands, millions, billions, and trillions.
            divisor //= 100
        case 6 | 9 | 12 | 15: #Special treatment for hundreds of millions, billions, and trillions.
            divisor //= 1000
        case _:
            divisor //= 10
    return divisor

main()
