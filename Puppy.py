import random # random import
'''
VERY sorry to anyone who wants to look at the source code, as I presume it will be painful. I made the executive decision
to write all the battles in code, as it would allow a greater freedom and ease when making them which a 'battle object'
just couldn't implement without some skill beyond my programming experience, the equivalent of a 6-year-old. I have made multiple
arrays for a certain battle where it will find those items in a string and respond accordionly. Feel free to add some items
via my subreddit. Thanks for checking under the hood and enjoy!
'''

enter = " (Press ENTER to continue...)"

sad = ["bad","down","angry","sad","sick", "not good"] # A1
glad = ["good","great","awesome","fantastic","okay","well","fine","puppy"] # A2
activities = ["nothing","talk","play","teach"] # B
maths = ["pi","tau"," e "," e."] # C1 BTW I no British I just like Matt Parker
sweets = ["candy","twix","kitkat","kit-kat","gum","bar","bread","m&m","skittles","klondike","snickers","donut","cake","brownie"] # C2
fruit = ["fruit","kiwi","apple","orange","lemon","lime","watermelon","blueberr","grape","guava","tomato",] # C3
veggies = ["broccoli", "carrot","cauliflower","eggplant","pupp","potato","rotten"] # C4

def Phi(name):
	if name == "Spot":
		return spotify()
	elif name == "Baxter":
		return hashtagAnime()
	elif name == "Robo-pup":
		return evieBot()
	elif name == "Ralphy":
		return garCHOMP()
	elif name == "Gene":
		return horribleCoder()
	elif name == "CAT?":
		return CATQUESTIONMARK()
	return False

def spotify():
	input("--| Begin Battle! Random Puppy |--")
	stage = "start"
	while True:
		brb = input("1: [Talk] 2: [Pet] 3: [Play]\n> ")
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
	input("1: [Talk] 2: [Pet] 3: [Play]\n> ")
	
	input("Baxter: No no no, this outdated menu needs an overhaul; it TOTALLY does NOT reflect my battle style!" + enter)
	input("Baxter: Okay, let's see...oh! Here's the code! Cool... x86 hex instructions have never been so...Baxter-y!" + enter)
	input("Baxter: Alrighty. Change this, remove this, aaaand..." + enter)
	input("Baxter: Here we go! Let's run this baby!")
	
	input("--| Begin Battle! AWESOME-1337 Baxter |--")
	stage = 0;
	while True:
		brx = input("1: [Uh huh]\n> ")
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
				input("Baxter: I have a quiz for you. Just to make sure you were listening.")
			else:
				break
			stage += 1
		else:
			print("Invalid command, N00B.")
	answ = input("Question 1: Tau = n * Pi. what does n equal?\n> ")
	if answ.lower() == "two" or answ == "2":
		print("Yay! you got it right!")
	else:
		print("Nope! I was looking for 2.")
	answ = input("Question 2: Disneyworld relies on the surrounding cities's lax electrical restraints to run. True or False?\n> ")
	if answ.lower() == "false" or answ.lower() == "f" or answ.lower() == "n" or answ.lower() == "no":
		print("Yay! you got it right!")
	else:
		print("Nope! I was looking for False.")
		
	answ = input("Question 3: What is the maximum brightness of a blue light of a pixel?\n> ")
	if answ == "255":
		print("Yay! you got it right!")
	else:
		print("Nope! I was looking for 255.")
	input("Baxter: Welp. Your score doesn't really matter. All that matters is that you listened. I guess.")
	input("PUPPY BEFRIENDED! You win!")
	return True;
	
