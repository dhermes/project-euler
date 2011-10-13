"""
The *sudoku* module offers three objects building a sudoku solver:

- the *Sudoku* class modelling the sudoku board and sudoku rules,

- the *stack_assumptions* generic backtracking algorithm. The function
  takes a list of generator functions as argument,

- the *make_generators* function returning a list of
  generator functions suited for manipulating a sudoku and compatible
  with the bactracking algorithm.

"""

import array
from contextlib import contextmanager

class Sudoku(object):
    """The *Sudoku* board class has the methods for reading the start
    state of a sudoku board, for representing a board. It also has the
    methods for setting and freeing a digit in a slot of the board,
    according to the rules of the sudoku game."""

    def __init__(self, problem):
        newarray = lambda: array.array('i', [0] * 9)
        # helper of initialisation of the data structures

        # Private bitfield presence sets
        self._lines   = newarray()  # Lines, columns and
        self._columns = newarray()  # square are bitfields of length 9.
        self._squares = newarray()  # When bit 3 is set in lines[5], 3
                                    # is present in the fifth line.

        self.board  = [newarray() for i in range(9)]
        # a 9x9 matrix of of ints between 1 and 9, an empty position
        # is represented by a false value.

        # Reading the problem
        k=0
        for i in range(9):
            for j in range(9):
                if int(problem[k]) != 0:
                    self.set(i, j, int(problem[k]))
                k+=1

    _one  = lambda self, val, index: val |   1 << index - 1
    _zero = lambda self, val, index: val & ~(1 << index - 1)
    _get  = lambda self, val, index: (val >>  index - 1) & 1
    # Bitfield manipulation

    def set(self, i, j, val):
        """Sets a new digit on the board in position i,j. This only
        updates the board *without* checking first if the rules of the
        sudo game are respected"""

        self.board[i][j]   = val

        # Not only update the board but also the lines, columns and
        # squares arrays
        self._lines[i]   = self._one(self._lines[i],   val)
        self._columns[j] = self._one(self._columns[j], val)
        self._squares[(j/3)*3+i/3] = self._one(
            self._squares[(j/3)*3+i/3], val)

    def free(self, i, j):
        """Frees the slot in position i,j"""

        # The value to be removed from the lines, columns and square
        # presence set is found in the *board* member attribute
        val, self.board[i][j] = self.board[i][j], 0

        # Also update the line, column and square presence sets.
        self._lines[i]   = self._zero(self._lines[i],   val)
        self._columns[j] = self._zero(self._columns[j], val)
        self._squares[(j/3)*3+i/3] = self._zero(
            self._squares[(j/3)*3+i/3], val)

    @contextmanager
    def attempt(self, col, row, candidate):
       """A context manager which sets the value of the board at
        position: *col*, *line* on entering the context and which
        frees the position on exiting the context."""

       self.set(col, row, candidate)
       yield
       self.free(col, row)

    def candidates(self, col, row):

        """Returns the list of possible values for the slot specified by
        the arguments, according to the current state of the sudoku
        board and according to the rules of the sudoku game.

        The sudoku rules states that the candidates are the numbers
        which are not present neither in the column *col*, neither in
        the line *row*, neither in the square identified by *col* and
        *row*."""

        return filter(
            lambda val: all( not self._get(bf, val) for bf in (
                    self._lines[col],
                    self._columns[row],
                    self._squares[(row/3)*3+col/3])),
            range(1,10))

    def __str__(self):

        # The matrix is transformed into a list of characters
        l = [str(self.board[i][j]) if self.board[i][j] else ' '
                    for i in range(9) for j in range(9)]

        l = ['\n   '+e if i%9 ==0 else e for (i,e) in enumerate(l)] # 1.
        l = ['  '+e    if i%3 ==0 else e for (i,e) in enumerate(l)] # 2.
        l = ['\n'+e    if i%27==0 else e for (i,e) in enumerate(l)] # 3.

        # 1.   New lines every 9 elements
        # 2,3. Squares are represented by extra spaces and another
        #      newline

        return ' '.join(l)


def make_generators(sudoku):

    """Returns a list of candidate generators for use with the
    backtrack algorithm stack_assumptions.  The sudoku argument must
    provide two functions: *candidates(i,j)*, and *attempt(col, row,
    candidate)* and a member attribute called *board*, which is a 9x9
    matrix.

    There are as many generator functions than there are slots on the
    sudoku board, they are stored in a list. Each generator function
    is specific to a slot: it actually *contains* the coordinates of
    the slot, like a closure.

    When called for the first time, the generator computes the list of
    candidate numbers for the slot, according to the current sudoku
    board. The list of candidates depends on the state of the board at
    the time the generator is called for the first time."""

    generators = []
    for i in range(9):
        for j in range(9):
            def gen_func(col=i,row=j):
                if sudoku.board[col][row] != 0:
                    yield
                else:
                    for candidate in sudoku.candidates(col, row):
                        with sudoku.attempt(col, row, candidate):
                            yield
            generators.append(gen_func)
    return generators


def stack_assumptions(generators, i=0):

    """Takes a list of generators. This list is assumed to manipulate
    a shared representation of the problem. When this algorithm
    yields, a solution has been found and can be printed.

    The algorithm works by calling the generator at the *nth* position
    of the list, and pulls the *next()* method on the iterator
    returned:

    #. either *next()* returns, in which case, the algorithm
       instantiates the generator from position **n+1** of the input
       list function and tries to pull its *next()* method,

    #. or the method raises a StopIteration, in which case, the
       algorithm trigger *next()* on the generator at position **n-1**,

    This algorithm yields whenever every generator of the list has
    yielded, at this point, every position of the board is filled with
    a digit according to the sudoku rules: a solution has been
    reached and the board can be printed.

    When a generator has yielded, this means that a suitable candidate
    could be found and was set in the board's slot and that an
    assumption can be tried on the next slot, with generator i+1.

    When a generator raises a StopIteration, then a dead-end was
    met. A wrong assumption must have been taken somewhere along the
    stack of the previous recursion: the algorithm backtracks at the
    previous recursion, another assumption can be attempted."""

    if i >= len(generators):
        yield
    else:
        for _ in generators[i]():
            for _ in stack_assumptions(generators, i+1):
                yield
