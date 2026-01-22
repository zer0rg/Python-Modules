from ex0.Card import Card


class ArtifactCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        game_state["mana"] -= self.cost
        game_state["artifacts_in_play"] = game_state.get("artifacts_in_play", [])
        game_state["artifacts_in_play"].append(self.name)
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
            "game_state": game_state
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
