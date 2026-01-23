from .Card import Card


class CreatureCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack < 0:
            raise ValueError(f"Attack must be positive integer, got {attack}")
        if health < 0:
            raise ValueError(f"Health must be positive integer, got {health}")
        self.attack_power = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        print(f"Playable: {super().is_playable(available_mana)}")
        if super().is_playable(available_mana):
            result: dict = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
            return result
        return {}

    def attack(self, target: 'CreatureCard') -> dict:
        result: dict = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack_power,
            "combat_resolved": True
        }
        return result
