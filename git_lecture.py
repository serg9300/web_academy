SSN_white_list = [1324,5678,9101]
while True:
    user_ssn_number = input('Enter your SSN number in format (0000): ')
    #length checker
    if len(user_ssn_number) != 4:
        print('Invalid SSN. Please check the format (0000)!!!')
        continue
    if not user_ssn_number.isdigit():
        print("Please enter digit only")
        continue