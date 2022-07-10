#!/usr/bin/env python3
import datetime
import subprocess
import time

import cli
import constants


def check_if_runnable(start, end = None):
    return start <= constants.NOW and (constants.NOW <= end if end else True)


def main():
    args = cli.PARSER.parse_args()
    cannot_run = not check_if_runnable(*args.times)
    
    if cannot_run and not args.wait:
        exit(1)
    
    if cannot_run and args.wait:
        next = args.start + datetime.timedelta(days=1)
        delta = next - constants.NOW
        
        time.sleep(delta.seconds)
    
    return_code = subprocess.call(args.command)
    
    exit(return_code)


if __name__ == "__main__":
    main()