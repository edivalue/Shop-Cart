#Designed, Constructed & Implement by edivalue
from tabulate import tabulate
from colorama import Fore,init

item_list=[Fore.RESET+"ITEMS"]
price_list=["PRICES"]
total_list=["TOTAL"]

init()
print((Fore.YELLOW+'\tWELCOME TO EDIVALUE\'S MALL\n')+'_'*40+'\n')

subtotal=0
item=input(Fore.CYAN+"WOULD YOU LIKE TO PURCHASE AN ITEM (Y or N): ")

while item.lower()=="y":
	item_name=input(Fore.GREEN+"\nKindly Enter item: ")
	item_list.append(item_name)
	price=float(input(Fore.LIGHTRED_EX+"\nPrice for item: "))
	subtotal+=price
	price_list.append(price)
	total_list.append("")
	item=input(Fore.LIGHTBLACK_EX+'WOULD YOU LIKE TO PURCHASE AN ITEM (Y or N): ')
	
print(Fore.RESET+"")	
item_list.append(Fore.RESET+"(SUBTOTAL)")
total_list.append(subtotal)
price_list.append(Fore.RESET+"✓")
edi=[item_list,price_list,total_list]
print(tabulate(edi))
