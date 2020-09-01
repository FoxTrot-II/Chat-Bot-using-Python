import os
import pyttsx3 as spk
import datetime
import wikipedia
import webbrowser
print("                                WELCOME                                         ")
print("--------------------------------------------------------------------------------") 
spk.speak("Thanks for choosing ME.")


spk.speak("Now make a wish")
    

def speaker(param):
	spk.speak("Here you go..."+param+"...launching for you!")


while True:
	print("See the menu below and choose anything ")
	print("1)  Wanna make your calculations easier ?........................type calculator") 

	print("2)  Do you want to gather some information on any topic ?........type wikipedia")

	print("3)  Do you want to search and watch videos ?.......................type youtube ")
    
	print("4)  Do you want to write something ?................................type notepad")

	print("5)  Do you want to draw and paint something ?.....................   type paint ")

	print("6)  Wanna surf internet ?.........................................  type google ")


	q = input(" PLEASE ENTER YOUR WISH : ")
	if ("notepad" in q):
		y = "notepad"
		speaker("notepad")
		os.system(y)
		print(y+ "..LAUNCHED..")
	elif ("calculator" in q):
		y = "calc"
		speaker("calculator")
		os.system(y)
		print(y+ "..LAUNCHED..")
	elif ("youtube" in q):
		spk.speak("Here you go...")
		webbrowser.open("youtube.com")
	elif ("paint" in q):
		y = "mspaint"
		speaker("Paint")
		os.system(y)
		print(y+"..LAUNCHED..")
	elif ("google" in q):
		spk.speak("Processing your request....")
		webbrowser.open("google.com")
	elif ("wikipedia" in q):
		spk.speak("OK,Great what you want me to search...")
		print("Your wish :")
		question = input()
		s = wikipedia.summary(question, sentences = 4)
		spk.speak(s)

	elif ("exit" in q):
		y = "exit"
		spk.speak("Thank you...hope you liked it")
		print("Exited Visit Again")
		break
	else:
		spk.speak("Oops!!!!..I am not allowed to fulfill your wish..Sorry")
		