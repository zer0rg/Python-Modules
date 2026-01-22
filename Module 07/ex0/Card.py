from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info: dict = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__
        }
        if hasattr(self, 'attack_power'):
            info["attack"] = self.attack_power
        if hasattr(self, 'health'):
            info["health"] = self.health
        return info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False
