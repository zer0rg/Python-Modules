import math


def calculate_distance_3d(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance


def parse_coordinates(coord_string):
    try:
        parts = coord_string.split(",")
        if len(parts) != 3:
            raise ValueError("Coordinates must have exactly 3 values (x,y,z)")
        x, y, z = int(parts[0]), int(parts[1]), int(parts[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def demonstrate_coordinate_system():
    print("=== Game Coordinate System ===")

    position1 = (10, 20, 5)
    print(f"Position created: {position1}")

    origin = (0, 0, 0)
    distance = calculate_distance_3d(origin, position1)
    print(f"Distance between {origin} and {position1}: {distance:.2f}")

    print()

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    position2 = parse_coordinates(coord_str)
    if position2:
        print(f"Parsed position: {position2}")
        distance2 = calculate_distance_3d(origin, position2)
        print(f"Distance between {origin} and {position2}: {distance2:.1f}")

    print()

    invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    parse_coordinates(invalid_str)

    print()

    print("Unpacking demonstration:")
    x, y, z = position2
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={position2[0]}, Y={position2[1]}, Z={position2[2]}")


if __name__ == "__main__":
    demonstrate_coordinate_system()
