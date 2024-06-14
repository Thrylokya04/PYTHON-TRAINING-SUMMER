class Solution:
    def getDecimalValue(self, head: listNode) -> int:
        answer = ' '
        if head is None:
            return

        current = head
        while  current:
            answer = answer + str(current.val)
            current = current.next
        return int(answer,2)
