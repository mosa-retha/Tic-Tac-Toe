class Key:
    def putXInSquares(self, num):
        # ASCII art for representing 'X' symbol in a square
        cross = [
            [' ', ' ', ' ', ' ', '?', '8', '8', '8', '8', 'P', ' ', ' ', ' ', ' '],  # Row 0
            [' ', ' ', ' ', ' ', ' ', '`', '8', '8', '`', ' ', ' ', ' ', ' ', ' '],  # Row 1
            [' ', '8', 'b', ',', ' ', ' ', '8', '8', ' ', ' ', ',', 'd', '8', ' '],  # Row 2
            [' ', '8', '8', '8', '8', 'S', 'I', 'C', 'K', '8', '8', '8', '8', ' '],  # Row 3
            [' ', '8', 'P', '~', ' ', ' ', '8', '8', ' ', ' ', '~', '?', '8', ' '],  # Row 4
            [' ', ' ', ' ', ' ', ' ', ',', '8', '8', '.', ' ', ' ', ' ', ' ', ' '],  # Row 5
            [' ', ' ', ' ', ' ', 'd', '8', '8', '8', '8', 'b', ' ', ' ', ' ', ' ']   # Row 6
        ]
        # Join all characters in the specified row (num) to create a single line string for 'X'
        mo = ''.join(map(str, cross[num]))
        return mo

    def putOInSquares(self, num):
        # ASCII art for representing 'O' symbol in a square
        cross = [
            [' ', ' ', ' ', ' ', '%', '8', '8', '8', '8', '%', ' ', ' ', ' ', ' '],  # Row 0
            [' ', ' ', ' ', '8', '%', ' ', ' ', ' ', ' ', '%', '8', ' ', ' ', ' '],  # Row 1
            [' ', ' ', ' ', '%', '8', ' ', ' ', ' ', ' ', '8', '%', ' ', ' ', ' '],  # Row 2
            [' ', ' ', ' ', '8', '8', ' ', ' ', ' ', ' ', '8', '8', ' ', ' ', ' '],  # Row 3
            [' ', ' ', ' ', '%', '8', ' ', ' ', ' ', ' ', '8', '%', ' ', ' ', ' '],  # Row 4
            [' ', ' ', ' ', '8', '%', ' ', ' ', ' ', ' ', '%', '8', ' ', ' ', ' '],  # Row 5
            [' ', ' ', ' ', ' ', '%', '8', '8', '8', '8', '%', ' ', ' ', ' ', ' ']   # Row 6
        ]
        # Join all characters in the specified row (num) to create a single line string for 'O'
        mo = ''.join(map(str, cross[num]))
        return mo

    def putEInSquares(self, num):
        # ASCII art for representing an empty space in a square
        cross = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Row 0
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Row 1
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Row 2
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Row 3
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Row 4
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Row 5
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']   # Row 6
        ]
        # Join all characters in the specified row (num) to create a single line string for an empty space
        mo = ''.join(map(str, cross[num]))
        return mo
