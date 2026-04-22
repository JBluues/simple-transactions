# NB: zero defensive coding, just wanted things to work systematically

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
	created_account = list((name,first_deposit_amount))
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
			accts = save_account()
		case 2:
			username = input('Please enter your username to view balance: ')
			for acct in accts:
				if acct[0] == username:
					print(f'{acct[0]} Balance: {acct[1]}')
		case 3:
			username = input('Please enter your username to send money: ')
			for acct in accts:
				if acct[0] == username:
					receiver = input("Please enter receiver's username: ")
					sender_amt = acct[1]
					for acct in accts:
						if acct[0] == receiver:	
							send_amt = float(input('Please enter amount to be sent: '))
							if sender_amt >= send_amt:
								print(f'{send_amt} cedis sent successfully to {acct[0]}')
								acct[1] += send_amt					
							for acct in accts:
								if acct[0] == username:
									if sender_amt >= send_amt:
										acct[1] -= send_amt
		case 4:
			username = input('Please enter your username to make deposit: ')
			for acct in accts:
				if acct[0] == username:
					deposit_amt = float(input('Please enter amount to be *deposited: '))
					print(f'{deposit_amt} cedis deposited successfully')
					print(f'Previous Balance: {acct[1]}')
					acct[1] += deposit_amt
					print(f'Current Balance: {acct[1]}')
		case 5:
			print('y means yes and n means no')
			exit_msg = input('Are you sure you want to exit. enter y/n: ')
			if exit_msg == 'y':
				exit()