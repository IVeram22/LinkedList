import time
import unittest
from random import randint

import HtmlTestRunner
from linkedlist.LinkedList import LinkedList, insert_node, find_intersect1, find_intersect2, find_intersect3, \
    search_an_effective_method, find_intersect4


class MyTest(unittest.TestCase):
    def test_create_linked_list(self):
        length = randint(0, 30)
        print("<b>Input data:</b>")
        print("Random Length = {}<br><hr>".format(length))
        linked_list = LinkedList(length)
        print("Create list:<br>")
        print("LinkedList.length = {}<br>".format(len(linked_list)))
        print("<b>{}</b><br><br><hr>".format(linked_list.__str__()))
        result = len(linked_list) == length
        print("LinkedList.length == Random Length, <b>Result = {}</b>".format(result))
        self.assertTrue(
            result,
            "Can not create List with length = {}, Current length = {}".format(length, len(linked_list))
        )

    def test_find_intersect_method_1(self):
        length1 = randint(1, 30)
        length2 = randint(1, 30)
        print("<b>Input data:</b>")
        print("Random Length1 = {}, Length2 = {}<br><hr>".format(length1, length2))
        linked_list1 = LinkedList(length1)
        print("Create list1:<br>")
        print("LinkedList1.length = {}<br>".format(len(linked_list1)))
        print("<b>{}</b><br><br><hr>".format(linked_list1.__str__()))
        result1 = len(linked_list1) == length1
        print("LinkedList1.length == Random Length1, <b>Result = {}</b><br><hr>".format(result1))
        self.assertTrue(
            result1,
            "Can not create List1 with length1 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        linked_list2 = LinkedList(length2)
        print("Create list2:<br>")
        print("LinkedList2.length = {}<br>".format(len(linked_list2)))
        print("<b>{}</b><br><br><hr>".format(linked_list2.__str__()))
        result2 = len(linked_list2) == length2
        print("LinkedList2.length == Random Length2, <b>Result = {}</b><br><hr>".format(result2))
        self.assertTrue(
            result2,
            "Can not create List2 with length2 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        print("Update list 2:<br>")
        node_index_insert = randint(0, length1 - 1)
        noge_index_change = randint(0, length2 - 1)

        print("List1: Node index to insert = {}<br>".format(node_index_insert))
        print("List2: Node index to change = {}<br><br>".format(noge_index_change))

        print("Insert node({}, {})<br>".format(
            linked_list1[node_index_insert].data,
            linked_list2[noge_index_change].data
        ))

        insert_node(linked_list1[node_index_insert], linked_list2[noge_index_change])

        print("<br>List1: <b>{}</b><br><br>".format(linked_list1.__str__()))
        print("List2: <b>{}</b><br><br><hr>".format(linked_list2.__str__()))

        result = find_intersect1(linked_list1[0], linked_list2[0])
        print("<br>Counter = {}<br>".format(result))

    def test_find_intersect_method_2(self):
        length1 = randint(1, 30)
        length2 = randint(1, 30)
        print("<b>Input data:</b>")
        print("Random Length1 = {}, Length2 = {}<br><hr>".format(length1, length2))
        linked_list1 = LinkedList(length1)
        print("Create list1:<br>")
        print("LinkedList1.length = {}<br>".format(len(linked_list1)))
        print("<b>{}</b><br><br><hr>".format(linked_list1.__str__()))
        result1 = len(linked_list1) == length1
        print("LinkedList1.length == Random Length1, <b>Result = {}</b><br><hr>".format(result1))
        self.assertTrue(
            result1,
            "Can not create List1 with length1 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        linked_list2 = LinkedList(length2)
        print("Create list2:<br>")
        print("LinkedList2.length = {}<br>".format(len(linked_list2)))
        print("<b>{}</b><br><br><hr>".format(linked_list2.__str__()))
        result2 = len(linked_list2) == length2
        print("LinkedList2.length == Random Length2, <b>Result = {}</b><br><hr>".format(result2))
        self.assertTrue(
            result2,
            "Can not create List2 with length2 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        print("Update list 2:<br>")
        node_index_insert = randint(0, length1 - 1)
        noge_index_change = randint(0, length2 - 1)

        print("List1: Node index to insert = {}<br>".format(node_index_insert))
        print("List2: Node index to change = {}<br><br>".format(noge_index_change))

        print("Insert node({}, {})<br>".format(
            linked_list1[node_index_insert].data,
            linked_list2[noge_index_change].data
        ))

        insert_node(linked_list1[node_index_insert], linked_list2[noge_index_change])

        print("<br>List1: <b>{}</b><br><br>".format(linked_list1.__str__()))
        print("List2: <b>{}</b><br><br><hr>".format(linked_list2.__str__()))

        result = find_intersect2(linked_list1[0], linked_list2[0])
        print("<br>Counter = {}<br>".format(result))

    def test_find_intersect_method_3(self):
        length1 = randint(1, 30)
        length2 = randint(1, 30)
        print("<b>Input data:</b>")
        print("Random Length1 = {}, Length2 = {}<br><hr>".format(length1, length2))
        linked_list1 = LinkedList(length1)
        print("Create list1:<br>")
        print("LinkedList1.length = {}<br>".format(len(linked_list1)))
        print("<b>{}</b><br><br><hr>".format(linked_list1.__str__()))
        result1 = len(linked_list1) == length1
        print("LinkedList1.length == Random Length1, <b>Result = {}</b><br><hr>".format(result1))
        self.assertTrue(
            result1,
            "Can not create List1 with length1 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        linked_list2 = LinkedList(length2)
        print("Create list2:<br>")
        print("LinkedList2.length = {}<br>".format(len(linked_list2)))
        print("<b>{}</b><br><br><hr>".format(linked_list2.__str__()))
        result2 = len(linked_list2) == length2
        print("LinkedList2.length == Random Length2, <b>Result = {}</b><br><hr>".format(result2))
        self.assertTrue(
            result2,
            "Can not create List2 with length2 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        print("Update list 2:<br>")
        node_index_insert = randint(0, length1 - 1)
        noge_index_change = randint(0, length2 - 1)

        print("List1: Node index to insert = {}<br>".format(node_index_insert))
        print("List2: Node index to change = {}<br><br>".format(noge_index_change))

        print("Insert node({}, {})<br>".format(
            linked_list1[node_index_insert].data,
            linked_list2[noge_index_change].data
        ))

        insert_node(linked_list1[node_index_insert], linked_list2[noge_index_change])

        print("<br>List1: <b>{}</b><br><br>".format(linked_list1.__str__()))
        print("List2: <b>{}</b><br><br><hr>".format(linked_list2.__str__()))

        result = find_intersect3(linked_list1[0], linked_list2[0])
        print("<br>Counter = {}<br>".format(result))

    def test_find_intersect_method_4(self):
        length1 = randint(1, 30)
        length2 = randint(1, 30)
        print("<b>Input data:</b>")
        print("Random Length1 = {}, Length2 = {}<br><hr>".format(length1, length2))
        linked_list1 = LinkedList(length1)
        print("Create list1:<br>")
        print("LinkedList1.length = {}<br>".format(len(linked_list1)))
        print("<b>{}</b><br><br><hr>".format(linked_list1.__str__()))
        result1 = len(linked_list1) == length1
        print("LinkedList1.length == Random Length1, <b>Result = {}</b><br><hr>".format(result1))
        self.assertTrue(
            result1,
            "Can not create List1 with length1 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        linked_list2 = LinkedList(length2)
        print("Create list2:<br>")
        print("LinkedList2.length = {}<br>".format(len(linked_list2)))
        print("<b>{}</b><br><br><hr>".format(linked_list2.__str__()))
        result2 = len(linked_list2) == length2
        print("LinkedList2.length == Random Length2, <b>Result = {}</b><br><hr>".format(result2))
        self.assertTrue(
            result2,
            "Can not create List2 with length2 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        print("Update list 2:<br>")
        node_index_insert = randint(0, length1 - 1)
        noge_index_change = randint(0, length2 - 1)

        print("List1: Node index to insert = {}<br>".format(node_index_insert))
        print("List2: Node index to change = {}<br><br>".format(noge_index_change))

        print("Insert node({}, {})<br>".format(
            linked_list1[node_index_insert].data,
            linked_list2[noge_index_change].data
        ))

        insert_node(linked_list1[node_index_insert], linked_list2[noge_index_change])

        print("<br>List1: <b>{}</b><br><br>".format(linked_list1.__str__()))
        print("List2: <b>{}</b><br><br><hr>".format(linked_list2.__str__()))

        result = find_intersect4(linked_list1[0], linked_list2[0])
        print("<br>Counter = {}<br>".format(result))

    def test_search_an_effective_method(self):
        length1 = randint(1, 1000)
        length2 = randint(1, 1000)
        print("<b>Input data:</b>")
        print("Random Length1 = {}, Length2 = {}<br><hr>".format(length1, length2))
        linked_list1 = LinkedList(length1)
        print("Create list1:<br>")
        print("LinkedList1.length = {}<br>".format(len(linked_list1)))
        print("<b>{}</b><br><br><hr>".format(linked_list1.__str__()))
        result1 = len(linked_list1) == length1
        print("LinkedList1.length == Random Length1, <b>Result = {}</b><br><hr>".format(result1))
        self.assertTrue(
            result1,
            "Can not create List1 with length1 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        linked_list2 = LinkedList(length2)
        print("Create list2:<br>")
        print("LinkedList2.length = {}<br>".format(len(linked_list2)))
        print("<b>{}</b><br><br><hr>".format(linked_list2.__str__()))
        result2 = len(linked_list2) == length2
        print("LinkedList2.length == Random Length2, <b>Result = {}</b><br><hr>".format(result2))
        self.assertTrue(
            result2,
            "Can not create List2 with length2 = {}, Current length = {}".format(length1, len(linked_list1))
        )

        print("Update list 2:<br>")
        node_index_insert = randint(0, length1 - 1)
        noge_index_change = randint(0, length2 - 1)

        print("List1: Node index to insert = {}<br>".format(node_index_insert))
        print("List2: Node index to change = {}<br><br>".format(noge_index_change))

        print("Insert node({}, {})<br>".format(
            linked_list1[node_index_insert].data,
            linked_list2[noge_index_change].data
        ))

        insert_node(linked_list1[node_index_insert], linked_list2[noge_index_change])

        print("<br>List1: <b>{}</b><br><br>".format(linked_list1.__str__()))
        print("List2: <b>{}</b><br><br><hr>".format(linked_list2.__str__()))
        result_search = search_an_effective_method(linked_list1, linked_list2)
        self.assertTrue(
            result_search,
            "Method 3 is not effective."
        )


if __name__ == "__main__":
    testRunner = HtmlTestRunner.HTMLTestRunner(
        output="/root/MyProjects/LinkedList/Report/",
        report_title="Linked List Tc",
        report_name="LinkedList",
        add_timestamp=False
    )

    unittest.main(testRunner=testRunner)
