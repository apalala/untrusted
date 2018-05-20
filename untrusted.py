#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import sys
import string
import hashlib
from getpass import getpass


__all__ = ['untrusted']

ALPHABET = string.digits + string.ascii_letters


def clip_copy(text):
    import pyperclip
    pyperclip.copy(text)


def i2text(value, width=1, alphabet=ALPHABET):
    n = len(alphabet)
    result = []
    while value != 0:
            c = value % n
            result.append(alphabet[c])
            value //= n
    np = width - len(result)
    if np <= 0:
        padding = []
    else:
        padding = [alphabet[0]] * np
    sresult = ''.join(padding + result)
    return sresult


def fingerprint(text):
    m = hashlib.sha512()
    m.update(text.encode('utf-8'))
    digest = m.hexdigest()
    m = hashlib.md5()
    m.update(digest.encode('utf-8'))
    m.update(text.encode('utf-8'))
    return m.hexdigest()


def untrusted(text, size=20):
    fp = fingerprint(text)
    ival = int(fp, 16)
    return i2text(ival)[:20]


def main(size=20):
    if len(sys.argv) >= 2:
        size = int(sys.argv[1])
    original = getpass('text?: ')
    pw = untrusted(original, size=size)
    print(pw)
    try:
        clip_copy(pw)
    except Exception:
        print('Could not copy to clipboard')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
