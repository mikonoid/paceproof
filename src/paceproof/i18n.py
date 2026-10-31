"""Minimal i18n hook: all user-facing strings go through `_()` so translations can be added later."""


def gettext(message: str) -> str:
    return message


_ = gettext
