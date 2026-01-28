class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insertion_spe(self, ele, posi):
        new_node = Node(ele)

        if posi == 0:
            new_node.next = self.head
            self.head = new_node
            return

        if self.head is None:
            print("Empty list")
            return

        temp = self.head
        c = 0

        while temp and c < posi - 1:
            temp = temp.next
            c += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    def delete_begin(self):
        if self.head is None:
            print("Empty List")
            return
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("Empty List")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def deletion_spe(self, posi):
        if self.head is None:
            print("Empty List")
            return

        if posi == 0:
            self.head = self.head.next
            return

        temp = self.head
        c = 0

        while temp.next and c < posi - 1:
            temp = temp.next
            c += 1

        if temp.next is None:
            print("Position out of range")
            return

        temp.next = temp.next.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


l = LinkedList()

while True:
    print("\n1.Insert at First")
    print("2.Insert at End")
    print("3.Display")
    print("4.Delete at End")
    print("5.Delete at Beginning")
    print("6.Insert at Specific Position")
    print("7.Delete at Specific Position")
    print("8.Exit")

    choice = int(input("Enter the operation no: "))

    if choice == 1:
        data = int(input("Enter the data: "))
        l.insert_begin(data)

    elif choice == 2:
        data = list(map(int, input("Enter the nodes: ").split()))
        for i in data:
            l.insert_end(i)

    elif choice == 3:
        l.display()

    elif choice == 4:
        l.delete_end()

    elif choice == 5:
        l.delete_begin()

    elif choice == 6:
        ele = int(input("Enter the element: "))
        posi = int(input("Enter the position: "))
        l.insertion_spe(ele, posi)

    elif choice == 7:
        posi = int(input("Enter the position: "))
        l.deletion_spe(posi)

    elif choice == 8:
        print("Exiting program")
        break
