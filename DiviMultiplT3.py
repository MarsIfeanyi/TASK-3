#program to find numbers which are divisible by 7 and multiple of 5...........
#between the range of 1500 and 2700 both inclusive

count = 0
for m in range(1500, 2701):
    if m % 7 == 0 and m % 5 == 0:
        print(m)
        count += 1
print(count)


