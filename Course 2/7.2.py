# Use the file name mbox-short.txt as the file name
count=0
avg=0;
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        pos=line.find(":")
        avg=avg+float(line[pos+1:].strip())
        count=count+1
print "Average spam confidence: "+str(avg/count)