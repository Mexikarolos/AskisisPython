def loadText():
    with open('two_cities_ascii.txt', 'r') as file:
        text = file.read()

    return text


def textToBinarySeven(text):
    binary_7 = [format(ord(char), '07b') for char in text]

    return binary_7


def getFirstAndLastTwo(array):
    string = ''
    for bin7Char in array:
        firstTwoBits = bin7Char[:2]
        lastTwoBits = bin7Char[-2:]
        fourBitsOfChar = firstTwoBits + lastTwoBits
        string += fourBitsOfChar

    return string


def splitBySixteenBits(string):
    array = [string[i:i + 16] for i in range(0, len(string), 16)]

    return array


def makeArrays(splitBits_16):
    dividedByTwo, dividedByThree, dividedByFive, dividedBySeven = [], [], [], []

    for sixteenBits in splitBits_16:
        number = int(sixteenBits, 2)
        if number % 2 == 0:
            dividedByTwo.append(number)

        if number % 3 == 0:
            dividedByThree.append(number)

        if number % 5 == 0:
            dividedByFive.append(number)

        if number % 7 == 0:
            dividedBySeven.append(number)

    return dividedByTwo, dividedByThree, dividedByFive, dividedBySeven


def main():
    text = loadText()
    sevenBitsArray = textToBinarySeven(text)
    firstAndLastTwoBits = getFirstAndLastTwo(sevenBitsArray)
    splitBits_16 = splitBySixteenBits(firstAndLastTwoBits)

    dividedByTwo, dividedByThree, dividedByFive, dividedBySeven = makeArrays(splitBits_16)

    lengthOfSixteenBitsArray = len(splitBits_16)

    print("From ", lengthOfSixteenBitsArray, " numbers, ", len(dividedByTwo), "can be divided exactly with 2.")
    print("From ", lengthOfSixteenBitsArray, " numbers, ", len(dividedByThree), "can be divided exactly with 3.")
    print("From ", lengthOfSixteenBitsArray, " numbers, ", len(dividedByFive), "can be divided exactly with 5.")
    print("From ", lengthOfSixteenBitsArray, " numbers, ", len(dividedBySeven), "can be divided exactly with 7.")


if __name__ == "__main__":
    main()
