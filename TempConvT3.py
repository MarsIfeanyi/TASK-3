#Program for temperature conversions

ans = int(input("1 for celsius to Fahrenheit, 2 for Fahrenheit to celsius"))
If temp == 1:
	celsius = int(input("enter a temp in celsius"))
	fah = (celsius - 9/5) + 32
	print('%.2f Celsius is: %.2f Fahrenheit' %(celsius, Fahrenheit))
else:
	Fahrenheit = int(input("yourtemp in Fahrenheit"))
	celsius = (Fahrenheit - 32) * 5/9
	print('%.2f Fahrenheit is: %.2f Celsius' %(Fahrenheit, celsius))