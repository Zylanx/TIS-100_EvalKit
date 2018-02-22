__author__ = 'Zylanx'

from ._generate_enum import generateEnum

__all__ = []

enumItems = ["ADD", "MOV", "SUB", "NEG", "SAV", "SWP", "JMP", "JRO"]

generateEnum()