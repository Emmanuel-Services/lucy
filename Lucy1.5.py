#updated codes to see functions
#added riddles

import random
from random import choice
from time   import sleep

name = '. ..................................\n. ................................. .\n. .##      ##  ##  ######  ##   ##. .\n. .##      ##  ##  ######   ## ## . .\n. .##      ##  ##  ##        ###  . .\n. .######  ######  ######    ##   . .\n. .######  ######  ######   ##    . .\n. ................................. .\n. .      #####       ######       . .\n. .      ## ##       ######       . .\n. .         ##       ##  ##       . .\n. .         ##       ##  ##       . .\n. .      ####### ### ######       . .\n. .      ####### ### ######       . .\n. ................................. .\n. ...................................'

def line():
	print('<------------------------------------------------------>')

points = 0
cpoints = 0
#Into
def intro():
	print(name)
	print('\n\nA [Key] Bot')
	print('Use the following keys')
	print('[D] for Database\n[G] for game\n[P] for Points'.title())
	#first key [D]atabase/[G]ame

#decoration
def decor(func):
	def wrap():
		print('\n<---------------------------->')
		func()
		print('<---------------------------->\n')
	return wrap
	
#Key-Value Database
def kvdb():
	db = {}
	print('Welcome to the simplest key-value database')
	while True:
		print('What do you want to do?')
		print('''Enter
	P to [P]ut,
	G to [G]et or
	L to [L]ist''')
		print('Or enter Q to [Q]uit')
		action = input()
		if action == 'P':
			k = input('Enter key: ')
			d = input('Enter data: ')
			db[k] = d
			
		elif action == 'G':
			k = input('Enter key: ')
			if not k in db:
				print('No such key')
			else:
				print('Your data: %s' % db[k])
		elif action == 'L':
			print('DB contents:')
			print(db)
		else:
			print('Bye')
			break

#Games
def guess_the_number():
	global points
	global cpoints
	#Random Number Game
	z = random.randint(1, 10)
	if u == '1' or u == 'GTN':
		print('\nI\'m thinking of a number between 0 - 10. What is the number'.title())
		line()
		guess = input('What\'s it: ')
		line()
		while True:
			if int(guess) == z:
				points += 1
				def text():
					print('You got the number!')
				decorated = decor(text)
				decorated()
				y = input('do you wanna play again y/n: ')
				if y == 'y' or y == 'Y':
					continue
				else:
					print('Bye!\n')
					break
			elif z > int(guess):
				guess = input('Too Low! Try again: ')
				continue
			elif z < int(guess):
				guess = input('Too High! Try again: ')
				continue
			else:
				print('bruh why')
				break
	#Game 1 Ends
