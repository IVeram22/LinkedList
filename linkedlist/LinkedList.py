from random import randint


class Node:
    def __init__(self, data, p_next=None):
        self.data = data
        self.p_next = p_next


class LinkedList:
    def __init__(self, length: int):
        self.head: Node = None
        self.tail: Node = self.head
        counter = 0
        while counter < length:
            self.add(randint(0, 999))
            counter += 1

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            self.tail.p_next = node
        self.tail = node

    def __len__(self):
        length = 0
        node = self.head
        while node:
            node = node.p_next
            length += 1
        return length

    def __str__(self):
        node: Node = self.head
        result_output = ""
        while node:
            result_output += "{} -> ".format(node.data)
            node = node.p_next
        result_output += "null"
        return result_output

    def __getitem__(self, item):
        counter = 0
        node: Node = self.head
        while counter < item:
            if not node:
                break
            node = node.p_next
            counter += 1
        return node

    def __contains__(self, item):
        node: Node = self.head
        while node:
            if node.data == item:
                return node
            node = node.p_next


def insert_node(node_insert: Node, node_change: Node):
    node_change.data = node_insert.data
    node_change.p_next = node_insert.p_next


def find_intersect1(node_one: Node, node_two: Node):
    one: Node = node_one
    index_one = 0
    counter = 0
    while one:
        two: Node = node_two
        index_two = 0
        while two:
            if one == two:
                print("node1: {}, node2: {}".format(one.data, two.data))
                return counter

            two = two.p_next
            index_two += 1
            counter += 1

        one = one.p_next
        index_one += 1
        counter += 1

    return -counter


def find_intersect2(node_one: Node, node_two: Node):
    one: Node = node_one
    two: Node = node_two
    index_one = 0
    index_two = 0
    counter = 0
    while one and two:
        counter += 1

        if one == two:
            print("node1: {}, node2: {}".format(one.data, two.data))
            return counter

        two = two.p_next
        one = one.p_next
        index_one += 1
        index_two += 1

        if one is None:
            one = node_one
            index_one = 0
        elif two is None:
            two = node_two
            index_two = 0

    return -counter


def find_intersect3(node_one: Node, node_two: Node):
    size_one = 0
    size_two = 0
    counter = 0
    one = node_one
    two = node_two
    while one or two:
        if one == two:
            print("node1: {}, node2: {}".format(one.data, two.data))
            return counter

        if one:
            one = one.p_next
            size_one += 1

        if two:
            two = two.p_next
            size_two += 1
        counter += 1

    different = size_one - size_two
    is_one = False
    is_two = False

    if different > 0:
        is_one = True
    elif different < 0:
        is_two = True

    one = node_one
    two = node_two
    breaker = different

    while True:
        if is_one and breaker > 0:
            one = one.p_next
            breaker -= 1
            counter += 1
        elif is_two and breaker < 0:
            two = two.p_next
            breaker += 1
            counter += 1
        elif breaker == 0:
            if (one or two) is None:
                break

            if one == two:
                print("node1: {}, node2: {}".format(one.data, two.data))
                return counter

            two = two.p_next
            one = one.p_next
            counter += 1

    return -counter


def find_intersect4(node_one: Node, node_two: Node):
    size_one = 0
    size_two = 0
    counter = 0
    one = node_one
    two = node_two
    stop_one = True
    stop_two = True
    while stop_one or stop_two:
        if one == two:
            print("node1: {}, node2: {}".format(one.data, two.data))
            return counter
        elif one.p_next is not None and one.p_next == two:
            print("node1: {}, node2: {}".format(one.p_next.data, two.data))
            return counter
        elif two.p_next is not None and two.p_next == one:
            print("node1: {}, node2: {}".format(one.p_next.data, two.data))
            return counter
        else:
            if one:
                if stop_one and one.p_next is None:
                    stop_one = False
                    one = node_one

                one = one.p_next
                if stop_one:
                    size_one += 1

                if one is None:
                    one = node_one

            if two:
                if size_two and two.p_next is None:
                    size_two = False
                    two = node_two

                two = two.p_next
                if size_two:
                    size_two += 1

                if two is None:
                    two = node_two

            counter += 1

    different = size_one - size_two
    is_one = False

    if different > 0:
        is_one = True

    print("s1: {}".format(size_one))
    print(", s2: {}".format(size_two))

    one = node_one
    two = node_two
    breaker = 0

    while True:
        if not one or not two:
            break

        if one == two:
            print("node1: {}, node2: {}".format(one.data, two.data))
            return counter

        if is_one:
            if breaker == different:
                breaker = 0
                one = one.p_next
            else:
                two = two.p_next
                breaker += 1
        else:
            if breaker == different:
                breaker = 0
                two = two.p_next
            else:
                one = one.p_next
                breaker += 1
        counter += 1

    return -counter


def search_an_effective_method(list_one: LinkedList, list_two: LinkedList):
    print("list1 length = {}<br>".format(len(list_one)))
    print("list2 length = {}<br>".format(len(list_two)))
    print("<br>Search for an effective method: <br><br>")
    counter1 = find_intersect1(list_one[0], list_two[0])
    # print("<br><br>Method1: <b>O(N**2)</b><br>")
    print("Method1 = <b>{}</b><br>".format(counter1))
    counter2 = find_intersect2(list_one[0], list_two[0])
    # print("<br><br>Method2: <b>O(N**N)</b><br>")
    print("Method2 = <b>{}</b><br>".format(counter2))
    counter3 = find_intersect3(list_one[0], list_two[0])
    # print("<br><br>Method3: <b>O(N)</b><br>")
    print("Method3 = <b>{}</b><br>".format(counter3))
    counter4 = find_intersect4(list_one[0], list_two[0])
    # print("<br><br>Method4: <b>O(N)</b><br>")
    print("Method4 = <b>{}</b><br>".format(counter4))
    if 0 < counter1 < counter2 and counter1 < counter3:
        print("<br>Method 1 more effective")

    if 0 < counter2 < counter1 and counter2 < counter3:
        print("<br>Method 2 more effective")

    if 0 < counter3 < counter1 and counter3 < counter2:
        print("<br>Method 3 more effective.")
        return True

    print("<hr>")
    return False
