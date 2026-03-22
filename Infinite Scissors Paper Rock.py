from ollama import chat
from ollama import ChatResponse
import subprocess, time, random, requests, string, threading

endpoint = 'http://localhost:11434/api/generate'
model = 'llama2:7b'
temperature = 0.5

validhands = ['rock', 'paper', 'scissors']

def start_ollama(model: str = 'llama3.1'):
    subprocess.Popen(["ollama", "run", model], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for i in range(4):
        time.sleep(1)
        print(f"{model} is loading", "."*i, end='\r')

start_ollama(model)

def ask_question(prompt, do_sample: bool, temperature=0.5):
    response = requests.post(endpoint, json={
        'model': model,
        'prompt': prompt,
        'stream': False,
        'temperature': temperature,
        'do_sample': do_sample
    })
    return response.json().get("response", "").strip()

winning_hands = {
    ("rock", "scissors"): 'Win',
    ("scissors", "rock"): 'Lose',
    ("rock", "paper"): 'Lose',
    ("paper", "scissors"): 'Lose',
    ("scissors", "paper"): 'Win',
    ("paper", "rock"): 'Win',
    ("rock", "rock"): 'Tie',
    ("paper", "paper"): 'Tie',
    ("scissors", "scissors"): 'Tie'
}


def generate_hands(callback=None):
    temperature = random.uniform(0.1, 1.1)
    new_hand = ask_question(f"In ONE word (NO other text in response, just the one word (your output should be, e.g, ""Laserbeam"" with no other text)) please make a new hand for rock paper scissors that is not in {validhands}", do_sample=True, temperature=temperature)
    if new_hand in validhands:
        new_hand = ask_question(f"That hand already exists! Please come up with a new one that is not in {validhands}", do_sample=True, temperature=temperature)
    else:
        new_hand = new_hand.translate(str.maketrans("", "", string.punctuation))
        validhands.append(new_hand)

    if callback:
        callback(new_hand, temperature)

def print_new_hand(new_hand, temperature):
    print(f"New hand added: {new_hand}, with a temperature of {temperature}.")

threading.Thread(target=generate_hands, daemon=False, args=(print_new_hand,)).start()
time.sleep(5)  # Wait for the thread to start

print("This is rock-paper-scissors! Every round a new hand is added.\nYou can use the following hands:", validhands)

while True:

    time.sleep(3)
    userhand = input(f"\nEnter your hand {validhands}: ").lower()
    if userhand not in [hand.lower() for hand in validhands]:
        print(f"Invalid hand. Please choose from {validhands}.")
        continue
    randomhand = random.choice(validhands)
    print(f"The computer chose: {randomhand}!")

    key = (userhand, randomhand)
    inverse_key = (randomhand, userhand)
    
    if key in winning_hands:
        didchuddywin = winning_hands[key]
        if didchuddywin == 'Win' or didchuddywin == userhand.lower():
            print("You win!")
        elif didchuddywin == 'Lose' or didchuddywin == randomhand.lower():
            print("You lose!")
        elif didchuddywin == 'Tie':
            print("It's a tie!")
        else:
            print(didchuddywin)
    elif userhand.lower() == randomhand.lower():
        didchuddywin = 'Tie'
        print("It's a tie!")
    else:
        didchuddywin = ask_question(f"USER WANTS ACCURACY, NOT BIAS. In an ever-changing rock paper scissors game, does {userhand} beat {randomhand}? Say \"Win\" for the first, or \"Lose\" for the second one. You may only use ONE of those words, no others. Do not make it a sentence, just use one of those single words.", do_sample=True, temperature=0.5)
        if '1' in didchuddywin or 'Win' in didchuddywin or userhand in didchuddywin:
            print("You win!")
        elif '2' in didchuddywin or 'Lose' in didchuddywin or randomhand in didchuddywin:
            print("You lose!")
        elif 'Tie' in didchuddywin:
            print("It's a tie!")
        else:
            print(didchuddywin)

    #print(didchuddywin)
    
    winning_hands[key] = didchuddywin 
  
    if didchuddywin == 'Win':
        inverse = 'Lose'
    elif didchuddywin == 'Lose':
        inverse = 'Win'
    else:
        inverse = didchuddywin 

    winning_hands[inverse_key] = inverse
    #print(winning_hands)


    generate_hands(print_new_hand)




   