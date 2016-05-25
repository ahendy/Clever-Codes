class Node:
	def __init__(self, val, next):
		self.val = val
		self.next = next



def _print(node):
	if node is None:
		return ""	
	print node.val
	_print(node.next)


def reverse(node, last):
	if node is None:
		return last
	next = node.next
	node.next = last
	return reverse(next, node)



if __name__ == '__main__':
	n0 = Node(4, None)
	n1 = Node(3, n0)
	n2 = Node(2, n1)
	n3 = Node(1, n2)

	_print(n3)
	result = reverse(n3, None)
	_print(result)