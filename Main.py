'''
Hi Happie! I got a GitHub AND a Reddit just to compete in this challenge, and so far, it has been a blast. 
I'm going to be on a D.C. school trip from Saturday to next Friday, so I'll still be checking on the competition when I can. LOLZ
Oh! looks like we have some imported goods for the program!
'''
# 535 lines of code!?!?

import Puppy #So true...
import time #yet another useful thingy, time is

enter = " (Press ENTER to continue...)"

name = input("???: Hello, human! Oh...you must be the trainer the owner hired. Well, I'm Spot. Nice to meet you! Wait...\nWhats your name?\n> ")
while len(name) < 4:
	name = input("Spot: That name's TOO short! Try again, with some more of those letter things on your 'typey box' there!\n> ")

asciiScramble = chr(ord(name[0]) + 1) + name[1:]
input("Spot: Ooh, \"" + name + "\"! I like it. Us puppies are very fond of anything that rhymes with " + asciiScramble + "!" + enter)
input("Spot: " + name + ", you have no idea how hard this job will be. Hundreds of billions of trainers apply here, only to run away in pure terror. You must have the stuff, seeing how you got the job.")
input("Spot: Wait. Don't tell me. YOU'RE AN UNTRAINED PUPPY TRAINER! Don't worry, though. I consider myself an expert in puppy training, as I have firsthand knowledge of how puppies work. Follow me!" + enter)
input("Spot: All right, so you can [Pet], [Talk], or [Play] with any kind of puppy, but there are some extra ones as well, for specific puppies. You need to judge what you should do based on how the puppy is acting." + enter)
input("Spot: So, I'll pretend I'm a random puppy, and you try to befriend me. Let's go!" + enter)

Puppy.Phi("Spot")

input("Spot: See? That was so much fun! For me at least. I have no idea if you were having fun too. I can't read minds.\nYet.\n" + enter[1:])
input("Spot: I'm quite surprised at your ability to befriend puppies, " + name + ". Or maybe I was going too easy on you." + enter)
input("Spot: Maybe if you're THAT good..." + enter)
input("Spot: You could try taming Baxter." + enter)
input("Spot: Who's Baxter? He's my big brother. Don't worry, he's not violent at all. He's just a bit..." + enter)
input("Spot: Nerdy. He also has a tendency to ignore people who don't respect his interests." + enter)
input("Spot: But then again, you seem to respect that puppies in this household speak fluent English, so I have NO doubt that you can make nice with him, too!" + enter)
input("Spot: Okay, here's where Baxter is. Try not to look down upon his interests; it's actually really cool. Well, good luck. Spot out!")

input("Baxter: Oh. Hello. I am BAXTER! I presume you're the new trainer. Hah! Like us puppies need a specialized human to keep us in line." + enter)
input("Baxter: Nevertheless, I always keep it in my highest regard never to make first look judgements. So..." + enter)
input("Baxter: Would you like to see my room?" + enter)

Puppy.Phi("Baxter")

input("Spot: Hey, " + name + "! I see you're having fun with Baxter." + enter)
input("Baxter: Oh, hey, Spot! Yeah, we were just talking about some cool stuff I found. Well, I was talking. " + name + " wasn't really conversing at all." + enter)
print("Baxter: Oh yeah, did you know that the keys of a piano corres-")
input("Spot: Woah woah woah. Take it down a notch. " + name + " has been given a LOT of trivia in a single sitting. Such amounts can be hazardous, or even lethal..." + enter)
input("Baxter: Spot. Plz." + enter)
input("Spot: Heh, LOLZ. So " + name + ", you've befriended Baxter. Good job, you've now done what no trainer has done before! Let's see what else you could do..." + enter)
print("Baxter: Robo-pup.")
input("Spot: Ralphy." + enter)
input("Baxter: Spot, we need to take care of the issue with Robo-pup before it becomes sentient and decides we're a waste of oxygen!" + enter)
input("Spot: 'It' is a HE, Baxter! And Robo-pup is NOT any threat! The one who really needs help is Ralphy. He's so sad right now, and his biting issue is getting worse." + enter)
input("Baxter: You're ridiculous, Spot. I knew Robo-pup was on to something the moment IT was brought in. We need to take it down as soon as physically possible. With Ralphy...we can try him after." + enter)

