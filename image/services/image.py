from shapely.geometry import Polygon
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
# from .area import g


def get_exif_data(image):
    info = image._getexif()

    if not info:
        raise ValueError("No metadata available")
    exif_data = {}

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)

        if decoded == "GPSInfo":
            gps_data = {}

            for t in value:
                sub_decoded = GPSTAGS.get(t, t)
                gps_data[sub_decoded] = value[t]
            exif_data["GPSInfo"] = gps_data
            return exif_data

    raise ValueError("No GPS data found. Turn on location tagging.")


def convert_to_degrees(value):
    d, m, s = value
    return d + (m / 60.0) + (s / 3600.0)


def get_coordinates(image_path):
    print(image_path)
    image = Image.open(image_path)
    # f"C:/Users/elvis/Desktop/image/farms/services/{image_path}")

    exif_data = get_exif_data(image)
    if not exif_data:
        print("no exif")
        return
    elif "GPSInfo" not in exif_data:
        print("no gps")
        return
    gps = exif_data["GPSInfo"]

    lat = convert_to_degrees(gps["GPSLatitude"])
    if gps["GPSLatitudeRef"] != "N":
        lat = -lat

    lon = convert_to_degrees(gps["GPSLongitude"])
    if gps["GPSLongitudeRef"] != "E":
        lon = -lon

    return lat, lon
