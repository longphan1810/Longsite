# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if  head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
    
        head.next.next = head
        head.next = None
       
       
        
        return p

a,b,c,d,e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

i = Solution()
z = i.reverseList(a)

cur = z
alist=[]
while cur:
    alist.append(cur.val)
    cur = cur.next
print(alist)