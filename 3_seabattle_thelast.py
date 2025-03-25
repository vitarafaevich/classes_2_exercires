import random

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
        if len(NavalBattle.playing_field) == 0:
            print('вы не заполнили поле')
        # minus one to match coefficient (starting from 0 for python, from 1 for user)
        elif NavalBattle.playing_field[y - 1][x - 1] == self.player or NavalBattle.playing_field[y - 1][x - 1] == '0':
            print('error')
        else:
            if NavalBattle.playing_field[y - 1][x - 1] == 0:
                print('мимо')
                NavalBattle.playing_field[y - 1][x - 1] = 'o'
            else:
                print('попал')
                NavalBattle.playing_field[y - 1][x - 1] = self.player

    @classmethod
    def new_game(cls):
        """
        Static method new_game(cls): ////////
        :param cls:
        :return:
        """
        cls.playing_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        directions = ['вертикальное', 'горизонтальное']

        # fore-decked ship
        for _ in range(1):
            boat_dir = random.choice(directions)
            if boat_dir == 'вертикальное':
                flag = False
                while flag is not True:
                    x_point = random.randint(0, 9)
                    y_point = random.randint(0, 9)

                    # checking the adequacy of y_point, to fit 4 decks
                    if y_point + 3 <= 9:
                        for i in range(3):
                            cls.playing_field[y_point + i][x_point] = '1'
                        flag = True
            else:
                flag = False
                while flag is not True:
                    x_point = random.randint(0, 9)
                    y_point = random.randint(0, 9)
                    if x_point + 3 <= 9:
                        for i in range(3):
                            cls.playing_field[y_point][x_point + i] = '1'
                        flag = True

        # three-decked ships
        for _ in range(2):
            dir_triple= random.choice(directions)
            if dir_triple == 'вертикальный':
                flag = False
                while flag is not True:
                    x_triple = random.randint(0, 9)
                    y_triple = random.randint(0, 9)

                    # checking the adequacy of y_point to fit 3 decks
                    cnt = 0
                    if y_triple + 2 <= 9:
                        # making sure that the cages are empty
                        for i in range(3):
                            if cls.playing_field[y_triple + i][x_triple] == 0:
                                cnt += 1

                        #VERTICAL POSITIONING!!!
                        if cnt == 3:
                            # checking that cages near the ship are empty
                            final = 0
                            # left touch
                            if y_triple == 0:
                                if x_triple == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple + i][x_triple] == 0 and
                                                cls.playing_field[y_triple + i][x_triple + 1] == 0):
                                            final += 1
                                elif y_triple + cnt - 1== 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple - 1 + i][x_triple] == 0 and
                                                cls.playing_field[y_triple - 1 + i][x_triple + 1] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_triple - 1 + i][x_triple] == 0 and
                                                cls.playing_field[y_triple - 1 + i][x_triple + 1] == 0):
                                            final += 1

                            # right touch
                            elif x_triple == 9:
                                if y_triple == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple + i][x_triple] == 0 and
                                                cls.playing_field[y_triple + i][x_triple - 1]  == 0):
                                            final += 1
                                elif y_triple + cnt - 1 == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple - 1 + i][x_triple] == 0 and
                                                cls.playing_field[y_triple - 1 + i][x_triple - 1] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_triple - 1 + i][x_triple] == 0 and
                                                cls.playing_field[y_triple - 1 + i][x_triple - 1] == 0):
                                            final += 1

                            # middle touch (two middle exceptions)
                            elif y_triple == 0 or (y_triple + cnt - 1) == 9:
                                if y_triple == 0:
                                    for i in range(cnt + 1):
                                        for j in range(3):
                                            if (cls.playing_field[y_triple + i][x_triple - 1 + j] == 0 and
                                                    cls.playing_field[y_triple + 1 + i][x_triple - 1 + j]) == 0:
                                                final += 1
                                else:
                                    for i in range(cnt + 1):
                                        for j in range(3):
                                            if (cls.playing_field[y_triple - 1 + i][x_triple - 1 + j] == 0 and
                                                    cls.playing_field[y_triple + i][x_triple - 1 + j] == 0):
                                                final += 1

                            #no border touching position
                            else:
                                for i in range(cnt + 2):
                                    if (cls.playing_field[y_triple - 1 + i][x_triple] == 0 and
                                            cls.playing_field[y_triple - 1 + i][x_triple - 1] == 0 and
                                            cls.playing_field[y_triple - 1 + i][x_triple + 1] == 0 ):
                                        final += 1

                            # final positioning of the ship
                            if final == 1:
                                for j in range(cnt):
                                    cls.playing_field[y_triple + j][x_triple] = '1'
                                    flag = True

            # horizontal three-decked
            else:
                flag = False
                while flag is not True:
                    x_triple = random.randint(0, 9)
                    y_triple = random.randint(0, 9)

                    cnt = 0
                    if x_triple + 2 <= 9:
                        for i in range(3):
                            if cls.playing_field[y_triple][x_triple + i] == 0:
                                cnt += 1

                        # FOR HORIZONTAL POSITIONING!!!
                        if cnt == 3:
                            # checking that cages near the ship are empty
                            final = 0
                            # left touch
                            if x_triple == 0:
                                if y_triple == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple][x_triple + i] == 0 and
                                                cls.playing_field[y_triple + 1][x_triple + i] == 0):
                                            final += 1
                                elif y_triple == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple][x_triple + i] == 0 and
                                                cls.playing_field[y_triple - 1][x_triple + i] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple][x_triple + i] == 0 and
                                                cls.playing_field[y_triple - 1][x_triple + i] == 0 and
                                                cls.playing_field[y_triple + 1][x_triple + i] == 0):
                                            final += 1

                            # right touch
                            elif x_triple + cnt - 1 == 9:
                                if y_triple == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple][x_triple + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_triple + 1][x_triple + cnt - 1 - i] == 0):
                                            final += 1
                                elif y_triple == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple][x_triple + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_triple + 1][x_triple + i] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_triple][x_triple + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_triple - 1][x_triple + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_triple + 1][x_triple + cnt - 1 - i] == 0):
                                            final += 1

                            # middle touch (two middle exceptions)
                            elif y_triple == 0 or y_triple == 9:
                                if y_triple == 0:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_triple][x_triple - 1 + i] == 0 and
                                                cls.playing_field[y_triple][x_triple + i] == 0 and
                                                cls.playing_field[y_triple + 1][x_triple - 1 + i] == 0):
                                            final += 1
                                else:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_triple][x_triple - 1 + i] == 0 and
                                                cls.playing_field[y_triple][x_triple + i] == 0 and
                                                cls.playing_field[y_triple - 1][x_triple - 1 + i] == 0):
                                            final += 1
                            # no border touching position
                            else:
                                for i in range(cnt + 2):
                                    if (cls.playing_field[y_triple][x_triple - 1 + i] == 0 and
                                            cls.playing_field[y_triple - 1][x_triple - 1 + i] == 0 and
                                            cls.playing_field[y_triple + 1][x_triple - 1 + i] == 0):
                                        final += 1

                            # final positioning of the ship
                            if final == 1:
                                for j in range(cnt):
                                    cls.playing_field[y_triple][x_triple + j] = '1'
                                    flag = True

        # two-decked ships
        for _ in range(3):
            dir_double = random.choice(directions)
            if dir_double == 'вертикальный':
                flag = False
                while flag is not True:
                    x_double = random.randint(0, 9)
                    y_double = random.randint(0, 9)
                    cnt = 0
                    if y_double + 1 <= 9:
                        # making sure that the cages are empty
                        for i in range(2):
                            if cls.playing_field[y_double + i][x_double] == '0':
                                cnt += 1

                        # VERTICAL POSITIONING!!!
                        if cnt == 2:
                            # checking that cages near the ship are empty
                            final = 0
                            # left touch
                            if y_double == 0:
                                if x_double == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double + i][x_double] == 0 and
                                                cls.playing_field[y_double + i][x_double + 1] == 0):
                                            final += 1
                                elif y_double + cnt - 1 == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                                cls.playing_field[y_double - 1 + i][x_double + 1] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                                cls.playing_field[y_double - 1 + i][x_double + 1] == 0):
                                            final += 1

                            # right touch
                            elif x_double == 9:
                                if y_double == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double + i][x_double - 1] == 0):
                                            final += 1
                                elif y_double + cnt - 1 == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                                cls.playing_field[y_double - 1 + i][x_double - 1] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                                cls.playing_field[y_double - 1 + i][x_double - 1] == 0):
                                            final += 1

                            # middle touch (two middle exceptions)
                            elif y_double == 0 or (y_double + cnt - 1) == 9:
                                if y_double == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double + i][x_double - 1 + i] == 0 and
                                            cls.playing_field[y_double + 1 + i][x_double - 1 + i]) == 0:
                                            final += 1
                                else:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double - 1 + i][x_double - 1 + i] == 0 and
                                                cls.playing_field[y_double + i][x_double - 1 + i] == 0):
                                            final += 1

                            # no border touching position
                            else:
                                for i in range(cnt + 2):
                                    if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                            cls.playing_field[y_double - 1 + i][x_double - 1] == 0 and
                                            cls.playing_field[y_double - 1 + i][x_double + 1] == 0):
                                        final += 1

                            # final positioning of the ship
                            if final == 1:
                                for j in range(cnt):
                                    cls.playing_field[y_double + j][x_double] = '1'
                                    flag = True

            # horizontal two-decked
            else:
                flag = False
                while flag is not True:
                    x_double = random.randint(0, 9)
                    y_double = random.randint(0, 9)

                    cnt = 0
                    if x_double + 2 <= 9:
                        for i in range(3):
                            if cls.playing_field[y_double][x_double + i] == 0:
                                cnt += 1

                        # FOR HORIZONTAL POSITIONING!!!
                        if cnt == 3:
                            # checking that cages near the ship are empty
                            final = 0
                            # left touch
                            if x_double == 0:
                                if y_double == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + i] == 0):
                                            final += 1
                                elif y_double == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double - 1][x_double + i] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double - 1][x_double + i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + i] == 0):
                                            final += 1

                            # right touch
                            elif x_double + cnt - 1 == 9:
                                if y_double == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + cnt - 1 - i] == 0):
                                            final += 1
                                elif y_double == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + i] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_double - 1][x_double + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + cnt - 1 - i] == 0):
                                            final += 1

                            # middle touch (two middle exceptions)
                            elif y_double == 0 or y_double == 9:
                                if y_double == 0:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_double][x_double - 1 + i] == 0 and
                                                cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double + 1][x_double - 1 + i] == 0):
                                            final += 1
                                else:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_double][x_double - 1 + i] == 0 and
                                                cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double - 1][x_double - 1 + i] == 0):
                                            final += 1
                            # no border touching position
                            else:
                                for i in range(cnt + 2):
                                    if (cls.playing_field[y_double][x_double - 1 + i] == 0 and
                                            cls.playing_field[y_double - 1][x_double - 1 + i] == 0 and
                                            cls.playing_field[y_double + 1][x_double - 1 + i] == 0):
                                        final += 1

                            # final positioning of the ship
                            if final == 1:
                                for j in range(cnt):
                                    cls.playing_field[y_double][x_double + j] = '1'
                                    flag = True


        #ONE-DECKED SHIPS

        #Horizontal checking the emptyness
        for i in range(1, 5):
            for _ in range(i): #количество итераций в зависимости от количества палуб
                flag = False
                while flag is not True:
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)

                    x_list, y_list = [], []
                    num_decks = 5 - i #количество палуб

                    for j in range(-1, 2, 1):
                        for i in range(num_decks + 2):
                            x_list.append([x + i])
                            y_list.append([y + j])

                    x_list = [max(0, min(x, 9)) for x in x_list]
                    y_list = [max(0, min(y, 9)) for y in y_list]

                    counter = 0
                    for k in x_list:
                        for p in y_list:
                            if cls.playing_field[p][k] == 0:
                                counter += 1

                    if counter == len(x_list):
                        cls.playing_field[y][x] = '1'
                        flag = True







                y_double = random.randint(0, 9)
                cnt = 0
                if y_double + 1 <= 9:
                    # making sure that the cages are empty
                    for i in range(2):
                        if cls.playing_field[y_double + i][x_double] == '0':
                            cnt += 1

                    # VERTICAL POSITIONING!!!
                    if cnt == 2:
                        # checking that cages near the ship are empty
                        final = 0
                        # left touch
                        if y_double == 0:
                            if x_double == 0:
                                for i in range(cnt + 1):
                                    if (cls.playing_field[y_double + i][x_double] == 0 and
                                            cls.playing_field[y_double + i][x_double + 1] == 0):
                                        final += 1
                            elif y_double + cnt - 1 == 9:
                                for i in range(cnt + 1):
                                    if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                            cls.playing_field[y_double - 1 + i][x_double + 1] == 0):
                                        final += 1
                            # middle touch
                            else:
                                for i in range(cnt + 2):
                                    if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                            cls.playing_field[y_double - 1 + i][x_double + 1] == 0):
                                        final += 1

                        # right touch
                        elif x_double == 9:
                            if y_double == 0:
                                for i in range(cnt + 1):
                                    if (cls.playing_field[y_double][x_double + i] == 0 and
                                            cls.playing_field[y_double + i][x_double - 1] == 0):
                                        final += 1
                            elif y_double + cnt - 1 == 9:
                                for i in range(cnt + 1):
                                    if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                            cls.playing_field[y_double - 1 + i][x_double - 1] == 0):
                                        final += 1
                            # middle touch
                            else:
                                for i in range(cnt + 2):
                                    if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                            cls.playing_field[y_double - 1 + i][x_double - 1] == 0):
                                        final += 1

                        # middle touch (two middle exceptions)
                        elif y_double == 0 or (y_double + cnt - 1) == 9:
                            if y_double == 0:
                                for i in range(cnt + 1):
                                    if (cls.playing_field[y_double + i][x_double - 1 + i] == 0 and
                                        cls.playing_field[y_double + 1 + i][x_double - 1 + i]) == 0:
                                        final += 1
                            else:
                                for i in range(cnt + 1):
                                    if (cls.playing_field[y_double - 1 + i][x_double - 1 + i] == 0 and
                                            cls.playing_field[y_double + i][x_double - 1 + i] == 0):
                                        final += 1

                        # no border touching position
                        else:
                            for i in range(cnt + 2):
                                if (cls.playing_field[y_double - 1 + i][x_double] == 0 and
                                        cls.playing_field[y_double - 1 + i][x_double - 1] == 0 and
                                        cls.playing_field[y_double - 1 + i][x_double + 1] == 0):
                                    final += 1

                        # final positioning of the ship
                        if final == 1:
                            for j in range(cnt):
                                cls.playing_field[y_double + j][x_double] = '1'
                                flag = True

                # horizontal three-decked
            else:
                flag = False
                while flag is not True:
                    x_double = random.randint(0, 9)
                    y_double = random.randint(0, 9)

                    cnt = 0
                    if x_double + 2 <= 9:
                        for i in range(3):
                            if cls.playing_field[y_double][x_double + i] == 0:
                                cnt += 1

                        # FOR HORIZONTAL POSITIONING!!!
                        if cnt == 3:
                            # checking that cages near the ship are empty
                            final = 0
                            # left touch
                            if x_double == 0:
                                if y_double == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + i] == 0):
                                            final += 1
                                elif y_double == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double - 1][x_double + i] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double - 1][x_double + i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + i] == 0):
                                            final += 1

                            # right touch
                            elif x_double + cnt - 1 == 9:
                                if y_double == 0:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + cnt - 1 - i] == 0):
                                            final += 1
                                elif y_double == 9:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + i] == 0):
                                            final += 1
                                # middle touch
                                else:
                                    for i in range(cnt + 1):
                                        if (cls.playing_field[y_double][x_double + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_double - 1][x_double + cnt - 1 - i] == 0 and
                                                cls.playing_field[y_double + 1][x_double + cnt - 1 - i] == 0):
                                            final += 1

                            # middle touch (two middle exceptions)
                            elif y_double == 0 or y_double == 9:
                                if y_double == 0:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_double][x_double - 1 + i] == 0 and
                                                cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double + 1][x_double - 1 + i] == 0):
                                            final += 1
                                else:
                                    for i in range(cnt + 2):
                                        if (cls.playing_field[y_double][x_double - 1 + i] == 0 and
                                                cls.playing_field[y_double][x_double + i] == 0 and
                                                cls.playing_field[y_double - 1][x_double - 1 + i] == 0):
                                            final += 1
                            # no border touching position
                            else:
                                for i in range(cnt + 2):
                                    if (cls.playing_field[y_double][x_double - 1 + i] == 0 and
                                            cls.playing_field[y_double - 1][x_double - 1 + i] == 0 and
                                            cls.playing_field[y_double + 1][x_double - 1 + i] == 0):
                                        final += 1

                            # final positioning of the ship
                            if final == 1:
                                for j in range(cnt):
                                    cls.playing_field[y_double][x_double + j] = '1'
                                    flag = True


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
player1.shot(1,1)
player1.shot(1,1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)



