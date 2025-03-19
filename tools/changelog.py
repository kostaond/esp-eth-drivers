#!/usr/bin/env python
# SPDX-FileCopyrightText: 2024-2025 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0
"""
Update CHANGELOG file
"""
import os
import pathlib
import re
import subprocess
import sys
from typing import Dict
from typing import List

RELEASE_TAG_BASE_URL = 'https://github.com/kostaond/esp-eth-drivers/releases/tag' # TODO change to espressif
PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
CZ_OLD_TAG = os.environ['CZ_PRE_CURRENT_TAG_VERSION']
CZ_NEW_TAG = os.environ['CZ_PRE_NEW_TAG_VERSION']
CZ_INITIAL = os.environ['CZ_PRE_IS_INITIAL']

CHANGELOG_SECTIONS = {
    'feat': 'Features',
    'fix': 'Bug Fixes',
    'breaking': 'Breaking Changes',
    'BREAKING CHANGE': 'Breaking Changes',
    'update': 'Updates',
    'change': 'Updates',
    'remove': 'Updates',
    'refactor': 'Updates',
    'revert': 'Updates',
}
CHANGELOG_TITLES = ['Features', 'Bug Fixes', 'Updates', 'Breaking Changes']
assert all(v in CHANGELOG_TITLES for v in CHANGELOG_SECTIONS.values())
CHANGELOG_PATTERN = re.compile(rf'({"|".join(CHANGELOG_SECTIONS.keys())})(?:\(([^)]+)\))?:\s*([^\n]+)')
COMMIT_PATTERN = re.compile(r'^[0-9a-f]{8}')


def check_repo() -> None:
    """Check current ref tag in repository"""
    subprocess.check_call(
        ['git', 'fetch', '--prune', '--prune-tags', '--force'],
        cwd=PROJECT_ROOT,
    )

    ref_tags = subprocess.check_output(
        ['git', 'show-ref', '--tags'],
        cwd=PROJECT_ROOT,
    ).decode()

     # Check old_ref in repository but only if not initial bump
    if CZ_INITIAL != 'True' and CZ_OLD_TAG not in ref_tags:
        raise RuntimeError(f'Previous reference ({CZ_OLD_TAG}) was not found in repo!')

    # Check if new_ref in repository
    if CZ_NEW_TAG in ref_tags:
        raise RuntimeError(f'New reference ({CZ_NEW_TAG}) already exists in repo!')


def update_changelog(component:str, release_notes:str) -> None:
    """Update Changelog file from git history"""
    changelog_path = str(PROJECT_ROOT / component / 'CHANGELOG.md')
    # Update changelog file
    changelog_data: List[str]
    try:
        with open(changelog_path, encoding='utf-8') as fr:
            changelog_data = fr.readlines()
    except FileNotFoundError:
        changelog_data = [f'# Changelog - {component}\n\n', '']
    changelog_data.insert(2, ''.join(release_notes))
    with open(changelog_path, 'w', encoding='utf-8') as fw:
        fw.write(''.join(changelog_data))
    # Stage updated changelog to be committed along with version bump
    subprocess.check_call(['git', 'add', changelog_path],
                          cwd=PROJECT_ROOT)


def create_release_notes(component:str, release_notes:str) -> None:
    """Format release notes"""
    release_notes = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', release_notes)
    release_notes = re.sub(r'\#\#[\#\s]*(.+)', r'\1', release_notes)
    release_notes = re.sub(r'\n\n', '\n', release_notes)
    # store release notes to temp file to be used later in the process
    with open(str(PROJECT_ROOT / component / '_release_notes.txt'), 'w', encoding='utf-8') as fw:
        fw.write(release_notes)


def get_commit_changes(component:str) -> str:
    """Get and markdown format git history"""
    # Update ChangeLog
    if CZ_INITIAL == 'True':
        git_logs = subprocess.check_output(
            # ignore merge commits
            ['git', 'log', '--no-merges', f'{component}'],
            cwd=PROJECT_ROOT,
        ).decode()
    else:
        git_logs = subprocess.check_output(
            # ignore merge commits
            ['git', 'log', '--no-merges', f'{CZ_OLD_TAG}..HEAD', f'{component}'],
            cwd=PROJECT_ROOT,
        ).decode()

    changelogs: Dict[str, List[str]] = {k: [] for k in CHANGELOG_TITLES[::-1]}
    # Get possible changelogs from title and notes.
    for commit_log in git_logs.split('commit ')[1:]:
        _commit_match = COMMIT_PATTERN.match(commit_log)
        assert _commit_match
        commit = _commit_match.group(0)
        for match in CHANGELOG_PATTERN.finditer(commit_log):
            if match.group(2) == component:
                _changelog = f'- {match.group(2)}: {match.group(3)} ([{commit}]({RELEASE_TAG_BASE_URL}{commit}))'
            else:
                # TODO commit is not related to the component, expect user action??
                _changelog = f'- {match.group(3)} ([{commit}]({RELEASE_TAG_BASE_URL}{commit}))'
            changelogs[CHANGELOG_SECTIONS[match.group(1)]].append(_changelog)

    changed = False
    formatted_changes: List[str] = ['']
    for key, values in changelogs.items():
        if not values:
            continue
        formatted_changes.insert(0, f'### {key}\n\n' + '\n'.join(values) + '\n\n')
        changed = True
    if changed:
        formatted_changes.insert(0, f'## [{CZ_NEW_TAG}]({RELEASE_TAG_BASE_URL}/{CZ_NEW_TAG})\n\n')
    else:
        raise RuntimeError('No changes found')
    return ''.join(formatted_changes)


if __name__ == '__main__':
    check_repo()
    args = sys.argv[1:]
    scope = args[0]
    CHANGES = get_commit_changes(scope)
    update_changelog(scope, CHANGES)
    create_release_notes(scope, CHANGES)
