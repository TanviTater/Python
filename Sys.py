import sys
while True:
    print("Type 'exit' to exit")
    response = input()
    if response == 'exit':
        print("Exiting the program.")
        sys.exit()
print("You entered:", response)