#!/usr/bin/python
import cgi,os,commands,time,cgitb
cgitb.enable()
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
dn=data.getvalue('dn')
ds=data.getvalue('ds')
print dn
print ds
 
 
x1=commands.getoutput('hostname -I')
#hostname -I shows all the network addresses(IP) of the hosts
ip=x1.split(' ')
#split ip on behalf of space
#to get client's ip address
 
 
#already pvcreate and vgcreate is done on linux platform ->name of vg is adhoccloud
 
commands.getoutput('sudo lvcreate --name {}   --size {}M adhoccloud'.format(dn,ds))
#logical volume is created of given name and size
commands.getoutput('sudo mkfs.fat /dev/adhoccloud/{}'.format(dn))
#format the lv created in before step 
commands.getoutput('sudo mkdir  /mnt/{}'.format(dn))
#directory is created where lv is mounted
commands.getoutput('sudo mount /dev/adhoccloud/{}    /mnt/{}'.format(dn,dn))
#mount is performed
#to make the partition permanent
 
nfs_write="/mnt/{}    *(rw,no_root_squash)\n".format(dn)
x=open('/etc/exports','a')
x.write(nfs_write)
x.close()
'''
By default, NFS shares change the root user to the nfsnobody user, an unprivileged user account. In this way, all root-created files are owned by nfsnobody, which prevents uploading of programs with the setuid bit set.
If no_root_squash is used, remote root users are able to change any file on the shared file system and leave trojaned applications for other users to inadvertently execute. 
'''
 
commands.getoutput('sudo exportfs -r')
#Causes all directories listed in /etc/exports to be exported by constructing a new export list in /etc/lib/nfs/etab. This option effectively refreshes the export list with any changes made to /etc/exports. 
 
 
 
commands.getstatusoutput("echo 'mkdir /mnt/{}' > /var/www/html/{}.sh".format(dn,dn))
commands.getstatusoutput("echo mount {}:/mnt/{} /mnt/{} >> /var/www/html/{}.sh".format(ip[0],dn,dn,dn))
 
commands.getstatusoutput('sudo chmod o+w /var/www/html/{}.sh'.format(dn))
commands.getstatusoutput('sudo chmod +x /var/www/html/{}.sh'.format(dn))
print commands.getoutput(' tar cvf ../html/{}.tar {}.sh'.format(dn,dn))
print "<script>"
print "alert('extract to mount your storage:')"
print "</script>"
m1= "<meta HTTP-EQUIV='refresh' content='0;url=http:///{}/{}.tar'/>".format(ip[0],dn)
print m1
