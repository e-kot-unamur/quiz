def adresseChecker(address):
    #Check first if the first char is digit or alphabetic
    #Check the last is alphabetic
    #Check if there is a @ follow by a "."
    arobase = False
    if not(address[0].isdigit() or address[0].isalpha()):
        return False
    if not address[-1].isalpha():
        return False
    iteration = 1
    while iteration < len(address)-1:
        if not arobase or address[iteration:iteration+2] == "@":
            arobase = True
        elif (address[iteration:iteration+2] == "."):
            return True
        else:
            iteration+=1
    return False