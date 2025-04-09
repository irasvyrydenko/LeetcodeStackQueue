class FreqStack(object):

    def __init__(self):
        self.count = {}
        self.max_freq = 0
        self.stacks = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        val_freq = 1 + self.count.get(val, 0)
        self.count[val] = val_freq
        if val_freq > self.max_freq:
            self.max_freq = val_freq
            self.stacks[val_freq] = []
        self.stacks[val_freq].append(val)

    def pop(self):
        """
        :rtype: int
        """
        res = self.stacks[self.max_freq].pop()
        self.count[res] -= 1
        if not self.stacks[self.max_freq]:
            self.max_freq -=1
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()