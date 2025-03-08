class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        # Empty linked list
        self.head = None
        # Number of nodes in the linked list
        self.n = 0

    def __len__(self):
        return self.n

    def insert_head(self, value):
        # Create new node
        new_node = Node(value)
        # Create connection
        new_node.next = self.head
        # Reassign head
        self.head = new_node
        # Increment node count
        self.n += 1

    def __str__(self):
        curr = self.head
        result = ''
        while curr is not None:
            result += str(curr.data) + '->'
            curr = curr.next
        return result[:-2] if result else "Empty LinkedList"

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            # Empty list case
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.n += 1

    def insert_after(self, after, value):
        new_node = Node(value)
        curr = self.head

        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next

        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'Item not Found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head is None:
            return 'Empty LinkedList'
        self.head = self.head.next
        self.n -= 1

    def pop(self):
        if self.head is None:
            return "Empty LinkedList"
        if self.head.next is None:
            return self.delete_head()
        
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.n -= 1

    def remove(self, value):
        if self.head is None:
            return 'Empty LinkedList'

        if self.head.data == value:
            self.delete_head()
            return

        curr = self.head
        while curr.next is not None:
            if curr.next.data == value:
                curr.next = curr.next.next
                self.n -= 1
                return
            curr = curr.next
        return 'Item Not Found'

    def search(self, item):
        curr = self.head
        pos = 0
        while curr is not None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos += 1
        return "Item Not Found"

    def __getitem__(self, index):
        if index < 0 or index >= self.n:
            return "Index Error"
        curr = self.head
        pos = 0
        while curr is not None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos += 1
        return "Index Error"


L = LinkedList()
L.append(6)
print(L)  
