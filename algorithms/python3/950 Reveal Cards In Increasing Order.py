from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque(range(len(deck)))
        ans = [0] * len(deck)
        for card in deck:
            ans[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        return ans
