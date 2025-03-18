# this class only for the first time setup init state for problem and is given to every search
class State:
    def __init__(self, pipes: list, parent, g_n: int, prev_action: tuple):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n
        self.prev_action = prev_action
        self.__cost = -1

    def set_cost(self, value: int):
        self.__cost = value

    def __hash__(self):
        hash_strings = []
        for i in self.pipes:
            hash_strings.append(i.__hash__())
        hash_strings = sorted(hash_strings)
        hash_string = ''
        for i in hash_strings:
            hash_string += i + '###'
        return hash_string

    def __lt__(self, others):
        return 0

    def h_n(self):
        pass

    def f_n(self):
        return self.g_n + self.h_n()
