class Node:
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return -1
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def min_right_node_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left = self.insert_node(data, node.left)
        elif data > node.data:
            node.right = self.insert_node(data, node.right)

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1:
            if data < node.left.data:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if data > node.right.data:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def delete(self, data):
        if self.root:
            self.root = self.delete_node(self.root, data)

    def delete_node(self, node, data):
        if not node:
            return node

        if data < node.data:
            node.left = self.delete_node(node.left, data)
        elif data > node.data:
            node.right = self.delete_node(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                del node
                return temp
            elif node.right is None:
                temp = node.left
                del node
                return temp

            temp = self.min_right_node_value(node.right)
            node.data = temp.data
            node.right = self.delete_node(node.right, temp.data)

        if data is None:
            return data

        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def print_tree(self):
        self.in_order_traversal(self.root)
        print()  # For a new line after printing all nodes

    def in_order_traversal(self, node):
        if not node:
            return
        self.in_order_traversal(node.left)
        print(node.data, end=' ')
        self.in_order_traversal(node.right)

    # Функції для знаходження найбільшого та найменшого значення

    def get_min(self, node):
        if node.left is None:
            return node.data
        return self.get_min(node.left)

    def get_max(self, node):
        if node.right is None:
            return node.data
        return self.get_max(node.right)

    # Сума всіх значень

    def sum_tree(self, node):
        if not node:
            return 0
        return node.data + self.sum_tree(node.left) + self.sum_tree(node.right)


if __name__ == '__main__':
    avl = AVL()
    avl.insert(6)
    avl.insert(10)
    avl.insert(20)
    avl.insert(5)
    avl.insert(13)
    avl.insert(14)
    avl.insert(3)
    avl.insert(2)
    avl.insert(7)
    avl.insert(8)
    avl.insert(4)
    avl.insert(15)
    avl.print_tree()
    avl.delete(10)
    avl.print_tree()
    print(f'Min value: {avl.get_min(avl.root)}')
    print(f'Max value: {avl.get_max(avl.root)}')
    print(f'Sum of all nodes: {avl.sum_tree(avl.root)}')
