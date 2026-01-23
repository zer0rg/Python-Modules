from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, name: str, cost: int, rarity: str) -> None:
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
        attack = getattr(self, 'attack_power', None)
        if attack is not None:
            info["attack"] = attack
        health = getattr(self, 'health', None)
        if health is not None:
            info["health"] = health
        return info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False
