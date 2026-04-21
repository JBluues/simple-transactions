'''
1. Create account
2. Check balance
3. Send money
4. Deposit
5. Exit
'''
accts = []
def menu():
	print('1. Create account')
	print('2. Check balance')
	print('3. Send money')
	print('4. Deposit')
	print('5. Exit')


def create_account():
	name = input('Enter your name: ')
	first_deposit_amount = float(input("Enter first deposit amount: "))
	print(f'{name} your account has been created successfully with an initial deposit of {first_deposit_amount} cedis')
	created_account = (name,first_deposit_amount)
	return created_account


def save_account():
		
		accts.append(create_account())
		print(accts)
		return accts
		
def select_option():
	opt = int(input('Select an option: '))
	return opt


'''
Program runs below
'''
menu()
while True:
	
	match select_option():
		case 1:
			a = save_account()
		case 2:
			print(a)