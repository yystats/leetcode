"""LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color.

Literal-simulation solution: model the game turn by turn.

Alice ('A') may remove a piece colored 'A' only when BOTH neighbors are 'A'.
Bob   ('B') may remove a piece colored 'B' only when BOTH neighbors are 'B'.
Edge pieces (index 0 and n-1) can never be removed. Alice moves first.
A player who cannot move on their turn loses.

Why greedy (remove the first valid piece) is enough: removing a middle 'A'
from an 'A'-run leaves its neighbors 'A' and never touches any 'B'-run, so a
move never creates or destroys any other move. The players' moves are
independent, the outcome is order-independent, and no search/minimax is needed.
"""


class _Game:
    def __init__(self, colors: str):
        self.state = list(colors)   # mutable line of pieces
        self.current = "A"          # Alice moves first

    def _find_move(self):
        """Index of the first piece the current player may remove, else None."""
        s = self.state
        for i in range(1, len(s) - 1):          # edges excluded
            if s[i] == self.current == s[i - 1] == s[i + 1]:
                return i
        return None

    def _switch(self):
        self.current = "B" if self.current == "A" else "A"

    def play(self) -> bool:
        """True if Alice wins under optimal play."""
        while True:
            i = self._find_move()
            if i is None:                       # current player is stuck -> loses
                return self.current == "B"      # so Alice wins iff Bob is stuck
            del self.state[i]                   # make the move
            self._switch()                      # opponent's turn


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # O(n) time, O(1) space. Count each player's available moves directly:
        # a piece is a move iff it and both neighbors share its color. Moves are
        # independent, Alice goes first, so Alice wins iff she has strictly more.
        a = b = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    a += 1
                else:
                    b += 1
        return a > b

    def winnerOfGame_simulation(self, colors: str) -> bool:
        """Reference O(n^2) literal simulation (TLEs on large inputs)."""
        return _Game(colors).play()


if __name__ == "__main__":
    sol = Solution()
    # "AAABABB": Alice's only A-run "AAA" -> 1 move; Bob has no "BBB" -> 0 moves.
    assert sol.winnerOfGame("AAABABB") is True
    # "AA": Alice cannot move at all.
    assert sol.winnerOfGame("AA") is False
    # "ABBBBBBBAAA": Bob's "BBBBBBB" -> 5 moves; Alice's "AAA" -> 1 move.
    assert sol.winnerOfGame("ABBBBBBBAAA") is False
    # Equal counts: Alice loses (needs strictly more). "AAABBB" -> a=1, b=1.
    assert sol.winnerOfGame("AAABBB") is False
    # Optimal and simulation must agree on every case.
    for c in ("AAABABB", "AA", "ABBBBBBBAAA", "AAABBB", "AAAABBBB", "AAAAB"):
        assert sol.winnerOfGame(c) == sol.winnerOfGame_simulation(c), c
    print("All tests passed.")
