print('CECS174 Project 5: Arithmetics with Roman/Arabic Numerals\nHector Reyes')
print()


def menu():
    # This function displays the menu interface to the user
    print('Please select from the following:\n')
    print('A - Add two Roman Numerals')
    print('S - Subtract two Roman Numerals')
    print('M - Multiply two Roman Numerals')
    print('D - Divide two Roman Numerals')
    print('Q - Quit')


# This function stores the 6 base values in Roman numeral format up to one thousand
def value(roman):
    # Assign I to 1
    if roman == 'I':
        return 1
    # Assign V to 5
    elif roman == 'V':
        return 5
    # Assign X to 10
    elif roman == 'X':
        return 10
    # Assign L to 50
    elif roman == 'L':
        return 50
    # Assign C to 100
    elif roman == 'C':
        return 100
    # Assign D to 500
    elif roman == 'D':
        return 500
    # Assign M to 1000
    elif roman == 'M':
        return 1000


# This function takes the roman numeral and returns true if the roman numeral is valid and false if invalid
def isValidRoman(roman):
    roman = roman.upper()
    # Import the regular expression module
    import re
    # Thousand dictionary stores roman numerals in the thousand section
    thousand_dic = 'M{0,3}'
    # Hundreds dictionary stores roman numerals in the hundreds section
    hundreds_dic = '(C[MD]|D?C{0,3})'
    # Tens dictionary stores roman numerals in the tenth place
    tens_dic = '(X[CL]|L?X{0,3})'
    # Units dictionary stores roman numeral units
    units_dic = '(I[VX]|V?I{0,3})'

    # This variable will search for a match of 4 or more roman numerals and return the boolean value as either True or False
    subtractive_notation = r'%s%s%s%s$' % (thousand_dic, hundreds_dic, tens_dic, units_dic)

    # Return the value of the boolean expression for the roman parameter
    return (bool(re.match(subtractive_notation, roman.upper())))

# getRomanN1/N2 both prompt the user to enter valid roman numerals
def getRomanN1():
    while True:
        # Prompt user to input the first roman numeral
        romanNumber = input('Enter the first roman numeral: ')
        # Return the roman numeral in uppercase
        romanNumber = romanNumber.upper()
        print()
        # Validate the users' entry
        valid = isValidRoman(romanNumber)
        # If the users' entry is valid, return True and print the roman numeral
        if valid:
            # print(check)
            return romanNumber
            break
        # Display error message and prompt the user to input a valid entry
        else:
            print('Invalid entry, please enter a valid roman numeral')


def getRomanN2():
    while True:
        # Prompt user to input the second roman numeral
        romanNumber = input('Enter the second roman numeral: ')
        # Return the roman numeral in uppercase
        romanNumber = romanNumber.upper()
        print()
        # Valdiate the users' entry
        valid = isValidRoman(romanNumber)
        # If the users' entry is valid, return True and print the roman numeral
        if valid:
            # print(check)
            return romanNumber
            break
        # Display error message and prompt the user to input a valid entry
        else:
            print('Invalid entry, please enter a valid roman numeral')


# This function takes a roman numeral and returns its arabic equivalent
def romanToArabic(roman):
    result = 0
    i = 0

    while (i < len(roman)):
        # Initialize value of roman symbol[i]
        v1 = value(roman[i])
        # calculate the value of the roman numeral[i+1]
        if (i + 1) < len(roman):
            v2 = value(roman[i + 1])
            # Check if the value of the roman symbol in v1 is equal to v2
            if v1 >= v2:
                result = result + v1
                i += 1
            else:
                result = result + v2 - v1
                i += 2
        else:
            result += v1
            i += 2
    return result


# This function takes the number in Arabic format and returns its equivalent Roman value
def arabicToRoman(arabic):
    # List will store collection of integer values corresponding to their roman values
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    # Initialize variable i to the highest index in both our lists[num/roman]
    i = 12
    # Variable will store value of roman numeral
    roman_num = ''
    # While loop will continue iterating until its reached 0
    while arabic != 0:
        if num[i] <= arabic:
            roman_num += roman[i]
            arabic = arabic - num[i]
        else:
            i -= 1
    # Return Arabic symbol in Roman numeral
    return roman_num


# This function takes two Roman numerals and returns the sum of both numerals
def add(roman1, roman2):
    # Initialize num1 to the first roman numeral in arabic symbol representation
    num1 = romanToArabic(roman1)
    # Initialize num2 to the second roman numeral in arabic symbol representation
    num2 = romanToArabic(roman2)
    # Return the sum of num1 and num2
    return arabicToRoman(num1 + num2)


