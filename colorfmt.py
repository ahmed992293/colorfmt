# -*- coding: utf-8 -*-
"""
    colorfmt
    ~~~~~~~~

    String formatter providing ANSI escape codes for text terminals.

    :copyright: (c) 2011 by Daniel Kertesz
    :license: BSD


    Example usage::

        from colorfmt import colorize
        print colorize("{green}{bold}Hello World!{reset}")
"""

import string

ANSI_CODES = {
    # Foreground colors
    'black': 30,
    'red': 31,
    'green': 32,
    'yellow': 33,
    'blue': 34,
    'magenta': 35,
    'cyan': 36,
    'white': 37,
    'default': 39,

    # Background colors
    'bblack': 40,
    'bred': 41,
    'bgreen': 42,
    'byellow': 43,
    'bblue': 44,
    'bmagenta': 45,
    'bcyan': 46,
    'bwhite': 47,
    'bdefault': 49,

    # reset colors and effects
    'reset': 0,

    # Effects ON
    'bold': 1,
    'b': 1,
    'italic': 3,
    'i': 3,
    'underline': 4,
    'blink': 5,
    'u': 4,
    'inverse': 7,
    'inv': 7,
    'strikethrough': 9,
    'st': 9,

    # Effects OFF
    'bold_off': 22,
    '/b': 22,
    'italic_off': 23,
    '/i': 23,
    'underline_off': 24,
    '/u': 24,
    'blink_off': 25,
    'inverse_off': 27,
    '/inv': 27,
    'strikethrough_off': 29,
    '/st': 29,
}


class ColorFormatter(string.Formatter):
    """
    This class do the magic.
    """

    def get_value(self, key, args, kwargs):
        if key in ANSI_CODES:
            return '\033[%dm' % ANSI_CODES[key]
        else:
            return super(ColorFormatter, self).get_value(key, args, kwargs)
cf = ColorFormatter()


def colorize(*args, **kwargs):
    """
    Simple helper function.

    >>> assert colorize("{green}Hello {bold}World!{reset}") == '\x1b[32mHello \x1b[1mWorld!\x1b[0m'
    >>> 
    """
    return cf.format(*args, **kwargs)

def _test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    _test()
