'''
Красно-черное дерево является бинарным деревом поиска, у которого ни один
простой путь от корня не отличается по длине от другого более чем в 2 раза.
Таким образом, данное дерево является сбалансированным бинарным деревом поиска.
'''


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.red = False

    def __str__(self):
        return f'{__class__.__name__}({self.key})'


class RBTree:
    def __init__(self, A=[]):
        self.none = Node(None)
        self.root = self.none
        for key in A:
            self.insert(key)

    def insert(self, k):
        z = Node(k)
        y = self.none
        x = self.root
        while x != self.none:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.none:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.none
        z.right = self.none
        z.red = True
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.parent.red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.red:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.red:
                    z.parent.red = False
                    y.red = False
                    z.parent.parent.red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.red = False
                    z.parent.parent.red = True
                    self._left_rotate(z.parent.parent)
        self.root.red = False

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.none:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.none:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.none:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.none:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def __str__(self):
        return F'{__class__.__name__}({str(list(self.__iter__()))[1:-1]})'

    def __iter__(self):
        s = []
        self._inorded_tree_walk(self.root, s)
        return s.__iter__()

    def _inorded_tree_walk(self, x, s):
        if x != self.none:
            self._inorded_tree_walk(x.left, s)
            s.append(x.key)
            self._inorded_tree_walk(x.right, s)

    def search(self, k):
        return self._tree_search(self.root, k)

    def _tree_search(self, x, k):
        if x == self.none or k == x.key:
            return x
        if k < x.key:
            return self._tree_search(x.left, k)
        else:
            return self._tree_search(x.right, k)

    @property
    def minimum(self):
        return self._minimum(self.root)

    @property
    def maximum(self):
        return self._maximum(self.root)

    def _minimum(self, x):
        while x.left != self.none:
            x = x.left
        return x

    def _maximum(self, x):
        while x.right != self.none:
            x = x.right
        return x

    def successor(self, k):
        x = self.search(k)
        if x != self.none:
            return self._successor(x)

    def predecessor(self, k):
        x = self.search(k)
        if x != self.none:
            return self._predecessor(x)

    def _successor(self, x):
        if x.right != self.none:
            return self._minimum(x.right)
        y = x.parent
        while y != self.none and x == y.right:
            x = y
            y = y.parent
        return y

    def _predecessor(self, x):
        if x.left != self.none:
            return self._maximum(x.left)
        y = x.parent
        while y != self.none and x == y.left:
            x = y
            y = y.parent
        return y

    def _transplant(self, u, v):
        if u.parent == self.none:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, k):
        z = self.search(k)
        if z != self.none:
            self._delete(z)

    def _delete(self, z):
        y_original_red = z.red
        if z.left == self.none:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.none:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_red = y.red
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.red = z.red
        if not y_original_red:
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while x != self.root and not x.red:
            if x == x.parent.left:
                w = x.parent.right
                if w.red:
                    w.red = False
                    x.parent.red = True
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if not (w.left.red or w.right.red):
                    w.red = True
                    x = x.parent
                else:
                    if not w.right.red:
                        w.left.red = False
                        w.red = True
                        self._right_rotate(w)
                        w = x.parent.right
                    w.red = x.parent.red
                    x.parent.red = False
                    w.right.red = False
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.red:
                    w.red = False
                    x.parent.red = True
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if not (w.left.red or w.right.red):
                    w.red = True
                    x = x.parent
                else:
                    if not w.left.red:
                        w.right.red = False
                        w.red = True
                        self._left_rotate(w)
                        w = x.parent.left
                    w.red = x.parent.red
                    x.parent.red = False
                    w.left.red = False
                    self._right_rotate(x.parent)
                    x = self.root
        x.red = False


def main():
    A = [13, 19, 9, 5, 5, 12, 8, 7, 4, 21, 2, 6, 11]
    tree = RBTree(A)
    print(tree)
    tree.insert(15)
    print(tree)
    print('Min:', tree.minimum)
    tree.delete(6)
    print(tree)


if __name__ == '__main__':
    main()
