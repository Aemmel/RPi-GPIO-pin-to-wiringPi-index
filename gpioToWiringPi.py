def error_operand():
    print("ERROR: UNKNOWN OPERAND")
    print("       PLEASE TRY AGAIN: ")


def error_operator():
    print("ERROR: UNKNOWN OPERATOR")
    print("       PLEASE TRY AGAIN: ")


def print_dict(di):
    for i in di:
        print(str(i) + ": " + str(di[i]))


# if the operator is "pin" or "gpio", print the respective item
def convert(operator, operand):
    try:
        operand = int(operand)
    except ValueError:
        error_operand()
        return False

    try:
        if operator == "gpio":
            print("as wiringPi: " + str(gpio_to_pin[operand]))
        elif operator == "pin":
            print("as GPIO: " + str(pin_to_gpio[operand]))

    except KeyError:
        error_operand()
        return False


# print the keys of gpio or pin
def print_keys_pin_gpio(op):
    if op == "gpio":
        print_dict(gpio_to_pin)
    elif op == "pin":
        print_dict(pin_to_gpio)
    else:
        error_operand()


# init the GPIO pin to wiringPi index
gpio_to_pin = {
    2: 8,
    3: 9,
    4: 7,
    14: 15,
    15: 16,
    17: 0,
    18: 1,
    27: 2,
    22: 3,
    23: 4,
    24: 5,
    10: 12,
    9: 13,
    25: 6,
    11: 14,
    8: 10,
    7: 11,
    5: 21,
    6: 22,
    12: 26,
    13: 23,
    19: 24,
    16: 27,
    26: 25,
    20: 28,
    21: 29
}

# create wiringPi index to GPIO as extra dictionary from gpio_to_pin
pin_to_gpio = {}
for i in gpio_to_pin:
    pin_to_gpio[gpio_to_pin[i]] = i

while True:
    print("")
    print("Please input command: ")
    inp = input("")
    # check if wants to quit
    if inp.lower() == "exit":
        break

    operator = inp[:inp.find(" ")].lower()
    operand = inp[inp.find(" ") + 1:].lower()

    if operator == "pin" or operator == "gpio":
        convert(operator, operand)
    elif operator == "print":
        print_keys_pin_gpio(operand)
    else:
        error_operator()

# make sure the program stays open for testing
print("")
print("")
xxxx = input("Press Enter to continue...")
