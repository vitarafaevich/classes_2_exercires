import random

class NavalBattle:
    """
    Class representing the Naval Battle (Sea Battle) game for 2 people
    :method show():
    :method shot(self, x, y):
    :method new_game(cls):
    """
    playing_field = []

    def __init__(self, player):
        self.player = player

    @staticmethod
    def show():
        """
        Static method show(): showing the playing field
        """
        if not NavalBattle.playing_field:
            print('The field is not initialized. Create a new game.')
            return

        lis = []
        for row in NavalBattle.playing_field:
            lis.append([])
            for i in range(len(row)):
                if row[i] == 0 or row[i] == 1:
                    lis[-1].append('~')
                else:
                    lis[-1].append(row[i])

        # Displaying the header with column numbers
        print("  " + " ".join([str(i + 1) for i in range(10)]))
        for i, elem in enumerate(lis):
            print(str(i + 1) + " " + ' '.join([str(j) for j in elem]))


    def shot(self, x, y):
        """
        Method shot: revealing the shots accuracy
        :param x: x coordinate
        :param y: y coordinate
        """
        if not NavalBattle.playing_field:
            print('The field is not filled. Restart the game')
            return

        if not (0 <= x <= 9 and 0 <= y <= 9):
            print('The shot coordinates are not in the field')
            return

        if (NavalBattle.playing_field[y - 1][x - 1] == self.player or
                NavalBattle.playing_field[y - 1][x - 1] == 'o'):
            print('You already shot to this cell :(')
        else:
            if NavalBattle.playing_field[y - 1][x - 1] == 0:
                print('You missed!')
                NavalBattle.playing_field[y - 1][x - 1] = 'o'
            else:
                print('You hit the target!')
                NavalBattle.playing_field[y - 1][x - 1] = self.player

    @classmethod
    def new_game(cls):
        """
        Static method new_game(cls): creates a new game board and places ships randomly.
        :param cls: referring to class
        """
        # Creating the playing field.
        cls.playing_field = [[0 for _ in range(10)] for _ in range(10)]

        directions = ['vertical', 'horizontal']

        ship_lengths = [4, 3, 2, 1]
        ship_counts = [1, 2, 3, 4]

        for length, count in zip(ship_lengths, ship_counts):
            for _ in range(count):
                placed = False
                while not placed:
                    direction = random.choice(directions)
                    if direction == 'vertical':
                        x = random.randint(0, 9)
                        y = random.randint(0, 9 - length)
                    else:
                        x = random.randint(0, 9 - length)
                        y = random.randint(0, 9)

                    # Check if the placement is valid.
                    valid_placement = True
                    for i in range(length):
                        if direction == 'vertical':
                            check_x = x
                            check_y = y + i
                        else:
                            check_x = x + i
                            check_y = y

                        # Check boundaries and adjacent cells for other ships.
                        for dx in range(-1, 2):
                            for dy in range(-1, 2):
                                neighbor_x = check_x + dx
                                neighbor_y = check_y + dy

                                if 0 <= neighbor_x < 10 and 0 <= neighbor_y < 10:
                                    if cls.playing_field[neighbor_y][neighbor_x] != 0:
                                        valid_placement = False
                                        break
                            if not valid_placement:
                                break
                        if not valid_placement:
                            break

                    # Place the ship.
                    if valid_placement:
                        for i in range(length):
                            if direction == 'vertical':
                                cls.playing_field[y + i][x] = 1
                            else:
                                cls.playing_field[y][x + i] = 1
                        placed = True


player1 = NavalBattle('#')
player1.shot(6, 2)
NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                             [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1, 1)
player1.shot(1, 1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)
