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
        count = 0
        for pipe in self.pipes:
            if pipe.is_empty():
                continue
            first_color = pipe.stack[0]
            is_misplaced = False
            for ball in pipe.stack:
                if ball != first_color:
                    is_misplaced = True
                if is_misplaced:
                    if ball == 'red':
                        count += 1
                    elif ball == 'blue':
                        count += 3
                    elif ball == 'green':
                        count += 5
                    elif ball == 'yellow':
                        count += 7
        return count

    def f_n(self):
        return self.g_n + self.h_n()