'''
import random

class NavalBattle:
    playing_field = []

    def __init__(self, symbol):
        self.symbol = symbol

    @staticmethod
    def show():
        internal_list = []
        for elem in NavalBattle.playing_field:
            internal_list.append([])
            for i in range(len(elem)):
                if elem[i] == 0 or elem[i] == 1:
                    internal_list[-1].append('~')
                else:
                    internal_list[-1].append(elem[i])

        for elem in internal_list:
            print(''.join([str(j) for j in elem]))

    def shot(self, x, y):
        if len(NavalBattle.playing_field) == 0:
            print('игровое поле не заполнено')
        else:
            if NavalBattle.playing_field[y - 1][x - 1] == self.symbol or NavalBattle.playing_field[y - 1][x - 1] == 'o':
                print('ошибка')
            else:
                if NavalBattle.playing_field[y - 1][x - 1] == 0:
                    print('мимо')
                    NavalBattle.playing_field[y - 1][x - 1] = 'o'
                else:
                    print('попал')
                    NavalBattle.playing_field[y - 1][x - 1] = self.symbol

    @classmethod
    def new_game(cls):
        cls.playing_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        direction = ['вертикальный', 'горизонтальный']
        dir_quadro = random.choice(direction)
        if dir_quadro == 'вертикальный':
            done = False
            while done is not True:
                x_quadro = random.randint(0, 9)
                y_quadro = random.randint(0, 9)
                if (y_quadro + 1 < 9) and (y_quadro + 2 < 9) and (y_quadro + 3 <= 9):

                    cls.playing_field[y_quadro][x_quadro] = '1'
                    cls.playing_field[y_quadro + 1][x_quadro] = '1'
                    cls.playing_field[y_quadro + 2][x_quadro] = '1'
                    cls.playing_field[y_quadro + 3][x_quadro] = '1'
                    done = True
        else:
            done = False
            while done is not True:
                x_quadro = random.randint(0, 9)
                y_quadro = random.randint(0, 9)
                if (x_quadro + 1 < 9) and (x_quadro + 2 < 9) and (x_quadro + 3 <= 9) :

                    cls.playing_field[y_quadro][x_quadro] = '1'
                    cls.playing_field[y_quadro][x_quadro + 1] = '1'
                    cls.playing_field[y_quadro][x_quadro + 2] = '1'
                    cls.playing_field[y_quadro][x_quadro + 3] = '1'
                    done = True

        for _ in range(2):
            dir_triple= random.choice(direction)
            if dir_triple == 'вертикальный':
                done = False
                while done is not True:
                    x_triple = random.randint(0, 9)
                    y_triple = random.randint(0, 9)
                    if (y_triple + 1 < 9) and (y_triple + 2 <= 9) and (cls.playing_field[y_triple][x_triple] == 0) and (
                            cls.playing_field[y_triple + 1][x_triple] == 0) and (
                            cls.playing_field[y_triple + 2][x_triple] == 0):

                        cls.playing_field[y_triple][x_triple] = '1'
                        cls.playing_field[y_triple + 1][x_triple] = '1'
                        cls.playing_field[y_triple + 2][x_triple] = '1'
            else:
                done = False
                while done is not True:
                    x_triple = random.randint(0, 9)
                    y_triple = random.randint(0, 9)
                    if (x_triple + 1 < 9) and (
                            x_triple + 2 <= 9) and (cls.playing_field[y_triple][x_triple] == 0) and (
                            cls.playing_field[y_triple][x_triple + 1] == 0) and (
                            cls.playing_field[y_triple][x_triple + 2] == 0):

                        cls.playing_field[y_triple][x_triple] = '1'
                        cls.playing_field[y_triple][x_triple + 1] = '1'
                        cls.playing_field[y_triple][x_triple + 2] = '1'

            for _ in range(3):
                dir_double = random.choice(direction)
                if dir_double == 'вертикальный':
                    done = False
                    while done is not True:
                        x_double = random.randint(0, 9)
                        y_double = random.randint(0, 9)
                        if (y_double + 1 <= 9) and (cls.playing_field[y_double][x_double] == 0) and (
                                cls.playing_field[y_double + 1][x_double] == 0):
                            cls.playing_field[y_double][x_double] = '1'
                            cls.playing_field[y_double + 1][x_double] = '1'
                else:
                    done = False
                    while done is not True:
                        x_double = random.randint(0, 9)
                        y_double = random.randint(0, 9)
                        if (x_double + 1 <= 9) and (cls.playing_field[y_double][x_double] == 0) and (
                                cls.playing_field[y_double][x_double + 1] == 0):
                            cls.playing_field[y_double][x_double] = '1'
                            cls.playing_field[y_double][x_double + 1] = '1'

            for _ in range(4):
                done = False
                while done is not True:
                    x_single = random.randint(0, 9)
                    y_single = random.randint(0, 9)
                    if cls.playing_field[y_single][x_single] == 0:
                        cls.playing_field[y_single][x_single] = '1'


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
'''