# This function takes two Roman numerals and returns the difference of both numerals in Roman numeral representation
def sub(roman1, roman2):
    # Initialize num1 to the first roman numeral in arabic symbol representation
    num1 = romanToArabic(roman1)
    # Initialize num2 to the second roman numeral in arabic symbol representation
    num2 = romanToArabic(roman2)
    # Initialize difference of first and second cases by 0
    diff1 = 0
    diff2 = 0

    # Calculate the difference if num1 is greater than num2 and return the difference
    if num1 > num2:
        diff1 = num1 - num2
        return arabicToRoman(diff1)
    # Calculate the difference if num2 is greater than num1 and return the difference with a negative in front of the roman numeral
    if num2 > num1:
        diff2 = num2 - num1
        return f'-{arabicToRoman(diff2)}'


# This function takes two Roman numerals and returns the difference of both numerals in Arabic symbol representation
def subArab(roman1, roman2):
    # Initialize num1 to the first roman numeral in arabic symbol representation
    num1 = romanToArabic(roman1)
    # Initialize num2 to the second roman numeral in arabic symbol representation
    num2 = romanToArabic(roman2)
    diff1 = 0
    diff2 = 0
    # Calculate the difference if num1 is greater than num2 and return the difference
    if num1 > num2:
        diff1 = num1 - num2
        return diff1
    # Calculate the difference if num2 is greater than num1 and return the difference with a negative sign in front of the arabic symbol
    if num2 > num1:
        diff2 = num2 - num1
        return f'-{diff2}'


# This function takes two Roman numerals and returns the product of both numerals
def mul(roman1, roman2):
    # Initialize num1 to the first roman numeral in arabic symbol representation
    num1 = romanToArabic(roman1)
    # Initialize num2 to the first roman numeral in arabic symbol representation
    num2 = romanToArabic(roman2)

    return (arabicToRoman(num1 * num2))


# This function takes two Roman numerals and returns the result of their integer division (and remainder, if any) in Roman numerals
def div(roman1, roman2):
    # Initialize num1 to the first roman numeral in arabic symbol representation
    num1 = romanToArabic(roman1)
    # Initialize num2 to the first roman numeral in arabic symbol representation
    num2 = romanToArabic(roman2)

    # Assign the results to 0(i.e., result = 6 / 3 = 2)
    result1 = 0
    result2 = 0

    # Initialize quotient1 and quotient2 to 0
    quotient1 = 0
    quotient2 = 0

    # Initialize remainder1 and remainder2 to 0
    remainder1 = 0
    remainder2 = 0

    # Check if the result is evenly divisible(for num1 > num2)
    if num1 > num2:
        result1 = num1 % num2

        # If the expression is evenly divisible return the quotient
        if result1 == 0:
            result1 = num1 / num2
            return (arabicToRoman(result1))

        # If the expression is not evenly divisible, calculate the quotient and remainder of the integer division and return both as whole numbers
        else:
            quotient1 = num1 // num2
            remainder1 = num1 % num2
            return f'Quotient: {arabicToRoman(quotient1)} Remainder: {arabicToRoman(remainder1)}'


    # Check if the result is evenly divisible(for num2 > num1)
    elif num2 > num1:
        result2 = num2 % num1

        # If the expression is evenly divisible return the quotient
        if result2 == 0:
            result2 = num2 / num1
            return (arabicToRoman(result2))

        # If the expression is not evenly divisible, calculate the quotient and remainder of the integer division and return both as whole numbers
        else:
            quotient1 = num2 // num1
            remainder2 = num2 % num1
            # sum2 = quotient2 + remainder2
            return f'Quotient: {arabicToRoman(quotient1)} Remainder: {arabicToRoman(remainder2)}'


# This function takes two Roman Numerals and returns the result of the their integer division (and remainder, if any) in Arabic symbol representation
def divArab(roman1, roman2):
    # Initialize num1 to the first roman numeral in arabic symbol representation
    num1 = romanToArabic(roman1)
    # Initialize num2 to the first roman numeral in arabic symbol representation
    num2 = romanToArabic(roman2)

    # Assign the results to 0
    result1 = 0
    result2 = 0

    # Initialize quotient1 and quotient2 to 0
    quotient1 = 0
    quotient2 = 0

    # Initialize remainder1 and remainder2 to 0
    remainder1 = 0
    remainder2 = 0

    # Check if the result is evenly divisible(for num1 > num2)
    if num1 > num2:
        result1 = num1 % num2

        # If the expression is evenly divisible return the quotient
        if result1 == 0:
            result1 = num1 / num2
            return (result1)

        # If the expression is not evenly divisible, calculate the quotient and remainder of the integer division and return both as whole numbers
        else:
            quotient1 = num1 // num2
            remainder1 = num1 % num2
            return f'Quotient: {quotient1} Remainder: {remainder1}'

    # Check if the result is evenly divisible(for num2 > num1)
    elif num2 > num1:
        result2 = num2 % num1

        # If the expression is evenly divisible return the quotient
        if result2 == 0:
            result2 = num2 / num1
            return (result2)

        # If the expression is not evenly divisible, calculate the quotient and remainder of the integer division and return both as whole numbers
        else:
            quotient2 = num2 // num1
            remainder2 = num2 % num1
            return f'Quotient: {quotient2} Remainder: {remainder2}'


