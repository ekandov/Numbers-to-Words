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

        wholeNum = targetVal // divisor    
        halfNum = (targetVal - (wholeNum * divisor))
        
        print(f"wholeNum: {wholeNum}")

        thousands:str = typeRes("thousands", targetVal, divisor, wholeNum, halfNum)
        hundreds:str = typeRes("hundreds", targetVal, divisor, wholeNum, halfNum)
        digits:str = typeRes("digits", targetVal, divisor, wholeNum, halfNum)
        tens:str = typeRes("tens", targetVal, divisor, wholeNum, halfNum)

        '''if targetVal < 100:
            print(f"Digits: {digits[0]}, {digits[1]}")
            print(f"Tens: {tens[0]}, {tens[1]}")
            result = (cardDict[tens[1]] + numDict[digits[1]])
        if targetVal > 100 or targetVal < 1000000:
            result = (numDict[wholeNum] + cardDict[divisor] + cardDict[thousands[0]] + numDict[hundreds[0]] + cardDict[hundreds[1]] + cardDict[tens[0]] + numDict[digits[0]])
        '''
       
        if wholeNum > 19 and wholeNum < 100 or wholeNum < 10:
            wholeNum = 0
        if wholeNum >= 100:
            wholeNum //= 100


        print(f"wholeNum2: {wholeNum}")
        print(f"tens2: {tens[2]}")
        print(f"digits2: {digits[2]}")
        result = (numDict[wholeNum] + cardDict[hundreds[2]] + cardDict[tens[2]] + numDict[digits[2]] + cardDict[divisor])
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
    hundreds.append(round(calcDiv(wholeNum))) # Isolates hundreds from wholeNum 
    
    tens.append(((targetVal - (wholeNum * divisor) - hundNum) // 10) * 10) # Isolates tens from numbers 100 and over.
    tens.append(targetVal - (targetVal - (wholeNum * divisor))) #Isolates digits from tens over 20.
    tens.append(((wholeNum - ((wholeNum // 100) * 100)) // 10) * 10 ) #Isolates tens from wholeNum

    digits.append((targetVal - (wholeNum * divisor) - hundNum) - tens[0]) # Digits calculation for large numbers
    digits.append(targetVal - tens[1]) #Isolates digits from 10s
    digits.append(wholeNum - ((wholeNum // 100) * 100) - tens[2]) #Isolates digits from wholeNum
    digits.append(wholeNum - tens[2] - digits[2]) # Isolates tens and digits from wholeNum

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
            if hundreds[2] < 20:
                hundreds[2] = 0
            return hundreds
        case "tens":
            if tens[1] < 20:
                tens[1] = 0
            if tens[2] < 20:
                tens[2] = 0
            return tens
        case "digits":
            if targetVal < 20:
                digits[1] = targetVal
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
    #divisor //= 10
    return divisor

main()
