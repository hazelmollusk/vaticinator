from enum import Flag, auto, EnumMeta


# dunno why this isn't available by default somehow?
class DefaultEnumMeta(EnumMeta):
    def __call__(cls, value=None, *args, **kwargs):
        if value is None:
            # Assume the first enum member is default
            return next(iter(cls))
        return super().__call__(value, *args, **kwargs)


class FortuneOptions(Flag, metaclass=DefaultEnumMeta):
    # may also contain .pattern, .length, .wait
    ALL = auto()
    EQUAL_SIZE = auto()
    LONG = auto()
    OFF = auto()
    SHORT = auto()
    IGNORE_CASE = auto()

    # cli-specific options
    SHOW_FILE = auto()
    LIST_FILES = auto()
