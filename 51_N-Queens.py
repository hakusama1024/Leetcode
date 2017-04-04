def nqueue(n):
	if n == 0 : return 0
	arr = [0] * n
	res = []
	go(0, arr, n, res)
	print res

def go(po, arr, n, res):
	print arr, po
	if po == n:
		res.append(arr[:])
		return
	for i in range(n):
		t = arr[:]
		t[po] = i
		if check(po, t):
			go(po+1, t, n, res)
			

def check(po, arr):
	for i in range(po):
		if arr[i] == arr[po]:return False
	for i in range(po):
		if abs(i-arr[i]) == abs(po-arr[po]) : return False
	return True
		


			


nqueue(7)


	


	
	



