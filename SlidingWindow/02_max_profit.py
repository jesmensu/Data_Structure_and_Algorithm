# find out the maximum profit for the stock price for one long long buy and sell

lst = [1,21,1,7,2,22,24]

fp = 0
sp = 1
max_profit = 0

while(sp<len(lst)):
    dif = lst[sp] - lst[fp]
    if dif > max_profit:
        max_profit = dif
    if lst[fp] > lst[sp]:
        fp = sp

    sp += 1
print(max_profit)






# find out the maximum profit for the stock price for multiple buy and sell
lst = [1,21,1,7,2,22,24]

fp = 0
sp = 1
max_profit = 0

while(sp<len(lst)-1):
    dif = lst[sp] - lst[fp]
    if dif > 0 and lst[sp+1] < lst[sp]:
            max_profit += dif
            fp = sp + 1

    sp += 1
dif = lst[sp-1] - lst[fp]
max_profit += dif

print(max_profit)




fp = 0
max_profit = 0

for i in range(1, len(lst)-1):
    dif = lst[i] - lst[fp]
    if dif > 0 and lst[i+1] < lst[i]:
        max_profit += dif
        fp = i + 1

dif = lst[len(lst)-1] - lst[fp]
max_profit += dif

print(max_profit)