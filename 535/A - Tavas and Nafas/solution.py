n = input().strip()
d = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"}
if int(n)<21:
    print(d[int(n)])
elif int(n)%10==0:
    print(d[int(n)])
else:
    f = ((int(n))//10)*10
    a = int(n[1])
 
    print((d[f])+"-"+(d[a]))