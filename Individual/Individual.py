#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Вариант – №3. Известны оценки по геометрии каждого из 24 учеников класса.
Сколько учеников имеет по геометрии оценку «5»?
Условный оператор не использовать.
"""

import sys

if __name__ == '__main__':
    C = tuple(map(int, input().split()))

    if len(C) != 24:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    print(C.count(5))
    