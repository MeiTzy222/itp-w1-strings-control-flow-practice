# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
O  |  O  |  X
--------------
X  |  X  |  O
--------------
O  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    a = "X  |  O  |  X"
    b = "--------------"
    c = "O  |  X  |  O"
    # d = "--------------\n"
    e = "O  |  O  |  X"
    #print(board.format(first_row,second_row,third_row) 
    print(a +\
    b +\
    c +\
    b +\
    e)
    
    """
    z = "--------------\n"
    y = "  |  "
    a = str(y.join(first_row))
    b = str(y.join(second_row))
    c = str(y.join(third_row))
    k = (a +\
    z +\
    b +\
    z +\
    c)
        
    print(k)
    """
    
    # z = "  |  "
    # print z.join(first_row)
    # print "--------------"
    # print z.join(second_row)
    # print "--------------"
    # print z.join(third_row)


def test_format_board():
    """
    This is the board used in this test:

        X  |  O  |  X
        --------------
        O  |  X  |  O
        --------------
        O  |  O  |  X

    """
    first_row = 'XOX'
    second_row = 'OXO'
    third_row = 'OOX'
    expected_board = """
X  |  O  |  X
--------------
O  |  X  |  O
--------------
O  |  O  |  X
"""
    board = format_tic_tac_toe_board(first_row, second_row, third_row)

    assert board == expected_board
    

first_row = 'XOX'
second_row = 'OXO'
third_row = 'OOX'