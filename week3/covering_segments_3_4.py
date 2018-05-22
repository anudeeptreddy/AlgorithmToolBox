# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_minimum_points(segments):
    # algorithm to find minimum number of points tha intersect among various given segments [a[i], b[i]]
    points = []
    # sort segments in increasing order of segment end points
    sorted_segments_by_end_point = sorted(segments, key=lambda x: x.end)

    point_to_include = sorted_segments_by_end_point[0].end
    points.append(point_to_include)

    for segment in sorted_segments_by_end_point:
        if segment.start > point_to_include:
            point_to_include = segment.end
            points.append(segment.end)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_minimum_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')


# Input:
# 4
# 4 7
# 1 3
# 2 5
# 5 6
# Output:
# 2
# 3 6
