def Phi(name):
	if name == "Spot":
		spotify()
	elif name == "Baxter":
		hashtagAnime()
	else:
		return False;
	return True
	
def spotify():
	input("--| Begin Battle! Random Puppy |--")
	stage = "start"
	while True:
		brb = input("1: [Talk] 2: [Pet] 3: [Play]\n")
		if brb == "1":
			if stage == "start" or stage == "sadStart":
				input("You talked with the puppy. She thinks you're going to play fetch with her.")
				stage = "plzFetch"
			elif stage == "plzFetch":
				input("The puppy is disappointed you're yapping instead of playing.")
				stage = "sadStart"
			elif stage == "plzPet":
				input("The puppy is too tired to be listening to your talking.")
		elif brb == "2":
			if stage == "plzPet":
				input("The puppy is admiring your petting ability.")
				input("PUPPY BEFRIENDED! You win!")
				break;
			else:
				input("The puppy doesn't trust you enough to be pet.")
		elif brb == "3":
			if stage == "start":
				input("But she had no idea what you were playing!")
			elif stage == "sadStart":
				input("But she forgot what you were going to play after all that yapping!")
				stage = "start"
			elif stage == "plzFetch":
				input("Yay! Fetch! The puppy is having so much fun!")
				input("Whew! After all that playing, the puppy is very sleepy...")
				input("She lies down on your lap. Aww, so cute.")
				stage = "plzPet"
			elif stage == "plzPet":
				input("The puppy is too tired for more fetch.")
		else:
			print("Invalid Command!")
	return True;

def hashtagAnime():
	input("--| Begin Battle! Baxter |--")
	input("1: [Talk] 2: [Pet] 3: [Play]\n")
	
	input("Baxter: No no no, this outdated menu needs an overhaul; it TOTALLY does NOT reflect my battle style!" + enter)
	input("Baxter: Okay, let's see...oh! Here's the code! Cool... x86 hex instructions have never been so...Baxter-y!" + enter)
	input("Baxter: Alrighty. Change this, remove this, aaaand..." + enter)
	input("Baxter: Here we go! Let's run this baby!")
	
	input("--| Begin Battle! AWESOME-1337 Baxter |--")
	stage = 0;
	while True:
		brx = input("1: [Uh huh]\n")
		if brx == "1":
			if stage == 0:
				input("Baxter: Yep. I am DEFINITELY feeling this battle screen! Now I can show you some of my stuff.")
			elif stage == 1:
				input("Baxter: Alright. Here are my DVD copies of the entire 'The Simpsons' series, seasons 1-9. They're the only real Simpsons episodes anyways.")
			elif stage == 2:
				input("Baxter: You know, a lot of the Simpsons writers were mathematicians, most with a college degree. So naturally, there are a TON of math jokes and references in the show.")
			elif stage == 3:
				input("Baxter: My favorite is in 'Homer 3D', where Euler's identity, e^(PI*i) = -1, shows up. People who favor pi over tau often use this as a reason for why pi is superior.")
			elif stage == 4:
				input("Baxter: But pi proponents are also wrong, since e^(TAU*i) = +1. Since tau is equivalent to 2*pi, it's essentially squaring -1, which is 1.")
			elif stage == 5:
				input("Baxter: But anyways! I found out that Disneyworld is its own city.")
			elif stage == 6:
				input("Baxter: Yeah! not even kidding! Appearantly, Florida makes some money out of it, so they're okay. What's really interesting is this:")
			elif stage == 7:
				input("Baxter: Disney wants it because of city electrical laws. Disneyworld can be Disneyworld because it doesn't have to conform to city electric laws, because it IS its own city.")
			elif stage == 8:
				input("Baxter: So, if the higher ups of Disney ever wanted to...")
			elif stage == 9:
				input("Baxter: Disneyworld could go nuclear, and nobody could do anything about it. Except the state of Florida, but they probably wouldn't care, considering that nuclear power is already legal there. Same for the U.S.")
			elif stage == 10:
				input("Baxter: Oh hey. Did you know that all colors can be made with just red, green, and blue light?")
			elif stage == 11:
				input("Baxter: Yeah. That's how every digital color monitor works. Every pixel has 3 lights: red, green, and blue. Those lights can have a brightness between 0 and 255, 255 being the largest vaalue you can store with an 8-digit binary number.")
			elif stage == 12:
				input("Baxter: This gives over 16 million different possible colors for every pixel! That's more than the human eye can distinguish!")
			elif stage == 13:
				input("Baxter: But of course, I'm a puppy, so I see the world with just yellow and blue. Red and green light are virtually indistinguishable by puppies.")
			elif stage == 14:
				input("Baxter: That's okay though. We are way better with sound and smell than ANY human! It's like humans smell in black and white! It's truly quite interesting!")
			elif stage == 15:
				input("Baxter: Oh, by the way...")
			elif stage == 16:
				input("Baxter: Your name's \"" + name + "\", right?")
			elif stage == 17:
				input("Baxter: I have a quiz for you. Just to make sure you were listening.")
			else:
				break
			stage += 1
		else:
			print("Invalid command, N00B.")
	answ = input("Question 1: Tau = n * Pi. what does n equal?")
	if answ.lower() == "two" or answ == "2":
		print("Yay! you got it right!")
	else:
		print("Nope! I was looking for 2.")
	answ = input("Question 2: Disneyworld relies on the surrounding cities's lax electrical restraints to run. True or False?")
	if answ.lower() == "false" or answ.lower() == "f" or answ.lower() == "n" or answ.lower() == "no":
		print("Yay! you got it right!")
	else:
		print("Nope! I was looking for False.")
		
	answ = input("Question 3: What is the maximum brightness of a blue light of a pixel?")
	if answ == "255":
		print("Yay! you got it right!")
	else:
		print("Nope! I was looking for 255.")
	input("Baxter: Welp. Your score doesn't really matter. All that matters is that you listened.")
	input("PUPPY BEFRIENDED! You win!")
	return True;