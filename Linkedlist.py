class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def count_nodes(self):
        if self is None:
            return 0
            return
        count = 1
        current = self
        while current.next is not None:
            current = current.next
            count += 1
        return count

    def print_nodes(self):
        current = self
        while current:
            print(current.data)
            current = current.next

    def get_item(self, index):
        if index > self.count_nodes() - 1:
            return "Index out of range"
        current = self

        for n in range(index):
            current = current.next
        return current.data


head = Node('10')
nodeB = Node('1')
nodeC = Node('8')
nodeD = Node('6')
nodeE = Node('2')
nodeF = Node('7')
nodeG = Node('3')
nodeH = Node('4')
nodeI = Node('5')
nodeJ = Node('9')

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH
nodeH.next = nodeI
nodeI.next = nodeJ

print('Count of Nodes: ')
print(head.count_nodes())

print('\nRight Nodes of 10:')
print(head.get_item(0))
print(head.get_item(1))
print(head.get_item(6))
print(head.get_item(9))

print('\nBottom Nodes of 1:')
print(head.get_item(1))
print(head.get_item(2))
print(head.get_item(3))

print('\nLeft Nodes of 6:')
print(head.get_item(3))
print(head.get_item(4))

print('\nBottom Nodes of 3:')
print(head.get_item(6))
print(head.get_item(7))

print('\nUpper Nodes of 3:')
print(head.get_item(6))
print(head.get_item(5))

print('\nLeft Nodes of 4:')
print(head.get_item(7))
print(head.get_item(8))

