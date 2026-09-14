# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        n1 = convert_to_num(l1)
        n2 = convert_to_num(l2)
        
        n3 = n1 + n2

        l3 = ListNode(val=n3)

        curr = l3
        while 10 <= n3:
            curr.val = n3 % 10
            n3 //= 10
            
            new = ListNode(val=n3)
            curr.next = new
            curr = new

        return l3
        
def convert_to_num(ll):
    result = 0
    degree = 1
    curr = ll
    while curr is not None:
        result += curr.val * degree
        degree *= 10
        curr = curr.next

    return result
