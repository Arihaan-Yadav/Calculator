#!/bin/sh
script_dir=$(CDPATH= cd -- "$(dirname "$0")" && pwd) || exit 1
cd "$script_dir/.." || exit 1
exec python3 main.py
