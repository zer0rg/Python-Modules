from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .CardFactory import CardFactory
    from .GameStrategy import GameStrategy


class GameEngine:
    
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
    
    def configure_engine(self, factory: 'CardFactory', strategy: 'GameStrategy') -> None:
        self.factory = factory
        self.strategy = strategy
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"Available types: {factory.get_supported_types()}")
    
    def simulate_turn(self) -> dict:
        """Simulate a game turn using the configured strategy"""
        hand = [
            self.factory.create_creature('dragon'),
            self.factory.create_creature('goblin'),
            self.factory.create_spell('lightning')
        ]
        self.cards_created += 3
        
        print(f"Hand: [{', '.join([f'{card.name} ({card.cost})' for card in hand])}]")
        print("Turn execution:")
        
        turn_result = self.strategy.execute_turn(hand, [])
        
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Actions: {turn_result}")
        
        self.turns_simulated += 1
        self.total_damage += turn_result.get('damage_dealt', 0)
        
        return turn_result
    
    def get_engine_status(self) -> dict:
        """Get the current engine status"""
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
