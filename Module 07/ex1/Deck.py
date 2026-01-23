from ex0.Card import Card
import random


class Deck:

    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card | None:
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        total_cards: int = len(self.cards)
        creatures: int = 0
        spells: int = 0
        artifacts: int = 0
        total_cost: int = 0

        for card in self.cards:
            total_cost += card.cost
            card_type: str = card.__class__.__name__
            if card_type == "CreatureCard":
                creatures += 1
            elif card_type == "SpellCard":
                spells += 1
            elif card_type == "ArtifactCard":
                artifacts += 1

        avg_cost = total_cost / total_cards if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
