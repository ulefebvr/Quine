Dr Quine
===================


School project consisting in solving the Quine exercices.

----------


Colleen
-------------

Lors de son exécution, le programme doit afficher sur la sortie standard un output identique au code source du fichier utilisé pour compiler ce même programme.

```
$> ls -al
total 12
drwxr-xr-x 2 root root 4096 Feb 2 13:26 .
drwxr-xr-x 4 root root 4096 Feb 2 13:26 ..
-rw-r--r-- 1 root root 647 Feb 2 13:26 Colleen.c
$> clang -Wall -Wextra -Werror -o Colleen Colleen.c; ./Colleen > tmp_Colleen ; diff tmp_Colleen
Colleen.c
$> _
```


Grace
-------

Lors de son exécution, le programme écrit dans un fichier nommé Grace_kid.c le code source du fichier utilisé pour compiler ce même programme.

```
$> ls -al
total 12
drwxr-xr-x 2 root root 4096 Feb 2 13:30 .
drwxr-xr-x 4 root root 4096 Feb 2 13:29 ..
-rw-r--r-- 1 root root 362 Feb 2 13:30 Grace.c
$> clang -Wall -Wextra -Werror -o Grace Grace.c; ./Grace ; diff Grace.c Grace_kid.c
$> ls -al
total 24
drwxr-xr-x 2 root root 4096 Feb 2 13:30 .
drwxr-xr-x 4 root root 4096 Feb 2 13:29 ..
-rwxr-xr-x 1 root root 7240 Feb 2 13:30 Grace
-rw-r--r-- 1 root root 362 Feb 2 13:30 Grace.c
-rw-r--r-- 1 root root 362 Feb 2 13:30 Grace_kid.c
$> _
```

Sully
-------
Lors de son exécution le programme écrit dans un fichier nommé Sully_X.c. Le X sera alors un entier donné dans la source. Une fois le fichier créé, le programme compile ce fichier puis exécute le nouveau programme (qui aura le nom de son fichier source).
L’arrêt du programme se fait en fonction du nom du fichier : si l’entier X est à 0, le programme résultant n’est pas exécuté.
Un entier est donc présent dans la source de votre programme et devra évoluer en se décrémentant à chaque création d’un fichier source depuis l’exécution du programme.

```
$> clang -Wall -Wextra -Werror ../Sully.c -o Sully ; ./ Sully
$> ls -al | grep Sully | wc -l
13
$> diff ../Sully.c Sully_0.c
1c1
< int i = 5;
---
> int i = 0;
$> diff Sully_3.c Sully_2.c
1c1
< int i = 3;
---
> int i = 2;
$> _
```