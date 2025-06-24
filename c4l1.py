#Jacob Sexton 6/24/25
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"The current temperature is {celsius:.2f} celsius this temperature in fahrenheit is {fahrenheit:.2f}")


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def is_valid_number(value):
    return value.replace('.', '', 1).isdigit()


def main():
    temp_input = input("What is the current temperature?  ")

    while is_valid_number(temp_input) == False:
        print("Invalid input, Please try again!")
        temp_input = input("What is the current temperature? ")

    temp = float(temp_input)

    scale = input("Is the temperature in (F)ahrenheit or (C)elsius? ").lower()

    while scale != 'f' and scale != 'c':
        print("Invalid input, Please enter F or C!")
        scale = input("Is the temperature in (F)ahrenheit or (C)elsius? ").lower()

    if scale == 'f':
        celsius = convert_fahrenheit_to_celsius(temp)
        print(f"The current temperature is {temp:.2f} fahrenheit this temperature in celsius is {celsius:.2f}")
    else:
        convert_celsius_to_fahrenheit(temp)

main()
