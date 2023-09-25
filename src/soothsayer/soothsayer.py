#!/usr/bin/env python3
"""
DOCSTRING for first public console interface.

USAGE:
    soothsayer [options]
"""
import sys
from argparse import ArgumentParser
# from soothsayer.libs import __version__
from soothsayer.libs.fortune_file import FortuneFile
from soothsayer.libs.fortune_options import FortuneOptions
from pprint import pp


class Soothsayer:
    def __init__(self, args=None):
        self.args = args

    def main(self):
        self.options = FortuneOptions()
        self.files = {}
        args = self.args or sys.argv[1:]
        cmd_opts = self.process_args(args)
        pp(cmd_opts)
        self.options = self.process_opts(cmd_opts)

    def process_args(self, args=None):
        parser = ArgumentParser()
        parser.add_argument('-a', '--all', action='store_true',
                            help='Choose from all lists of maxims, both offensive and not.')
        parser.add_argument('-c', '--show-file', action='store_true',
                            help='Show the cookie file from which the fortune came.')
        parser.add_argument('-e', '--equal', action='store_true',
                            help='Consider all fortune files to be of equal size.')
        parser.add_argument('-f', '--files', action='store_true',
                            help='Print out the list of files which would be searched; don’t print a fortune.')
        parser.add_argument('-l', '--long', action='store_true',
                            help='Long dictums only.')
        parser.add_argument('-m', '--match', type=str,
                            help='Print out all fortunes which match the basic regular expression pattern.')
        parser.add_argument('-n', '--short_max', default=160, type=int,
                            help='Set the longest fortune length considered short.')
        parser.add_argument('-o', '--off', action='store_true',
                            help='Choose only from potentially offensive aphorisms.')
        parser.add_argument('-s', '--short', action='store_true',
                            help='Short apothegms only.')
        parser.add_argument('-i', '--ignore-case', action='store_true',
                            help='Ignore case for -m patterns.')
        parser.add_argument('-w', '--wait', action='store_true',
                            help='Wait before termination for an amount of time calculated from the number of characters in the message.')
        parser.add_argument('-u', action='store_true',
                            help='Don’t translate UTF-8 fortunes to the locale when searching or translating.')
        parser.add_argument('params', metavar='arg', nargs='*',
                            help='[#% file/directory/all]')
        return parser.parse_args(args)
        
    def process_opts(self, opts):
        pass


def main():
    return Soothsayer().main()


if __name__ == '__main__':
    main()
