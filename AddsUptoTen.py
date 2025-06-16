import pyinputplus as pyip
def addUptoTen(numbers):
    numberList = list(numbers)
    for i , digit in enumerate(numberList):
        numberList[i] = int(digit)
    if sum(numberList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numberList)))
    return int(numbers)
response = pyip.inputCustom(addUptoTen, prompt='Enter a number with digits that add up to 10: ' )