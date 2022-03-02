# violent-python3
Practiced the concepts of the book [Violent Python: A Cookbook for Hackers, Forensic Analysts, Penetration Testers and Security Engineers](https://www.amazon.com/Violent-Python-Cookbook-Penetration-Engineers/dp/1597499579) using virtual machines. I used the book as a guide but for the most I tried to use my own implementations to accomplish the tasks outlined the book. 
## Environment Setup
To do the execises I used VMware for my hypervisor. In my VM setup, I used two machines, an attacker and victim. 
### Victim Machine Notes
- Operating System is Ubuntu 18.04
- Exists an ftp server in order to complete chapter 1. In this case, I used an [vsftpd](https://en.wikipedia.org/wiki/Vsftpd) server. For the purposes of following the book I just used the default configuration, i.e. ```sudo apt update && sudo apt install vsftpd -y```. 

### Attacker Machine Notes
 - a Kali Linux machine
 - added a mapping of the Victim's machine's hostname to IP address to the ```/etc/hosts``` file. 