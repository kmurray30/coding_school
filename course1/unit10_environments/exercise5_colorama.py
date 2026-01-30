# Install colorama first: pip install colorama

from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.RED + "This text is red!")
print(Fore.GREEN + "This text is green!")
print(Fore.BLUE + "This text is blue!")
print(Style.BRIGHT + "This text is bright!")
print(Fore.YELLOW + Style.BRIGHT + "This is bright yellow!")

# Expected output:
# (colored text in terminal)
