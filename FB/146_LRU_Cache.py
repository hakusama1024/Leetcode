
class Node(object):
    def __init__(self, val, key):
        self.val = val
        self.key = key 
        self.next = None
        self.pre = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def add(self, val, key):
        node = Node(val, key)
        n = self.head.next
        n.pre = node
        node.next = n
        self.head.next = node
        node.pre = self.head
        return node

    def remove(self, node):
        p = node.pre
        n = node.next
        p.next = node.next
        n.pre = node.pre

    def removelast(self):
        key = self.tail.pre.key
        node = self.tail.pre.pre
        node.next = self.tail
        self.tail.pre = node
        return key

    def printlist(self):
        node = self.head
        while node.next and node.next != self.tail:
            print node.next.val
            node = node.next

class LRU(object):
    def __init__(self, n):
        self.capacity = n
        self.dic = {}
        self.dll = DoubleLinkedList()

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            val = node.val
            self.dll.remove(node)
            self.dic[key] = self.dll.add(val, key)
        else:
            return -1
        print self.dic.keys()

    def set(self, key, val):
        if key in self.dic:
            self.dll.remove(self.dic[key])
            self.dic[key] = self.dll.add(val, key)
        else:
            if len(self.dic) >= self.capacity:
                del self.dic[self.dll.removelast()]
                self.dic[key] = self.dll.add(val, key)
            else:
                self.dic[key] = self.dll.add(val, key)
        print self.dic.keys()

    def printlru(self):
        self.dll.printlist()

lru = LRU(3)
lru.set(1, 2)
lru.printlru()
lru.set(2, 3)
lru.printlru()
lru.set(3, 4)
lru.printlru()
lru.set(4, 5)
lru.printlru()
lru.get(4)
lru.printlru()
lru.set(4, 6)
lru.printlru()
lru.get(2)
lru.printlru()

                



        
