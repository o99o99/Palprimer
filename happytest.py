print("NOW HAPPY PALPRIMES:")
time.sleep(1)
for item in primeslist:
    itemstring = str(item)
    if item > 999999:
        digit7 = int(itemstring[6])
    else: digit7 =0
    if item >99999:
       digit6 = int(itemstring[5])
    else: digit6 = 0
    if item >9999:
        digit5 = int(itemstring[4])
    else: digit5=0
    if item >999:
        digit4 = int(itemstring[3])
    else:digit4=0
    if item > 99:
        digit3 = int(itemstring[2])
    else:digit3=0
    if item > 9:
        digit2 = int(itemstring[1])
    else:digit2=0
    digit1 = int(itemstring[0])
    square = 0
    squaredcount = 0
    sqwasprime = False
    square = digit7^2 + digit6^2 + digit5^2 + digit4^2 + digit3^2 + digit2^2 + digit1^2
    if square != 1:
        while square != 0 or squaredcount >25:
            squaredcount = squaredcount + 1
            square = str(square)
            sdig1 = int(square[0])
            if int(square) > 9:
                sdig2 = int(square[1])
            else: sdig2 = 0
            if int(square) > 99:
                sdig3 = int(square[2])
            else: sdig3 = 0
            if int(square) > 999:
                sdig4 = int(square[3])
            else: sdig4 = 0
            square = sdig1^2 + sdig2^2 + sdig3^2 + sdig4^2
            if square ==1:
                sqwasprime = True
                break
            elif squaredcount > 25:
                break
            else:pass
    elif square == 1:
        sqwasprime = True
    if squaredcount > 25 or sqwasprime == False:
        print(item, "false")
    elif sqwasprime == True:
        print(item, "true")
        
    
