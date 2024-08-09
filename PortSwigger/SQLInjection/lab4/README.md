---
title: Lab 1 SQL Injection - Port Swigger

---

# Lab 4 SQL Injection - Port Swigger

## Statement
 This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.


## Solution

Home page is 
![image](https://hackmd.io/_uploads/SkIeaIm9C.png)


In order to obtain the number of columns in the table we have to perform a query, for example searching by the pets category. The link is 

![image](https://hackmd.io/_uploads/SkkETLQ50.png)


The SQL query may be something like

`SELECT * FROM products WHERE category = 'Pets'`

We want to know the number of columns, so we can try to order the columns by its index. If we get an error is because the column with that index doesn't exist. 

`SELECT * FROM products WHERE category = 'Pets' order by 2`

We can try the query above by adding a payload in the link:

[https://0a5d007004f6ccc385cb9171007b00f6.web-security-academy.net/filter?category=Gifts'+order+by+3--]()

And we see that the products are ordered by its price, so the price is the column with index 3.

![image](https://hackmd.io/_uploads/rkpgC8Q5A.png)

Let's try ordering the products by column 4.

![image](https://hackmd.io/_uploads/BJ8R68XqC.png)

The fourth column doesn't exist, then we know that there are 3 columns. Now we have to find which one contains string data. The query below gives an error if the first column isn't a string, and prints a new row otherwhise.

`SELECT * FROM products WHERE category = 'Gifts' union select 'a',null,null`

If we make an injection to execute the query, we obtain an error.

![image](https://hackmd.io/_uploads/HytZCv7qC.png)

Let's see if the second column data type is a string:

![image](https://hackmd.io/_uploads/rkhEAvX9C.png)

Yeah!! We have a new row containing 'a', that implies that the second column contains strings. 

At this point, the lab provides a random word, such as 'Nk5xG6', and we have to make it appear in the new row. That's easy, just changing 'a' by 'Nk5xG6' in the link.

[https://0a67002003f27d1080d3bc0d004a004e.web-security-academy.net/filter?category=Pets'+union+select+null,'Nk5xG',null--]()

And we did it! Great job!


