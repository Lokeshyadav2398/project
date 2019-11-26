def count_substring_by_filename(fname):
	count = 0
	fd=open(fname,"r")
	for line in fd:
		count = count + line.count("warning")
	fd.close()
	return count

c1 = count_substring_by_filename("1log.txt")
c2 = count_substring_by_filename("2log.txt")
print (c1)
print (c2)

if(c2 > c1):
    print("reject")
else:
    print("promot")