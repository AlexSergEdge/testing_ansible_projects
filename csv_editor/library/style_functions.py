#coding=utf-8
from __future__ import print_function
from openpyxl import Workbook, cell
from openpyxl import load_workbook
from copy import copy
from openpyxl.styles import Font, PatternFill, Border, Protection, Alignment, Side


class StyleClass:
    # Функция используется в copy_header для того, что бы скоприровать полный стиль ячейки
    def copyStyle(self, toStyle, fromStyle):
        toStyle.font = copy(fromStyle.font)
        toStyle.fill = copy(fromStyle.fill)
        toStyle.border = copy(fromStyle.border)
        toStyle.alignment = copy(fromStyle.alignment)
        toStyle.number_format = copy(fromStyle.number_format)
        toStyle.protection = copy(fromStyle.protection)
    
    # Функция сравнения стилей двух ячеек
    def areStylesEqual(self, toStyle, fromStyle):
        return (toStyle.font.name == fromStyle.font.name
                and toStyle.font.size == fromStyle.font.size
                and toStyle.font.bold == fromStyle.font.bold
                and toStyle.font.italic == fromStyle.font.italic
                and toStyle.font.vertAlign == fromStyle.font.vertAlign
                and toStyle.font.underline == fromStyle.font.underline
                and toStyle.font.strike == fromStyle.font.strike
                and toStyle.font.color == fromStyle.font.color
                
                and toStyle.fill.fill_type == fromStyle.fill.fill_type
                and toStyle.fill.start_color == fromStyle.fill.start_color
                and toStyle.fill.end_color == fromStyle.fill.end_color
                
                and toStyle.border.left.border_style == fromStyle.border.left.border_style
                and toStyle.border.left.color == fromStyle.border.left.color
                and toStyle.border.right.border_style == fromStyle.border.right.border_style
                and toStyle.border.right.color == fromStyle.border.right.color
                and toStyle.border.top.border_style == fromStyle.border.top.border_style
                and toStyle.border.top.color == fromStyle.border.top.color
                and toStyle.border.bottom.border_style == fromStyle.border.bottom.border_style
                and toStyle.border.bottom.color == fromStyle.border.bottom.color
                and toStyle.border.diagonal.border_style == fromStyle.border.diagonal.border_style
                and toStyle.border.diagonal.color == fromStyle.border.diagonal.color
                and toStyle.border.diagonal_direction == fromStyle.border.diagonal_direction
                and toStyle.border.outline == fromStyle.border.outline
                             
                and toStyle.alignment.horizontal == fromStyle.alignment.horizontal
                and toStyle.alignment.vertical == fromStyle.alignment.vertical
                and toStyle.alignment.text_rotation == fromStyle.alignment.text_rotation
                and toStyle.alignment.wrap_text == fromStyle.alignment.wrap_text
                and toStyle.alignment.shrink_to_fit == fromStyle.alignment.shrink_to_fit
                and toStyle.alignment.indent == fromStyle.alignment.indent
                
                and toStyle.number_format == fromStyle.number_format
                
                and toStyle.protection.locked == fromStyle.protection.locked
                and toStyle.protection.hidden == fromStyle.protection.hidden)
    
if __name__ == '__main__':
    # любые действия при вызове упоминать здесь (пока пусто)
    print('Imported style_functions')