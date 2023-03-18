#!/bin/sh
trap ":" INT
while true
do
    python3 game-of-life-CLI.py
done
