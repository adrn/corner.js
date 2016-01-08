# coding: utf-8

from __future__ import division, print_function

__author__ = "adrn <adrn@astro.columbia.edu>"

# Standard library
import sys

# Project
from app import app

if __name__ == "__main__":
    from argparse import ArgumentParser

    # Define parser object
    parser = ArgumentParser(description="")
    parser.add_argument("--debug", action="store_true", dest="debug",
                        default=False, help="Run flask with debugging.")
    parser.add_argument("--extern", action="store_true", dest="extern",
                        default=False, help="Run on an external server")

    args = parser.parse_args()

    if args.extern:
        host = "0.0.0.0"
    else:
        host = "127.0.0.1"

    app.run(host=host, debug=args.debug)
