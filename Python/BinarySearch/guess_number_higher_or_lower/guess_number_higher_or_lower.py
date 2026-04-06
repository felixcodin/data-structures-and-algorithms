# LeetCode 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

_picked_number = None


def set_picked_number(num: int) -> None:
    """Set the hidden number for local testing outside LeetCode."""
    global _picked_number
    _picked_number = num


def guess(num: int) -> int:
    """LeetCode-compatible guess API for local execution."""
    if _picked_number is None:
        raise ValueError("Picked number is not set. Call set_picked_number first.")
    if num > _picked_number:
        return -1
    if num < _picked_number:
        return 1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1
        return -1