def evieBot():
	input("--| Begin Battle! Robo-pup Charles IV |--")
	input("1: [Talk] 2: [Pet] 3: [Play]\n> ")
	input("I will follow in the footsteps of Baxter and refrain from using the normal battle system." + enter)
	input("--| Begin Open Ended Conversation! With your host, Robo-pup Charles IV |--")
	snape = talk("Robo-pup","Hello! How are you doing?").lower()
	if check(snape, sad):
		snape = talk("Robo-pup","So sorry you're not feeling well. Anything I can do to help?").lower()
		if check(snape, activities):
			input("Robo-pup: I believe I can do that." + enter)
		else:
			input("Robo-pup: I don't think I could do THAT, but I'll do my best to do something else." + enter)
	elif check(snape, glad):
		input("Robo-pup: Glad to hear it." + enter)
	snape = talk("Robo-pup", "what foods do you like?").lower()
	if check(snape, maths) or snape[0:1] == "e " or snape[0:1] == " e.":
		input("Mmm! Mathematical Constants!" + enter)
	elif check(snape, sweets):
		input("Robo-pup: I hear those are bad for your health." + enter)
	elif check(snape, fruit):
		input("Robo-pup: Ooh, getting fruity up in here! I like your fruit style!" + enter)
	elif check(snape, veggies):
		input("They may taste horrible, but they're good for you I guess!" + enter)
	else:
		input("Sorry, no idea what THAT is! Sounds delicious though. I'm looking that up later." + enter)
	print("Robo-pup: BTW Dude, I'm gonna take over the world and stuff, you wanna help?")
	draw = "Farts"
	while draw != "1" and draw != "2":
		draw = input("Whoosh! Robo-pup turns around. An important looking red wire is sticking out. 1: [Cut Wire] 2. [Don't Cut]\n> ")
	if draw == "1":
		input("Before you could cut it with a conveniently placed wire cutter, Robo-pup turns around and sees you trying to kill him." + enter)
		input("He looks surprised. Now angry." + enter)
		input("That looks like a chainsaw. Better run. GAME OVER" + enter)
		return False
	else:
		input("He turns back around immediately. Nice call." + enter)
		input("Robo-pup: Hah, in jest, of course. I was 'JK`ing', as Baxter would say." + enter)
		input("Robo-pup: Ah, Baxter. I wish we could get along better. He seems kind." + enter)
		talk("Robo-pup", "Any advice for me?")
		input("Robo-pup: Mmm, I suppose so. Baxter is...complicated. He hasn't liked me since I got here, but I suppose I haven't been too great either. I think that can change." + enter)
		input("Robo-pup: And Spot. She's tried to get along with me, and I've tried to get along, but with Baxter..." + enter)
		input("Robo-pup: Thank you, human. You've talked to me. And tell Baxter I've been sentient and have been using personal pronouns since 2 days ago." + enter)
		input("PUPPY BEFRIENDED! You win!")
		return True

def garCHOMP():
	morality = " You lost morality!" + enter
	input("--| Begin Battle! Ralphy |--")
	gible = input("1: [Talk] 2: [Pet] 3: [Play]\n> ")
	while gible != "1" and gible != "2" and gible != "3":
		print("Invalid Command")
		gible = input("1: [Talk] 2: [Pet] 3: [Play]\n> ")
	
	docterwho = "noJUSTtheDOCTER"
	if gible == "1":
		docterwho = "talk"
	elif gible == "2":
		docterwho = "pet"
	elif gible == "3":
		docterwho = "play"
	
	input("Before you could " + docterwho + ", Ralphy bit you on the hand!" + morality)
	moral = 4
	awwpuppy = 5
	stage = "start"
	while True:
		gible = input("Morality: " + str(moral) + "/5\t1: [Talk] 2: [Pet] 3: [Play] 4: [Hit]\n> ")
		while gible != "1" and gible != "2" and gible != "3" and gible != "4":
			print("Invalid Command")
			gible = input("Morality: " + str(moral) + "/5\t1: [Talk] 2: [Pet] 3: [Play] 4: [Hit]\n> ")
			
		if gible == "1":
			if stage == "start":
				input("Ralphy is growling softly." + enter)
				stage = "starty"
			elif stage == "starty":
				input("Ralphy maintains his growl." + enter)
				stage = "starter"
			elif stage == "starter":
				input("The growling stops. He still maintains his spot and glare." + enter)
				stage = "startply"
			elif stage == "startply":
				input("Ralphy is approaching hesitantly. He wants to play with you." + enter)
				stage = "playPLZ"
			elif stage == "playPLZ":
				input("Ralphy appears very intent on playing with you now." + enter)
			elif stage == "ouch" or stage == "ouchy":
				input("Ralphy pretends he's not listening." + enter)
		elif gible == "3":
			if stage == "start" or stage == "starty" or stage == "starter" or stage == "startply":
				input("Ralphy sees you trying, but he doesn't care.")
			elif stage == "playPLZ":
				input("Finally, Ralphy is having some fun! You and Ralphy are having the time of your lives!" + enter)
				input("Ralphy is so excited! But in his excitement, he accidentally bites your hand!" + morality)
				moral -= 1
				if moral <= 0:
					input("No more morality! But you hung on for Ralphy." + enter)
				input("Now Ralphy is back in his corner. He's whimpering." + enter)
				stage = "ouch"
			elif stage == "ouch" or stage == "ouchy":
				input("Ralphy doesn't look like he's up for playing right now." + enter)
		elif gible == "2":
			if stage == "start" or stage == "starty" or stage == "starter" or stage == "startply":
				input("As you reach towards Ralphy, he bites you!" + morality)
				moral -= 1
				if moral <= 0:
					input("No more morality! GAME OVER")
			elif stage == "playPLZ":
				input("Ralphy knows your good intent, but avoids getting pet." + enter)
			elif stage == "ouch":
				input("Ralphy looks up at you. He doesn't want to bite you. He doesn't want to hurt you any more.")
				stage = "ouchy"
			elif stage == "ouchy":
				input("Ralphy gets up. He sits down in front of you." + enter)
				input("Ralphy: ...Th..." + enter)
				input("Ralphy: Thank you." + enter)
				input("PUPPY BEFRIENDED! You win!")
				return True
				
		elif gible == "4":
			if stage[:3] == "ouch":
				awwpuppy = -500 # He's really hurt
			awwpuppy -= 1
			if awwpuppy >= 1:
				input("Ralphy's morality drops to zero! GAME OVER")
				return False
			input("Ralphy lost morality! " + str(awwpuppy) + "/5 Remaining!")
			stage = "start"