def riddles():
	global points
	global cpoints
	#Game 2 Start
	if u == '2' or u == 'Riddles':
		print('Here\'s how to play riddles'.title())
		print('I ask you a question you guess the answer'.title())
		print('as simple as that, okay. Let\'s go.\n\n'.title())
		print('NOTE: Lower Case Only')
		while True:
			z = random.randint(1, 10)
			if z == 1:
				print('\nyou beg me before you use me'.title())
				ans = input('What Am I? ')
				if ans == 'Cream' or ans == 'A Cream' or ans == 'a cream' or ans == 'cream':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
				else:
					print('Incorrect\n')
					continue
			elif z == 2:
				print('\nWhat belong to you but u hardly use than anyone'.title())
				ans = input('What Am I? ')
				if ans == 'Name' or ans == 'My Name' or ans == 'a name' or ans == 'my name' or ans == 'name':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
				else:
					print('Incorrect\n')
					continue
			elif z == 3:
				print('\nwe are 3 brothers but can never meet each other'.title())
				ans = input('What Am I? ')
				if ans == 'Fan' or ans == 'Blades of a Fan' or ans == 'Fan Blades' or ans == 'blades of a fan' or ans == 'fan' or ans == 'fan blades' or ans == 'a fan' or ans == 'A fan':
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
				else:
					print('Incorrect\n')
					continue
			elif z == 4:
				print('\nI kiss my mother before I die'.title())
				ans = input('What Am I? ')
				if ans == 'a match stick' or ans == 'matches' or ans == 'a match' or ans == 'a matches':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
				else:
					print('Incorrect\n')
					continue
			elif z == 5:
				print('\nA Tiny Rod that touches the heavens and earth'.title())
				ans = input('What Am I?\n')
				if ans == 'rain' or ans == 'a rain drop':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
				else:
					print('Incorrect\n')
					continue
			elif z == 6:
				print('\nwhat room does a ghost avoid'.title())
				ans = input('What Am I? ')
				if ans == 'living room' or ans == 'a livingroom' or ans == 'livingroom' or ans == 'a living room':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
			elif z == 7:
				print('\nwhat has a forest with no trees, lakes without water, roads with no cars and deserts with no sand'.title())
				ans = input('What Am I? ')
				if ans == 'a map' or ans == 'A map' or ans == 'A MAP' or ans == 'A Map':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
			elif z == 8:
				print('\nIf I have it I don\'t share it, if I share it I don\'t have it'.title())
				ans = input('What Am I? ')
				if ans == 'a secret' or ans == 'A Secret' or ans == 'secret' or ans == 'Secret':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
			elif z == 9:
				print('\nWhat goes up when rain comes down'.title())
				ans = input('What Am I? ')
				if ans == 'an umbrella' or ans == 'An umbrella' or ans == 'An Umbrella' or ans == 'AN UMBRELLA':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
			elif z == 10:
				print('\nhow many months have 28 days'.title())
				ans = input('What Am I? ')
				if ans == 'A 12 Months' or ans == 'A Twelve Months' or ans == 'All 12 months' or ans == 'all twelve months':
					points += 1
					def text():
						print('Correct!')
					decorated = decor(text)
					decorated()
					again = input('Do You Want To Play Again? Y/N: ')
					if again == 'Y' or again == 'y':
						continue
					else:
						break
			else:
				print('Incorrect\n')
				break
