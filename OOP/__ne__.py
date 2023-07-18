class Example:
    def __init__(self, val):
        self.val = val

    def __ne__(self, other):
        return self.val != other.val

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

    def __le__(self, other):
        return self.val <= other.val

    def __gt__(self, other):
        return self.val > other.val

    def __ge__(self, other):
        return self.val >= other.val

    # В случае отсутствия проверки значения other, функция будет работать либо для
    # целого числа other, либо для ссылки на другой класс other.val

    def __add__(self, other):
        value = other if isinstance(other, int) else other.val
        return Example(self.val + value)

    def __sub__(self, other):
        value = other if isinstance(other, int) else other.val
        return Example(self.val - value)

    def __iadd__(self, other):
        value = other if isinstance(other, int) else other.val
        self.val += value
        return self

    def __isub__(self, other):
        value = other if isinstance(other, int) else other.val
        self.val -= value
        return self

    def __str__(self):
        return str(self.val)
