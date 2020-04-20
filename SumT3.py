#Program to sum two integers,and if the sum is between 15 to 20 it will return 20

mars=int(input("Enter first Number:>>>"))
ifeanyi=int(input("Enter second Number:>>>"))
sum= mars+ ifeanyi
if(sum in range(15,21)):
    print(20)
else:
    print(sum)

