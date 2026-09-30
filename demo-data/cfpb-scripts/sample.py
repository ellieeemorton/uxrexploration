import csv,collections,random,os,re
csv.field_size_limit(10**9)
rows=list(csv.DictReader(open('filtered.csv',encoding='utf-8')))
N=40;MINCO=8
sub=collections.Counter(r['Sub-issue'] for r in rows)
tot=sum(sub.values())
raw={k:N*v/tot for k,v in sub.items()}
alloc={k:int(x) for k,x in raw.items()}
for k in sorted(raw,key=lambda k:raw[k]-alloc[k],reverse=True)[:N-sum(alloc.values())]: alloc[k]+=1
print("allocation",alloc,sum(alloc.values()))
random.seed(20260930)
byc=collections.Counter();sel=[]
for attempt in range(1,1001):
    byc=collections.Counter();sel=[]
    for k,n in alloc.items():
        sel+=random.sample([r for r in rows if r['Sub-issue']==k],n)
    byc=collections.Counter(r['Company'] for r in sel)
    if len(byc)>=MINCO: break
print("attempts",attempt,"companies",len(byc),dict(byc))
assert len(sel)==N and len(byc)>=MINCO
d='/home/user/uxrexploration/demo-data/cfpb-sample'; os.makedirs(d,exist_ok=True)
for r in sel:
    open(f"{d}/{r['Complaint ID']}.txt",'w',encoding='utf-8').write(r['Consumer complaint narrative'].strip()+"\n")
with open(f"{d}/cfpb-labels.csv",'w',newline='',encoding='utf-8') as fh:
    w=csv.writer(fh); w.writerow(['Complaint ID','Company','Issue','Sub-issue','Date received'])
    for r in sorted(sel,key=lambda r:r['Complaint ID']): w.writerow([r['Complaint ID'],r['Company'],r['Issue'],r['Sub-issue'],r['Date received']])
# diagnostics
def wc(t): return len(t.split())
allw=sorted(wc(r['Consumer complaint narrative']) for r in rows)
print("population words median",allw[len(allw)//2],"p10",allw[len(allw)//10],"<30 words",sum(w<30 for w in allw))
norm=lambda t:re.sub(r'\W+',' ',t.lower()).strip()
full=collections.Counter(norm(r['Consumer complaint narrative']) for r in rows)
print("pop exact-dup texts (groups>1):",sum(1 for v in full.values() if v>1),"rows in them",sum(v for v in full.values() if v>1))
pre=collections.Counter(norm(r['Consumer complaint narrative'])[:150] for r in rows)
print("pop same-first-150 groups>1:",sum(1 for v in pre.values() if v>1),"rows",sum(v for v in pre.values() if v>1))
print("pop XXXX share",sum('XXXX' in r['Consumer complaint narrative'] for r in rows)/len(rows))
print("SAMPLE")
for r in sorted(sel,key=lambda r:r['Sub-issue']):
    t=r['Consumer complaint narrative']; x=len(re.findall(r'X{2,}',t))
    print(r['Complaint ID'],wc(t),"words XXrun",x,"|",r['Company'][:18],"|",r['Sub-issue'][:25])
print("sample exact dup:",[k for k,v in collections.Counter(norm(r['Consumer complaint narrative']) for r in sel).items() if v>1])
