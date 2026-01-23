from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete Strategy implementation - Prioritizes attacking and dealing damage"""
    
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Execute an aggressive turn: play low-cost cards first"""
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        
        # Play cards with cost <= 3
        for card in hand:
            if card.cost <= 3:
                cards_played.append(card.name)
                mana_used += card.cost
                if hasattr(card, 'attack_power'):
                    damage_dealt += card.attack_power
                else:
                    damage_dealt += card.cost
        
        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt
        }
    
    def get_strategy_name(self) -> str:
        """Return the strategy name"""
        return "AggressiveStrategy"
    
    def prioritize_targets(self, available_targets: list) -> list:
        """Prioritize enemy player first"""
        return available_targets
