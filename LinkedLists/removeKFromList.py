# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    p = curr = l
    
    while curr:
        if curr.value == k and curr == l:
            l = p = l.next
            curr = None
            curr = p
            
        elif curr.value == k:
            p.next = curr.next
            curr = None
            curr = p.next
            
        else:
            p = curr
            curr = curr.next
           
    return l