def ttt():
	global points
	global cpoints
	if u == '3' or u == 'ttt':
		def Welcome():
			print('----- Tic Tac Toe Game -----')
			#dont take sleep more than 2 seconds then user will get bored
			sleep(1)
			print()
			print('Computer will decide who will play first')
			print()
			#for Hint Feature In Computer AI i have passed Player letter instead of computer letter
			print('If you need Hint in the middle of game \npress any of this [Hint,hint,H,h]')
			
			print()
			print('''******* Format of Game ******
            |   |          1 | 2 | 3
          - - - - -        - - - - - 
            |   |          4 | 5 | 6
          - - - - -        - - - - - 
            |   |          7 | 8 | 9
                                            ''')


		#Fuction to draw Board
		#you can modify this sleep method if you dont need it
		def DrawBoard(board,NeedSleep=True):
			#I thought for hint u dont need sleep method so i given default value for Needsleep 
			if NeedSleep:
				sleep(1)
			print()
			print('			 '+board[1]+'  |  '+board[2]+'  |  '+board[3])
			print('			 - - - - - - - ')
			print('			 '+board[4]+'  |  '+board[5]+'  |  '+board[6])
			print('			 - - - - - - - ')
			print('			 '+board[7]+'  |  '+board[8]+'  |  '+board[9])
			print()

		#asking the player to choose thier Letter  (X or O)
		def InputPlayerLetter():
			letter=''
			#Ask untill user enters x or o
			while not(letter == 'X' or letter == 'O'):
				print('Do you want to be X or O')
				letter = input().upper()
			
			#returning list bcz of later use
			if letter == 'X':
				return ['X','O']
			if letter == 'O':
				return ['O','X']

		#Deciding who should play first randomly
		#in usual tic-tac-toe games player first,but it selects randomly between computer and player
		def WhoFirst():
			opponents = ['computer','player']
			if choice(opponents) == 'computer':
				return 'computer'
			else :
				return 'player'
				
		#this function asks player to play again
		def PlayAgain():
			print()
			print('Do you want to Play Again (y or n)')
			playagain = input().lower().startswith('y')
			return playagain

		#function for making move
		def MakeMove(board,letter,move):
			board[move] = letter

		#check if any one win,returns True if wins
		#In tic-tac-toe there are 8 possibilities of winning
		#horizontal => 3 | vertical => 3 | diagonal => 2
		def IsWinner(board,letter):
			return ( (board[7] == letter and board[8] == letter and board[9] == letter ) or
					(board[4] == letter and board[5] == letter and board[6] == letter ) or
					(board[1] == letter and board[2] == letter and board[3] == letter ) or
					(board[1] == letter and board[4] == letter and board[7] == letter ) or
					(board[2] == letter and board[5] == letter and board[8] == letter ) or
					(board[3] == letter and board[6] == letter and board[9] == letter ) or
					(board[1] == letter and board[5] == letter and board[9] == letter ) or
					(board[3] == letter and board[5] == letter and board[7] == letter )  )

		#duplicate board is useful when we wanted to make temporary changes to the temporary copy of the board without changing the original board
		def GetBoardCopy(board):
			DupeBoard = []
			for i in board:
				DupeBoard.append(i)
			return DupeBoard
			
		#fuction to check is space is free
		def IsSpaceFree(board,move):
			return board[move] == ' '

		#Getting the player move
		def GetPlayerMove(board):
			move = ''
		
			while move not in '1 2 3 4 5 6 7 8 9'.split() or not IsSpaceFree(board,int(move)):
				print()
				print('Enter your move (1 - 9)')
				move = input()
				#if player wants Hint
				if move in HintInput:
					return move
					break  
			return int(move)

		#choose random move from given list
		#it is used when AI  wants to choose out of many possibilities
		def ChooseRandomFromList(board,MoveList):
			PossibleMoves = []
			for i in MoveList:
				if IsSpaceFree(board,i):
					PossibleMoves.append(i)
			if len(PossibleMoves) != 0:
				return choice(PossibleMoves)
			else:
				return None

		#creating computers AI
		#this ai works on this algorithm
		#1.it checks if computer can win in next move,else
		#2.it checks if player can win in next move,then it blocks it,else
		#3.it chooses any available spaces from the corner[1,3,7,9],else
		#4.it fills middle square if space free,else
		#5.it chooses any available spaces from sides,ie,[2,4,6,8]
		#if you interchange the 3 and 4 steps the AI becomes little Hard,ie,it fills middle then corner
		#--------------------------------------
		#Get computer move
		def GetComputerMove(board,ComputerLetter):
			if ComputerLetter == 'X':
				PlayerLetter = 'O'	
			else:
				PlayerLetter = 'X'

			#1.check computer can win in next move
			for i in range(1,10):
				copy = GetBoardCopy(board)
				if IsSpaceFree(copy,i):
					MakeMove(copy,ComputerLetter,i)
					if IsWinner(copy,ComputerLetter):
						return i


			#2.check player can win in next move
			for i in range(1,10):
				copy = GetBoardCopy(board)
				if IsSpaceFree(copy,i):
					MakeMove(copy,PlayerLetter,i)
					if IsWinner(copy,PlayerLetter):
						return i

			#3.checking for corner
			move = ChooseRandomFromList(board,[1,3,7,9])
			if move != None:
				return move
				
			#4.checking for the center
			if IsSpaceFree(board,5):
				return 5
				
			#5.checking for sides
			return ChooseRandomFromList(board,[2,4,6,8])
			
		#---------------------------------------   

		#checking board is full or not
		def IsBoardFull(board):
			for i in range(1,10):
				if IsSpaceFree(board,i):
					return False
			return True
					
		#fuction to print  the final win or tie board
		#made this to separate usual board and winning or tie board
		def FinalBoard(board,NeedSleep=True):
			print('			|-------------|')
			DrawBoard(board,NeedSleep)
			print('			|-------------|')

							
		#LETS START THE GAME
		Welcome()
		while True:
			#intialising board
			TheBoard = [' '] * 10
			PlayerLetter,ComputerLetter = InputPlayerLetter()
			turn = WhoFirst()
			print(f'The {turn} will go first')
			
			#gameloop
			Playing = True
			while Playing:
				
				if turn == 'player':
					print(f"	Turn => {turn}") 
					HintInput = ['Hint','hint','H','h'] 
					#taking players input
					move = GetPlayerMove(TheBoard)
					#if player needs Hint
					while move in HintInput:				
						#following code gives hint to the user
						#it runs player letter to computer AI
						HintBox = []
						for i in TheBoard:
							HintBox.append(i)
						hint = GetComputerMove(HintBox,PlayerLetter)
						MakeMove(HintBox,PlayerLetter,hint)
						print(f'HINT : placing at {hint} is better')
						FinalBoard(HintBox,False)
						move = GetPlayerMove(TheBoard)
					
					MakeMove(TheBoard,PlayerLetter,move)
					
					
					if IsWinner(TheBoard,PlayerLetter):
						FinalBoard(TheBoard)
						points += 1			
						print('❤You have WON the game❤')
						Playing = not Playing
					elif IsBoardFull(TheBoard):
						FinalBoard(TheBoard)
						print('The game is TIE\nIts good to PLAY untill you WIN❤')
						Playing = not Playing
					else :
						DrawBoard(TheBoard)
						turn = 'computer'
		
				else :
					#computer move
					print(f"	Turn => {turn}")
					move = GetComputerMove(TheBoard,ComputerLetter)
					MakeMove(TheBoard,ComputerLetter,move)
					
					
					if IsWinner(TheBoard,ComputerLetter):
						FinalBoard(TheBoard)
						cpoints += 1
						print('❤Try again bro you will win❤')
						Playing = not Playing
					elif IsBoardFull(TheBoard):
						FinalBoard(TheBoard)
						print('The game is TIE\nIts good to PLAY untill you WIN❤')
						Playing = not Playing
					else :
						DrawBoard(TheBoard)
						turn = 'player'

			if not PlayAgain():
				print("Bye!\n")
				break

