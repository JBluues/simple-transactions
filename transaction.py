'''
1. Create account
2. Check balance
3. Send money
4. Deposit
5. Exit
'''

def menu():
	print('1. Create account')
	print('2. Check balance')
	print('3. Send money')
	print('4. Deposit')
	print('5. Exit')


def create_account():
	name = input('Enter your name: ')
	first_deposit_amount = float(input("Enter first deposit amount: "))
	# print(f'{name} your account is created successfully with an initial deposit of {first_deposit_amount} cedis')
	return name,first_deposit_amount


def accounts():
		accts = []
		accts.append(create_account())
		print(accts)

def select_option():
	opt = int(input('Select an option: '))
	return opt



'''
Program runs below
'''

# menu()

match select_option():
	case 1:
		create_account()
		accounts()
