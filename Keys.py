

class Key:
    def putXInSquares(self, num):
        # the ascii art of 'X' , 'O' and white space

        cross = [[' ', ' ', ' ', ' ', '?', '8', '8', '8', '8', 'P', ' ', ' ', ' ', ' '],  # 0        
                 [' ', ' ', ' ', ' ', ' ', '`', '8', '8', '`', ' ', ' ', ' ', ' ', ' '],  # 1        
                 [' ', '8', 'b', ',', ' ', ' ', '8', '8', ' ', ' ', ',', 'd', '8', ' '],  # 2        
                 [' ', '8', '8', '8', '8', 'S', 'I', 'C', 'K', '8', '8', '8', '8', ' '],  # 3        
                 [' ', '8', 'P', '~', ' ', ' ', '8', '8', ' ', ' ', '~', '?', '8', ' '],  # 4        
                 [' ', ' ', ' ', ' ', ' ', ',', '8', '8', '.', ' ', ' ', ' ', ' ', ' '],  # 5        
                 [' ', ' ', ' ', ' ', 'd', '8', '8', '8', '8', 'b', ' ', ' ', ' ', ' ']]  # 6        
        mo = ''.join(map(str, cross[num]))
        return mo

    def putOInSquares(self, num):
        cross = [[' ', ' ', ' ', ' ', '%', '8', '8', '8', '8', '%', ' ', ' ', ' ', ' '],  # 0        
                 [' ', ' ', ' ', '8', '%', ' ', ' ', ' ', ' ', '%', '8', ' ', ' ', ' '],  # 1        
                 [' ', ' ', ' ', '%', '8', ' ', ' ', ' ', ' ', '8', '%', ' ', ' ', ' '],  # 2        
                 [' ', ' ', ' ', '8', '8', ' ', ' ', ' ', ' ', '8', '8', ' ', ' ', ' '],  # 3        
                 [' ', ' ', ' ', '%', '8', ' ', ' ', ' ', ' ', '8', '%', ' ', ' ', ' '],  # 4        
                 [' ', ' ', ' ', '8', '%', ' ', ' ', ' ', ' ', '%', '8', ' ', ' ', ' '],  # 5        
                 [' ', ' ', ' ', ' ', '%', '8', '8', '8', '8', '%', ' ', ' ', ' ', ' ']]  # 6        
        mo = ''.join(map(str, cross[num]))
        return mo

    def putEInSquares(self, num):
        cross = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 0        
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 1        
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 2        
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 3        
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 4        
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 5        
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]  # 6        
        mo = ''.join(map(str, cross[num]))
        return mo

