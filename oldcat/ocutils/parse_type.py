# -*- coding: utf-8 -*-


def none_map(func, lst, default=None):
    result = []
    for item in lst:
        try:
            v = func(item)
        except:
            v = default
        result.append(v)
    return result


def parse_int(*args):
    result = none_map(int, args)
    if len(args) == 1:
        return result[0]
    return result
