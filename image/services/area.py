from geopy.distance import geodesic


def polygon_area_geodesic(coords):
    """
    Compute approximate polygon area in m² using geodesic distances
    and shoelace formula. Works for small areas like farms.
    """
    n = len(coords)
    if n < 3:
        return 0  # Not a polygon

    # Convert lat/lon to meters using local reference (first point)
    meters_coords = []
    ref_lat, ref_lon = coords[0]
    for lat, lon in coords:
        y = geodesic((ref_lat, ref_lon), (lat, ref_lon)).meters
        x = geodesic((ref_lat, ref_lon), (ref_lat, lon)).meters
        # adjust sign for south/west
        if lat < ref_lat:
            y = -y
        if lon < ref_lon:
            x = -x
        meters_coords.append((x, y))

    # Shoelace formula
    area = 0
    for i in range(n):
        x0, y0 = meters_coords[i]
        x1, y1 = meters_coords[(i + 1) % n]
        area += x0 * y1 - x1 * y0
    return abs(area) / 2
