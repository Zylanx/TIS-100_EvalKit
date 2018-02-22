__author__ = 'Zylanx'

from ._generate_enum import generateEnum

__all__ = []

enumItems = ["NIL", "ACC", "COMM_PORT", "JMP_DEST", "JRO_OFFSET", "CONST"]

generateEnum()