# Main function calls all other functions
def main():
    print('Welcome to the Roman Numerals Calculator!\n')
    while True:
        print()
        # Call menu function to output the menu interface
        menu()
        print()
        # Prompt user to input an operation
        user_choice = input('Selection: ')
        # Upper method returns string in uppercase
        user_choice = user_choice.upper()

        # If statement will perform addition if the users' selection is 'A'
        if user_choice == 'A':
            # Call getRomanN1 function
            roman1 = getRomanN1()
            roman1 = roman1.upper()

            '''roman1 = romanToArabic(roman1)
            roman1 = arabicToRoman(roman1)'''
            # Display the value of the roman numeral in arabic symbol representation
            print(f'Value of {roman1}: {romanToArabic(roman1)}')
            print()

            # Call getRomanN2 function
            roman2 = getRomanN2()
            roman2 = roman2.upper()

            '''roman2 = romanToArabic(roman2)
            roman2 = arabicToRoman(roman2)'''
            # Display the value of the roman numeral in arabic symbol representation
            print(f'Value of {roman2}: {romanToArabic(roman2)}')
            print()

            print(f'{roman1} + {roman2} = {add(roman1, roman2)}')
            print(romanToArabic(roman1), ' + ', romanToArabic(roman2), ' = ',
                  (romanToArabic(roman1) + romanToArabic(roman2)))
            continue

        # Elif statement will perform subtraction if the users' selection is 'S'
        elif user_choice == 'S':
            # Call getRomanN1 function
            roman1 = getRomanN1()
            roman1 = roman1.upper()

            '''roman1 = romanToArabic(roman1)
            roman1 = arabicToRoman(roman1)'''
            # Display the value of the roman numeral in arabic symbol representation
            print(f'Value of {roman1}: {romanToArabic(roman1)}')
            print()

            # Call getRomanN2 function
            roman2 = getRomanN2()
            roman2 = roman2.upper()

            '''roman2 = romanToArabic(roman2)
            roman2 = arabicToRoman(roman2)'''
            # Display the value of the roman numeral in arabic symbol representation
            print(f'Value of {roman2}: {romanToArabic(roman2)}')
            print()

            print(f'{roman1} - {roman2} = {sub(roman1, roman2)}')
            print(f'{romanToArabic(roman1)} - {romanToArabic(roman2)} = {subArab(roman1, roman2)}')
            continue


        # Elif statement will perform multiplication if the users' selection is 'M'
        elif user_choice == 'M':
            # Call getRomanN1 function
            roman1 = getRomanN1()
            roman1 = roman1.upper()

            '''roman1 = romanToArabic(roman1)
            roman1 = arabicToRoman(roman1)'''
            # Display the value of the roman numeral in arabic symbol representation
            print(f'Value of {roman1}: {romanToArabic(roman1)}')
            print()

            # Call getRomanN2 function
            roman2 = getRomanN2()
            roman2 = roman2.upper()

            '''roman2 = romanToArabic(roman2)
            roman2 = arabicToRoman(roman2)'''
            # Display the value of the roman numeral in arabic symbol representation
            print(f'Value of {roman2}: {romanToArabic(roman2)}')
            print()

            print(f'{roman1} * {roman2} = {mul(roman1, roman2)}')
            print(romanToArabic(roman1), ' * ', romanToArabic(roman2), ' = ',
                  (romanToArabic(roman1) * romanToArabic(roman2)))
            continue


        # Elif statement will perform division if the users' selection is 'D'
        elif user_choice == 'D':
            # Call getRomanN1 function
            roman1 = getRomanN1()
            roman1 = roman1.upper()

            '''roman1 = romanToArabic(roman1)
            roman1 = arabicToRoman(roman1)'''
            # Display the value of the roman numeral in arabic symbol representation
            print(f'Value of {roman1}: {romanToArabic(roman1)}')
            print()

            # Call getRomanN2 function
            roman2 = getRomanN2()
            roman2 = roman2.upper()

            '''roman2 = romanToArabic(roman2)
            roman2 = arabicToRoman(roman2)'''
            # Display the value of the roman numeral in arabic symbol representation
            print(f'Value of {roman2}: {romanToArabic(roman2)}')
            print()

            print(f'{roman1} / {roman2} = {div(roman1, roman2)}')
            print(f'{romanToArabic(roman1)} / {romanToArabic(roman2)} = {divArab(roman1, roman2)}')
            continue


        # Elif statement will exit the while loop
        elif user_choice == 'Q':
            # Display exit message
            print('Thank you for playing with Arabic and Roman numerals, have a good day!')
            break
        # Else statement prompts user to enter a valid entry
        else:
            print('Invalid entry, please try again.')
            print()


main()
