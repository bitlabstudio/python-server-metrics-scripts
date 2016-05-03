"""Collects memory usage for the given user into InfluxDB."""
import sys

from server_metrics.memory import get_memory_usage

import settings
from utils import write_points


def main(argv):
    user = None
    if argv:
        user = argv[0]
    total, largest_process, largest_process_name = get_memory_usage(user)
    series_name = 'default.{0}.memory.usage'.format(settings.SERVER_NAME)
    data = [{
        'measurement': series_name,
        'columns': ['value', 'largest_process', 'largest_process_name', ],
        'points': [[total, largest_process, largest_process_name]], }]
    write_points(data)


if __name__ == "__main__":
    main(sys.argv[1:])
