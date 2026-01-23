from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }
        return result

    def activate_ability(self) -> dict:
        result = {
            "artifact": self.name,
            "effect": self.effect,
            "durability": self.durability,
            "activated": True
        }
        return result
