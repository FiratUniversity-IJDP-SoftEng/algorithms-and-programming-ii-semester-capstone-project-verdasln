
def graham_scan(points):
    points = sorted(points)
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def jarvis_march(points):
    if len(points) < 3:
        return points
    hull = []
    l = points.index(min(points))
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % len(points)
        for i in range(len(points)):
            o = orientation(points[p], points[i], points[q])
            if o == 2:
                q = i
        p = q
        if p == l:
            break
    return hull

def quickhull(points):
    def side(a, b, p):
        return (p[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (p[0] - a[0])

    def dist(a, b, p):
        return abs((p[1] - a[1]) * (b[0] - a[0]) - (b[1] - a[1]) * (p[0] - a[0]))

    def find_hull(points, a, b, side_val):
        idx = -1
        max_dist = 0
        for i in range(len(points)):
            temp = dist(a, b, points[i])
            if side(a, b, points[i]) == side_val and temp > max_dist:
                idx = i
                max_dist = temp
        if idx == -1:
            return [a, b]
        left = find_hull(points, points[idx], a, -side(points[idx], a, b))
        right = find_hull(points, points[idx], b, -side(points[idx], b, a))
        return left[:-1] + right

    if len(points) < 3:
        return points
    min_x = min(points)
    max_x = max(points)
    left = find_hull(points, min_x, max_x, 1)
    right = find_hull(points, min_x, max_x, -1)
    return left[:-1] + right

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # colinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise
