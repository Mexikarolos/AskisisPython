with open("two_cities_ascii.txt", 'r+') as f:
    f = f.read()


#Ascii_To_Binary
def ascii_to_binary(text):
    total_binary = ''

    for i in range(len(text)):
        binary = ''
        str_ord = ord(text[i: i + 1])

        while str_ord > 0:
            x = str_ord % 2
            str_ord = str_ord // 2
            binary = str(x) + str(binary)
        total_binary += binary + ' '

    print(total_binary)

    return total_binary


ascii_to_binary(f)


def MaxLength1(array, n):
    count1 = 0
    result1 = 0

    for i in range(0, n):

        if (array[i] == "0" or array[i] == " "):
            count1 = 0

        else:
            count1 += 1
            result1 = max(result1, count1)

    return result1


def MaxLength0(array, n):
    count0 = 0
    result0 = 0

    for i in range(0, n):
        if (array[i] == "1" or array[i] == " "):
            count0 = 0

        else:
            count0 += 1
            result0 = max(result0, count0)

    return result0


array = ascii_to_binary(f)
n = len(array)

#Prints
print("Maximum Sequence of Number 0 appearances : ")
print(MaxLength0(array, n))
print("Maximum Sequence of Number 1 appearances : ")
print(MaxLength1(array, n))

