#Designed, Constructed & Implement by edivalue
from tabulate import tabulate
from colorama import Fore,init

init()
m=1
Total=0.0
listc=[['#','ITEM','PRICE']]
it,e=0,int(input(Fore.RED+'Enter "0" to stop & "1" to start: '))

while e!=0 and it!='0':
		it=input(Fore.GREEN+"\nKindly Enter item: ")
		pt=float(input(Fore.LIGHTRED_EX+"\nPrice for item: "))
		ar=m,it,pt
		y=list(ar)
		Total+=pt
		listc.append(y)
		e=int(input(Fore.LIGHTBLACK_EX+'Enter "0" to stop: '))
		if e!=0:
			m+=1
T=(Fore.WHITE+'TOTAL: ',"",Total)
to=list(T)
listc.append(to)
print(tabulate(listc))
