#!/usr/bin/env python3
from .vaticinator import Vaticinator


def main(*args, **kwargs):
    return Vaticinator(*args, **kwargs).main()


if __name__ == '__main__':
    exit(main())
