SSN_white_list = [1324,5678,9101,7777,44557]

def input_validator(user_input, white_list):
    validate = False
    #length checker
    if len(user_input) not in (4,5):
        return ('Invalid SSN. Please check the format (0000)!!!', validate)
    #digit checker
    if not user_input.isdigit():
        return ("Please enter digit only", validate)
    #white list checker
    if int(user_input) not in white_list:
        return ("Your premissions are prohibitted, please contact with your manager", validate)

    validate = True
    return 'Welcome'

while True:
    user_ssn_number = input('Enter your SSN number in format (0000): ')
    result = input_validator(user_ssn_number,SSN_white_list)
    if result[1]:
        print(result)
        break