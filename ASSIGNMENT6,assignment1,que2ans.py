import json

Dictionary = {
    'Andhra Pradesh': 'Hyderabad',
    'Gujarat': 'Gandhinagar',
    'Karnataka': 'Bengaluru',
    'Maharashtra': 'Mumbai',
    'Punjab': 'Chandigarh',
    'Tamil Nadu': 'Chennai',
    'West Bengal': 'Kolkata'
}

print(Dictionary)
with open("state_capital.json","w") as f:
     json.dump(Dictionary,f)