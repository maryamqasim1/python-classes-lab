class Game:
    def __init__(self, board=None, turn="X", tie=False, winner=False):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            "a1": None,
            "b1": None,
            "c1": None,
            "a2": None,
            "b2": None,
            "c2": None,
            "a3": None,
            "b3": None,
            "c3": None,
        }

    def play_game(self):
        print("Shall we play a game?")
        while self.winner == False and self.tie == False:
            self.render()
            self.get_move()
            self.check_for_winner()
            self.check_for_tie()
            self.switch_turn()
        self.render()

    def print_board(self):
        b = self.board
        print(
            f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """
        )

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.turn} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        move = input(f"Enter a valid movie (example: A1): ").lower()
        if move in self.board and self.board[move] is None:
            self.board[move] = self.turn
        else:
            print("Invalid move, try again.")

    def check_for_winner(self):
        for row in range(1, 3):
            if self.board[f"a{row}"] and (
                self.board[f"a{row}"] == self.board[f"b{row}"] == self.board[f"c{row}"]
            ):
                return self.winner

        for col in ("a", "b", "c"):
            if self.board[f"{col}1"] and (
                self.board[f"{col}1"] == self.board[f"{col}2"] == self.board[f"{col}3"]
            ):
                self.winner = True

        # diagonal
        if self.board["a1"] and (
            self.board["a1"] == self.board["b2"] == self.board["c3"]
        ):
            self.winner = True

        if self.board["a3"] and (
            self.board["a3"] == self.board["b2"] == self.board["c1"]
        ):
            self.winner = True

    def check_for_tie(self):
        if self.winner is False:
            if None in self.board.values():
                self.tie = False
            else:
                self.tie = True

    def switch_turn(self):
        if self.winner == False and self.tie == False:
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"


game_instance = Game()
game_instance.play_game()ب
