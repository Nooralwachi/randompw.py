import re
from collections import Counter
def random_passwords(filename):
	pattern= '^([a-z0-9]{4}\-){2}[a-z0-9]{4}$'
	passwords= []
	with open (filename, 'r') as file, open('output.txt', 'w') as fw:
		for line in file:
			line= line.strip()
			if re.match(pattern, line) :
				passwords.append(line)
		pw=Counter(passwords)
		print(pw)
		for line,count in pw.items():
			if count==1:
				fw.write(line + '\n')

random_passwords("randompw.txt")