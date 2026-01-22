def create_inventory():
    inventory = {
        "health_potion": {"quantity": 5, "category": "potion", "value": 50},
        "iron_sword": {"quantity": 1, "category": "weapon", "value": 150},
        "leather_armor": {"quantity": 1, "category": "armor", "value": 100},
        "mana_potion": {"quantity": 3, "category": "potion", "value": 75},
        "gold_coins": {"quantity": 250, "category": "currency", "value": 1},
        "steel_shield": {"quantity": 1, "category": "armor", "value": 120},
    }
    return inventory


def calculate_total_value(inventory):
    total = 0
    for item_name, item_data in inventory.items():
        total += item_data["quantity"] * item_data["value"]
    return total


def organize_by_category(inventory):
    categories = {}
    for item_name, item_data in inventory.items():
        category = item_data["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(item_name)
    return categories


def display_inventory(inventory):
    print("=== Player Inventory ===")
    print(f"Total items: {len(inventory)}")
    print()

    for item_name, item_data in inventory.items():
        quantity = item_data["quantity"]
        category = item_data["category"]
        value = item_data["value"]
        total_value = quantity * value
        print(f"{item_name}:")
        print(f"  Category: {category}")
        print(f"  Quantity: {quantity}")
        print(f"  Unit value: {value} gold")
        print(f"  Total value: {total_value} gold")

    print()


def display_category_report(inventory):
    print("=== Inventory by Category ===")
    categories = organize_by_category(inventory)

    for category, items in sorted(categories.items()):
        print(f"\n{category.upper()}:")
        for item in sorted(items):
            quantity = inventory[item]["quantity"]
            print(f"  - {item} (x{quantity})")


def inventory_system():
    inventory = create_inventory()

    # Display full inventory
    display_inventory(inventory)

    total_value = calculate_total_value(inventory)
    print(f"Total inventory value: {total_value} gold")
    print()

    display_category_report(inventory)

    print()
    print("=== Item Lookup Demo ===")

    item = inventory.get("iron_sword")
    if item:
        print(f"Found iron_sword: {item}")

    item = inventory.get("diamond_sword", "Item not found")
    print(f"Looking for diamond_sword: {item}")

    print()
    print("=== Update Demo ===")

    inventory["health_potion"]["quantity"] += 2
    print(
        f"Added 2 health potions. New quantity: \
          {inventory['health_potion']['quantity']}"
    )

    inventory.update(
        {"magic_staff": {"quantity": 1, "category": "weapon", "value": 300}}
    )
    print("Added magic_staff to inventory")
    print(f"Inventory now has {len(inventory)} different items")


if __name__ == "__main__":
    inventory_system()
