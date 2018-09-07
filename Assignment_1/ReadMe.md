# Assignment 1

  A Python Rest API web application for the users using Python Flask MicroFramework.
  
## Pre-requites
   
   * ubuntu 14.04
   * Python2.7
   * docker CE edition for Ubuntu 
   
  
  To run the Assignment. 
  
  ```
   $ git clone https://github.com/stuxnet78/NutanixStuff.git
   $ cd NutanixStuff/Assignment_1
   $ docker build -t user-app-details .
   $ docker images
   $ docker run -d -p 80:5000 -v $(pwd):/app user-app-details
   $ docker ps
  ```

Now Our Docker user app details application is running. Now to create/delete/update/read users. Only "Admin" user has the permission.

A Unauthorized access.

```
root@haproxy:~/Nautnix/Docker/NutanixStuff/Assignment_1# curl -X GET localhost/user
{                                                                                  
  "Message": "Please Authenticate",                                                
  "error": "Unauthorized",                                                         
  "status": 401                                                                    
}
```

We need credentials to create/read/update/delete user. But only admin as the permission.

To Read All Users

```
curl -u 'admin:admin123' -X GET localhost/user
{
  "Users": [
    {
      "homedir": null,
      "id": 1,
      "shelltype": null,
      "username": "admin"
    },
    {
      "homedir": "/home/ranganathan",
      "id": 3,
      "shelltype": "/bin/bash",
      "username": "ranganathan"
    }
  ]
}
```

To create a user

```
root@haproxy:~/Nautnix/Docker/NutanixStuff/Assignment_1# curl -u 'admin:admin123' -X POST -d '{"username":"prasanna","shelltype":"/bin/bash","homedir":"/root/"}' -H "Content-Type: applicati

on/json" localhost/user
{
  "Status": "User Created Successfully"
}

To Read again,

$ curl -u 'admin:admin123' -X GET localhost/user
{
  "Users": [
    {
      "homedir": null,
      "id": 1,
      "shelltype": null,
      "username": "admin"
    },
    {
      "homedir": "/home/ranganathan",
      "id": 3,
      "shelltype": "/bin/bash",
      "username": "ranganathan"
    },
    {
      "homedir": "/root/",
      "id": 4,
      "shelltype": "/bin/bash",
      "username": "prasanna"
    }
  ]
}
```

To Update the **bash shell for user 3 to /bin/sh**

```
 root@haproxy:~/Nautnix/Docker/NutanixStuff/Assignment_1# curl  -u 'admin:admin123' -X PUT -d '{"username":"ranganathan","homedir":"/home/ranganathan","shelltype":"/bin/sh"}' -H "Content-Type: application/json" localhost/user/3
{
  "Status": " User Details Update"
}


root@haproxy:~/Nautnix/Docker/NutanixStuff/Assignment_1# curl -u 'admin:admin123' -X GET localhost/user   
{                                                                                                         
  "Users": [                                                                                              
    {                                                                                                     
      "homedir": null,                                                                                    
      "id": 1,                                                                                            
      "shelltype": null,                                                                                  
      "username": "admin"                                                                                 
    },                                                                                                    
    {                                                                                                     
      "homedir": "/home/ranganathan",                                                                     
      "id": 3,                                                                                            
      "shelltype": "/bin/sh",                                                                             
      "username": "ranganathan"                                                                           
    },                                                                                                    
    {                                                                                                     
      "homedir": "/root/",                                                                                
      "id": 4,                                                                                            
      "shelltype": "/bin/bash",                                                                           
      "username": "prasanna"                                                                              
    }                                                                                                     
  ]                                                                                                       
}
```

TO delete a user 4

```
root@haproxy:~/Nautnix/Docker/NutanixStuff/Assignment_1#curl -u 'admin:admin123' -X DELETE localhost/user/4
{
  "Status": "User Details Deleted"
}

root@haproxy:~/Nautnix/Docker/NutanixStuff/Assignment_1# curl -u 'admin:admin123' -X GET localhost/user
{
  "Users": [
    {
      "homedir": null,
      "id": 1,
      "shelltype": null,
      "username": "admin"
    },
    {
      "homedir": "/home/ranganathan",
      "id": 3,
      "shelltype": "/bin/bh",
      "username": "ranganathan"
    }
  ]
}
```

Note: you cannot delete User ID 1 (i.e Admin)

```
 curl -u 'admin:admin123' -X DELETE localhost/user/1
{
  "Status": "Cannot Delete Admin User"
}
```

