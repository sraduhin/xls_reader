#!/usr/bin/env python3
import argparse
import os
from app.parser import parse
from app.queries import get_all


def main():
    parser = argparse.ArgumentParser(
        description='XLS Parser'
    )
    parser.add_argument('path', help="path to file")
    args = parser.parse_args()
    path = os.path.join(os.getcwd(), args.path)
    parse(path)
    get_all()



if __name__ == '__main__':
    main()