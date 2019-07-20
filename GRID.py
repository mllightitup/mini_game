GRID_SIZE = 10

grid = [['#' for i in range(GRID_SIZE)] for i in range(GRID_SIZE)]
x = 1
y = 1
grid[x][y] = 'P'

while True:
    print('\n' * 50)
    print('Текущая доска:')
    for j in range(GRID_SIZE):
        s = ''
        for k in range(GRID_SIZE):
            s += f'{grid[j][k]} '
        print(s)

    print('')
    print("Куда идем?")
    command = input()
    grid[x][y] = '#'
    if command == 'верх' and x > 0:
        x -= 1
    elif command == 'низ' and x < GRID_SIZE - 1:
        x += 1
    elif command == 'лево' and y > 0:
        y -= 1
    elif command == 'право' and y < GRID_SIZE - 1:
        y += 1
    grid[x][y] = 'P'
