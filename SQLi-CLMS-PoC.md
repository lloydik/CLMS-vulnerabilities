
# SQLi in Computer Laboratory Management System
+ Exploit Author: Artem Glazyrin
# Vendor Homepage
+ https://www.sourcecodester.com/php/17268/computer-laboratory-management-system-using-php-and-mysql.html
# Software Link
+ https://www.sourcecodester.com/php/17268/computer-laboratory-management-system-using-php-and-mysql.html
# Overview
+ A SQL injection vulnerability in manage_damage.php in Sourcecodester Computer Laboratory Management System using PHP and MySQL v1.0 allows authenticated attacker to execute arbitrary SQL commands via the "id" parameter
# Vulnerability Details

+ Vulnerable Endpoint: /php-lms/admin/damage/manage_damage.php?id=1
+ Parameter: id
# Description
+ The lack of proper input validation and sanitization on the 'id' parameter allows an attacker to craft SQL injection queries and gaining unauthorized access to the database.

# Proof of Concept (PoC) : 
+ `http://192.168.1.167/php-lms/admin/damage/manage_damage.php?id=0'%20OR%20'1'='1`