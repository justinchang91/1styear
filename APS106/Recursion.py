def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def backwards_letter(letter):
    if letter == "a":
        print(letter)
    else:
        print(letter)
        previous_letter = chr(ord(letter)-1)
        backwards_letter(previous_letter)

backwards_letter("z")