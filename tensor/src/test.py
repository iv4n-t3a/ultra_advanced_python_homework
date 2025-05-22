from matrix import Matrix


def test_invalid_dimension():
    try:
        Matrix((1, 2), [1, 2, 3])
    except ValueError:
        return

    # this line shall not be reached as exception handler exit function
    assert (False)


test_matrix = Matrix((5, 3), [
    1, 2, 3, 4, 5,
    5, 4, 3, 2, 1,
    2, 3, 4, 5, 2,
])


def test_conv_rc2i():
    assert test_matrix.conv_rc2i(2, 2) == 12
    assert test_matrix.conv_rc2i(0, 2) == 2


def test_conv_i2rc():
    assert test_matrix.conv_i2rc(12) == (2, 2)
    assert test_matrix.conv_i2rc(2) == (0, 2)


def test_get_single_item():
    assert test_matrix[1, 1] == 4


def test_get_single_line():
    assert test_matrix[1] == [5, 4, 3, 2, 1]


def test_get_single_line_with_negative_index():
    assert test_matrix[-2] == [5, 4, 3, 2, 1]


def test_get_lines_slice():
    assert test_matrix[0:2] == Matrix((5, 2),
                                      [1, 2, 3, 4, 5,
                                       5, 4, 3, 2, 1])
    assert test_matrix[:2] == Matrix((5, 2),
                                      [1, 2, 3, 4, 5,
                                       5, 4, 3, 2, 1])
    assert test_matrix[1:] == Matrix((5, 1),
                                      [1, 2, 3, 4, 5])
    print(test_matrix[1:])
