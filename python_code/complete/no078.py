from python_code.functions import polygonal_number

def find_residue(residue):
    p = {0: 1}

    pentagonal = []
    pent_index = 1
    while True:
        if pent_index > 0:
            next_index = -pent_index
        else:
            next_index = -pent_index + 1
        begin = polygonal_number(5, pent_index)
        end = polygonal_number(5, next_index)
        pentagonal.append(begin)
        for n in range(begin, end):
            p[n] = 0
            for index, val in enumerate(pentagonal):
                if (index/2) % 2 == 0:
                    p[n] = (p[n] + p[n - val]) % residue
                else:
                    p[n] = (p[n] - p[n - val]) % residue
            if p[n] == 0:
                return n
        pent_index = next_index

print find_residue(10**6)
