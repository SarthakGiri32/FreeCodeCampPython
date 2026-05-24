try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('"else" block runs if no error occurs')
    print('Division successful:', x)
finally:
    print('\n"finally" block always runs.')
