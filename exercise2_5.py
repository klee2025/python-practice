#2.5.1 1부터 30까지 3의 베수를 제외하고 출력하세요
x=1
for x in range (1,31):
    if x % 3==0:
        continue
    print(x)