#FOR HORIZONTAL POSITIONING NOT VERTICAL!!!
'''
:param cnt_y: vertical
:param cnt_x: horizontal
=> 0 or 1 depending on position
'''
if cnt_x == 3:
    # checking that cages near the ship are empty
    final = 0
    # left touch
    if x_triple == 0:
        if y_triple == 0:
            for i in range(cnt_x + cnt_y):
                if (cls.playing_field[y_triple + cnt_y][x_triple + i] == 0 and
                        cls.playing_field[y_triple + 1][x_triple + i] == 0):
                    final += 1
        elif y_triple == 9:
            for i in range(cnt_x + cnt_y)):
                if (cls.playing_field[y_triple + cnt_y][x_triple + i] == 0 and
                        cls.playing_field[y_triple - 1][x_triple + i] == 0):
                    final += 1
        # middle touch
        else:
            for i in range(cnt_x + cnt_y)):
                if (cls.playing_field[y_triple][x_triple + i] == 0 and
                        cls.playing_field[y_triple - 1][x_triple + i] == 0 and
                        cls.playing_field[y_triple + 1][x_triple + i] == 0):
                    final += 1

    # right touch
    elif x_triple + cnt_x - 1 == 9:
        if y_triple == 0:
            for i in range(cnt_x + cnt_y):
                if (cls.playing_field[y_triple + cnt_y][x_triple + cnt_x - 1 - i] == 0 and
                        cls.playing_field[y_triple + 1][x_triple + cnt_x - 1 - i]  == 0):
                    final += 1
        elif y_triple == 9:
            for i in range(cnt_x):
                if (cls.playing_field[y_triple][x_triple + cnt_x - 1 - i] == 0 and
                        cls.playing_field[y_triple + 1][x_triple + i] == 0):
                    final += 1
        # middle touch
        else:
            for i in range(cnt_x):
                if (cls.playing_field[y_triple][x_triple + cnt_x - 1 - i] == 0 and
                        cls.playing_field[y_triple - 1][x_triple + cnt_x - 1 - i] == 0 and
                        cls.playing_field[y_triple + 1][x_triple + cnt_x - 1 - i] == 0):
                    final += 1

    # middle touch (two middle exceptions)
    elif y_triple == 0 or y_triple == 9:
        if y_triple == 0:
            for i in range(cnt_x):
                if (cls.playing_field[y_triple][x_triple - 1 + i] == 0 and
                        cls.playing_field[y_triple][x_triple + i] == 0 and
                        cls.playing_field[y_triple + 1][x_triple - 1 + i] == 0):
                    final += 1
        else:
            for i in range(cnt):
                if (cls.playing_field[y_triple][x_triple - 1 + i] == 0 and
                        cls.playing_field[y_triple][x_triple + i] == 0 and
                        cls.playing_field[y_triple - 1][x_triple - 1 + i] == 0):
                    final += 1

    # final positioning of the ship
    if final == 1:
        for j in range(cnt_x):
            cls.playing_field[y_triple + j][x_triple] = '1'
