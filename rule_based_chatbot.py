import re #regular expression
import random
from colorama import Fore,init #intializer
#automatically resets text color
init(autoreset=True)
destination={"beaches":["Bali", "Maldives","phuket"],"mountains":["Himalyas", "Rocky Mountains", "Swiz elsps", "Mount Fiji" ], "citiys":["Tokyo", "Paris", "Shenzhen", "Pune"]}
jokes=["why don't programmers like nature? too many bugs", "Why did the computer go to the doctor? because it had a virus! ","Why do travlers always feel warm? becuase of all their hot spots!", "Why do computers wear glasses? to improve there websight!",]

def greet_user():
    print(Fore.CYAN+"Hello! I am travelBot🤖 your virtual travel assistant")
    name = input(Fore.YELLOW+"May I know your name?")
    print(Fore.GREEN+f"Nice to meet you {name} !😁 How can I assist you today?") 
    return name

def show_help():
    print(Fore.MAGENTA+"\n I can assist you with the following : ")
    print(Fore.GREEN+"-Provide travel recommandation.")
    print(Fore.GREEN+"-Offer packing trips.")
    print(Fore.GREEN+"-Tell travel jokes.")
    print(Fore.CYAN+"Just ask me a question or type exit to leave. ")
    
def process_input(user_input):
    user_input = user_input.strip().lower()
    user_input = re.sub(r'\s+','',user_input)

def provide_recomendations():
    print(Fore.CYAN+"🤖:Are you intrested in beaches, mountains, or cities?")
    prefrence = input(Fore.YELLOW+"You:")
    prefrence = process_input(prefrence)
    if prefrence in destination:
        suggestion = random.choice(destination[prefrence])
        print(Fore.GREEN+f"🤖: How about visiting {suggestion}.")
        print(Fore.CYAN+"🤖: Do you like this suggestion? (Yes/No)")
        responce = input(Fore.YELLOW+"You:").strip().lower()
        if responce == "yes":
            print(Fore.GREEN+f"🤖: Great have an amazing time in {suggestion}!")
        elif responce == "no":
            print(Fore.RED+"🤖: No worries! lets find another place")
            provide_recomendations()
        else:
            print(Fore.RED+"🤖: I didnt catch that, lets start over")
            provide_recomendations()
    else:
        print(Fore.RED+"🤖: Sorry!, I dont have recomendations for that prefrence")
        show_help()

def offer_packing_tips():
    print(Fore.CYAN+"🤖: Where are you traveling to? ")
    destination = input(Fore.YELLOW+"You: ")
    destination = process_input(destination)
    print(Fore.CYAN+"🤖: How many day+s will you be staying?")
    days = input(Fore.YELLOW+"You:")
    print(Fore.GREEN+f"Packing tips for {days} days in {destination}:")
    print(Fore.GREEN+"-Pack versictile clothing items")
    print(Fore.GREEN+"-Dont forget travel adapters and chargers")
    print(Fore.GREEN+"-Check the weather forecast before packing")