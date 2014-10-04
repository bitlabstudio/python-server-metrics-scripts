"""Collects disk usage for the given folder into InfluxDB."""
import sys

from server_metrics.hard_disk import get_disk_usage

import settings
from utils import write_point


def main(argv):
    folder = argv[0]
    total = get_disk_usage(folder)
    series_name = 'default.{0}.disk.usage'.format(settings.SERVER_NAME)
    write_point(series_name, total)


if __name__ == "__main__":
    main(sys.argv[1:])
