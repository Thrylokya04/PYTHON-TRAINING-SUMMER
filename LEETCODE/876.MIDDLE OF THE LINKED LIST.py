class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        current=head
        while current:
            count+=1
            current=current.next
        current=head
        for i in range(count//2):
            current=current.next
        return current
