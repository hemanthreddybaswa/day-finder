import sys
def leapyear(y):
	if (y%100==0 and y%400==0) or y%4==0:
		return 1
	else:
		return 0
daycodes={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",0:"Saturday"}
monthcodes={1:1,2:4,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
lmonthcodes={1:0,2:3,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:4,12:6}
yearcodes={10:2,11:0,12:6,13:4,14:2,15:0,16:6,17:4,18:2,19:0,20:6,21:4,22:2,23:0,24:6,25:4,26:2,27:0,28:6,29:4,30:2}
a=input("Enter date(dd/mm/yy):")
try:
	while True:
		b=a.split("/")
		date=int(b[0])
		month=int(b[1])
		year=int(b[2])
		if month in [1,3,5,7,8,10,12] and date in range(1,32):
			break
		if month in [4,6,9,11] and date in range(1,30):
			break
		if month==2 and leapyear(year) and date in range(1,30):
			break
		elif month ==2 and date in range(1,29):
			break
		a=input("Enter correct date format(dd/mm/yyyy):")
except:
	print("Wrong input type")
	sys.exit()
	

	
if leapyear(year):
	calc=date+lmonthcodes[month]+yearcodes[year//100]+(year%100)+((year%100)//4)
else:
	calc=date+monthcodes[month]+yearcodes[year//100]+(year%100)+((year%100)//4)
code=calc%7
print(daycodes[code])
 


