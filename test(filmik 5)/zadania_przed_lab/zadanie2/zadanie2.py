def calculate_distance_one_dimension(N, a, b):
    # a i b sa tego samego znaku, dobra odpowiedz to zasze
    if a * b > 0:
        return abs(a - b)

    # a i b róznych znakow - rozwazamy dwa przypadki
    a = abs(a)
    b = abs(b)
    normal_route = a + b
    around_route = 2 * N - (a + b) + 1

    return min(normal_route, around_route)


def distance(N, point_a, point_b):
    try:
        distance_x = calculate_distance_one_dimension(N, point_a[0], point_b[0])
        distance_y = calculate_distance_one_dimension(N, point_a[1], point_b[1])
    except Exception:
        return None
    return distance_x + distance_y
