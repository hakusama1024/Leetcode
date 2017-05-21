class Node(object):
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None


class DDL(object):
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, val):
        n = Node(val)
        n.next = self.head.next
        n.next.pre = n
        self.head.next = n
        n.pre = self.head

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        return node.val

    def printnode(self):
        t = self.head.next
        while t != self.tail:
            print t.val
            t = t.next

    def removerandome(self):
        t = self.head.next
        t = t.next
        t = t.next
        print t.val
        self.remove(t)


ddl = DDL()
ddl.add(1)
ddl.add(2)
ddl.add(3)
ddl.add(4)
ddl.add(5)

ddl.printnode()
print "--------------"
ddl.removerandome()
print "--------------"
ddl.printnode()



        