def hangman():
	global points
	global cpoints
	if u == '4' or u == 'hm':
		while True:
			print()
			print()
			sleep(0.5)
			print('----- Hangman -----')
			print()
			sleep(1)
			print('select one of the following topics, select by numbers'.title())
			print('(1) Science Hangman\n(2) Eddibles')
			line()
			user = input('Your Choice: ').lower()
			line()
			print()
			if user == '1' or user == 'one':
				# List of words for the game
				halogens = ["fluorine", "bromine", "chlorine", "iodine", "astatine", "tennessine"]

				# Select a random word from the list
				word = random.choice(halogens)

				# Create a list to represent the word with dashes
				guesses = ["_" for letter in word]

				# Set the number of guesses allowed
				num_guesses = 6
				print()
				print('Halogens')

				# Loop until the player has guessed the word or run out of guesses
				while num_guesses > 0 and "_" in guesses:
					sleep(1)
					print()
					print(" ".join(guesses))  # Print the word with dashes
					sleep(0.5)
					print()
					letter = input("Guess a letter: ").lower()  # Prompt the user to guess a letter
					if letter in word:
						# If the letter is in the word, reveal the letter in the appropriate position(s)
						for i in range(len(word)):
							if word[i] == letter:
								guesses[i] = letter
					else:
						# If the letter is not in the word, decrease the number of guesses left
						num_guesses -= 1
						sleep(1)
						print("Incorrect! You have", num_guesses, "guesses left.")

				# Check if the player has won or lost
				if "_" not in guesses:
					print()
					sleep(1)
					print(' '.join(guesses))
					print("Congratulations, you guessed the word!")
					line()
					cu = input('Do you want to play again y/n: ')
					if cu == 'y':
						continue
					else:
						break
				else:
					print("Sorry, you ran out of guesses. The word was", word + ".")
					cu = input('Do you want to play again y/n: ')
					if cu == 'y':
						continue
					else:
						break
			elif user == '2' or user == 'two':
				# List of words for the game
				fruits = ["grape", "guava", "cherry", "apple", "pineapple", "banana"]

				# Select a random word from the list
				word = random.choice(fruits)

				# Create a list to represent the word with dashes
				guesses = ["_" for letter in word]

				# Set the number of guesses allowed
				num_guesses = 6
				print()
				print('Fruits')

				# Loop until the player has guessed the word or run out of guesses
				while num_guesses > 0 and "_" in guesses:
					sleep(1)
					print()
					print(" ".join(guesses))  # Print the word with dashes
					sleep(0.5)
					print()
					letter = input("Guess a letter: ").lower()  # Prompt the user to guess a letter
					if letter in word:
						# If the letter is in the word, reveal the letter in the appropriate position(s)
						for i in range(len(word)):
							if word[i] == letter:
								guesses[i] = letter
					else:
						# If the letter is not in the word, decrease the number of guesses left
						num_guesses -= 1
						sleep(1)
						print("Incorrect! You have", num_guesses, "guesses left.")

				# Check if the player has won or lost
				if "_" not in guesses:
					print()
					sleep(1)
					print("Congratulations, you guessed the word!")
					line()
					cu = input('Do you want to play again y/n: ')
					if cu == 'y':
						continue
					else:
						break
				else:
					print("Sorry, you ran out of guesses. The word was", word + ".")
					cu = input('Do you want to play again y/n: ')
					if cu == 'y':
						continue
					else:
						break


