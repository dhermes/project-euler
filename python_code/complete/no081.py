from python_code.functions import get_data

def diamond_matrix(data):
    result = {}
    max_index = len(data) - 1
    max_depth = 2*max_index
    result[(max_index, max_index)] = data[-1][-1]

    for depth in range(max_depth - 1, -1, -1):
        initial = 0
        final = depth
        if depth > max_index:
            initial = depth - max_index
            final = max_index
        for row in range(initial, final + 1):
            column = depth - row
            choices = []
            if (row + 1, column) in result:
                choices.append(result[(row + 1, column)])
            if (row, column + 1) in result:
                choices.append(result[(row, column + 1)])
            result[(row, column)] = data[row][column] + min(choices)
    return result[(0, 0)]

# EXAMPLE = [[131, 673, 234, 103,  18],
#            [201,  96, 342, 965, 150],
#            [630, 803, 746, 422, 111],
#            [537, 699, 497, 121, 956],
#            [805, 732, 524,  37, 331]]
# print diamond_matrix(EXAMPLE) == 2427

data = [[int(entry) for entry in row.split(",")]
        for row in get_data(81).split("\n") if row]

print diamond_matrix(data)
