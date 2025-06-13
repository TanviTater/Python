def spam(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print("Error: You tried to divide by zero.")
    except TypeError:
        print("Error: You must enter a number.")
print(spam(2))
print(spam(0))
print(spam('hello'))
print(spam(1.5))

print("\n")

# OR
def spam2(dividedBy):
    return 50/dividedBy
try:
    print(spam2(2))
    print(spam2('hello'))
    print(spam2(0))
    print(spam2(1.5))
except ZeroDivisionError:
    print("Error: You tried to divide by zero.")
except TypeError:
    print("Error: You must enter a number.")