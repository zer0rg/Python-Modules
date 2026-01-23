from ex0 import Card
from . import Combatable, Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int = 5, defense: int = 3,
                 max_mana: int = 10):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.max_mana = max_mana
        self.current_mana = max_mana

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "type": "EliteCard",
            "combat_ready": True,
            "magic_ready": True,
            "game_state": game_state
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(incoming_damage, self.defense)
        damage_taken = incoming_damage - damage_blocked
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense,
            "combat_type": "melee"
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = 4
        if self.current_mana >= mana_cost:
            self.current_mana -= mana_cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": mana_cost
            }
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [],
            "mana_used": 0,
            "error": "Not enough mana"
        }

    def channel_mana(self, amount: int) -> dict:
        self.current_mana = min(self.current_mana + amount, self.max_mana)
        return {
            "channeled": amount,
            "total_mana": self.current_mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "current_mana": self.current_mana,
            "max_mana": self.max_mana,
            "spell_power": self.attack_power
        }