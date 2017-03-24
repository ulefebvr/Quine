#include <stdio.h>
int main(void)
{
	// Un des commentaires doit être présent dans la fonction main.
	char*a="#include <stdio.h>%1$cint main(void)%1$c{%1$c"
	"%2$c// Un des commentaires doit être présent dans la fonction main.%1$c"
	"%2$cchar*a=%3$c%4$.45s%3$c%1$c%2$c%3$c%5$.73s%3$c%1$c%2$c%3$c%6$.76s%3$c%1$c"
	"%2$c%3$c%7$.95s%3$c%1$c%2$c%3$c%8$.133s%3$c%1$c%2$c%3$c%9$.73s%3$c%1$c%2$c%3$c%10$.90s%3$c;%1$c"
	"%2$cprintf(a,10,9,34,a,a+45,a+45+73,a+45+73+76,a+45+73+76+95,a+45+73+76+95+133,a+45+73+76+95+133+73);%1$c%2$creturn (0);%1$c}%1$c%1$c"
	"int other_function(int a, int b)%1$c{%1$c%2$creturn (a + b);%1$c}%1$c%1$c"
	"// Un des commentaires doit être présent en dehors des fonctions de votre programme.%1$c";
	printf(a,10,9,34,a,a+45,a+45+73,a+45+73+76,a+45+73+76+95,a+45+73+76+95+133,a+45+73+76+95+133+73);
	return (0);
}

int other_function(int a, int b)
{
	return (a + b);
}

// Un des commentaires doit être présent en dehors des fonctions de votre programme.
