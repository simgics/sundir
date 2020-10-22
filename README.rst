sundir
======

*sundir* is an application that displays the direction of the sun at specified latitude, longitude, altitude and time in azimuth and elevation.

Installation and usage
----------------------

Installation
^^^^^^^^^^^^

``pip install sundir``

Usage
^^^^^

::

    sundir {Latitude} {Longitude}
    
        Latitude, Longitude: {degrees}d{minutes}m{seconds}s or {degrees}d

Execution example
~~~~~~~~~~~~~~~~~

::

    sundir 35d37m0s 139d47m3s --date "2020/09/18 13:00:00" --repeat 10
    
    latitude    : 35d37m0s
    longitude   : 139d47m3s
    altitude(m) : 0.0
    
             Date            AZ(deg)   EL(deg)
    2020/09/18 13:00:00     214.9717   50.7684
    2020/09/18 13:00:10     215.0299   50.7489
    2020/09/18 13:00:20     215.0881   50.7294
    2020/09/18 13:00:30     215.1462   50.7099
    2020/09/18 13:00:40     215.2043   50.6904
    2020/09/18 13:00:50     215.2623   50.6708
    2020/09/18 13:01:00     215.3203   50.6512
    2020/09/18 13:01:10     215.3782   50.6315
    2020/09/18 13:01:20     215.4361   50.6118
    2020/09/18 13:01:30     215.4940   50.5921


Command line options
~~~~~~~~~~~~~~~~~~~~

You can list them by running ``sundir --help``:

::

    Usage: sundir [OPTIONS] [Latitude] [Longitude]

    Options:

        --altitude FLOAT            Set the altitude (m) of the calculated position.
                                    [default: 0.0]

        --date "2020/8/11 13:45:10" 
                                    Set the date and time.
                                    [default: Current time. Truncate in 1 second increments.]

        --interval INTEGER          Set the time interval when calculating 
                                    multiple times.
                                    [default: 10]

        --repeat INTEGER            Set the number of calculations.
                                    [default: 1]

        --csv FILE                  Write in CSV format to the path specified by FILE.

        --version                   Show the version and exit.

        -h, --help                  Show this message and exit.

License
-------

`Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__

Change log
----------

0.3.0
^^^^^

- first published version


Authors
-------

`Takayuki Matsuda <mailto:taka.matsuda@simgics.co.jp>`__

