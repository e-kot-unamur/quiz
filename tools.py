def adresseChecker(address):
    #Check first if the first char is digit or alphabetic
    #Check the last is alphabetic
    #Check if there is a @ follow by a "."
    print(address)
    arobase = False
    if not(address[0].isdigit() or address[0].isalpha()):
        return False
    if not address[-1].isalpha():
        return False
    iteration = 1
    while iteration < len(address)-1:
        if (not arobase and address[iteration] == "@"):
            arobase = True
        elif (arobase and address[iteration] == "."):
            return True
        iteration+=1
    return False