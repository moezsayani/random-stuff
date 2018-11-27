# wordlist generator for attackdefenselabs excerise
# allowed characters are a,b,c,d,e,1,2,3,4,5, exactly 6 char. 
import itertools
wordlist = open('dict.txt','w')
res = itertools.product('abcde12345', repeat=6)
for i in res: 
  wordlist.write(''.join(i) + '\n')    
