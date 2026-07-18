import math
import os

# Coordenadas permitidas. Ajusta estos valores a tu aula/universidad.
CLASSROOM_LAT = float(os.getenv("CLASSROOM_LAT", "-17.768736"))
CLASSROOM_LNG = float(os.getenv("CLASSROOM_LNG", "-63.182693"))
ALLOWED_RADIUS_METERS = float(os.getenv("ALLOWED_RADIUS_METERS", "7000"))


def calculate_distance(lat1, lng1, lat2, lng2):
    earth_radius = 6371000

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lng2 - lng1)

    a = (
        math.sin(delta_phi / 2) ** 2
        + math.cos(phi1)
        * math.cos(phi2)
        * math.sin(delta_lambda / 2) ** 2
    )

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return earth_radius * c


def validate_location(user_lat, user_lng):
    distance = calculate_distance(
        user_lat,
        user_lng,
        CLASSROOM_LAT,
        CLASSROOM_LNG
    )

    return {
        "valid": distance <= ALLOWED_RADIUS_METERS,
        "distance_meters": round(distance, 2),
        "allowed_radius_meters": ALLOWED_RADIUS_METERS,
    }


def is_valid_location(user_lat, user_lng):
    return validate_location(user_lat, user_lng)["valid"]
