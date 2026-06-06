def verify_card_number(digits_str: str) -> str:
    digits_str = digits_str.replace("-", "").replace(" ", "")

    validation_sum: int = 0

    for i in range(len(digits_str) - 2, -1, -2):
        double_of_digit = int(digits_str[i]) * 2
        if double_of_digit > 9:
            double_of_digit -= 9
        validation_sum += double_of_digit

    validation_sum += sum([int(digits_str[i]) for i in range(len(digits_str) - 1, -1, -2)])

    return "VALID!" if validation_sum % 10 == 0 else "INVALID!"


def main():
    print(verify_card_number("453914889"))
    print(verify_card_number("4111-1111-1111-1111"))
    print(verify_card_number("1234 5678 9012 3456"))


if __name__ == "__main__":
    main()
