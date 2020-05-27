# Adds new node to linked list
def addNode(last, newnode):
    last.next = newnode
    last = last.next

    return(last)


# Reverses linked list nodes
def reverse(h):
    curr = temp = h
    p = None

    while curr:
        temp = temp.next
        curr.next = p
        p = curr
        curr = temp

    return p


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    carry = c = idx = 0

    revA = reverse(a)
    revB = reverse(b)

    while revA or revB:
        if revA and revB:
            c = (revA.value + revB.value + carry) % 10000
            carry = (revA.value + revB.value + carry) // 10000
            revA = revA.next
            revB = revB.next
        elif revA:
            c = (revA.value + carry) % 10000
            carry = (revA.value + carry) // 10000
            revA = revA.next
        elif revB:
            c = (revB.value + carry) % 10000
            carry = (revB.value + carry) // 10000
            revB = revB.next

        if idx is not 0:
            last = addNode(last, ListNode(c))
        else:
            last = newList = ListNode(c)

        idx = idx + 1

    if carry:
        addNode(last, ListNode(carry))

    return reverse(newList)
