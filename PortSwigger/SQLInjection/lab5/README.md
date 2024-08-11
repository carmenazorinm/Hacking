# Lab 5 SQL Injection - Port Swigger

## Statement
 This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user. 


## Solution

Home page is 

![image](https://hackmd.io/_uploads/Sys5cd7c0.png)


In order to obtain the number of columns in the table we have to perform a query, for example searching by the accesories category. And we can try a UNION attack selecting 2 null columns.

![image](https://hackmd.io/_uploads/HJkvj_790.png)

If we select 3 null columns we get an error. So there are 2 columns in total.
Now we want to know if both columns contain string type.

![image](https://hackmd.io/_uploads/rkzMhuQqR.png)

We don't get an error, so both columns save strings. 

In order to obtain all usernames and their passwords we perform a UNION attack, selecting the products table union the users table. We look forward to performing the query:

`SELECT * FROM products WHERE category='Accesories' union select username,password from users`


To do it, we can use this payload



![image](https://hackmd.io/_uploads/SJsdTu75R.png)

Great! We can see some users and their passwords. Let's find administrator password...

![image](https://hackmd.io/_uploads/SkHJRu79R.png)


Now we can login as the administrator

![image](https://hackmd.io/_uploads/ryuz0uQ5R.png)

Good job!!


