
##
# 20CS080 Jekeel Shah
# Practical 7
# # 
for T in range(int(input())):
     lst = list(input()) 
     splt = len(lst) // 2 
     lst1 = lst[:splt] 
     if len(lst) % 2 == 0: 
         lst2 = lst[splt:]  
     else: 
         lst2 = lst[splt + 1:] 
     lst1.sort() 
     lst2.sort() 
     if lst1 == lst2: 
         print('YES') 
     else: 
         print('NO')