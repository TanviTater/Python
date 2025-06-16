import pyinputplus as pyip

response = pyip.inputNum(prompt='Enter a number: ', min=0, max=100)
print("You entered:", response)

password = pyip.inputPassword(prompt = 'Enter your password : ') 
print("Your password is:", password)

email = pyip.inputEmail(prompt='Enter your email: ')
print("Your email is:", email)

choice = pyip.inputChoice(['yes', 'no', 'maybe'], prompt='Do you want to continue? ')
print("Your choice is:", choice)

menu = pyip.inputMenu(['Option 1', 'Option 2', 'Option 3'], numbered=True, prompt='Choose an option: ')
print("You selected:", menu)

yes_no = pyip.inputYesNo(prompt='Do you agree? ')
print("Your response is:", yes_no)

boolean_response = pyip.inputBool(prompt='Is it true? ')
print("Your boolean response is:", boolean_response)

filePath = pyip.inputFilepath(prompt='Enter a file path: ')
print("You entered file path:", filePath)