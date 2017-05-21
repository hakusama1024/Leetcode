class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def Palindrome_Linked_List(head):
    if not head : return head
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    right = slow.next
    slow.next = None

    pre = None
    while right:
        t = right.next
        right.next = pre
        pre = right 
        right = t

    while pre and head:
        if pre.val == head.val:
            pre = pre.next
            head = head.next
        else:
            return False
    return True

node = Node(1)
node.next = Node(2)
#node.next.next = Node(3)
#node.next.next.next = Node(2)
#node.next.next.next.next = Node(1)

print Palindrome_Linked_List(node)

