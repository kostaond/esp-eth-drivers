#!/usr/bin/env python
# SPDX-FileCopyrightText: 2025 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0
"""
Annotate release tag
"""
import os
import pathlib
import subprocess
import sys

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
CZ_CURRENT_TAG = os.environ['CZ_POST_CURRENT_TAG_VERSION']


def update_tag(component:str) -> None:
    """Annotate release tag with release notes"""
    release_notes_path = str(PROJECT_ROOT / component / '_release_notes.txt')
    with open(release_notes_path, encoding='utf-8') as fr:
        release_notes = fr.read()
    subprocess.check_call(['git', 'tag', '-a', CZ_CURRENT_TAG, '-m', release_notes, '-f' ],
                          cwd=PROJECT_ROOT)
    os.remove(release_notes_path)


if __name__ == '__main__':
    args = sys.argv[1:]
    update_tag(args[0])
