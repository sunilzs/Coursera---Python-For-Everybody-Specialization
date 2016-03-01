#from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dict=dict()
for line in handle:
	if line.startswith('From '):
		words=line.split()
		words=words[5].split(':')
		dict[words[0]]=dict.get(words[0],0)+1
	
for key in sorted(dict):
	print key, dict[key]