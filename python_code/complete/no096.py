#############################
########## Imports ##########
#############################

import operator
from os.path import exists
import time
from python_code.functions import get_data

#############################
######### Constants #########
#############################

GRID_KEY = {1: 1,
            2: 4,
            3: 7,
            4: 28,
            5: 31,
            6: 34,
            7: 55,
            8: 58,
            9: 61}

#############################
########## Errors ###########
#############################

class Error(Exception):
    pass


class NonuniqueListForSubset(Error):
    pass


class NonsenseSudokuValue(Error):
    pass


class NonsenseIndex(Error):
    pass


class NonsenseGridIndex(Error):
    pass


class BadSudokuFileInput(Error):
    pass


class WronglySpecifiedNode(Error):
    pass


class WronglySpecifiedStructure(Error):
    pass


class WronglySpecifiedValueDeclaration(Error):
    pass


class TooManyOccurences(Error):
    pass


class CheckFoundNoImprovement(Error):
    pass


class NodelistMissingValue(Error):
    pass

#############################
###### Helper Functions #####
#############################

def subset(list_, size):
    if len(list_) != len(set(list_)):
        raise NonuniqueListForSubset(list_)
    if size == 1:
        return [ [entry] for entry in list_ ]
    result = []
    for entry in list_:
        candidates = list_[:] # copy, though not entirely deep
        candidates.remove(entry)
        for subset_ in subset(candidates, size - 1):
            to_add = sorted(subset_ + [entry])
            if to_add not in result:
                result.append(to_add)
    return [ entry for entry in result ]


def get_indices(structure, index):
    if structure not in ('row', 'column', 'subgrid'):
        raise WronglySpecifiedStructure(structure)
    elif index not in range(1, 10):
        raise NonsenseGridIndex(index)

    if structure == 'row':
        return [ 9*(index - 1) + j + 1 for j in range(9) ]
    elif structure == 'column':
        return [ index + 9*j for j in range(9) ]
    elif structure == 'subgrid':
        return [ GRID_KEY[index] + i + 9*j
                 for i in range(3) for j in range(3) ]


def get_first_node(nodes, value):
    for node in nodes:
        if value in node.choices:
            # returns the actual object, not a copy
            return node
    raise NodelistMissingValue(value)


def copy_remove(list_, val):
    # assume val occurs 0 or 1 times in list_
    if list_.count(val) > 1:
        raise TooManyOccurences("%s in %s" % (val, list_))

    result = list_[:]
    if val in result:
        result.remove(val)
    return result


def all_possible(structure_choices):
    if len(structure_choices) == 0:
        return []
    elif len(structure_choices) == 1:
        return [ choices[:] for choices in structure_choices[:] ]
    result = []
    working_choices = [ choices[:] for choices in structure_choices[1:] ]
    # if this entry is empty, result will be as well, which is fine
    for val in structure_choices[0]:
        curr = [ copy_remove(choices, val) for choices in working_choices ]
        result.extend([ [val] + arr for arr in all_possible(curr) ])
    return result


def hypothetical_setval(structure, index, value):
    """
    Helper for check structure

    Returns hypothetical arrangements for structure given the
    node at index is set to value.
    """
    if type(structure) != list:
        raise WronglySpecifiedStructure(
            "Type is %s, rather than list" % type(structure))
    # since only called by check_structure, structure is
    # validated there
    if index not in range(9):
        # this is the index within the structure, which is handed
        # to us as a list
        raise NonsenseIndex(index)
    working_structure = [ node.copy() for node in structure ]
    for ind in range(9):
        # checks if value is legitimate
        if ind != index:
            working_structure[ind].scratch_value(value)
    working_structure[index].set_final(value)
    return all_possible([ node.choices for node in working_structure ])


def uniq(list_):
    return sorted(list(set(list_)))


def check_structure(structure):
    # assumes the structure is cleaned
    if len(structure) != 9:
        WronglySpecifiedStructure("Structure of length %s." % len(structure))
    remaining = [ node.choices for node in structure
                  if len(node.choices) > 1 ]
    if remaining == []:
        return (False, 0)
    values = uniq(reduce(operator.add, remaining))
    for value in values:
        for i in range(9):
            if value in structure[i].choices:
                # may need to actually use the hypo, but for now
                # just being empty or not is our criterion
                if hypothetical_setval(structure, i, value) == []:
                    structure[i].scratch_value(value)
                    return (True, i)
    return (False, 0)

#############################
########## Objects ##########
#############################

