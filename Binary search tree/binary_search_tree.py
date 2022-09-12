class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f'{__class__.__name__}({self.key})'


class BSTree:
    def __init__(self, A=[]):
        self.root = None
        for key in A:
            self.insert(key)

    def insert(self, k):
        z = Node(k)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def __str__(self):
        return F'{__class__.__name__}({str(list(self.__iter__()))[1:-1]})'

    def __iter__(self):
        s = []
        self._inorded_tree_walk(self.root, s)
        return s.__iter__()

    def _inorded_tree_walk(self, x, s):
        if x is not None:
            self._inorded_tree_walk(x.left, s)
            s.append(x.key)
            self._inorded_tree_walk(x.right, s)

    def search(self, k):
        return self._tree_search(self.root, k)

    def _tree_search(self, x, k):
        if x is None or k == x.key:
            return x
        if k < x.key:
            return self._tree_search(x.left, k)
        else:
            return self._tree_search(x.right, k)

    def minimum(self):
        return self._minimum(self.root)

    def maximum(self):
        return self._maximum(self.root)

    def _minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def _maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def successor(self, k):
        x = self.search(k)
        if x is not None:
            return self._successor(x)

    def predecessor(self, k):
        x = self.search(k)
        if x is not None:
            return self._predecessor(x)

    def _successor(self, x):
        if x.right is not None:
            return self._minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def _predecessor(self, x):
        if x.left is not None:
            return self._minimum(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, k):
        z = self.search(k)
        if z is not None:
            self._delete(z)

    def _delete(self, z):
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y


def main():
    A = [13, 19, 9, 5, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    tree = BSTree(A)
    print(tree)
    tree.insert(15)
    print(tree)
    print('Min:', tree.minimum())
    tree.delete(6)
    print(tree)


if __name__ == '__main__':
    main()
