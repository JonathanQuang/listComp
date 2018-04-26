def minimumThreshold(password):
    lowerList = [character for character in password if character.islower()]
    upperList = [character for character in password if character.isupper()]
    numList = [character for character in password if character.isdigit()]
    return (len(lowerList)>0 and len(upperList)>0 and len(numList)>0)

print (minimumThreshold("ABcd12qwerty"))
print (minimumThreshold("holdUp"))

def passwordStrength(password): 
    lowerList = [character for character in password if character.islower()]
    upperList = [character for character in password if character.isupper()]
    numList = [character for character in password if character.isdigit()]
    weirdSymbols = [character for character in password if (not(character in lowerList or character in upperList or character in numList))]
    if (len(lowerList)==0 or len(upperList)==0 or len(numList)==0 or len(weirdSymbols)==0):
        return 0
    retSum = len(lowerList)+len(upperList)+len(numList)+len(weirdSymbols)
    retSum = retSum / 1.5
    if retSum > 10:
        return 10
    return retSum

print(passwordStrength("querty"))
print(passwordStrength("AbCdEfG1234$%"))
print(passwordStrength("ABCDEfghijklmn1234678%"))

