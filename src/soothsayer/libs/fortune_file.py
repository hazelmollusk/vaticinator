"""
provides an interface for fortune-style .dat files.

Contains:
    - FortuneFile
    - FortuneFileError
"""
from pathlib import Path
from logging import warn
import struct
from enum import Enum
from pprint import pp


class FortuneFileError(BaseException):
    pass


class FortuneFile:
    """Interface for fortune-style .dat files"""

    def __init__(self, filename=None):
        self.path = None
        self._offsets = []
        if filename is not None:
            self.load(filename)

    def load(self, filename):
        self.path = filename if isinstance(filename, Path) else Path(filename)
        if self.path.exists():
            try:
                with self.path.open('rb') as dat:
                    header = struct.unpack('>IIIIIcxxx', dat.read(24))
                    (self.version, self.length,
                     self.longest, self.shortest) = header[0:4]
                    self.offsets = [
                        struct.unpack('>I', dat.read(4))[0]
                        for i in range(self.length + 1)
                        ]
                    pp(self.offsets)
            except:     # noqa: E722
                warn(f'error reading fortune file "{filename}"!')
                raise FortuneFileError
        else:
            warn(f'fortune file "{filename}" not found!')
            raise FortuneFileError

    def get_random(self, options=None):
        pass
