import gpxpy
import datetime
import sys

if __name__ == '__main__':
    f1_name = sys.argv[1]
    f2_name = sys.argv[2]
    out_name = f"{f1_name.split('.')[0]}_{f2_name.split('.')[0]}.gpx"

    with open(f1_name, 'r') as file:
        gpx1 = gpxpy.parse(file)
    with open(f2_name, 'r') as file:
        gpx2 = gpxpy.parse(file)

    dt = gpx2.tracks[0].segments[0].points[0].time - gpx1.tracks[0].segments[0].points[-1].time
    dt = dt - datetime.timedelta(seconds=5)

    for point in gpx2.tracks[0].segments[0].points:
        point.adjust_time(-dt)
        gpx1.tracks[0].segments[0].points.append(point)

    with open(out_name, 'w') as file:
        file.write(gpx1.to_xml())
