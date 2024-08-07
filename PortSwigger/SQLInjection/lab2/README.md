---
title: Lab 1 SQL Injection - Port Swigger

---

# Lab 2 SQL Injection - Port Swigger

## Statement
 This lab contains a SQL injection vulnerability in the login function.

To solve the lab, perform a SQL injection attack that logs in to the application as the administrator user. 

## Solution

Home page is 

![image](https://hackmd.io/_uploads/HJGupRecC.png)


Since we want to perform a SQL injection attack in the login function, we have to enter in 'My account' page to log in.

![image](https://hackmd.io/_uploads/r1Y2T0g5R.png)

If we try any random username or any random password, we probably won't log in. The query performed may be as follows:

`SELECT * FROM users WHERE username = 'random_username' AND password = 'random_password'`

It would be great if the password condition doesn't execute, maybe seen as comment. Something like

`SELECT * FROM users WHERE username = 'random_username'-- AND password = 'random_password'`

Let's try ![image](https://hackmd.io/_uploads/BJO6kybq0.png)

Finally, we did it!

![image](https://hackmd.io/_uploads/S1zggyWq0.png)
