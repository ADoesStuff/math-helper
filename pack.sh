#!/usr/bin/env bash
nuitka --onefile src/main.py
mv main.bin math-helper-linux.bin
mv math-helper-linux.bin out