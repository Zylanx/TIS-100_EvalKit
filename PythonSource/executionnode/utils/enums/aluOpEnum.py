__author__ = 'Zylanx'

from ._generate_enum import generateEnum

__all__ = []

# TODO: PASS_ACC could just be part of ADD as long as it the other input is NIL
enumItems = ["ADD", "SUB", "NEG", "PASS_ACC", "PASS_OTHER"]

generateEnum()