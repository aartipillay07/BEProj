import sys
import os

print ("MENU: \n1. Scale up\n2. Scale down\nEnter your choice: \n")
a=input()
if(a==1):
	n=input("Enter number of nodes: ")
	f=open("a.txt","w+")
	f.write("%d" % (n))
	f.close()
	print "Number of nodes = ",n
	os.system('MY_VAR=%d vagrant up' % (n))
else:
	x=input("Enter the number of nodes: ")
	print "Scaling down."
	buff=[]
	str1='[master]'
	str2='[nodes]'
	fl=0
	text= open("/home/aarti/pred/.vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory","r")
	for line in text:
		for word in line.split():
			if(word==str1):
				fl=1
			if(word==str2):
				fl=0
			if(fl==1):
				buff.append(word)
	text.close()
	f=open("a.txt","r")
	c=int(f.read())
	b=int(c)
	f.close()
	print buff
	while(x!=0):
		fl=0
		if(b==len(buff)-1):
			print "No more VMs can be destroyed. Exiting."
			break
		str3='node%d' % (c)
		for i in range(1,len(buff)):
			w=buff[i]
			if str3 in w:
				print "Can't destroy master node. Moving on."
				fl=1
		if(fl==0):
			os.system('MY_VAR=%d vagrant destroy node%d -f' % (b,c))
			b=b-1
			x=x-1
		c=c-1
	f=open("a.txt","w")
	f.write("%d" % (b))
	f.close()
	
