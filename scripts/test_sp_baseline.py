#!/usr/bin/env python3
"""The English baseline pages share one Saving Planets snapshot.

Fail if About, Contact, Ways to Help, and Search grow different menus,
title banners, or help controls. The search worker is out of this check.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sp_baseline

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    if not sp_baseline.GAPS:
        raise SystemExit("baseline gaps must stay listed")
    sp_baseline.check(ROOT)
    if sp_baseline.TITLE != "four-stills":
        raise SystemExit("title treatment must stay recorded as four stills")
    print("baseline ok", sp_baseline.COMMIT, "frozen", sp_baseline.FROZEN, "title", sp_baseline.TITLE)


if __name__ == "__main__":
    main()
