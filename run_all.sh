#!/bin/bash
path=input
files=$(ls $path)

python main.py --input $files --output output