#!/usr/bin/env python3
import argparse
import contextlib
import datetime

import constants

VALID_TIME_FORMATS = [
    "%H:%M",
    "%H:%M:%S"
]


def time_type(arg):
    parsed = []
    times_as_text = arg.split("-")
    
    for time in times_as_text:
        for format in VALID_TIME_FORMATS:
            with contextlib.suppress(ValueError):
                converted = datetime.datetime.strptime(time, format)
                converted_date = constants.NOW.replace(hour=converted.hour, minute=converted.minute, second=converted.second, microsecond=0)
                
                parsed.append(converted_date)
    
    if len(parsed) == len(times_as_text):
        return parsed

    formats = ", ".join(VALID_TIME_FORMATS)
    
    raise TypeError(f"{arg} does not match format, valid formats are: {formats}")


PARSER = argparse.ArgumentParser(prog="schdexec")
PARSER.add_argument("--time", dest="times", metavar="times", type=time_type)
PARSER.add_argument("--wait", action="store_true")
PARSER.add_argument("command", metavar="command", nargs="*")