def rps():
	global points
	global cpoints
	if u == '5' or u == 'rps':
		print()
		print()
		sleep(0.5)
		print('----- Rock Paper Scissors -----')
		#dont take sleep more than 2 seconds then user will get bored
		sleep(1)
		print()
		print('How To Play:')
		sleep(0.2)
		print('There are 3 values to choose from')
		sleep(0.1)
		print('1. Rock')
		sleep(0.1)
		print('2. Paper')
		sleep(0.1)
		print('3.Scissors')
		sleep(0.1)
		print('''Rock Beats Scissors, Paper Beats Rock, Scissors Beats Paper. Now from the values 1 - 3 choose one by trying to guess what your opponent is to play.''')
		print()
		print()
		r = 'rock'
		p = 'paper'
		s = 'scissors'
		while True:
			line()
			pgus = input('Players Guess: ').lower()
			line()
			cnum = random.randint(1, 3)
			if cnum == 1:
				cgus = r
			elif cnum == 2:
				cgus = p
			else:
				cgus = s
			if pgus == cgus:
				sleep(0.5)
				print('Computer Guess: ', cgus)
				sleep(0.2)
				print()
				print('It\'s a Tie\n')
			elif pgus == p and cgus == r:
				sleep(0.5)
				print('Computer Guess: ', cgus)
				sleep(0.2)
				print()
				print('Player Wins!')
				points += 1
				print('Player Point: ', points)
				print()
			elif pgus == s and cgus == p:
				sleep(0.5)
				print('Computer Guess: ', cgus)
				sleep(0.2)
				print()
				print('Player Wins!')
				points += 1
				print('Player Point: ', points)
				print()
			elif pgus == r and cgus == s:
				sleep(0.5)
				print('Computer Guess: ', cgus)
				sleep(0.2)
				print()
				print('Player Wins!')
				points += 1
				print('Player Point: ', points)
				print()
			elif cgus == p and pgus == r:
				sleep(0.5)
				print('Computer Guess: ', cgus)
				sleep(0.2)
				print()
				print('Computer Wins!')
				cpoints += 1
				print('Computer Point: ', cpoints)
				print()
			elif cgus == s and pgus == p:
				sleep(0.5)
				print('Computer Guess: ', cgus)
				sleep(0.2)
				print()
				print('Computer Wins!')
				cpoints += 1
				print('Computer Point: ', cpoints)
				print()
			elif cgus == r and pgus == s:
				sleep(0.5)
				print('Computer Guess: ', cgus)
				sleep(0.2)
				print()
				print('Computer Wins!')
				cpoints += 1
				print('Computer Point: ', cpoints)
				print()
			elif pgus == 'quit' or pgus == 'q':
				break
			else:
				print('invalid input')
#Main Code
while True:
	#start text
	intro()
	line()
	user = input('Key: ')
	#case checking for game (1)
	if user == 'G' or user == 'g' or user == 'GAME' or user == 'Game' or user == 'game' or user == '1':
		line()
		points += 3
		print('\nThe Games Available are')
		print('(1) Guess The Number (GTN)')
		print('(2) Riddles')
		print('(3) Tic Tac Toe')
		print('(4) Hangman')
		print('(5) Rock Paper Scissors (rps)')
		line()
		u = input('Game Number: ')
		line()
		guess_the_number()
		riddles()
		ttt()
		hangman()
		rps()
	#case checking for database
	elif user == 'D' or user == 'Database' or user == 'd' or user == 'database' or user == 'db' or user == 'DB' or user == '2':
		kvdb()
		line()
	elif user == 'P' or user == 'p' or user == 'Points' or user == '#points' or user == 'POINTS' or user == '#points' or user == 'Point':
		def text():
			print('Your Points Is ', points)
			print('Total Lucy Points Are ', cpoints)
			if points > 20:
				print('\nGood Job Bro!')
			else:
				print('\nBetter Luck Next Session!')
		decorated = decor(text)
		decorated()
	elif user == 'quit' or user == 'q' or user == 'quit()':
		break
	else:
		def text():
			print('Invalid Key Retry The Program\n')
		decorated = decor(text)
		decorated()