typePlz = input("Spot: " + name + ", I hate to put you on the spot, but should we try helping [1] Robo-pup, or [2] Ralphy?\n> ")

while typePlz != "1" and typePlz != "2":
	typePlz = input("Spot: Please just put a 1 or 2.\n> ")

if typePlz == "1":
	input("Baxter: See? I KNEW someone here would have some sense." + enter)
	input("Spot: But Ralph really needed the help, Baxter! " + name + " doesn't understand that!" + enter)
	input("Baxter: Okay, well " + name + " has decided, just like you wanted. So let's go to Robo-pup's room." + enter)
	input("Baxter: I'd prefer if you'd do this alone...Robo-pup doesn't exactly like me..." + enter)
	input("Robo-pup: [Beeping]" + enter)
	returnSnape = Puppy.Phi("Robo-pup")
	while not returnSnape:
		input("Try again!")
		returnSnape = Puppy.Phi("Robo-pup")
	input("Baxter: Whew! I thought you were never going to come out! So glad you 'took care' of Robo-pup!" + enter)
	print("Robo-pup: Hello, Baxter!")
	time.sleep(0.3) # Delay 4 Comedy
	input("Baxter: Ahhh! Robo-pup!" + enter)
	input("Baxter: He's still alive? That's not how it should've gone!" + enter)
	input("Spot: It's exactly how I wanted it to go. Robo-pup isn't evil, Baxter!" + enter)
	input("Baxter: Heh. You AND " + name + ". Why won't you guys ever listen to ME once and a while?" + enter)
	input("Baxter: Wait, what? He's been sentient and has been using personal pronouns since 2 days ago?" + enter)
	input("Robo-pup: Yes, Baxter. Can we please stop fighting and be...friends?" + enter)
	input("Baxter: ..." + enter)
	input("Baxter: ...Okay." + enter)
	print("Spot: Yipee!")
	input("Robo-pup: Yay!" + enter)
	input("Spot: Listen, Robo-pup. I'd hate to spoil your fun, but we need to help Ralphy." + enter)
	input("Robo-pup: Oh, yes. He really does need the support. Okay. It will give me and Baxter some well needed 1-to-1 talk. Right, Baxter?" + enter)
	input("Baxter: yay..." + enter)
	input("Spot: Come on, " + name + "! Just down this hall!" + enter)
	input("Spot: Okay. Here it is. Ralphy's room. Just remember. He needs his personal space. Okay, good luck." + enter)
	input("Ralphy: [Growling]")
	returnwhy = Puppy.Phi("Ralphy")
	while not returnwhy:
		input("Try again!" + enter)
		returnwhy = Puppy.Phi("Ralphy")
	input("Spot: Yay! You did it! Ralphy! It's been so long since I saw you!" + enter)
	input("Robo-pup: Hey! What's all the hub-bub about? My goodness! Ralphy's back?" + enter)
	input("Baxter: Wow! It's a miracle! Hi Ralphy. How are you doing?" + enter)
	input("Ralphy: Good." + enter)
