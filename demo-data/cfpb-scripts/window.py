import csv,os
csv.field_size_limit(10**9)
rows=[r for r in csv.DictReader(open('filtered.csv',encoding='utf-8')) if '2026-02-01'<=r['Date received']<='2026-07-31']
d='/home/user/uxrexploration/demo-data/cfpb-sample/feb-jul-2026'; os.makedirs(d+'/narratives',exist_ok=True)
cols=['Complaint ID','Date received','Company','Product','Sub-product','Issue','Sub-issue','Submitted via','Date sent to company','Company response to consumer','Company public response','Timely response?','Tags','State','ZIP code']
rows.sort(key=lambda r:(r['Date received'],int(r['Complaint ID'])))
with open(d+'/labels.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.DictWriter(fh,fieldnames=cols,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
for r in rows: open(f"{d}/narratives/{r['Complaint ID']}.txt",'w',encoding='utf-8').write(r['Consumer complaint narrative'].strip()+"\n")
print(len(rows),rows[0]['Date received'],rows[-1]['Date received'],len({r['Complaint ID'] for r in rows}))
