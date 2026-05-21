def pin_extractor(poems):
    """
    This function returns a list of secret codes, where the nth digit is the length of the nth word in the
    nth line of a poem in the list of poems (zero-indexed n). If the number of words in the nth line is
    less than or equal to n, then zero is appended to the secret code for that line.
    :param poems: a list of poems
    :return: a list of secret codes extracted from each poem
    """
    secret_codes = []
    for poem in poems:
        secret_code = ""
        lines = poem.split("\n")
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += "0"
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"
poem3 = "There\nonce\nwas\na\ndragon"

print(pin_extractor([poem, poem2, poem3]))
