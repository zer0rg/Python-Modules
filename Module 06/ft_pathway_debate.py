import alchemy.transmutation.basic as basic_module
import alchemy.transmutation.advanced as advanced_module
import alchemy.transmutation


def main():
    print("=== Pathway Debate Mastery ===")
    
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {basic_module.lead_to_gold()}")
    print(f"stone_to_gem(): {basic_module.stone_to_gem()}")
    
    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {advanced_module.philosophers_stone()}")
    print(f"elixir_of_life(): {advanced_module.elixir_of_life()}")
    
    print("\nTesting Package Access:")
    print(f"alchemy.transmutation.lead_to_gold(): \
{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): \
{alchemy.transmutation.philosophers_stone()}")
    
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
