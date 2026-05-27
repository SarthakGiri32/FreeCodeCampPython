def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    elif n < 1:
        return "Argument must be an integer greater than 0."
    else:
        number_pattern_string = ""
        for i in range(1, n + 1):
            number_pattern_string += str(i) + " "
        return number_pattern_string.strip(" ")

if __name__ == "__main__":
    print(number_pattern(4))
    print(number_pattern(12))
