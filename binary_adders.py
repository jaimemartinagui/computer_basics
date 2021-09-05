"""
    Module with binary adders.
    A general adder for two binary numbers is constructed from logic gates AND, OR, XOR.
"""

from basic_logic_gates import and_
from compound_logic_gates import or_, xor_

def general_adder(a, b):
    """
    General binary adder.
    Returns the sum (string) of a and b.

    Parameters:
    - a and b must be strings of binary elements (0, 1) --> e.g. '0111010'.
    """

    if not len(a) == len(b):
        zeros_to_add = '0' * abs(len(a) - len(b))
        a, b = (a, zeros_to_add + b) if len(a) > len(b) else (zeros_to_add + a, b)

    carry = False
    sum_  = ''

    for bit_a, bit_b in reversed(list(zip(a, b))):
        carry, sum_bit = adder_2_bits(int(bit_a), int(bit_b), carry)
        sum_ = str(sum_bit) + sum_

    if carry:
        sum_ = str(int(carry)) + sum_

    return sum_

def adder_4_bits(a, b, carry_input):
    """
    4 bits binary adder.
    Returns the 4 bits sum (string) and the carry output (binary element).
    It overflows when the sum is greater than 4 bits (indicated by the carry output).

    Parameters:
    - a and b must be strings of 4 binary elements (0, 1) --> e.g. '0110'.
    - carry_input must be a binary element (0, 1, True, False).
    """

    a_1, a_2, a_3, a_4 = map(int, a)
    b_1, b_2, b_3, b_4 = map(int, b)

    carry_1, sum_4 = adder_2_bits(a_4, b_4, carry_input)
    carry_2, sum_3 = adder_2_bits(a_3, b_3, carry_1)
    carry_3, sum_2 = adder_2_bits(a_2, b_2, carry_2)
    carry,   sum_1 = adder_2_bits(a_1, b_1, carry_3)

    sum_ = str(sum_1) + str(sum_2) + str(sum_3) + str(sum_4)

    return carry, sum_

def adder_2_bits(a, b, carry_input):
    """2 bits binary adder."""

    carry_aux, sum_aux = adder(a, b)

    sum_  = xor_(sum_aux, carry_input)
    carry = or_(and_(sum_aux, carry_input), carry_aux)

    return carry, sum_

def adder(a, b):
    """Binary adder."""

    sum_   = xor_(a, b)
    carry = and_(a, b)

    return carry, sum_
