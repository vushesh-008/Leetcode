from typing import List


class Solution:
    def compute(self, x: float, n: int) -> float:
        """Compute the power of a number

        Args:
            x (float): Input number
            n (int): Power

        Returns:
            float: Result of x^n
        """
        if n == 0:
            return 1

        if n % 2 == 0:
            temp = self.compute(x, n // 2)
            return temp * temp

        else:
            temp = self.compute(x, (n - 1) // 2)
            return temp * temp * x

    def myPow(self, x: float, n: int) -> float:
        """Compute the power of a number

        Args:
            x (float): Input number
            n (int): Power

        Returns:
            float: Result of x^n
        """

        if n >= 0:
            return self.compute(x, n)
        else:
            return 1.0 / (self.compute(x, -1 * n))


if __name__ == "__main__":
    obj = Solution()
    print(obj.myPow(2.00000, 10))
    print(obj.myPow(2.10000, 3))
    print(obj.myPow(2.00000, -2))
