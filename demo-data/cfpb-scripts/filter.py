import csv,zipfile,glob,io,collections,re
csv.field_size_limit(10**9)
out=[];seen=set();stats=collections.Counter();dates=[]
for z in sorted(glob.glob('zips/*.zip'),key=lambda p:int(re.search(r'Export_(\d+)_',p).group(1))):
    zf=zipfile.ZipFile(z); n=zf.namelist()[0]
    with zf.open(n) as fh:
        r=csv.DictReader(io.TextIOWrapper(fh,encoding='utf-8-sig',newline=''))
        for row in r:
            stats['rows_all']+=1
            if 'student loan' not in row['Product'].lower(): continue
            stats['student_loan']+=1
            if row['Issue'].strip().lower()!='dealing with your lender or servicer': continue
            stats['issue_match']+=1
            if not row['Consumer complaint narrative'].strip(): continue
            stats['with_narrative']+=1
            if row['Complaint ID'] in seen: stats['dup_id']+=1; continue
            seen.add(row['Complaint ID']); row['_file']=z.split('/')[-1]
            out.append(row)
    print(z.split('/')[-1],dict(stats),flush=True)
ds=sorted(r['Date received'] for r in out)
print('date range',ds[0],ds[-1],'n',len(out))
with open('filtered.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
