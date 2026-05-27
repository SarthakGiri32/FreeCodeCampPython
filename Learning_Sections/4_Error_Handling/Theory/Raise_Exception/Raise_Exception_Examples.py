# example 1
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    print("Example 1:")
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}')

# example 2
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging: Invalid data received')
        raise  # Re-raises the same ValueError

try:
    print("\nExample 2:")
    process_data('abc')
except ValueError:
    print('Handled at higher level')
