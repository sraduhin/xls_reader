#!/usr/bin/env python3
import argparse
import os
import prompt
from app.parser import parse
from app.queries import get_all, get_total


def main():
    parser = argparse.ArgumentParser(
        description='XLS Parser'
    )
    parser.add_argument('path', help="path to file")
    args = parser.parse_args()
    path = os.path.join(os.getcwd(), args.path)
    parse(path)
    get_all()

    # get period for calc Total
    start = prompt.string('Enter startdate kind "YYYY-mm-dd": ')
    end = prompt.string('Enter enddate kind "YYYY-mm-dd": ')
    get_total(start, end)


if __name__ == '__main__':
    main()
