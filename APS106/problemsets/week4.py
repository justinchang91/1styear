def is_this_my_name():  # 1a
    full_name = input("Enter your full name: ")
    names = full_name.split(" ")
    first = names[0].lower()
    last = names[1].lower()

    my_first = "justin"

    if first == my_first:
        print("How did you know my name?")
    else:
        print("It's rude to not know my name.")


def matching_strings(str1, str2):  # 1b
    str1 = str1.lower()
    str2 = str2.lower()

    print(str1, str2)
    if str1 == str2:
        return True

    else:
        return False


def find_length_using_ints(number):  # 2
    status = True
    digits = 0

    while status:                       # loop until finish (status == false)
        number = number / 10            # number is the number divided by 10
        if number >= 0.1:
            digits = digits + 1         # digit counter adds 1 if the number is above 0.1
        else:
            status = False              # if the number is less than 0.1, status = false and loops stops

# I chose if to be less than 0.1 to stop because by then, the counter would have counted every digit.
# if I went further to like 0.01, that's over counting

    return digits


def what_is_the_state(temp):  # 3
    if temp >= 100:
        state = "gas"
    elif temp <= 0 :
        state = "solid"
    else:
        state = "liquid"

    return state


def type_of_flow(speed, length, viscosity, situation):  # 4

    v = float(speed)
    l = float(length)
    n = float(viscosity)

    reynolds = v*l/n

    if situation == "pipe":
        if reynolds > 4000:
            flow = "turbulent"
        elif reynolds < 2000:
            flow = "laminar"
        else:
            flow = "transitional"

    elif situation == "plate":
        if reynolds < 5 * 10**5:
            flow = "laminar"
        else:
            flow = "turbulent"

    return flow


print(type_of_flow(1000000, 700, 10, "plate"))