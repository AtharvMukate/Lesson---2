from textblob import TextBlob
import colorama
from colorama import Fore,Back,Style
import sys
import time
user_name = " "
convention_history = []
positive_count = 0
negative_count = 0
neutral_count = 0
def show_processing_animation():
    print ( f"{fore.CYAN}", "detection sentiment clues", end = ' '  )
    for _ in range(3):
        time.sleep(0.5)
        print(".", end = " ")
        sys.stdout.flush()
def analyze_sentitment(text):
    try:
        global positive_count,neutral_count,negative_count
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        convention_history.append(text)
        if sentiment > 0.75:
            positive_count += 1
            return f"\n {fore.GREEN} ✨✨ Very positive sentiment!, agent {user_name} (score : {sentiment:.2f})"
        elif 0.25 < sentiment <= 0.75:
            positive_count += 1
            return f"\n {fore.GREEN} 😁 positive sentiment!, agent {user_name} (score : {sentiment:.2f})"
        elif -0.25 <= sentiment <= 0.25:
            neutral_count += 1
            return f"\n {fore.YELLOW} 😐 netural sentiment!, agent {user_name} (score : {sentiment:.2f})"
        elif -0.75 <= sentiment <= -0.25:
            negative_count += 1
            return f"\n {fore.RED} 💔 negative sentiment!, agent {user_name} (score : {sentiment:.2f})"
        else:
            negative_count += 1
            return f"\n {fore.RED} 💔💔 Very negative sentiment!, agent {user_name} (score : {sentiment:.2f})"
    except Exception as e:
        return f"\n {fore.RED} an error occured during sentiment analys: {str(e)}"
def execute_command(command):
    if command == "summary":
        return (f"{fore.CYAN} mission report: \n "
                f"{fore.GREEN} positive message detected: {positive_count} \n"
                f"{fore.RED} negative message detected: {negative_count} \n"
                f"{fore.YELLOW} neutral message detected: {neutral_count} \n")
    elif command == "reset":
        convention_history.clear()
        positive_count = negative_count = neutral_count = 0
        return f"{fore.CYAN} mission reset! all previous data has been cleared"
    elif command == "history":
        return "".join([f"{fore.CYAN} message {i+1}: {msg}" for i,msg in enumerate (convention_history)])\
            if "convention_history" else f"no convention history available"
    elif command == "help":
        return {f"{fore.CYAN} Available commands: \n  "
                f" - type any sentence to analize its sentiment- "
                f" - type summary to get a mission report on anailzed sentiments"
                f" - type reset to clear or mission data and start fresh - "
                f" - tyoe history to view all preivious messages and analizes - "
                f" - type exit to conclude your mission and leave the chat"}
    else:
        return f"{fore.RED} Unkown commande, type help for the list of commands"
def get_valid_name():
    while True:
        name = input(" whats your name? ")
        if name and name.isalpha():
            return name
        else:
            print(f" {fore.RED}please enter a valid name with only a aplphabetic charecter")
def start_sentiment_chart():
    print(f" {fore.CYAN} {style.BRIGHT} 😀 welcome to the sentiment spy, this is your personal emotion detection!")
    global user_name
    user_name = get_valid_name()
    print(f" \n {fore.CYAN} nice to meet you agent 😀 {user_name}! type your sentence to analize emotions \n type help for options")
    while True:
        user_input = input(f" \n {fore.MAGENTA} {style.BRIGHT} agent {user_name}: {style.RESET_ALL} ").strip
        if not user_input:
            print (f"{fore.RED} please enter a non empty message or type 'help' for available commands")
            print (execute_command(user_input.lower()))
        elif user_input.lower() == "exit":
            print (f"\n {fore.BLUE} mission complete exiting sentiment spy farewell agent {user_name}!")
            break
        elif user_input.lower() in ["summary","reset","history","help"]:
            print (execute_command(user_input.lower()))
        else:
            show_processing_animation()
            result = analyze_sentitment(user_input)
            print (result)
if __name__ == "__main__":
    start_sentiment_chart()
