##
# 20CS080 Jekeel Shah
# Practical 6
# #
N = int(input()) 
COUNT_DICT = {} 
WL = [] 
for i in range(N): 
    M = input() 
    WL.append(M) 
    if M in COUNT_DICT: 
        COUNT_DICT[M] += 1 
    else: COUNT_DICT[M] = 1 
print()
print(len(COUNT_DICT)) 
print(' '.join([str(COUNT_DICT[M]) for M in COUNT_DICT]))