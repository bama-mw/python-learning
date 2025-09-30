# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            cur.next = ListNode(val % 10)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    l1_input = input("l1: ")
    l2_input = input("l2: ")

    l1_list = list(map(int, l1_input.strip().split()))
    l2_list = list(map(int, l2_input.strip().split()))

    l1 = list_to_linked_list(l1_list)
    l2 = list_to_linked_list(l2_list)

    sol = Solution()
    result_node = sol.addTwoNumbers(l1, l2)

    result_list = linked_list_to_list(result_node)
    print("output:", result_list)