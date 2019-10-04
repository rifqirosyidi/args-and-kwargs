from example import MyObjects

data = {'game': 'Tetris', 'data': '3d'}
MyObjects(**data)

# data = 3d
# kwargs = {}
# game = tetris

data = {'game': 'Tetris', 'data': '3d', 'tag': 'arcade'}
MyObjects(**data)

# data = 3d
# kwargs = {'tag':'arcade'}
# game = tetris
