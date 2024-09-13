import pyautogui
import time
import argparse
import os

parser = argparse.ArgumentParser(description="Spam messages using pyautogui")
parser.add_argument("-m", "--message", type=str, help="Message to spam")
parser.add_argument("-f", "--file", type=str, help="Path to text file with the message to spam")
parser.add_argument("-c", "--count", type=int, default=10, help="Number of times to spam the message")
parser.add_argument("-d", "--delay", type=float, default=1.0, help="Delay between each message in seconds")
args = parser.parse_args()

if args.file:
    if not os.path.exists(args.file):
        print(f"File {args.file} does not exist.")
        exit()
    with open(args.file, "r") as f:
        spam_message = f.read().strip()
elif args.message:
    spam_message = args.message
else:
    print("You must provide either a message or a file.")
    exit()

print("Switch to your Discord chat window...")
time.sleep(5) 

for _ in range(args.count):
    pyautogui.typewrite(spam_message)  
    pyautogui.press("enter")  
    time.sleep(args.delay)  