class Node(object):
    """Represents a node in the sudoku grid"""
    def __init__(self, value=None):
        if value in range(1, 10):
            self.choices = [ value ]
        else:
            # Notice this doesn't throw an error for bad values
            self.choices = range(1, 10)
        self.row = None
        self.column = None
        self.subgrid = None
        self.final = False

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.choices)

    def scratch_value(self, value):
        if value not in range(1, 10):
            raise NonsenseSudokuValue(value)
        elif value in self.choices:
            self.choices.remove(value)

    def set_final(self, value):
        if value not in self.choices:
            raise NonsenseSudokuValue("Choice %s already removed." % value)
        self.choices = [value]
        self.final = True

    def set_value(self, attr, value):
        if value not in range(1, 10):
            raise NonsenseSudokuValue(value)
        setattr(self, attr, value)

    def set_row(self, row):
        self.set_value('row', row)

    def set_column(self, column):
        self.set_value('column', column)

    def set_subgrid(self):
        if self.row in range(1, 10) and self.column in range(1, 10):
            row_contrib = (self.row - 1)/3 # integer division intended
            column_contrib = (self.column - 1)/3 # integer division intended
            self.set_value('subgrid', 3*row_contrib + column_contrib + 1)
        # Doesn't fail when they aren't specified

    def copy(self):
        result = Node()
        result.choices = self.choices[:]
        result.row = self.row
        result.column = self.column
        result.subgrid = self.subgrid
        return result


