#include"stdio.h"
int leapyear(int y){
	if ((y%100==0 && y%400==0) || y%4==0)
		return 1;
	else
		return 0;
}
int main()
{
	int date,month,year,calc,code;
	const char* daycodes[20]={"Saturday","Sunday","Monday","Tuesday","Wednesday","THursday","Friday"};
int monthcodes[20]={0,1,4,4,0,2,5,0,3,6,1,4,6};
int lmonthcodes[20]={0,0,3,4,0,2,5,0,3,6,1,4,6};
int yearcodes[50];
yearcodes[16]=6;
yearcodes[17]=4;
yearcodes[18]=2;
yearcodes[19]=0;
yearcodes[20]=6;
printf("Enter date(dd/mm/yyyy):");
scanf("%d/%d/%d",&date,&month,&year);
if(leapyear(year))
{
	calc=date+lmonthcodes[month]+yearcodes[year/100]+(year%100)+((year%100)/4);
}
else{
	calc=date+monthcodes[month]+yearcodes[year/100]+(year%100)+((year%100)/4);
}
code=calc%7;
printf(daycodes[code]);
}

