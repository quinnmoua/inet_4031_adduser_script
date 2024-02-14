#!/usr/bin/python2
import os
import re
import sys

def main():
	for line in sys.admin:
		match = re.match(r'^#', line)
	
		if not match:
			print"%s" (line)

		match = re.match('%')

		fields = line.strip().split(':')

		if match or len(fields) != 5:
			continue

	username = fields[0]
	password = fields[1]

	gecos = "%s %s,,," % (fields[3],fields[2])
	groups = fields[4].split(',') #this put a comma in whitespce.

	print "==> Create account for %s..." % (username)
	cmd = "usr/bin/adduser --disabled-password --gecos '%s' %s" %(gecos,username)

	os.system(cmd) #this runs the cmd command detailed in the above line
	print "Setting the password for %s" %(username)
	cmd = "/bin/echo/ -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" %(password,password,username)
	os.system(cmd)

	for group in groups: #
		if group != '-':
			print "Assigning %s to the %s group" %(username,group)
			cmd = "/usr/sbin/adduser %s %s" %(username,group)
			os.system(cmd)
	
	if __name__ == '__main__':
		main()
