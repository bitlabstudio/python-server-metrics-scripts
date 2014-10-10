"""Utilities for working with InfluxDB."""
import settings

from influxdb import client as influxdb


def get_db():
    """Returns an ``InfluxDBClient`` instance based on the settings."""
    return influxdb.InfluxDBClient(
        settings.INFLUXDB_HOST,
        settings.INFLUXDB_PORT,
        settings.INFLUXDB_USER,
        settings.INFLUXDB_PASSWORD,
        settings.INFLUXDB_DATABASE,
    )


def write_point(series_name, value, column_name=None):
    """
    Writes a single point with a single column to a series.

    :param series_name: String representing the series name.
    :param value: The value that should be saved.
    :param column_name: String representing the column name for the value.
      If ``None``, the name will be set to ``value``.

    """
    if column_name is None:
        column_name = 'value'

    data = [{
        'name': series_name,
        'columns': [column_name, ],
        'points': [[value]], }]
    write_points(data)


def write_points(data):
    """
    Wrapper for the ``write_points`` function of ``InfluxDBClient``.

    Conveniently gets an ``InfluxDBClient`` instance based on the settings.

    :param data: The data dict that ``InfluxDBClient.write_points`` expects.

    """
    db = get_db()
    print(data)
    db.write_points(data)
