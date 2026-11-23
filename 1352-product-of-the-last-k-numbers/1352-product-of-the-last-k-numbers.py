class ProductOfNumbers:

    def __init__(self):
        self.li = [1]
        self.size = 0
    def add(self, num: int) -> None:
        if num == 0:
            self.li = [1]
            self.size = 0
        else:
            self.li.append(self.li[self.size] * num)
            self.size += 1   

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        else:
            return self.li[self.size] // self.li[self.size - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)