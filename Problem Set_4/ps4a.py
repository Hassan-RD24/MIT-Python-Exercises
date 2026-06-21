# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # base case: a sequence with only one character has just one permutation
    if len(sequence) == 1:
        return [sequence]

    # recursive case: get all permutations of everything but the first char
    first_char = sequence[0]
    rest_permutations = get_permutations(sequence[1:])

    all_permutations = []
    # insert first_char into every possible position of each smaller permutation
    for permutation in rest_permutations:
        for position in range(len(permutation) + 1):
            new_permutation = permutation[:position] + first_char + permutation[position:]
            all_permutations.append(new_permutation)

    return all_permutations

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a
    # sequence of length n)

    # Test Case 1
    test_input_1 = 'a'
    print('Input:', test_input_1)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(test_input_1))

    # Test Case 2
    test_input_2 = 'ab'
    print('Input:', test_input_2)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(test_input_2))

    # Test Case 3
    test_input_3 = 'xyz'
    print('Input:', test_input_3)
    print('Expected Output:', ['xyz', 'yxz', 'yzx', 'xzy', 'zxy', 'zyx'])
    print('Actual Output:', get_permutations(test_input_3))