import pyautogui
import random


def easy_mode():
	guess = random.randint(1,10)
	step = 1

	choice = pyautogui.prompt(
		text='Guess the number between 1 and 10 :)',
	    title='Guess Game (Easy)',
	)
	while choice != str(guess):
		pre = choice
		if int(choice) > guess:
		    choice = pyautogui.prompt(
			text=f'Enter a number smaller than {pre}',
		    	title='Guess Game (Easy)',
		    )
		elif int(choice) < guess:
		    choice = pyautogui.prompt(
			text=f'Enter a number bigger than {pre}',
		    	title='Guess Game (Easy)',
		    )
		step += 1

	check = pyautogui.confirm(
		text=f'You found the number in {step} steps', 
		title='Guess Game (Easy)', 
		buttons=['Again', 'Exit']
	)
	
	with open("Scores/easy", "r") as data1:
	    best = data1.readlines()[0]
	    if step < int(best):
	        with open("Scores/easy", "w") as data2:
	            data2.write(str(step))
	
	if check == "Again":
		easy_mode()
	else:
		pyautogui.alert(
			text="Bye Bye", 
			title='Guess Game'
		)


def medium_mode():
	guess = random.randint(1,10)
	step = 1

	choice = pyautogui.prompt(
		text='Guess the number between 1 and 50 :)',
	    title='Guess Game (Medium)',
	)
	while choice != str(guess):
		pre = choice
		if int(choice) > guess:
		    choice = pyautogui.prompt(
			    text=f'Enter a number smaller than {pre}',
		    	title='Guess Game (Medium)',
		    )
		elif int(choice) < guess:
		    choice = pyautogui.prompt(
			    text=f'Enter a number bigger than {pre}',
		    	title='Guess Game (Meduim)',
		    )
		step += 1

	check = pyautogui.confirm(
		text=f'You found the number in {step} steps', 
		title='Guess Game (Medium)', 
		buttons=['Again', 'Exit']
	)

	with open("Scores/medium", "r") as data1:
	    best = data1.readlines()[0]
	    if step < int(best):
	        with open("Scores/medium", "w") as data2:
	            data2.write(str(step))

	if check == "Again":
		easy_mode()
	else:
		pyautogui.alert(
			text="Bye Bye", 
			title='Guess Game'
		)


def hard_mode():

	guess = random.randint(1,100)
	step = 1

	choice = pyautogui.prompt(
		text='Guess the number between 1 and 100 :)',
	    title='Guess Game (Hard)',
	)
	while choice != str(guess):
		pre = choice
		if int(choice) > guess:
		    choice = pyautogui.prompt(
			    text=f'Enter a number smaller than {pre}',
		    	title='Guess Game (Hard)',
		    )
		elif int(choice) < guess:
		    choice = pyautogui.prompt(
			    text=f'Enter a number bigger than {pre}',
		    	title='Guess Game (Hard)',
		    )
		step += 1

	check = pyautogui.confirm(
	    text=f'You found the number in {step} Steps', 
	    title='Guess Game (Hard)', 
	    buttons=['Again','Exit']
	)
	
	with open("Scores/hard", "r") as data1:
	    best = data1.readlines()[0]
	    if step < int(best):
	        with open("Scores/hard", "w") as data2:
	            data2.write(str(step))
	
	if check == "Again":
		hard_mode()
	else:
		pyautogui.alert(text="Bye Bye", title='Guess Game')


mode = pyautogui.confirm(
    text = "Please select game mode\nEase: 1 to 10\nMedium: 1 to 50\nHard: 1 to 100",
    title = "Guess Game",
    buttons = ['Easy','Medium','Hard','Score']
)

if mode == "Easy":
	easy_mode()
elif mode == "Medium":
	medium_mode()
elif mode == "Hard":
	hard_mode()
else:
	with open('Scores/easy') as data:
	    lines = data.readlines()
	    easy_score = lines[0]

	with open('Scores/medium') as data:
	    lines = data.readlines()
	    medium_score = lines[0]
	    
	with open('Scores/hard') as data:
	    lines = data.readlines()
	    hard_score = lines[0]
	
	pyautogui.confirm(
            title = "Guess Game (Score)",
            text = f"easy{easy_score.rjust(10)}\nMedium{medium_score.rjust(10)}\nHard{hard_score.rjust(10)}",
	    buttons = ["OK"]	
	)
