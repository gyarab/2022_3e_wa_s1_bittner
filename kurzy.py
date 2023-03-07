import httpx
from pprint import pprint
from colorama import Fore, Back, Style

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=96FE83E9CC12D50E27DB4C33A2239874?date=23.01.2023"

res = httpx.get(url)

rows = res.text.split("\n")

rows = rows[2:-1]

data = {}

for r in rows:
    cols = r.split("|")
    curr = cols[-2]
    rate = cols[-1]
    amount = cols[-3]
    rate = rate.replace(",", ".")
    rate = float(rate)
    data[curr] = float(rate)/float(amount)

user_case = input(Fore.CYAN + 
    "Pokud chcete převádět z Kč na cizí měnu stiskněte 1\n"
    "Pokud chcete převádět z cizí měny stiskněte 2\n"
)

if user_case == "1":
    user_amount = input(Fore.MAGENTA + "Zadejte částku v CZK: ")
    user_amount = float(user_amount)
    user_curr = input(Fore.MAGENTA + "Zadejte cílovou měnu: ")

    result = user_amount / data[user_curr]
    result = round(result, 2)

    print(Fore.GREEN + f"Vysledna castka je {result} {user_curr}")

elif user_case == "2":
    user_curr = input(Fore.MAGENTA + "Zadejte púvodní měnu: ")
    user_amount = input(Fore.MAGENTA + "Zadejte částku: ")
    user_amount = float(user_amount)

    result = user_amount * data[user_curr]
    result = round(result, 2)

    print(Fore.GREEN + f"Vysledna castka je {result} Kč")

else:
    print(Fore.RED + Back.YELLOW + "nevalidni input")
