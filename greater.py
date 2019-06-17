n,k=[int(i) for i in input().split()]
def reduceN( n, k) :
	if k <= 0 : return n

	if n == 0 : return 10	# Fail
	h = reduceN(n//10, k)*10 + n%10
	l = reduceN(n//10, k-1)
	if h < l :
		return h
	else :
		return l
print(reduceN(n,k))
