import Puppy #So true...

enter = " (Press ENTER to continue...)"

name = input("???: Hello, human! Oh...you must be the trainer the owner hired. Well, I'm Spot. Nice to meet you! Wait...\nWhats your name?\n")
while len(name) < 4:
	name = input("Spot: That name's TOO short! Try again, with some more of those letter things on your 'typey box' there!")

asciiScramble = chr(ord(name[0]) + 1) + name[1:]
input("Spot: Ooh, \"" + name + "\"! I like it. Us puppies are very fond of anything that rhymes with " + asciiScramble + "!" + enter)
input("Spot: Wait. Don't tell me. YOU'RE AN UNTRAINED PUPPY TRAINER! Don't worry, though. I consider myself an expert in puppy training, as I have firsthand knowledge of how puppies work. Follow me!" + enter)
input("Spot: All right, so you can [Pet], [Talk], or [Play] with any kind of puppy, but there are some extra ones as well, for specific puppies. You need to judge what you should do based on how the puppy is acting." + enter)
input("Spot: So, I'll pretend I'm a random puppy, and you try to befriend me. Let's go!" + enter)

Puppy.Phi("Spot")

input("Spot: See? That was so much fun! For me at least. I have no idea if you were having fun too. I can't read minds.\nYet.\n" + enter[1:])
input("Spot: I'm quite surprised at your ability to befriend puppies, " + name + ". Or maybe I was going too easy on you." + enter)
input("Spot: Maybe if you're THAT good..." + enter)
input("Spot: You could try taming Baxter." + enter)
input("Spot: Who's Baxter? He's my big brother. Don't worry, he's not violent at all. He's just a bit..." + enter)
input("Spot: Nerdy. He has a tendency to ignore people who don't respect his interests." + enter)
input("Spot: But then again, you seem to respect that puppies in this household speak fluent English, so I have NO doubt that you can make nice with him, too!" + enter)
input("Spot: Okay, here's where Baxter is. Try not to look down upon his interests; it's actually really cool. Well, good luck. Spot out!")

input("Baxter: Oh. Hello. I am BAXTER! I presume you're the new trainer. Hah! Like us puppies need a specialized human to keep us in line." + enter)
input("Baxter: Nevertheless, I always keep it in my highest regard never to make first look judgements. So..." + enter)
input("Baxter: Would you like to see my room?" + enter)

Puppy.Phi("Baxter")

input("Spot: Hey, " + name + "! I see you're having fun with Baxter." + enter)
input("Baxter: Oh, hey, Spot! Yeah, we were just talking about some cool stuff I found. Well, I was talking. " + name + "wasn't really conversing at all." + enter)
print("Baxter: Oh yeah, did you know that the keys of a piano corres-")
input("Spot: Woah woah woah. Take it down a notch. " + name + " has been given a LOT of trivia in a single sitting. Such amounts can be hazardous, or even lethal..." + enter)
input("Baxter: Spot. Plz.")

#input("End of program. Press enter to exit.")