class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        cards = {}
        for card in hand:
            if card in cards:
                cards[card] += 1
            else:
                cards[card] = 1
        while cards:
            start = min(cards)
            for i in range(groupSize):
                if start + i not in cards:
                    return False
                cards[start + i] -= 1
                if cards[start + i] == 0:
                    del cards[start + i]
        return True