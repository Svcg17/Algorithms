# Reverses a linked list
def reverse(h):
    curr = t = h
    p = None
    
    while curr:
        t = t.next
        curr.next = p
        p = curr
        curr = t
        
    return p        

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    s = f = l
    while f and f.next:
        s = s.next
        f = f.next.next
        
    r = reverse(s)
    
    while r:
        if (r.value != l.value):
            return False
        r = r.next
        l = l.next
    
    return True
