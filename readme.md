# Security project

Hello there!
<br>
Shall we get started?

## Configuring the DB

First of all, run the following command in the root project:
``` console
docker-compose up db
```
Once that is done, run:
``` console
docker exec -it mysql bash
```
Now you're in the container, run the following to access mySQL:
``` console
mysql -uroot -p
```
Enter the password __root__. The let's create the user DB!
``` SQL
USE security;
CREATE TABLE user ( email VARCHAR(50), first_name VARCHAR(50), last_name VARCHAR(50), pwd VARCHAR(200));
```

And now just run the __main.py__ and you are all set!