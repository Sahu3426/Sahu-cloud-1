#!/usr/bin/python
 
import  cgi
import cgitb
cgitb.enable()
 
print  "Content-Type:text/html"
print  ""
 
#  storing all the data from client 
client_data=cgi.FieldStorage()
# extracting LANGuage 
web_lang=client_data.getvalue('lang')
print web_lang
#  extracting only OS name 
os_name=client_data.getvalue('os')
print  os_name
#  extracting  only RAM 
os_ram=client_data.getvalue('ram')
print os_ram
#  extracting only CPU in Core 
os_cpu=client_data.getvalue('cpu')
print  os_cpu 
 
# making  a random number 
number=random.random()
# int to string 
strnumber=str(number)
# defining port no
osn=strnumber[2:6]
#  making clone/snapshot of original images  
print  commands.getoutput('sudo qemu-img  create -f qcow2 -b /var/lib/libvirt/images/rhvmdnd.qcow2   /var/lib/libvirt/images/adhoc'+osn+'.qcow2')
#  passing  all this information to  Hypervisor  that QEMU-kVM 
 
os_install="sudo virt-install  --name  adhoc"+osn+"  --ram  "+os_ram+"  --vcpu  "+os_cpu+"   --disk path=/var/lib/libvirt/images/adhoc"+osn+'.qcow2   --import  --noautoconsole'
 
print  commands.getoutput(os_install)
 
#showing vm status page
print  "<meta http-equiv='refresh' content='2;url=http://192.168.10.203/cgi-bin/vm_status.py'/>"
