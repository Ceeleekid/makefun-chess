import json,os,sys,urllib.request as U
E=os.environ["MAKEFUN_ENV_URL"]
def J(p,b):
 with U.urlopen(U.Request(E+p,json.dumps(b).encode(),{"content-type":"application/json"}))as r:return json.load(r)
def sq(s):return(10-int(s[1]))*10+ord(s[0])-96
V={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':20000}
def pf(f):
 b=[' ']*120;p=f.split()
 for i in range(2,10):
  for j in range(1,9):b[i*10+j]='.'
 r=2;c=1
 for h in p[0]:
  if h=='/':r+=1;c=1
  elif h.isdigit():c+=int(h)
  else:b[r*10+c]=h;c+=1
 return b,p[1]=='w'
Z=lambda b:[c.swapcase()if c.isalpha()else c for c in reversed(b)]
def ev(b):
 s=0;wk=bk=wb=bb=0
 for i in range(21,99):
  c=b[i]
  if c<'A':continue
  r=i//10-2;f=i%10-1;u=c.upper();v=V.get(u,0);t=0
  if u=='K':
   if c<'a':wk=i
   else:bk=i
   continue
  elif u=='P':t=max(0,8-abs(2*f-7))*2+((7-r)*5 if c<'a'else r*5)
  elif u=='N':t=max(0,7-abs(2*r-7))*3+max(0,7-abs(2*f-7))*3
  elif u=='B':
   t=max(0,7-abs(2*r-7))*2+max(0,7-abs(2*f-7))*2
   if c<'a':wb+=1
   else:bb+=1
  elif u=='R':
   col=f+1;op=0
   for rr in range(2,10):
    p=b[rr*10+col]
    if p=='P'and c<'a':op=1;break
    if p=='p'and c>='a':op=1;break
   if not op:t=20
   elif(c<'a'and r==1)or(c>='a'and r==6):t=15
  s+=v+t if c<'a'else-(v+t)
 if wb>=2:s+=30
 if bb>=2:s-=30
 if wk:
  for d in(-11,-10,-9):
   if b[wk+d]=='P':s+=15
 if bk:
  for d in(9,10,11):
   if b[bk+d]=='p':s-=15
 return s
def gm(b):
 m=[]
 for i in range(21,99):
  p=b[i]
  if p<'A'or p>'Z':continue
  if p=='P':
   if b[i-10]=='.':
    if i<40:m+=[(i,i-10,q)for q in'QRBN']
    else:
     m+=[(i,i-10,'')]
     if 81<=i<=88 and b[i-20]=='.':m+=[(i,i-20,'')]
   for d in(-11,-9):
    t=i+d
    if'a'<=b[t]<='z':
     if i<40:m+=[(i,t,q)for q in'QRBN']
     else:m+=[(i,t,'')]
  elif p=='N':
   for d in(-21,-19,-12,-8,8,12,19,21):
    t=i+d
    if b[t]!=' 'and not('A'<=b[t]<='Z'):m+=[(i,t,'')]
  else:
   ds=[]
   if p in'BQ':ds+=[-11,-9,9,11]
   if p in'RQ':ds+=[-10,-1,1,10]
   if p=='K':ds=[-11,-10,-9,-1,1,9,10,11]
   for d in ds:
    t=i+d
    while b[t]!=' ':
     if'A'<=b[t]<='Z':break
     m+=[(i,t,'')]
     if'a'<=b[t]<='z'or p=='K':break
     t+=d
 return m
def mm(b,mv):
 n=b[:];f,t,pr=mv;n[t]=pr or n[f];n[f]='.'
 if n[t]=='P'and b[t]=='.'and f%10!=t%10:n[t+10]='.'
 return n
def ic(b):
 i=b.index('K')
 for d in(-21,-19,-12,-8,8,12,19,21):
  if b[i+d]=='n':return 1
 for ds,p in(((-11,-9,9,11),'bq'),((-10,-1,1,10),'rq')):
  for d in ds:
   t=i+d
   while b[t]=='.':t+=d
   if b[t]in p:return 1
 return b[i-11]=='p'or b[i-9]=='p'
H={};NC=0;NL=250000
def qs(b,a,be,qd=0):
 global NC;NC+=1
 s=ev(b)
 if s>=be:return be
 if s+900<a or qd>4:return a
 if s>a:a=s
 for m in gm(b):
  if not('a'<=b[m[1]]<='z')and not m[2]:continue
  n=mm(b,m)
  if b[m[1]]=='k':return 20000
  s=-qs(Z(n),-be,-a,qd+1)
  if s>a:a=s
  if a>=be:return a
 return a
def sr(b,d,a,be):
 global NC;NC+=1
 if d==0 and ic(b):d=1
 if d==0 or NC>NL:return qs(b,a,be) if d==0 else ev(b)
 k=''.join(b);e=H.get(k)
 ms=gm(b)
 ms.sort(key=lambda m:0 if m==e else(-V.get(b[m[1]].upper(),0)if'a'<=b[m[1]]<='z'else 999))
 bm=e
 for m in ms:
  n=mm(b,m)
  if b[m[1]]=='k':H[k]=m;return 20000+d
  s=-sr(Z(n),d-1,-be,-a)
  if s>a:a=s;bm=m
  if a>=be:break
 if bm:H[k]=bm
 return a
while 1:
 g=J("/game",{})
 if g["status"]=="done":break
 while g["status"]=="your_move":
  b,w=pf(g["fen"])
  if not w:b=Z(b)
  lm=g["legal_moves"];bm=lm[0]
  if len(lm)==1:
   g=J("/move",{"game":g["game"],"move":bm});continue
  rm=[]
  for mv in lm:
   f=sq(mv[:2]);t=sq(mv[2:4]);pr=mv[4].upper()if len(mv)>4 else''
   if not w:f=119-f;t=119-t
   rm.append((mv,f,t,pr))
  for d in range(1,9):
   NC=0;bs=-999999;cb=bm;ok=1
   for mv,f,t,pr in rm:
    n=mm(b,(f,t,pr))
    s=-sr(Z(n),d-1,-999999,-bs)
    if NC>NL:ok=0;break
    if s>bs:bs=s;cb=mv
   if ok:bm=cb
   else:break
  g=J("/move",{"game":g["game"],"move":bm})
 print(f"game {g['game']}: {g['outcome']}",file=sys.stderr)
print("done",file=sys.stderr)
