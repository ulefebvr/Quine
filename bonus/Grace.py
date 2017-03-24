#!/usr/bin/env python3
# c1
d1=0
d2=0
def main():
	a='#!/usr/bin/env python3{nl}# c1{nl}d1=0{nl}d2=0{nl}def main():{nl}{tb}a={quote}{str}{quote}{nl}{tb}with open({quote}Grace_kid.py{quote}, {quote}w{quote}) as out:{nl}{tb}{tb}out.write(a.format(str=a,nl=chr(10),tb=chr(9),quote=chr(39),nwl={quote}{nwl}{quote})){nl}d3=main{nl}if __name__=={quote}__main__{quote}:{nl}{tb}d3(){nl}'
	with open('Grace_kid.py', 'w') as out:
		out.write(a.format(str=a,nl=chr(10),tb=chr(9),quote=chr(39),nwl='{nwl}'))
d3=main
if __name__=='__main__':
	d3()
