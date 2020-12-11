# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Ryan Earl

class Stack:
    def __init__(self): 
        self.stack  = []
        self.capacity = 10
        return None 

    def is_empty(self):
        if len(self.stack) == 0: 
            return True 
        return False  

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.stack.pop()
