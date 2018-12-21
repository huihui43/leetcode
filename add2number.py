# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        solu = ListNode(0)
        head = solu
        length1, length2 = 1, 1
        tmp_1, tmp_2 = l1, l2
        while tmp_1.next != None:
            length1 += 1
            tmp_1 = tmp_1.next

        while tmp_2.next != None:
            length2 += 1
            tmp_2 = tmp_2.next

        if length1 > length2:
            for i in range(length2):
                value = l1.val + l2.val + head.val
                if value >= 10:
                    value = value % 10
                    head.val = value
                    head.next = ListNode(1)
                    head = head.next
                else:
                    head.val  = value
                    head.next = ListNode(0)
                    head = head.next
                l1 = l1.next
                l2 = l2.next

            while l1:
                value = head.val + l1.val
                if value >= 10:
                    head.val = value % 10
                    head.next = ListNode(1)
                    head = head.next
                else:
                    head.val = value
                    head.next = l1.next
                    break
                l1 = l1.next




        elif length2 > length1:
            for i in range(length1):
                value = l1.val + l2.val + head.val
                if value >= 10:
                    value = value % 10
                    head.val  = value
                    head.next = ListNode(1)
                    head = head.next
                else:
                    head.val  = value
                    head.next = ListNode(0)
                    head = head.next
                l2 = l2.next
                l1 = l1.next
            while l2:
                value = head.val + l2.val
                if value >= 10:
                    head.val = value % 10
                    head.next = ListNode(1)
                    head = head.next
                else:
                    head.val = value
                    head.next = l2.next
                    break
                l2 = l2.next

        else:
            while l1 and l2:
                value = l1.val + l2.val + head.val
                if value >= 10:
                    value = value % 10
                    head.val = value
                    head.next = ListNode(1)
                    head = head.next

                else:
                    head.val += value
                    if l1.next:
                        head.next = ListNode(0)
                        head = head.next
                l1 = l1.next
                l2 = l2.next


        return solu

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
