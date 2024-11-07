'''Brute force rotating each element at one step
1)last but one varaku traverse chesi then
2)last element store cheskuni
3)last but one next null ki point chesi
4)last element next head ki point chesi
5)end ni new head laga assign cheyali'''

def rotateRight(head,k):
    if head == None or head.next == None:
        return head
    
    for i in range(k):
        temp=head
        while temp.next.next != None:
            temp=temp.next
        end = temp.next
        temp.next = None
        end.next = head
        head = end
    return head

'''optimal approach
brute force lo if k value is more then the time complexity is too worse so
idi chala better
steps
1)find length
2)make it a circular linked list by setting the last node next as head
3)calculate end=length-k traverse till there
4)assign the head value as temp.next and set the end's next pointer as null
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        temp=head
        length=1
        while temp.next:
            temp=temp.next
            length+=1
        temp.next=head #making the list circular
        k=k%length
        end=length-k
        while end:
            temp=temp.next
            end-=1
        head=temp.next
        temp.next = None

        return head'''