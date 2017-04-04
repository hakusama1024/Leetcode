arr = [2, 5, 6, 0, 3, 1]


class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def maxtree(arr):
	if len(arr) == 0 : return None
	t = arr[0]
	index = 0
	for i in range(1, len(arr)):
		if t < arr[i]:
			t = arr[i]
			index = i
	print t
	node = Node(t)
	node.left = maxtree(arr[:index])
	node.right = maxtree(arr[index+1:])
	return node
	

def test(arr):
	size = len(arr)
	if size == 0 : return None
	node = maxtree(arr)
	if not node : print "nothing"
	
	dp = [node]

	while dp:
		size = len(dp)
		tmp = []
		for i in range(size):
			t = dp.pop(0)
			tmp.append(t.val)
			if t.left : dp.append(t.left)
			if t.right : dp.append(t.right)
		print tmp


test(arr)



