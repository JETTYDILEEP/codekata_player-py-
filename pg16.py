def count(s):
	(max,c)=(-1,0)
	r=[]
	for i in range(len(s)):
		if s[i] in r:
			continue
		r.append(s[i])
		for j in range(len(s)):
			if s[i]==s[j] :
				c=c+1
		if c==1:
			print(s[i])
		c=0
def main():
	try:
		a=int(input())
		m=[]
		for i in range(n):
			m.append(int(input()))
		count(m)
	except:
		print('invalid')
main()