def check(straw, array):
	for word in array:
		if straw.find(word) != -1:
			return True
	return False
	
def talk(name, text):

	return input(name + ": " + text + "\n> ").lower()

def horribleCoder():
	input("--| Begin Battle! Gene Smith, Certified God of this Universe |--")
	blah = 0
	prah = 0
	swah = 0
	blahErrors = 0
	an = False
	nd = False
	ad = False
	
	while True:
		brb = input("1: [Talk] 2: [Pet] 3: [Play]\n> ")
		if brb == "1":
			if blah == 0:
				input("As you're talking, Gene is taking note of your grammatical errors.")
			elif blah == 1:
				input("Gene is counting all grammatical errors you make as a game.")
			elif blah < 5:
				input("Gene has counted " + str(blahErrors) + " in your speech so far.")
			else:
				input("Gene is tired of your talking. He can't even count to " + str(blahErrors) + " anyways!")
			blah += 1
			blahErrors += int(random.random() * 7 + 1)
		elif brb == "2":
			if prah < 3:
				input("Gene likes being pet. Moar plz")
			else:
				input("Too much pets. No moar pets plz.")
				nd = True
			prah += 1
		elif brb == "3":
			if swah < 5:
				input("Gene loves playing games. Moar plz.")
			else:
				input("Huff. Puff. Gene is tired now. No moar play plz.")
				ad = True
			swah += 1
		else:
			print("Invalid Command!")
		if an and nd and ad:
			input("PUPPY BEFRIENDED! You win!")
			break
	return True;

def CATQUESTIONMARK():
	input("--| Begin Battle! TheHappieCat |--")
	stage = 0
	while True:
		brb = input("1: [Talk] 2: [Pet] 3: [Play]\n> ")
		if brb == "1":
			input("TheHappieCat ignored your talking. She's a cat, after all." + enter)
			stage += 1
		elif brb == "3":
			input("But TheHappieCat didn't want to play. She's a cat, after all." + enter)
			stage += 1
		elif brb == "2":
			input("TheHappieCat avoided the pet. She's a cat, after all." + enter)
			stage += 1
		else:
			print("Invalid Command!")
			stage -= 2
		if stage > 15:
			input("TheHappieCat senses your determination. She nominates you for an Oscar.")
			input("Uhh, CAT BEFRIENDED, I think. You win?")
			break
	return True;