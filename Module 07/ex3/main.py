from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    
    # Create factory and strategy
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    
    # Create and configure engine
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    
    # Simulate a turn
    print("\nSimulating aggressive turn...")
    engine.simulate_turn()
    
    # Get final report
    print("\nGame Report:")
    status = engine.get_engine_status()
    print(status)
    
    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
