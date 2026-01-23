from .CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from enum import Enum
from random import choice


class CardType(Enum):
    CREATURE = "creature"
    SPELL = "spell"
    ARTIFACT = "artifact"


class FantasyCardFactory(CardFactory):
    """Concrete factory that creates fantasy-themed cards"""
    
    def __init__(self) -> None:
        self.creatures = ['dragon', 'goblin']
        self.spells = ['fireball']
        self.artifacts = ['mana_ring']
        # Extended types for variety
        self._all_spells = ['fireball', 'ice', 'lightning']
        self._all_artifacts = ['mana_ring', 'staff', 'crystal']
    
    def create_creature(self, name_or_power) -> Card:
        if name_or_power == 'dragon':
            return CreatureCard("Fire Dragon", 5, "legendary", 5, 5)
        else:
            return CreatureCard("Goblin Warrior", 2, "common", 2, 2)
    
    def create_spell(self, name_or_power) -> Card:
        if name_or_power == 'fireball':
            return SpellCard("Fireball", 3, "common", "damage")
        elif name_or_power == 'ice':
            return SpellCard("Ice Bolt", 2, "common", "freeze")
        else:
            return SpellCard("Lightning Bolt", 3, "uncommon", "damage")
    
    def create_artifact(self, name_or_power) -> Card:
        if name_or_power == 'mana_ring':
            return ArtifactCard("Mana Ring", 1, "common", 3, "+1 mana")
        elif name_or_power == 'staff':
            return ArtifactCard("Wizard Staff", 3, "rare", 5, "+2 spell power")
        else:
            return ArtifactCard("Power Crystal", 2, "uncommon", 2, "Draw card")
    
    def create_themed_deck(self, size: int) -> dict:
        """Create a themed deck with mixed card types"""
        deck = []
        for i in range(size):
            card_type = choice(list(CardType))
            if card_type == CardType.CREATURE:
                deck.append(self.create_creature(choice(self.creatures)))
            elif card_type == CardType.SPELL:
                deck.append(self.create_spell(choice(self._all_spells)))
            else:
                deck.append(self.create_artifact(choice(self._all_artifacts)))
        return {'deck': deck, 'size': len(deck), 'theme': 'Fantasy'}
    
    def get_supported_types(self) -> dict:
        """Return all supported card types"""
        return {
            'creatures': self.creatures,
            'spells': self.spells,
            'artifacts': self.artifacts
        }
