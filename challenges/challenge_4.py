"""
    Solving the knapsack and another dynamic programming problem
    of my choice.
"""


class Item:
    """
        Item to store meta information for items that
        are to be stored within the knapsack.
    """

    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def __eq__(self, other_item):
        return self.value == other_item.value

    def __lt__(self, other_item):
        return self.value < other_item.value

    def __gt__(self, other_item):
        return self.value < other_item.value

    def __str__(self):
        return f"<Item: {self.name}, Value: {self.value}, Weight: {self.weight}>"


def main():
    capacity = 100
    items = [
        Item("Macbook", 20, 15),
        Item("TV", 15, 30),
        Item("IPhone", 5, 8),
        Item("USB", 1, 1),
    ]


if __name__ == "__main__":
    main()
