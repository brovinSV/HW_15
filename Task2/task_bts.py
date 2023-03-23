"""
Взявши за основу код домашнього завдання лекції 14, розробіть
набір тестів з використанням бібліотеки pytest для методів додавання
нових елементів, пошуку мінімального і максимального значень та
видалення елементів бінарного дерева.
"""
class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None


    def __str__(self):
        """
        Повертає ключ вузла.
        :return: рядок, у вигляді "id_node"
        """
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    # метод додавання до бінарного дерева пошуку нових елементів зі списку
    def insert_list(self, list_key):
        for key in list_key:
            self.insert(key) # запускаємо вставку елемента зі списку

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    # метод пошуку мінімального значення елемента в бінарному дереві пошуку
    def minValue(self):
        if self.id_node:
            if self.left is None:
                return self.id_node
            else:
                return self.left.minValue()

    # метод пошуку максимального значення елемента в бінарному дереві пошуку
    def maxValue(self):
        if self.id_node:
            if self.right is None:
                return self.id_node
            else:
                return self.right.maxValue()

    # метод видалення елементів в бінарному дереві пошуку
    def delete_elem_bts(self, val):
        if self.id_node > val:
            if self.left:
                self.left = self.left.delete_elem_bts(val)
        elif self.id_node < val:
            if self.right:
                self.right = self.right.delete_elem_bts(val)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                max_val = self.left.maxValue()
                self.id_node = max_val
                self.left = self.left.delete_elem_bts(max_val)
        return self

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

tree = Tree(13)
tree.insert(9)
tree.insert(17)
tree.insert(4)
tree.insert(3)
tree.insert(6)

tree.print_tree()
print()
my_list = [15, 13, 1, 5, 7]
tree.insert_list(my_list)
tree.print_tree()
print()
print('Min value: ', tree.minValue())
print('Max value: ', tree.maxValue())
print()
v = int(input("Enter a element to delete : "))
tree.delete_elem_bts(v)
tree.print_tree()