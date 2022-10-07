'''
Динамическое программирование.
Задача:
Дискретная задача о рюкзаке. Нужно уместить в рюкзак предметы, суммарная
стоимость которых будет как можно большей. Предмет нельзя взять два раза или
взять часть от него.
'''


from typing import List


class Item:
    def __init__(self, weight: int, cost: int) -> None:
        self.weight = weight
        self.cost = cost

    def __repr__(self) -> str:
        return f'{__class__.__name__}({self.weight}, {self.cost})'


class Knapsack:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.free_place = capacity
        self.items = []
        self.cost = 0

    def add_item(self, item: Item) -> None:
        if self.is_fit(item):
            self.items.append(item)
            self.free_place -= item.weight
            self.cost += item.cost

    def is_fit(self, item: Item) -> bool:
        if item.weight <= self.free_place:
            return True
        else:
            return False

    def add_max_cost(self, items: List) -> None:
        items = self.max_cost(items)
        for item in items:
            self.add_item(item)

    def max_cost(self, items: List) -> List:
        n = len(items)
        cost = [0 for _ in range(self.capacity+1)]
        sub = [[True for _ in range(n)] for _ in range(self.capacity+1)]
        for i in range(1, self.capacity+1):
            k = None
            for j in range(n):
                i_prev = i - items[j].weight
                if i_prev >= 0 and sub[i_prev][j]:
                    costi = cost[i_prev] + items[j].cost
                    if cost[i] < costi:
                        cost[i] = costi
                        k = j
            if k is not None:
                sub[i] = sub[i - items[k].weight].copy()
                sub[i][k] = False
        return [items[i] for i in range(n) if not sub[self.capacity][i]]


def main():
    items = [
            Item(10, 60),
            Item(20, 100),
            Item(30, 120)
            ]
    knapsack = Knapsack(50)
    knapsack.add_max_cost(items)
    print(f'cost: {knapsack.cost}; items: {knapsack.items}')


if __name__ == '__main__':
    main()
