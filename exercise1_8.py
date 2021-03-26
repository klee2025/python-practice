#1.8.1 Write a Python program to get the largest number from a list.
sample = [-8,-10,1,2,0]
ans = sample[0]

for x in sample:
    #x가 최대면 ans에 추가
    if  ans < x :
        ans = x
print(ans)

#1.8.2 Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
sample = ['abc','xyz','aba','1221']
ans = []

for x in sample:
    #x가 조건에 맞으면 ans에 append
    if len(x)>=2 and x[0] == x[-1]:
        ans.append(x)
print(ans)

#1.8.5 Write a Python program to remove duplicates from a list.
sample=[1,1,2,2,3,3,4,4,5]
ans=[]

for x in sample:
    if x not in ans:
        ans.append(x)

print(ans)

#1.8.7 write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
sample=[1,1,2,2,3,3,4,4,5]
sample2=[1,5,6,7]
ans2=[]

for x in ans:
    if x in sample2:
        ans2.append(x)

print(ans2)
