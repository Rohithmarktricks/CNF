import random
def guessNumber(reference_num):
	count = 0
	while True:
		system_num = random.randint(1, 50)
		# print("---"+str(system_num))
		# inn = input("Enter the number: ")
		received_num = int(reference_num)
		count += 1

		if received_num > system_num :
			return "Input is greater than guess number"
		elif received_num < system_num :
			return "Input is less than guess number"
		else:
			return "Correct, Number of guesses : " +str(count)
			break