class Grid(object):
    """Represents a sudoku grid"""
    def __init__(self, board=''):
        if board != '':
            data = [ [int(entry) for entry in row if entry ]
                     for row in board.split("\n") if row ]
            error = False
            if len(data) != 9:
                error = True
                message = "Too few rows in file."
            elif min([len(row) for row in data]) != 9:
                error = True
                message = "Too few entries in some row(s)."
            elif max([len(row) for row in data]) != 9:
                error = True
                message = "Too many entries in some row(s)."
            if error:
                raise BadSudokuFileInput(message)
            data = reduce(operator.add, data)
            try:
                data = [ int(entry) for entry in data ]
            except ValueError:
                raise BadSudokuFileInput("Data in file not all integers.")
            if min(data) < 0 or max(data) > 9:
                raise BadSudokuFileInput("Entries in file out of range.")
        else:
            data = [0] * 81

        self.data = {}
        for i in range(81):
            entry = data[i]
            if entry == 0:
                to_add = Node()
            else:
                to_add = Node(entry)
            to_add.set_row(i/9 + 1) # integer division intended
            to_add.set_column(i % 9 + 1)
            to_add.set_subgrid() # works based off of row and column
            self.data[i+1] = to_add

        rows = {}
        columns = {}
        subgrids = {}
        for i in range(1, 10):
            rows[i] = False
            columns[i] = False
            subgrids[i] = False
        self.checked = {'row': rows, 'column': columns, 'subgrid': subgrids}

    @property
    def solved(self):
        # reduce(operator.and_, [self.data[i].final for i in range(1, 82)])
        for i in range(1, 82):
            if not self.data[i].final:
                return False
        return True

    @property
    def pretty(self):
        values = []
        # row
        for i in range(9):
            to_add = []
            # column
            for j in range(9):
                index = 9*i + j + 1
                to_add.append(", ".join([str(entry) for entry
                                         in self.data[index].choices]))
            values.append(to_add)

        column_widths = [ max([ len(values[row][col]) for row in range(9) ])
                          for col in range(9) ]
        horiz_bars = [ ('-' * width) for width in column_widths ]
        result = []
        for i in range(9):
            result.append(horiz_bars)
            for j in range(9):
                values[i][j] = values[i][j].center(column_widths[j])
            result.append(values[i])
        result.append(horiz_bars)

        result = "\n".join(["| " + " | ".join(row) + " | " for row in result])
        return result

    def declare_values(self, structure, indices, values):
        for node_ind in indices:
            if node_ind not in range(1, 82):
                raise WronglySpecifiedNode(node_ind)
        if len(indices) != len(values) or len(indices) == 0:
            raise WronglySpecifiedValueDeclaration(indices)
        elif len(indices) == 1:
            raise WronglySpecifiedValueDeclaration(
                "Use declare_value for single values.")
        valid_nodes = [ self.data[index] for index in indices ]
        for value in values:
            if value not in range(1, 10):
                raise NonsenseSudokuValue(value)
            for node in valid_nodes:
                if value not in node.choices:
                    raise WronglySpecifiedValueDeclaration(
                        "%s not in %s for declaration." % (value, node.choices))

        structure_indices = get_indices(structure,
                                        getattr(valid_nodes[0], structure))
        invalid_nodes = [ self.data[index] for index in structure_indices
                          if index not in indices ]
        changed = False
        for node in invalid_nodes:
            for value in values:
                if value in node.choices:
                    changed = True
                    node.scratch_value(value)
                    self.checked['row'][node.row] = False
                    self.checked['column'][node.column] = False
                    self.checked['subgrid'][node.subgrid] = False
        for node in valid_nodes:
            for choice in node.choices:
                if choice not in values:
                    changed = True
                    node.scratch_value(choice)
                    self.checked['row'][node.row] = False
                    self.checked['column'][node.column] = False
                    self.checked['subgrid'][node.subgrid] = False
        return changed

    def declare_value(self, node_ind, value):
        if node_ind not in range(1, 82):
            raise WronglySpecifiedNode(node_ind)
        node = self.data[node_ind]
        node.set_final(value)

        row_indices = get_indices('row', node.row)
        col_indices = get_indices('column', node.column)
        grid_indices = get_indices('subgrid', node.subgrid)
        affected_nodes = [ self.data[index] for index in
                           set(row_indices + col_indices + grid_indices)
                           if index != node_ind ]
        for affected in affected_nodes:
            if value in affected.choices:
                affected.scratch_value(value)
                self.checked['row'][affected.row] = False
                self.checked['column'][affected.column] = False
                self.checked['subgrid'][affected.subgrid] = False

    def clean(self):
        all_checked = False

        while not all_checked:
            all_checked = True
            for i, node in self.data.items():
                if len(node.choices) == 1 and not node.final:
                    self.declare_value(i, node.choices[0])
                    all_checked = False

    def try_pick(self, structure, index):
        # get indices will validate the data
        value_indices = {} # The keys are the sudoku possible values
        # and the values are the indices that contain those sudoku values
        for ind in get_indices(structure, index):
            node = self.data[ind]
            if node.final:
                continue
            for choice in node.choices:
                if choice in value_indices:
                    value_indices[choice].append(ind)
                else:
                    value_indices[choice] = [ind]

        frequency_hash = {}
        for key, value in value_indices.items():
            length = len(value)
            if length in frequency_hash:
                frequency_hash[length].append(key)
            else:
                frequency_hash[length] = [key]

        for frequency in sorted(frequency_hash):
            if len(frequency_hash[frequency]) < frequency:
                continue
            for possible in subset(frequency_hash[frequency], frequency):
                # ordered by nature in which value_indices is created
                change = True
                indices = value_indices[possible[0]]
                for elt in possible[1:]:
                    if indices != value_indices[elt]:
                        change = False
                if change:
                    if frequency == 1:
                        self.declare_value(indices[0], possible[0])
                        return True
                    else:
                        if self.declare_values(structure, indices, possible):
                            return True

        return False

    def pick_all(self):
        for structure in ('row', 'column', 'subgrid'):
            for index in range(1, 10):
                if self.try_pick(structure, index):
                    return

        raise CheckFoundNoImprovement

    # def try_pick(self, structure, index):
    #     # get indices will validate the data
    #     result = False

    #     nodes = [ self.data[ind] for ind in get_indices(structure, index) ]
    #     values = reduce(operator.add, [ node.choices for node in nodes ])
    #     for value in range(1, 10):
    #         if values.count(value) == 1:
    #             node = get_first_node(nodes, value)
    #             node_index = 9*(node.row - 1) + node.column
    #             if not node.final:
    #                 self.declare_value(node_index, value)
    #                 result = True
    #     return result

    # def pick_all(self):
    #     result = False
    #     for structure in ('row', 'column', 'subgrid'):
    #         for index in range(1, 10):
    #             if self.try_pick(structure, index):
    #                 result = True
    #     return result

    def check(self, structure, index):
        # get indices will validate the data
        nodes = [ self.data[ind] for ind in get_indices(structure, index) ]
        bool_, changed_index = check_structure(nodes)
        if bool_:
            node = nodes[changed_index]
            self.checked['row'][node.row] = False
            self.checked['column'][node.column] = False
            self.checked['subgrid'][node.subgrid] = False
        else:
            self.checked[structure][index] = True
        return bool_

    def check_all(self):
        """
        Checks all unchecked rows in order, then columns, then subgrids

        Terminates the check once a structure is changed so we can clean
        """
        for structure in ('row', 'column', 'subgrid'):
            checked_dict = self.checked[structure]
            for index in range(1, 10):
                if not checked_dict[index]:
                    if self.check(structure, index):
                        return

        raise CheckFoundNoImprovement

    # def solve(self):
    #     while not self.solved:
    #         self.clean()
    #         if not self.solved:
    #             self.check_all()
    #     print self.pretty

    def solve(self):
        count = 1
        while not self.solved:
            count += 1
            self.clean()
            if not self.solved:
                try:
                    count += 1
                    self.check_all()
                except CheckFoundNoImprovement:
                    count += 1
                    self.pick_all()
                    # Will raise CheckFoundNoImprovement if fails
        # return self
        return count


    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, 'Sudoku')

def get_corner_sum(board):
    puzzle = Grid(board)
    puzzle.solve()
    return (100*puzzle.data[1].choices[0] + \
            10*puzzle.data[2].choices[0] + \
            puzzle.data[3].choices[0])

puzzles = get_data(96).split("\r\n")
# with open('../../problem_data/no096.txt','r') as fh:
#     puzzles = fh.read().split("\r\n")

# count = 0
# for puzzle in range(50):
#     if puzzle not in [5, 6, 41, 47]:
#         board = '\n'.join(puzzles[10*puzzle + 1:10*(puzzle + 1)])
#         count += get_corner_sum(board)
print 23138+176+143+384+861
