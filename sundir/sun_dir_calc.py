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
import traceback
import argparse, csv
import datetime as dt
import astropy.time as ap_t
import astropy.units as ap_u
import astropy.coordinates as ap_crd
import pytz
import tzlocal as tzl


class SunDirCalc:
    def _localtime_to_utc(self, localtime: str):
        """Convert local time to UTC."""
        date = dt.datetime.strptime(localtime, "%Y/%m/%d %H:%M:%S")
        loc = tzl.get_localzone()
        as_utc = loc.localize(date).astimezone(pytz.utc)
        return as_utc

    def _calc(self, datetime, lat: str, lon: str, height=0.0):
        """Calculate the azimuth and elevation of the sun.

        Calculates the azimuth and elevation of the sun as seen from the specified
        time and place (latitude, longitude, sea level).

         Args:
             datetime (datetime): datetime to calculate. (aware instance)
             lat (str): latitude.
             lon (str): longitude.
             height (float, optional): height above sea level. Default to 0.0

         Returns:
             az (float): azimuth of sun.
             el (float): elevation of sun.

        """
        time = ap_t.Time(datetime)
        loc = ap_crd.EarthLocation(
            lat=ap_crd.Angle(lat), lon=ap_crd.Angle(lon), height=height
        )
        sun = ap_crd.get_sun(time).transform_to(
            ap_crd.AltAz(obstime=time, location=loc)
        )
        az = sun.az.degree
        el = sun.alt.degree

        return az, el

    def _save_to_csv(self, file_path: str, header: list, result: list):
        """Save the calculation result to a CSV file."""
        with open(file_path, "w") as f:
            writer = csv.writer(f, lineterminator="\n")
            writer.writerows(header)
            writer.writerows(result)

    def _print_result(self, header: list, result: list):
        """Display the calculation result."""
        for row in header:
            print(f"{row[0]: <12}: {row[1]}")

        print(
            f"\n{result[0][0]: ^22}" + f"{result[0][1]: >10}" + f"{result[0][2]: >10}"
        )
        for row in result[1:]:
            az = f"{row[1]:.4f}"
            el = f"{row[2]:.4f}"
            print(f"{row[0]: <22}{az: >10}{el: >10}")

    def _argument_parse(self):
        """Analyze the arguments."""
        parser = argparse.ArgumentParser(description="Calculate the AZ, EL of the sun.")
        parser.add_argument("--version", action="version", version="sundir 0.3.1")

        parser.add_argument("lat", help="latitude ex: 35d37m51s or 35.6799d")
        parser.add_argument("lon", help="longitude ex: 139d47m3s or 139.6806d")
        parser.add_argument("--date", default="", help="start date time")
        parser.add_argument(
            "--interval",
            type=int,
            default=10,
            help="time interval(s) when calculating multiple times.",
        )
        parser.add_argument(
            "--repeat", type=int, default=1, help="number of calculations."
        )
        parser.add_argument(
            "--csv",
            default="",
            help="Specify the file path when writing to a CSV file.",
        )
        parser.add_argument(
            "--altitude", type=float, default=0.0, help="sea level altitude (m)"
        )
        args = parser.parse_args()

        if args.date == "":
            # Truncate less than seconds.
            date_str = dt.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        else:
            date_str = args.date

        date = self._localtime_to_utc(date_str)

        return (
            args.lat,
            args.lon,
            date,
            args.interval,
            args.repeat,
            args.csv,
            args.altitude,
        )

    def execute(self):
        """The entity of the main process.

        Process according to the following flow.
        (1) Analyze the arguments.
        (2) Calculate the azimuth and elevation of the sun.
        (3) View the results or save to a csv file.

        """
        # (1) Analyze the arguments.
        lat, lon, date, interval, repeat, csv, altitude = self._argument_parse()

        header = [["latitude", lat], ["longitude", lon], ["altitude(m)", altitude]]

        # (2) Calculate the azimuth and elevation of the sun.
        loc = tzl.get_localzone()
        result = [["Date", "AZ(deg)", "EL(deg)"]]
        for _ in range(repeat):
            az, el = self._calc(date, lat, lon, altitude)
            date_str = date.astimezone(loc).strftime("%Y/%m/%d %H:%M:%S")
            result.append([date_str, az, el])
            date = date + dt.timedelta(seconds=interval)

        # (3) View the results or save to a csv file.
        if csv == "":
            self._print_result(header, result)
        else:
            self._save_to_csv(csv, header, result)


def main():
    sundir = SunDirCalc()

    try:
        sundir.execute()

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    main()
