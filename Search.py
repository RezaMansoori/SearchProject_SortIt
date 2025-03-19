from Solution import Solution
from Problem import Problem
from datetime import datetime
from queue import PriorityQueue

class Search:
    @staticmethod
    def bfs(prb: Problem) -> Solution:  # this method get a first state of Problem and do bfs for find solution if no
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    def dfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        stack = []
        state = prb.initState
        stack.insert(0, state)
        while len(stack) > 0:
            # pop state from stack
            state = stack.pop(0)
            
            # check if state is goal
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            
            # get neighbors
            neighbors = prb.successor(state)
            
            # add neighbors to stack
            for c in neighbors:
                stack.insert(0, c)

        return None
    
    def dfs_with_explore(prb: Problem) -> Solution:
        start_time = datetime.now()
        stack = []
        state = prb.initState
        stack.insert(0, state)
        visited_hash = set()
        while len(stack) > 0:
            # pop state from stack
            state = stack.pop(0)
            
            # add state to visited hash
            visited_hash.add(state.__hash__())
            
            # check if state is goal
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            
            # get neighbors
            neighbors = prb.successor(state)
            
            # add neighbors to stack
            for c in neighbors:
                if c.__hash__() not in visited_hash:
                    stack.insert(0, c)

        return None
        
    def ids(prb: Problem) -> Solution:
        start_time = datetime.now()
        l = 0
        while True:
            stack = []
            state = prb.initState
            stack.insert(0, state)
            stack_hash = set()
            visited_hash = set()
            while len(stack) > 0:
                # pop state from stack
                state = stack.pop(0)
                
                # calculate depth
                save_state = state
                depth = 0
                while state.parent is not None:
                    state = state.parent
                    depth += 1
                state = save_state
                
                # check if depth is greater than cutoff
                if depth > l:
                    continue
                
                # add state to visited hash
                visited_hash.add(state.__hash__())
                
                # check if state is goal
                if prb.is_goal(state):
                    return Solution(state, prb, start_time)
                
                # get neighbors
                neighbors = prb.successor(state)
                
                # add neighbors to stack
                for c in neighbors:
                    if c.__hash__() not in visited_hash and c.__hash__() not in stack_hash:
                        stack.insert(0, c)
                        stack_hash.add(c.__hash__())
            l += 1
            if l == 1000:
                break
        return None
        
    def ucs(prb: Problem) -> Solution:
        start_time = datetime.now()
        prb.set_path_cost([7, 5, 3, 1])
        pq = PriorityQueue()
        state = prb.initState
        pq.put((0,state))
        arr = [0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0,
                
               0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0, 
               
               0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0,
               
               0, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               
               0, 0, 0, 0, 0]
        arr2 = [0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0,
                
               0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0, 
               
               0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0,
               
               0, 0, 0, 0, 0,
               0, 0, 0, 0, 0,
               
               0, 0, 0, 0, 0]
        while pq.qsize() > 0:
            # pop state from stack
            cost, state = pq.get()
            arr2[cost] -= 1
            print(f"\nState:\n{cost}")
            # check if state is goal
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            
            # get neighbors
            neighbors = prb.successor(state)
            
            # add neighbors to stack
            print("Neighbors:")
            for c in neighbors:
                # print(c.__hash__())
                print(c.g_n)
                if c.g_n < 45:
                    arr[c.g_n] += 1
                    arr2[c.g_n] += 1
                pq.put((c.g_n, c))
        return None
        
    def greedy_bfs(prb: Problem) -> Solution:
        start_time = datetime.now()
        pq = PriorityQueue()
        state = prb.initState
        pq.put((0,state))
        while pq.qsize() > 0:
            # pop state from priority queue
            cost, state = pq.get()

            # check if state is goal
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            
            # get neighbors
            neighbors = prb.successor(state)
            
            # add neighbors to priority queue
            for c in neighbors:
                pq.put((c.h_n(), c))
        return None
        
    def a_star(prb: Problem) -> Solution:
        start_time = datetime.now()
        prb.set_path_cost([1, 3, 5, 7])
        pq = PriorityQueue()
        state = prb.initState
        pq.put((0,state))
        while pq.qsize() > 0:
            # pop state from priority queue
            cost, state = pq.get()

            # check if state is goal
            if prb.is_goal(state):
                return Solution(state, prb, start_time)
            
            # get neighbors
            neighbors = prb.successor(state)
            
            # add neighbors to priority queue
            for c in neighbors:
                pq.put((c.f_n(), c))
        return None
    
    def ida_star(prb: Problem) -> Solution:
        pass
    def rbfs(prb: Problem) -> Solution:
        pass
