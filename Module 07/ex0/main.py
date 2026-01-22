from . import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    card_info = fire_dragon.get_card_info()
    print(f"{card_info}")

    print("\nPlaying Fire Dragon with 6 mana available:")
    game_state = {"available_mana": 6}
    play_result = fire_dragon.play(game_state)
    print(f"Play result: {play_result}")

    goblin_warrior = CreatureCard("Goblin Warrior", 2, "Common", 2, 3)

    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result = fire_dragon.attack(goblin_warrior)
    print(f"Attack result: {attack_result}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
