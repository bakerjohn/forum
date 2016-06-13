


Step 1. Download this software to your laptop

http://releases.ubuntu.com/14.04/ubuntu-14.04.4-desktop-i386.iso 

#save to your desktop


http://www.linuxliveusb.com/downloads/?stable
 
#run the program- get a desktop icon

Step 2. Insert USB drive


Step 3. Open linux live usb creator (follow the steps below) 

	1. choose the usb key should look like <E: UUI – FAT32 – 3.7 GB>
	2. Choose a source- ISO/IMG/ZIP – 
	< Find the ISO file you saved to the desktop earlier. >
	3. add 1000mb Persistence
	4. OPTIONS – select formate the key in FAT32 and Enable launching linuxlive 	in Windows.
	5. click on the lightening bolt

# Wait about 30 minutes for the software to complete.


Step 4. Test 
	1. turn off your laptop.
	2. Insert the linux usb key.
	3. turn on your laptop and start hitting the F12 key until the boot drive screen pops up.
	4. each system is different however you want to boot from usb or disk.
	5. you should see the Ubuntu boot screen come up. Remember this is running on a usb key so it going to be slow.
	6. click on the wifi icon > Select internet  > password is ################


STEP 5. Go to the linux command line utility- you may have to search by typing in command in search field

Command prompt: Ubuntu@Ubuntu:-$

	Ubuntu@Ubuntu:-$ sudo  apt-get install postgresql python-psycopg2 
	Ubuntu@Ubuntu:-$ sudo apt-get update 

	Ubuntu@Ubuntu:-$ sudo apt-get install git  ( 5 minutes )


STEP 6. Make a directory for your files

	Ubuntu@Ubuntu:-$ mkdir vagrant
	Ubuntu@Ubuntu:-$ cd vagrant

STEP 7. Clone the respository from github
	Ubuntu@Ubuntu:-$ git clone https://github.com/bakerjohn/forum.git


STEP 8. Create a new user
	Ubuntu@Ubuntu:-$ sudo adduser vagrant

	Create the password vagrant
	-then just click enter through all the other stuff

STEP 9. Switch to the new user.
	Ubuntu@Ubuntu:-$ su – vagrant

STEP 10. Login to the database

	Ubuntu@Ubuntu:-$ sudo –u postgres psql

#You will get the Postgres prompt- Postgres=# 

Step 11. Create the database and owner

	Postgres=# CREATE USER vagrant WITH PASSWORD 'vagrant';

	Postgres=# CREATE DATABASE forum OWNER vagrant;

	Postgres=# \q (to quit out of the database)


#back at the ubuntu command prompt: Ubuntu@Ubuntu:-$

Step 12.  switch to the user vagrant

Ubuntu@Ubuntu:-$ Sudu su – vagrant

Step 13. login to the database called forum

	vagrant:Ubuntu@Ubuntu:-$ Psql forum

	#you are now in the forum database Forum=>

Forum=>

 STEP 14. type \d to verify there are no tables in the database.

# you should see No relations found

STEP 15. create a table in the database

Forum=> CREATE TABLE posts ( content TEXT,time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,id SERIAL );


STEP 16. \d

# you should see the database table you just created.


STEP 17. type exit to close the terminal.

STEP18. Open a new terminal and type the following commands.
	Ubuntu@Ubuntu:-$ cd vagrant
	Ubuntu@Ubuntu:-$ cd forum
	Ubuntu@Ubuntu:-$ python forum.py




congrats your done with. you know have a fullstack website on a stick!!! go see your website at localhost:8000
