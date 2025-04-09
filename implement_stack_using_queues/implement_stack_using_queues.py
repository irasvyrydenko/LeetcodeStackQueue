from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.q1:
            for i in range(len(self.q1)-1):
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        for i in range(len(self.q2)-1):
            self.q1.append(self.q2.popleft())
        return self.q2.popleft()

    def top(self):
        """
        :rtype: int
        """
        if not self.q1:
            return self.q2[-1]
        return self.q1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1 and not self.q2

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()