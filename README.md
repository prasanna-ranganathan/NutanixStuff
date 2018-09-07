# NutanixStuff

### Assignment 1

**Web application:**

Write a web application to accept the following and create, delete or modify a user with the same on a Linux box:
    1. Username
    2. Shell type
    3. Home folder
    4. Password 
    5. Grant sudo privileges to the user or not.
    6. Select between create, delete and modify.
The application has to be written in Python using the flask web framework. The application will need to run as a specified user (The user will have sudo privileges). The application will need to validate the input, verify that the username provided can indeed be created, and go ahead with the specified operation that has been input.

#### Assignment 2

**Shell script**

Given a file of the form (you can use /etc/passwd):

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh

Write a bash 4.0 shell script that does not use any external commands that will sum the third field, delimited by ':'.
Your script should take the name of the file to process as the first command line argument.
The prohibition on external commands means that you do not have access to commands like sed, grep, awk, cut and so on.
