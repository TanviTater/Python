import pyinputplus as pyip
breadType = pyip.inputMenu(['White', 'Wheat', 'Sourdough'], prompt='Choose a type of bread:\n')
proteinType = pyip.inputMenu(['Turkey', 'Ham', 'Tofu'], prompt='Choose a type of protein:\n')
wantCheese = pyip.inputYesNo(prompt='Do you want cheese? (yes/no): ')
if wantCheese:  
    cheeseType = pyip.inputMenu(['Cheddar', 'Swiss', 'Provolone'], prompt='Choose a type of cheese:\n')
wnatSauce = pyip.inputYesNo(prompt='Do you want sauce? (yes/no): ')
if wnatSauce:
    sauceType = pyip.inputMenu(['Mayo', 'Mustard', 'Ketchup'], prompt='Choose a type of sauce:\n')
quantity = pyip.inputInt(prompt='How many sandwiches do you want? ', min=1, max=100)
prices = {
    'White': 2.00,  
    'Wheat': 2.50,
    'Sourdough': 3.00,
    'Turkey': 1.50,
    'Ham': 1.75,    
    'Tofu': 1.25,
    'Cheddar': 0.50,
    'Swiss': 0.75,
    'Provolone': 0.60,  
    'Mayo': 0.20,
    'Mustard': 0.15,
    'Ketchup': 0.10
}
cost = prices[breadType] + prices[proteinType]
if wantCheese:
    cost += prices[cheeseType]  
if wnatSauce:
    cost += prices[sauceType]
totalCost = cost * quantity
print(f'\nYour order summary:\nBread: {breadType}\nProtein: {proteinType}')
if wantCheese:
    print(f'Cheese: {cheeseType}')  
if wnatSauce:
    print(f'Sauce: {sauceType}')
print(f'Quantity: {quantity}\nTotal Cost: ${totalCost:.2f}')
print('Thank you for your order!')