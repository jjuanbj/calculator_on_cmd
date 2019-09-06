finishProgram = False
operationHasValue = False

while not finishProgram: 
    if operationHasValue == False:
        operation = ""
        while operation != "+" and operation != "-" and operation != "*" and operation != "/":
            operation = input("What do you want to do? Sum(+) Subt(-) Mult(*) Div(/) ")
        else:
            operationHasValue = True

        if operation == "+" or operation == "*":
            print("Press 'F' when you finished entering numbers...")        

    finishEnteringNumbers = False
    total = 0
    numberList = []    
    rounds = 0

    while not finishEnteringNumbers:
        try:
            if finishEnteringNumbers == False:
                numberToCalculateCaption = "Insert a number to calculate:"

                if operation == "-" and rounds == 0:
                    numberToCalculateCaption = "Insert minuend to calculate:"
                elif operation == "-" and rounds > 0:
                    numberToCalculateCaption = "Insert subtracting to calculate:"
                elif operation == "/" and rounds == 0:
                    numberToCalculateCaption = "Insert dividend to calculate:"
                elif operation == "/" and rounds > 0:
                    numberToCalculateCaption = "Insert divider to calculate:"

                userInputToCalculate = input(numberToCalculateCaption)

                if userInputToCalculate != "F":
                    numberToCalculate = float(userInputToCalculate)

            if operation == "-" or operation == "/":                
                rounds += 1
                if rounds >= 2:
                    finishEnteringNumbers = True                

            if userInputToCalculate == "F":
                finishEnteringNumbers = True        
            elif isinstance(numberToCalculate, float):
                numberList.append(numberToCalculate)    
                continue                                
            
        except ValueError:
            print("Expecting a number or 'F'")            
            finishEnteringNumbers = False
            continue            

    if not numberList:
        total = 0
    elif len(numberList) == 1:
        total = numberList[0]
    elif operation == "+":
        total = sum(numberList)
    elif operation == "-":
        total = numberList[0] - numberList[1]    
    elif operation == "*":    
        total = 1    
        for x in numberList:
            total = total * x  
    elif operation == "/":
        total = numberList[0] / numberList[1]

    print("Result is: ", total)    
    print()

    anotherOperation = ""
    while anotherOperation != "Y" and anotherOperation != "N":
        anotherOperation = input("Want another operation? (Y) Yes, (N) No:")

    if anotherOperation == "Y":
        operationHasValue = False
        continue
    elif anotherOperation == "N":
        finishProgram = True
