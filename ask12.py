from re import X
from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
l=str(data)
#findround
txt = l.split(':')
#print(txt[1])
txt2 = txt[1].split(',')
round = int(txt2[0])
def decimalToBinary(n):
    return "{0:b}".format(int(n))
#print(decimalToBinary(dec))
list3=0 
lista4=0      
list=""
p=0
m=0
for i in range(100):
    round = round - i
    req = Request('https://drand.cloudflare.com/public/'+str(round), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    l2=str(data)
    s=l2.split('"randomness":',1)
    a2=str(s[1])
    f=a2.split(",",1)
    num=int((f[0][-6:-1]),16)
    x=(f[0][-65:-1])
    dec = int(x,16)
    list = decimalToBinary(dec)
    print(list)
    if list[i-1]==0:
        p=0
        m=m+1
        list3= list3 + m
    elif list[i-1]==1:
        p=p+1
        m=0
        lista4=lista4+1
#print(max(list3)) 
#print(max(lista4))  

    

    

    #print(decimalToBinary(dec))
     


    
 
       
   