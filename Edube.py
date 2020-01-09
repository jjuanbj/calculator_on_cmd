finishProgram = False
operationHasValue = False

while not finishProgram: 
    if operationHasValue == False:
        operation = ""
        while operation not in ("+", "-", "*", "/"):
            operation = input("What do you want to do? Sum(+) Subt(-) Mult(*) Div(/) ")
        else:
            operationHasValue = True

        if operation in ("+", "*"):
            print("Press 'F' or Enter button when you finished entering numbers...")        

    finishEnteringNumbers = False
    total = 0
    numberList = []  
    rounds = 0

    while not finishEnteringNumbers:
        try:
            if finishEnteringNumbers == False:
                numberToCalculateCaption = "Insert a number to calculate: "

                if operation == "-" and rounds == 0:
                    numberToCalculateCaption = "Insert minuend to calculate: "
                elif operation == "-" and rounds > 0:
                    numberToCalculateCaption = "Insert subtracting to calculate: "
                elif operation == "/" and rounds == 0:
                    numberToCalculateCaption = "Insert dividend to calculate: "
                elif operation == "/" and rounds > 0:                  
                    numberToCalculateCaption = "Insert divider to calculate: "

                userInputToCalculate = input(numberToCalculateCaption)

                if userInputToCalculate not in ("F", "f", ""):
                    numberToCalculate = float(userInputToCalculate)                    

            if operation == "/" and rounds == 1 and numberToCalculate == 0:
              print("Can't divide by 0")                                          
              continue

            if operation in ("-", "/"):                
                rounds += 1
                if rounds >= 2:
                    finishEnteringNumbers = True                

            if userInputToCalculate in ("F", "f", ""):
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

    if (total).is_integer():
      print("Result is: ", int(total))
    else:
      print("Result is: ", total)    
    print()

    anotherOperation = ""
    while anotherOperation not in ("Y", "N", "y", "n"):
        anotherOperation = input("Want another operation? (Y) Yes, (N) No: ")

    if anotherOperation in ("Y", "y"):
        operationHasValue = False
        continue
    elif anotherOperation in ("N", "n"):
        print("Bye!")
        finishProgram = True
