head = None

slow, fast = head, head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        print("true")
        exit()

print("false")