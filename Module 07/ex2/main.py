#!/usr/bin/env python3
"""
DataDeck Master the Art of Abstract Card Architecture
Demonstrates multiple inheritance with EliteCard
"""

from . import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    
    elite = EliteCard("Arcane Warrior", cost=5, rarity="Legendary")
    
    print("\nEliteCard capabilities:")
    
    card_methods = ['play', 'get_card_info', 'is_playable']
    print(f"- Card: {card_methods}")
    
    combatable_methods = ['attack', 'defend', 'get_combat_stats']
    print(f"- Combatable: {combatable_methods}")
    
    magical_methods = ['cast_spell', 'channel_mana', 'get_magic_stats']
    print(f"- Magical: {magical_methods}")
    
    print(f"\nPlaying {elite.name} (Elite Card):")
    
    print("\nCombat phase:")
    attack_result = elite.attack("Enemy")
    print(f"Attack result: {attack_result}")
    
    defense_result = elite.defend(5)
    print(f"Defense result: {defense_result}")
    
    print("\nMagic phase:")
    spell_result = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print(f"Spell cast: {spell_result}")
    
    mana_result = elite.channel_mana(3)
    print(f"Mana channel: {mana_result}")
    
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
