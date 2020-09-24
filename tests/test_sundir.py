"""
  Copyright 2020  Simple Logic Systems Ltd.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

"""

import sun_dir_calc as sd
from datetime import datetime as dt
import math
import astropy.coordinates as ap_crd

from pytz import timezone, utc
from tzlocal import get_localzone


class SunDirCalcMock(sd.SunDirCalc):
    def __init__(self):
        self.header = ""
        self.result = ""

        self.local_time = "2020/09/18 08:00:00"
        self.lat = "32d48m0s"  # 32.8(deg)
        self.lon = "130d43m0s"  # 130.7166667(deg)
        self.interval = 10
        self.repeat = 1
        self.csv = ""
        self.altitude = 0.0

    def _argument_parse(self):
        date = self._localtime_to_utc(self.local_time)

        return (
            self.lat,
            self.lon,
            date,
            self.interval,
            self.repeat,
            self.csv,
            self.altitude,
        )

    def _print_result(self, header, result):
        self.header = header
        self.result = result


def test_to_utc_1():
    sundir = sd.SunDirCalc()
    local_time = "2020/09/18 13:00:00"  # JST+9
    expected = "2020-09-18 04:00:00+00:00"  # UTC
    date = sundir._localtime_to_utc(local_time)

    assert expected == str(date)


def test_to_utc_2():
    sundir = sd.SunDirCalc()
    local_time = "2020/05/24 19:00:00"  # JST+9
    expected = "2020-05-24 10:00:00+00:00"  # UTC
    date = sundir._localtime_to_utc(local_time)

    assert expected == str(date)


def test_calc_sun_dir_1():
    """The confirmation data was calculated at the following site.
    https://www.esrl.noaa.gov/gmd/grad/solcalc/index.html
    """
    sundir = sd.SunDirCalc()
    local_time = "2020/09/18 08:00:00"
    date = sundir._localtime_to_utc(local_time)
    latitude = "32d48m0s"  # 32.8(deg)
    longitude = "130d43m0s"  # 130.7166667(deg)

    exp_az = 103.97
    exp_el = 23.66

    act_az, act_el = sundir._calc(date, latitude, longitude)

    assert math.isclose(exp_az, act_az, abs_tol=0.05)
    assert math.isclose(exp_el, act_el, abs_tol=0.05)


def test_calc_sun_dir_2():
    """The confirmation data was calculated at the following site.
    https://www.esrl.noaa.gov/gmd/grad/solcalc/index.html
    """
    sundir = sd.SunDirCalc()
    local_time = "2020/09/18 13:00:00"
    date = sundir._localtime_to_utc(local_time)
    latitude = "32d48m0s"  # 32.8(deg)
    longitude = "130d43m0s"  # 130.7166667(deg)

    exp_az = 202.71
    exp_el = 56.88

    act_az, act_el = sundir._calc(date, latitude, longitude)

    assert math.isclose(exp_az, act_az, abs_tol=0.05)
    assert math.isclose(exp_el, act_el, abs_tol=0.05)


def test_sundir_execute():
    """The confirmation data was calculated at the following site.
    https://www.esrl.noaa.gov/gmd/grad/solcalc/index.html
    """
    sundir = SunDirCalcMock()

    sundir.local_time = "2020/09/18 08:00:00"
    sundir.lat = "32d48m0s"  # 32.8(deg)
    sundir.lon = "130d43m0s"  # 130.7166667(deg)
    sundir.interval = 60
    sundir.repeat = 2
    sundir.csv = ""
    sundir.altitude = 1.2

    sundir.execute()

    exp_header = [
        ["latitude", "32d48m0s"],
        ["longitude", "130d43m0s"],
        ["altitude(m)", 1.2],
    ]
    exp_result = [["Date", "AZ(deg)", "EL(deg)"]]

    local_time = "2020/09/18 08:00:00"
    exp_result.append([local_time, 103.97, 23.66])

    local_time = "2020/09/18 08:01:00"
    exp_result.append([local_time, 104.12, 23.85])

    # header, result を検証
    assert exp_header == sundir.header

    assert exp_result[0] == sundir.result[0]

    for i in range(1, len(exp_result)):
        assert exp_result[i][0] == sundir.result[i][0]  # date
        assert math.isclose(exp_result[i][1], sundir.result[i][1], abs_tol=0.05)  # AZ
        assert math.isclose(exp_result[i][2], sundir.result[i][2], abs_tol=0.05)  # EL
