import random
import string
import time

def generate_nitro_code():
    code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    return f'Discord Promo Code: https://discord.gift/{code}'

print("\033[91m" + "╔" + "═" * 50 + "╗")
print("║" + " " * 19 + "NITRO GENERATOR BY GOOF" + " " * 19 + "║")
print("╚" + "═" * 50 + "╝" + "\033[0m")
print("Press Ctrl+C to stop generating Discord promo codes.\n")

try:
    while True:
        nitro_code = generate_nitro_code()
        print(nitro_code)
        time.sleep(1)  

except KeyboardInterrupt:
    print("\nCode generation stopped.")


