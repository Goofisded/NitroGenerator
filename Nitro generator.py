import random
import string
import time

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


