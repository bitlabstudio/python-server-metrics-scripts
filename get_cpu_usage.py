"""Collects memory usage for the given user into InfluxDB."""
import sys

from server_metrics.cpu import get_cpu_usage

import settings
from utils import write_points


def main(argv):
    user = None
    if argv:
        user = argv[0]
    total, largest_process, largest_process_name = get_cpu_usage(user)
    total = float(total)
    largest_process = float(largest_process)
    series_name = 'default.{0}.cpu.usage'.format(settings.SERVER_NAME)
    data = [{
        'measurement': series_name,
        'columns': ['value', 'largest_process', 'largest_process_name', ],
        'points': [[total, largest_process, largest_process_name]], }]
    write_points(data)


if __name__ == "__main__":
    main(sys.argv[1:])
