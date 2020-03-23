import os
os.system("tput setaf 2") 
print("\t\t\t WELCOME TO OUR LIFE")
print("\t\t\t---------------------------") 
os.system("tput setaf 4") 
print("THESE Are SOME COMMANDS WE ONLY CAN DO TIll NOw")

print("""
         PRESS 1 TO SEE DATE
         PRESS 2 FOR CALENDER
         PRESS 3 FOR IFCONFIG
 	 PRESS 4 TO EXIT
	 PRESS 5 FOR Web CONFIGUARE WEB SERVER
         PRESS 6 FOR uninstall httpd
         """)

while True :

    print("ENTER THE NO. IN BETWEEN ABOVE MENTION", end=" ")
    os.system("tput setaf 7") 
    usript=input("") #variable for all conditions

    if usript=="1":
      
       os.system("date") 

    elif usript=="2": 
      
         os.system("cal")

    elif usript=="3":
         os.system("hostname -I | awk '{print $1}'") #ip

    elif usript=="4":
        break    #loop break and exit

    elif usript=="5":
         os.system(""" wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
              rpm -i epel-release-6-8.noarch.rpm """) #epel-release
         os.system("yum --enablerepo=epel install httpd -y") # repo
         
         os.system("yum install httpd -y ") #install httpd
         os.system("systemctl start httpd ")
         os.system("echo THIS IS FAKE WEBSITE  > /var/www/html/index.html") #create example file in documentroot
         os.system("tput setaf 2")
         os.system("systemctl status  httpd | grep Active:") #show service status
         os.system("tput setaf 7")
         print ("\t\t\tSERVICE IS ACTIVATED")
         a=os.popen("hostname -I | awk '{print $1}'").read() #store command in var(a)
         print("use this ip on locahost webclient {}".format(a)) # print (a)

    elif usript=="6":
         os.system("rm -f /etc/yum.repos.d/code.repo") 
         os.system("yum remove httpd -y")
         os.system("yum remove epel-release.noarch -y")

    else:
        print ("SORRY :(")
        break
