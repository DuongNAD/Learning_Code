#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"
python3 "$DIR/pick_today.py"
echo ""
read -n 1 -s -r -p "Press any key to close..."
