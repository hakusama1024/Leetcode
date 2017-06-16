import heapq


class Node(object):
    def __init__(val):
        self.val = val
        self.pre = None
        self.next = None

class DLL(object):
    def __init__(object):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def push(self, node):
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node

    def pop(self):
        if self.head.next != self.tail:
            t = self.head.next
            self.head.next = t.next
            t.next.pre = self.head
            t.next = None
            t.pre = None
            return t
        return None

    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre


class MaxHead(object):
    def __init__(object):
        self.DLL = DLL()
        self.hq = []

    def push(self, val):
        node = Node(val)
        self.DLL.push(node)
        heqpq.heappush(dq, (val, node))
        
    def pop(self):


    


