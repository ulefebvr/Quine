#include <stdio.h>
/*
	c1
*/
int add(int a, int b){return (a + b);}int main(void){/*c2*/char*a="#include <stdio.h>%1$c/*%1$c%2$cc1%1$c*/%1$cint add(int a, int b){return (a + b);}int main(void){/*c2*/char*a=%3$c%4$s%3$c;printf(a,add(5,5),9,34,a);}%1$c";printf(a,add(5,5),9,34,a);}
