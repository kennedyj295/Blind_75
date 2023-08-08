prev, curr = None, head

while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
print(prev)

#
# N->1->2->3
#
# nxt=2
# curr.next=None
# prev=1
# curr=nxt
#
# nxt=3
# curr.next=1
# prev=2
# curr=nxt
#
# nxt=
# curr.next=2
# prev=3
# curr=