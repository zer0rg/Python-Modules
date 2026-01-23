from ex0 import CreatureCard
from . import ArtifactCard, SpellCard, Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()

    creature = CreatureCard("Fire Dragon", 5, "Rare", 4, 6)
    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Uncommon", 5,
                            "+1 mana per turn")

    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")

    print("\nDrawing and playing cards:")

    game_state = {"available_mana": 10}

    card1 = deck.draw_card()
    if card1:
        print(f"Drew: {card1.name} \
({card1.__class__.__name__.replace('Card', '')})")
        result = card1.play(game_state)
        print(f"Play result: {result}")

    card2 = deck.draw_card()
    if card2:
        print(f"\nDrew: {card2.name} \
({card2.__class__.__name__.replace('Card', '')})")
        result = card2.play(game_state)
        print(f"Play result: {result}")

    card3 = deck.draw_card()
    if card3:
        print(f"\nDrew: {card3.name} \
({card3.__class__.__name__.replace('Card', '')})")
        result = card3.play(game_state)
        print(f"Play result: {result}")

    print("\nPolymorphism in action: Same interface, different card \
behaviors!")


if __name__ == "__main__":
    main()
