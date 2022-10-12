class Node:
    def __init__(self, t):
        self.n = None
        self.c = [None for _ in range(2*t)]
        self.key = [None for _ in range(2*t - 1)]
        self.leaf = False

    def __str__(self):
        return self.key.__str__()

    def __repr__(self):
        return self.key.__str__()


class B_tree:
    def __init__(self, A=[], t=2):
        self.t = t
        x = Node(self.t)
        x.leaf = True
        x.n = 0
        self.disk_write(x)
        self.root = x
        for k in A:
            self.insert(k)

    def __str__(self):
        return f'{__class__.__name__}({str(list(self.__iter__()))[1:-1]})'

    def __iter__(self):
        s = []
        self._inorded_tree_walk(self.root, s)
        return s.__iter__()

    def _inorded_tree_walk(self, x, s):
        if x is not None:
            for i in range(x.n):
                self._inorded_tree_walk(x.c[i], s)
                s.append(x.key[i])
            self._inorded_tree_walk(x.c[x.n], s)

    def disk_read(self, x):
        pass

    def disk_write(self, x):
        pass

    def search(self, k):
        return self._search(self.root, k)

    def _search(self, x, k):
        i = 0
        while i < x.n and k > x.key[i]:
            i += 1
        if i < x.n and k == x.key[i]:
            return x, i
        elif x.leaf:
            return None
        else:
            self.disk_read(x.c[i])
            return self._search(x.c[i], k)

    def split_child(self, x, i):
        z = Node(self.t)
        y = x.c[i]
        z.leaf = y.leaf
        z.n = self.t - 1
        for j in range(z.n):
            z.key[j] = y.key[j+self.t]
        if not y.leaf:
            for j in range(self.t):
                z.c[j] = y.c[j+self.t]
        y.n = self.t - 1
        for j in range(x.n, i, -1):
            x.c[j+1] = x.c[j]
        x.c[i+1] = z
        for j in range(x.n-1, i-1, -1):
            x.key[j+1] = x.key[j]
        x.key[i] = y.key[self.t-1]
        x.n += 1
        for j in range(y.n, 2*self.t-1):
            y.key[j] = None
        for j in range(y.n+1, 2*self.t):
            y.c[j] = None
        self.disk_write(y)
        self.disk_write(z)
        self.disk_write(x)

    def insert(self, k):
        r = self.root
        if r.n == 2*self.t - 1:
            s = Node(self.t)
            self.root = s
            s.n = 0
            s.c[0] = r
            self.split_child(s, 0)
            self.insert_nonfull(s, k)
        else:
            self.insert_nonfull(r, k)

    def insert_nonfull(self, x, k):
        i = x.n - 1
        if x.leaf:
            while i >= 0 and k < x.key[i]:
                x.key[i+1] = x.key[i]
                i -= 1
            x.key[i+1] = k
            x.n += 1
            self.disk_write(x)
        else:
            while i >= 0 and k < x.key[i]:
                i -= 1
            i += 1
            self.disk_read(x.c[i])
            if x.c[i].n == 2*self.t - 1:
                self.split_child(x, i)
                if k > x.key[i]:
                    i += 1
            self.insert_nonfull(x.c[i], k)

    def delete(self, k):
        self._delete(self.root, k)

    def _delete(self, x, k):
        i = 0
        while i < x.n and k > x.key[i]:
            i += 1

        if i < x.n and k == x.key[i]:
            if x.leaf:
                for j in range(i, x.n-1):
                    x.key[j] = x.key[j+1]
                x.n -= 1
                x.key[x.n] = None
                x.c[x.n+1] = None
            else:
                self.disk_read(x.c[i])
                self.disk_read(x.c[i+1])
                y = x.c[i]
                z = x.c[i+1]
                if y.n >= self.t:
                    k = self._maximum(y)
                    x.key[i] = k
                    self._delete(y, k)
                elif z.n >= self.t:
                    k = self._minimum(z)
                    x.key[i] = k
                    self._delete(z, k)
                else:
                    print('2 в')
                    y.key[self.t-1] = x.key[i]
                    for j in range(z.n):
                        y.key[self.t+j] = z.key[j]
                    for j in range(z.n+1):
                        y.c[self.t+j] = z.c[j]
                    y.n = 2*self.t - 1
                    for j in range(i, x.n-1):
                        x.key[j] = x.key[j+1]
                    for j in range(i+1, x.n):
                        x.c[j] = x.c[j+1]
                    x.n -= 1
                    x.key[x.n] = None
                    x.c[x.n+1] = None
                    self._delete(y, k)
        elif x.c[i] is not None:
            self.disk_read(x.c[i])
            y = x.c[i]
            if y.n == self.t - 1:
                if i > 0 and x.c[i-1].n >= self.t:
                    z = x.c[i-1]
                    y.n += 1
                    for j in range(y.n-1, 0, -1):
                        y.key[j] = y.key[j-1]
                    for j in range(y.n, 0, -1):
                        y.c[j] = y.c[j-1]
                    y.key[0] = x.key[i-1]
                    y.c[0] = z.c[z.n]
                    x.key[i-1] = z.key[z.n-1]
                    z.n -= 1
                    z.key[z.n] = None
                    z.c[z.n+1] = None
                elif i < x.n and x.c[i+1].n >= self.t:
                    z = x.c[i+1]
                    y.n += 1
                    y.key[y.n-1] = x.key[i]
                    y.c[y.n] = z.c[0]
                    x.key[i] = z.key[0]
                    for j in range(z.n-1):
                        z.key[j] = z.key[j+1]
                    for j in range(z.n):
                        z.c[j] = z.c[j+1]
                    z.n -= 1
                    z.key[z.n] = None
                    z.c[z.n+1] = None
                elif i > 0:
                    z = x.c[i-1]
                    z.key[self.t-1] = x.key[i-1]
                    for j in range(y.n):
                        z.key[self.t+j] = y.key[j]
                    for j in range(y.n+1):
                        z.c[self.t+j] = y.c[j]
                    z.n = 2*self.t - 1
                    for j in range(i-1, x.n-1):
                        x.key[j] = x.key[j+1]
                    for j in range(i, x.n):
                        x.c[j] = x.c[j+1]
                    x.n -= 1
                    x.key[x.n] = None
                    x.c[x.n+1] = None
                    y = z
                    if x == self.root and x.n == 0:
                        self.root = y
                elif i < x.n:
                    z = x.c[i+1]
                    y.key[self.t-1] = x.key[i]
                    for j in range(z.n):
                        y.key[self.t+j] = z.key[j]
                    for j in range(z.n+1):
                        y.c[self.t+j] = z.c[j]
                    y.n = 2*self.t - 1
                    for j in range(i, x.n-1):
                        x.key[j] = x.key[j+1]
                    for j in range(i+1, x.n):
                        x.c[j] = x.c[j+1]
                    x.n -= 1
                    x.key[x.n] = None
                    x.c[x.n+1] = None
                    if x == self.root and x.n == 0:
                        self.root = y
            self._delete(y, k)

    @property
    def minimum(self):
        return self._minimum(self.root)

    def _minimum(self, x):
        while x.c[0] is not None:
            x = x.c[0]
        return x.key[0]

    @property
    def maximum(self):
        return self._maximum(self.root)

    def _maximum(self, x):
        while x.c[x.n] is not None:
            x = x.c[x.n]
        return x.key[x.n-1]


def main():
    s = [13, 19, 45, 6, 3, 9, 5, 63, 45, 64, 75, 12]
    B = B_tree(s, t=2)
    print(B)
    B.insert(15)
    print(B)
    print('Min:', B.minimum)
    B.delete(6)
    print(B)


if __name__ == '__main__':
    main()
