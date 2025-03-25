class NavalBattle:
    """
    Class representing the Naval Battle (Sea Battle) game for 2 people
    """
    playing_field = []

    def __init__(self, player):
        self.player = player

    @staticmethod
    def show():
        """
        Static method show(): showing the playing field
        :return:
        """
        lis = []
        for row in NavalBattle.playing_field:
            lis.append([])
            for i in range(len(row)):
                if row[i] == 0 or row[i] == 1:
                    lis[-1].append('~')
                else:
                    lis[-1].append(row[i])

        for elem in lis:
            print(''.join([str(j) for j in elem]))

    def shot(self, x, y):
        """
        Method shot: revealing the shots accuracy
        """
        if NavalBattle.playing_field[y - 1][x - 1] == 0:
            print('мимо')
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
        else:
            print('попал')
            NavalBattle.playing_field[y - 1][x - 1] = self.player


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
player1 = NavalBattle('#')
player2 = NavalBattle('*')
NavalBattle.show()
player1.shot(6, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)
player2.show()
player1.shot(1, 1)
NavalBattle.show()
