from scripts.clear import clearConsole


def refreshDisplay():
    left_max = 10
    middle_max = 50
    right_max = 10
    left_column = [0,12345,123456789012345,3,4,5,6,7]
    middle_column = [0,12345678901234567890,2,3]
    right_column = [0,1234567890,2,3,4]
    
    max_rows = len(left_column)
    if len(middle_column) > max_rows:
        max_rows = len(middle_column)
    if len(right_column) > max_rows:
        max_rows = len(right_column)
    
    left_column = normalizeRows(left_column, max_rows, left_max)
    middle_column = normalizeRows(middle_column, max_rows, middle_max)
    right_column = normalizeRows(right_column, max_rows, right_max)

    clearConsole()
    for n in range(0, max_rows):
        print(f'{left_column[n]}|{middle_column[n]}|{right_column[n]}')
    
def normalizeRows(list, rows, cols):
    if len(list) < rows:
        i = rows - len(list)
        list += [' '] * i
    for l in range(0, len(list)):
        line = str(list[l])
        if len(line) < cols:
            c = cols - len(line)
            line = line + " " * c
        elif len(line) > cols:
            line = line[0:cols]
        list[l] = line
    return list


refreshDisplay()