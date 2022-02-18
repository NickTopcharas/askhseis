from urllib.request import Request, urlopen
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
#print(data)    
l=str(data)
#find round
txt = l.split(':')
#print(txt[1])
txt2 = txt[1].split(',')
round = int(txt2[0])

#print(round)
    



for i in range(20):
    round = round - i
    req = Request('https://drand.cloudflare.com/public/'+str(round), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()

    #print(round)
 
       
    l2=str(data)
    s=l2.split('"randomness":',1)
    a2=str(s[1])
    f=a2.split(",",1)
    num=int((f[0][-6:-1]),16)
    x=(f[0][-65:-1])
#print(num)
    print(x)




