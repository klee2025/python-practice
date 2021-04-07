#2.5.1 1부터 30까지 3의 베수를 제외하고 출력하세요
x=1
for x in range (1,31):
    if x % 3==0:
        continue
    print(x) 

#2.5.3 Consider this dna:
#2.5.3.a Store this dna string in a list.
dna = 'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctgggcctttacttcgcctccgcgccctgcattccgttcctggcctcg'

#2.5.3.b 각 염기의 개수를 dictionary형태로 저장하세요. Ex: {‘g’:30}
dna.count('g')
dna.count('c')
dna.count('a')
dna.count('t')
thisdict = {'g':30,'c':36,'a':10,'t':27}

#2.5.3.c Draw a graph with values in the dictionary
