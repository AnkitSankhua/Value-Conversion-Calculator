# This Code would show the value of the given number in other number systems namely
# BINARY , OCTAL , HEXADECIMAL and SCIENTIFIC FORM........

def NumberConverter():
    while True:
        number = input(" Enter the Number you wish to see the converted values of : ")
        if number.isdigit():
            number = int(number)

            break
        else:
            print("Strictly Enter a number !!!")
            print("The Number Should be without Decimal points as this code does not support float conversion.....")

    print(str("You Have Entered the Number : {:,}".format(number)))
    print(str("The BINARY Representation of the number is : {:b}".format(number)))
    print(str("The OCTAL Representation of the number is : {:o}".format(number)))
    print(str("The HEXA-DECIMAL Representation of the number is : {:E}".format(number)))
    print(str("The Scientific Notation of the number is : {:X}".format(number)))

NumberConverter()


