import os 



os.system(""" wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
              rpm -i epel-release-6-8.noarch.rpm """)
os.system("yum --enablerepo=epel install httpd -y")
os.system("echo THIS IS EXAMPLE WEBSITE  > /var/www/html/index.html") 
os.system("systemctl start httpd ")
os.system("tput setaf 2")
os.system("systemctl status  httpd | grep Active:")
os.system("tput setaf 7")
print ("\t\t\tSERVICE IS ACTIVATED")
a=os.popen("hostname -I | awk '{print $1}'").read() #store command in var(a)
print("use this ip on locahost webclient {}".format(a)) # print (a)


"""cd /var/www/html/

/var/www/html/index.html

echo THIS IS EXAMPLE WEBSITE  > /var/www/html/index.html """

"""out = os.popen('date').read()""" #variable in cmd


"""wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm """ #epel repo

