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
        
        wholeNum = getNum(targetVal, divisor, "wholeNum")
        halfNum = getNum(targetVal, divisor, "halfNum")

        thousands:str = typeRes("thousands", targetVal, divisor, wholeNum, halfNum)
        hundreds:str = typeRes("hundreds", targetVal, divisor, wholeNum, halfNum)
        digits:str = typeRes("digits", targetVal, divisor, wholeNum, halfNum)
        tens:str = typeRes("tens", targetVal, divisor, wholeNum, halfNum)

        print(f"wholeNum: {wholeNum}, Hundreds0: {hundreds[0]}, Hundreds1: {hundreds[1]}, Tens0: {tens[0]}, Tens1: {tens[1]}, Digits0: {digits[0]}, Digits1: {digits[1]}, halfNum: {halfNum}")

        result = (numDict[digits[0]] + cardDict[hundreds[0]] + cardDict[tens[0]] + numDict[digits[1]] + cardDict[divisor] + numDict[digits[2]] + 
            cardDict[hundreds[1]] + cardDict[tens[1]] + numDict[digits[3]])
        search_res += (result)
        targetVal = math.floor(targetVal % divisor)
        divisor /= 10
        return search_res

def typeRes(typeVal: str, targetVal: int, divisor: int, wholeNum: int, halfNum: int):

    thousands, hundreds, tens, digits = [], [], [], [] 

    #Calculations that separates numbers before divisor

    hundreds.append(calcDiv(wholeNum)) #Calculates hundred divisor of wholeNum

    tens.append((wholeNum // calcDiv(wholeNum)) * calcDiv(wholeNum)) #Separates tens from wholeNum
    print(f"tenNum: {tens[0]}")

    if wholeNum > 100:
        tens[0] = ((wholeNum - (wholeNum // calcDiv(wholeNum)) * calcDiv(wholeNum)) // 10) * 10
    
    digits.append(wholeNum // calcDiv(wholeNum)) #Separates wholeNum as a single digit from hundreds.
    digits.append(wholeNum - (digits[0] * calcDiv(wholeNum)) - tens[0]) #Separates digits from tens.

    #Calculations that separates numbers after divisor

    hundreds.append(calcDiv(halfNum)) #Separates hundreds from halfNum

    tens.append((halfNum // calcDiv(halfNum)) * 10) #Separates tens from halfNum

    digits.append(halfNum // calcDiv(halfNum)) #Separates single digit from hundreds.
    digits.append(halfNum - (digits[2] * calcDiv(halfNum)) - tens[1]) #Separates digits from halfNum

    if wholeNum < 100:
        digits[1] = wholeNum - tens[0]

    print(f"digits1: {digits[1]}")

    match typeVal:
        case "thousands":
            return thousands
        case "hundreds":
            if hundreds[0] < 100:
                hundreds[0] = 0
            return hundreds
        case "tens":
            if tens[0] < 20:
                tens[0] = 0
            return tens
        case "digits":
            if wholeNum < 100 and wholeNum >= 10 or wholeNum < 10:
                digits[0] = 0
            if wholeNum < 20:
                digits[1] = wholeNum
            return digits
        case _:
            return print("Invalid input fed to typeRes function.")

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

def getNum(targetVal: int, divisor: int, typeVal: str):

    result = 0
    
    match typeVal:
        case "wholeNum":
            result = targetVal // divisor
            return result
        case "halfNum":
            if targetVal >= 1000000:
                pass
            result = targetVal - ((targetVal // divisor) * divisor)
            return result
        case _:
            return print("Invalid input fed to getNum function.")

    return result

main()
