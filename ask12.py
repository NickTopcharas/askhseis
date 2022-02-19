from re import X
from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
l=str(data)
#findround
txt = l.split(':')
txt2 = txt[1].split(',')
round = int(txt2[0])
def decimalToBinary(n):
    return "{0:b}".format(int(n))       
list=""
#Max ZEROES
def max_consecutive_0(input_str): 
     return  max(map(len,input_str.split('1')))
#MAX ONES     
def max_consecutive_1(input_str): 
     return  max(map(len,input_str.split('0')))     
p=0
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
    lista =  max_consecutive_0(list)
    print(lista)
    lista4 =  str(max_consecutive_1(list))
    print(lista4)
#εκτυπωνονται τα max 0,1 του κάθε γύρου ξεχωριστά 
    


    

    

   
     


    
 
       
   