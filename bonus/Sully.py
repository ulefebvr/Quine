#!/usr/bin/env python3
import sys
import subprocess
if __name__=='__main__':
	i = 5
	i=i if sys.argv[0][len(sys.argv[0])-4] == 'y' else i-1
	with open('Sully_'+str(i)+'.py','w') as out:
		a="#!/usr/bin/env python3{nl}import sys{nl}import subprocess{nl}if __name__=='__main__':{nl}{tb}i = {ival}{nl}{tb}i=i if sys.argv[0][len(sys.argv[0])-4] == 'y' else i-1{nl}{tb}with open('Sully_'+str(i)+'.py','w') as out:{nl}{tb}{tb}a={dquote}{str}{dquote}{nl}{tb}{tb}out.write(a.format(str=a,nl=chr(10),tb=chr(9),dquote=chr(34),ival=i)){nl}{tb}com='chmod +x '+'Sully_'+str(i)+'.py'{nl}{tb}subprocess.call(com.split()){nl}{tb}if i==0:{nl}{tb}{tb}sys.exit(0){nl}{tb}com='./Sully_'+str(i)+'.py'{nl}{tb}subprocess.call(com.split())"
		out.write(a.format(str=a,nl=chr(10),tb=chr(9),dquote=chr(34),ival=i))
	com='chmod +x '+'./Sully_'+str(i)+'.py'
	subprocess.call(com.split())
	if i==0:
		sys.exit(0)
	com='./Sully_'+str(i)+'.py'
	subprocess.call(com.split())
