from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Deal {self.cost} damage to target",
        }
        return result

    def resolve_effect(self, targets: list) -> dict:
        result = {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": targets,
            "resolved": True
        }
        return result
