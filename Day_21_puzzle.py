# Example input:
# Player 1 starting position: 4
# Player 2 starting position: 8

# Real input:
# Player 1 starting position: 9
# Player 2 starting position: 3

class d_game:
    def __init__(self, p1_pos, p2_pos):
        self.p1_pos = p1_pos
        self.p2_pos = p2_pos
        self.p1_score = 0
        self.p2_score = 0
        self.last_roll = 0
        self.num_rolls = 0
    def move_p1(self, dice_roll):
        self.p1_pos += dice_roll
        if self.p1_pos > 10:
            self.p1_pos %= 10
            if self.p1_pos == 0:
                self.p1_pos = 10
        self.p1_score += self.p1_pos
    def move_p2(self, dice_roll):
        self.p2_pos += dice_roll
        if self.p2_pos > 10:
            self.p2_pos %= 10
            if self.p2_pos == 0:
                self.p2_pos = 10
        self.p2_score += self.p2_pos
    def roll(self):
        self.last_roll += 1
        self.num_rolls += 1
        if self.last_roll > 100:
            self.last_roll %= 100
        return self.last_roll
    def roll3(self):
        sum = 0
        for roll in range(3):
            sum += self.roll()
        return sum
    def p1_turn(self):
        self.move_p1(self.roll3())
        if self.p1_score >= 1000:
            print(self.p2_score * self.num_rolls)
            return True
    def p2_turn(self):
        self.move_p2(self.roll3())
        if self.p2_score >= 1000:
            print(self.p1_score * self.num_rolls)
            return True

class q_game:
    def __init__(self, p1_pos, p2_pos):
        #(p1_pos, p2_pos, p1_score, p2_score)
        #three rolls: 3x1, 4x3, 5x6, 6x7, 7x6, 8x3, 9x1
        self.games = {(p1_pos, p2_pos, 0, 0): 1}
        self.new_games = {}
        self.wins = [0, 0]
    def get_pos(self, old_pos, roll):
        if old_pos + roll > 10:
            new_pos = old_pos + roll - 10
        else:
            new_pos = old_pos + roll
        return new_pos
    def move_p1(self, game, roll, count):
        new_pos = self.get_pos(game[0], roll)
        if (new_pos, game[1], game[2], game[3]) in self.new_games:
            self.new_games[(new_pos, game[1], game[2], game[3])] += count * self.games[game]
        else:
            self.new_games[(new_pos, game[1], game[2], game[3])] = count * self.games[game]
    def move_p2(self, game, roll, count):
        new_pos = self.get_pos(game[1], roll)
        if (game[0], new_pos, game[2], game[3]) in self.new_games:
            self.new_games[(game[0], new_pos, game[2], game[3])] += count * self.games[game]
        else:
            self.new_games[(game[0], new_pos, game[2], game[3])] = count * self.games[game]
    def score_p1(self):
        self.games = {}
        for game in self.new_games:
            if (game[0], game[1], game[2] + game[0], game[3]) in self.games:
                self.games[(game[0], game[1], game[2] + game[0], game[3])] += self.new_games[game]
            else:
                self.games[(game[0], game[1], game[2] + game[0], game[3])] = self.new_games[game]
        self.new_games = {}
    def score_p2(self):
        self.games = {}
        for game in self.new_games:
            if (game[0], game[1], game[2], game[3] + game[1]) in self.games:
                self.games[(game[0], game[1], game[2], game[3] + game[1])] += self.new_games[game]
            else:
                self.games[(game[0], game[1], game[2], game[3] + game[1])] = self.new_games[game]
        self.new_games = {}
    def count_wins(self):
        check_games = self.games.copy()
        for game in check_games:
            if game[2] > 20:
                self.wins[0] += self.games[game]
                self.games.pop(game)
            elif game[3] > 20:
                self.wins[1] += self.games[game]
                self.games.pop(game)
    def p1_turn(self):
        for game in self.games:
            self.move_p1(game, 3, 1)
            self.move_p1(game, 4, 3)
            self.move_p1(game, 5, 6)
            self.move_p1(game, 6, 7)
            self.move_p1(game, 7, 6)
            self.move_p1(game, 8, 3)
            self.move_p1(game, 9, 1)
            # self.move_p1(game, 1, 1)
            # self.move_p1(game, 2, 1)
            # self.move_p1(game, 3, 1)
        self.score_p1()
        self.count_wins()
        if not self.games:
            return True
    def p2_turn(self):
        for game in self.games:
            self.move_p2(game, 3, 1)
            self.move_p2(game, 4, 3)
            self.move_p2(game, 5, 6)
            self.move_p2(game, 6, 7)
            self.move_p2(game, 7, 6)
            self.move_p2(game, 8, 3)
            self.move_p2(game, 9, 1)
            # self.move_p2(game, 1, 1)
            # self.move_p2(game, 2, 1)
            # self.move_p2(game, 3, 1)
        self.score_p2()
        self.count_wins()
        if not self.games:
            return True

def main():
    part1 = d_game(9, 3)
    win = False
    while True:
        win = part1.p1_turn()
        if win:
            break
        win = part1.p2_turn()
        if win:
            break
    part2 = q_game(9, 3)
    end = False
    while True:
        end = part2.p1_turn()
        if end:
            break
        end = part2.p2_turn()
        if end:
            break
    print(part2.wins)

if __name__ == '__main__':
    main()

# heheheheh >:) you found me