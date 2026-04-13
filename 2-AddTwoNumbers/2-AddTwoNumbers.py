# Last updated: 4/12/2026, 10:23:23 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        M = list()
        M2 = list()

        while l1:
            M.append(l1.val)
            l1 = l1.next

        while l2:
            M2.append(l2.val)
            l2 = l2.next

        M += [0] * max(0, len(M2) - len(M))
        M = M[::-1]
        M2 += [0] * max(0, len(M) - len(M2))
        M2 = M2[::-1]
        Y = list()

        TF = False
        for ii in range(len(M)*-1, 0):
            Y.append(M2[ii] + M[ii])
        Y = Y[::-1]
        for nn in range(len(Y)):
            if TF:
                Y[nn] = Y[nn] + a
                TF = False
            if Y[nn]//10 >= 1 and nn != len(Y)-1:
                a = Y[nn]//10
                b = Y[nn]%10
                Y[nn] = b
                TF = True
        if Y[nn]//10 >= 1 and nn == len(Y)-1:
            Y.append(0)
            a = Y[nn]//10
            b = Y[nn]%10
            Y[nn] = b
            Y[nn+1] = Y[nn+1] + a

        dummy = ListNode(0)
        curr = dummy

        for v in Y:
            curr.next = ListNode(v)
            curr = curr.next
            
        return dummy.next