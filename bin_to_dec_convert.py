# bin = '10100111001'
# converted to decimal: 1337

def bin_convert_to_dec(bin):
    bin_arr = []

    for x in bin:
        bin_arr.append(int(x))

    reversed_bin = bin_arr[::-1]

    sum = 0

    # store indeces when value in bin_arr is 1
    indeces = []

    for x in reversed_bin:
        if (x == 1 and len(indeces) == 0):
            indeces.append(reversed_bin.index(x))
        elif (x == 1):
            indeces.append(reversed_bin.index(x, indeces[-1] + 1))

    for x in indeces:
        sum = sum + 2**x

    # sum is decimal number
    return sum

given_binary = str(raw_input("Please provide the binary number you would like to convert to a decimal value: "))

print(bin_convert_to_dec(given_binary))
