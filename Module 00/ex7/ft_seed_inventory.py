def ft_seed_inventory(seed_type: str, n: int, unit: str):
    if not isinstance(seed_type, str):
        print("Error: El tipo de semilla debe ser un string")
        return
    if not isinstance(n, int):
        print("Error: El numero de semillas debe ser un entero")
        return
    if not isinstance(unit, str):
        print("Error: La unidad debe ser un string")
        return
    seed_type = seed_type.capitalize()
    match unit:
        case "packets":
            print(f"{seed_type} seeds: {n} packets available")
        case "grams":
            print(f"{seed_type} seeds: {n} grams total")
        case "area":
            print(f"{seed_type} seeds: covers {n} square meters")
        case _:
            print("Error: Unidad no soportada")
