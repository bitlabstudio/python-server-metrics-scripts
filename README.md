# Python Server Metrics Scripts

This repository contains a few Python scripts that make use of
[python-server-metrics](https://github.com/bitmazk/python-server-metrics). The
data will be saved in an [InfluxDB](http://influxdb.com/) instance.

# Usage

Clone this repository somewhere on your server:

```
cd /opt/
git clone https://github.com/bitmazk/python-server-metrics-scripts
cd python-server-metrics-scripts
```

Now prepare your ``settings.py``:

```
cp settings.py.sample settings.py
vim settings.py
```

Finally make sure to have dependencies installed. On a Ubuntu server, you need
something like this:

```
sudo apt-get install python-dev, python-pip
sudo pip install -r requirements.txt
```

NOTE: You might want to create a virtual environment for this repository.

Now you should be able to testrun the scripts and results should show up in
your InfluxDB:

```
python get_memory_usage.py
python get_disk_usage.py $HOME
python get_cpu_usage.py
```

Finally you will want to schedule the metrics collection via crontab:

```
* * * * * python /opt/python-server-metrics-scripts/get_memory_usage.py influxdb > /opt/python-server-metrics-scripts/logs/get_memory_usage.log 2&1
* * * * * python /opt/python-server-metrics-scripts/get_cpu_usage.py influxdb > /opt/python-server-metrics-scripts/logs/get_cpu_usage.log 2&1
* 0 */1 * * * python /opt/python-server-metrics-scripts/get_disk_usage.py /opt/influxdb/shared/data/ > /opt/python-server-metrics-scripts/logs/get_disk_usage.log 2&1
```

NOTE: For some reason ``get_memory_usage.py`` returns 0 when called without
a username from crontab. It works when called from the command line. If someone
figures out how to fix this, please send a pull request :)