else:
	input("Spot: See, Baxter? Our trainer " + name + " has chosen Ralphy." + enter)
	input("Baxter: Okay, I can respect that, but we NEED to get to Robo-pup IMMEDIATELY afterwards!" + enter)
	input("Spot: Okay, Baxter. If you insist. But right now, we are taking care of Ralph." + enter)
	input("Ralph: [Growling]" + enter)
	input("Spot: Well...good luck, " + name + "." + enter)
	returnwhy = Puppy.Phi("Ralphy")
	while not returnwhy:
		input("Try again!" + enter)
		returnwhy = Puppy.Phi("Ralphy")
	input("Spot: " + name + "! You did it! Oh my goodness, Ralphy! You look happy!" + enter)
	input("Ralphy: Yeah." + enter)
	input("Baxter: Wow, Ralphy! I'm just glad you're here. It's been too long." + enter)
	input("Spot: Listen, Ralphy. " + name + " needs to get to Robo-pup. We'll just stay here. Okay?" + enter)
	input("Ralphy: Okay.")
	input("Baxter: It's down the hall to the right. Make it quick." + enter)
	input("Robo-pup: [Beeping]" + enter)
	while not returnSnape:
		input("Try again!")
		returnSnape = Puppy.Phi("Robo-pup")
	input("Spot: There you are, " + name + "!" + enter)
	input("Baxter: " + name + "? Why is Robo-pup following you around?" + enter)
	input("Robo-pup: I'm a friend, Baxter. Why won't you believe me?")
	input("Baxter: Great. Now you AND Spot AND " + name + ". You're all friends and now you're cutting me off." + enter)
	input("Robo-pup: So why can't WE be friends?" + enter)
	input("Baxter: ..." + enter)
	input("Baxter: ...Fine." + enter)
	print("Spot: Yay!")
	input("Robo-pup: Yay!")
	input("Spot: And great news, " + name + "; I can read minds now! I have ze MIND CONTROL POWAHZ! Check it out." + enter)
	input(name + "-Spot" + ": Herp derp! Derpity derp! My name is " + asciiScramble + " the puppie traner! Ahuhuhuhu!!!1" + enter)
	input("Baxter: Very funny, Spot." + enter)
	input("Spot: It's never too late to control YOU, Baxter!" + enter)
	input("Baxter: Hah! Doesn't work. I've developed an immunity from the 18-some doses of 'mind control'.")
	input("Robo-pup: Wow, quite the show you two are putting on. Quite the show." + enter)

input("Spot: Thank you, " + name + ". Thank you for everything." + enter)
print("Spot: Thank you!")
print("Baxter: Thank you!")
print("Robo-pup: Thank you!")
input("Ralphy: Thank you!" + enter)
input("THE END" + enter)
input("Credits:")
input("Writing:")
input("Gene Smith")
input("Coding:")
input("Gene Smith")
input("Special Thanks:")
input("To TheHappieCat, for hosting the competition and giving me a reason to get a Reddit and GitHub account.")
input("And to my good friend Blake, who questioned every aspect of my code.")
input("And to you, " + name + ", for playing the game in its entirety.")
input("In fact, I believe it is time you battled me.")
revero = "3"
while revero != "1" and revero != "2":
	revero = input("1: [Battle Creator] 2: [Quit]\n> ")
if revero == "2":
	input("See you later!")
	f = 5/0
Puppy.Phi("Gene")
input("Well Done. I am now great friends with at least 5 people or something.")
input("Ahh, but there is something missing, no? Oh yes, HappieCat.")
input("It is time you battled her, and possibly with my horrible coding skill.")
input("You need not know a strategy, but persistence and determination will be an important trait.")
input("I can only say...good luck. Oh, and Spot says hi, and also to have fun outside after you're done. I know I haven't been the best at managing my time on the screen.")
input("Have fun.")
Puppy.Phi("CAT?")
input("Congratulations. I can't say I could've befriended her had I not been the one making the game.")
input("Go have fun outside. Whatever's online can wait.")
input("THE END")
f = 5/0


'''Hi I'm a footnote

Dear Happie,
	I realize that you, like many others, put your C++ brackets on a new line, which I find not very good.
		if (Slime.health <= 0)
		{
			~Slime()
		}
	I personally prefer keeping it on a same line, as that is the way I was taught.
		if (Slime.health <= 0) {
			Slimes.push(new Slime(200, 10, "Magic")) // Save the Animals!
		}
	I am very pleased to say Python only uses a colon and a tabbed area, so something like this would become absurd:
		if Slime.health <= 0
		:
			Slimes.append(new Slime(200, 10, "Magic")) // Save the Animals!
	Thank you for your consideration for an Oscar.
With all due respect, Gene.
'''