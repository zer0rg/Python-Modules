def handle_crisis(filename):
    print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as vault:
            content = vault.read().strip()
            print(f'SUCCESS: Archive recovered - "{content}"')
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unknown system anomaly - {type(e).__name__}")
        print("STATUS: Crisis handled, diagnostics required")


def crisis_response():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    handle_crisis("lost_archive.txt")
    handle_crisis("classified_vault.txt")

    try:
        with open("standard_archive.txt", "w") as f:
            f.write("Knowledge preserved for humanity")
    except Exception:
        pass

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    try:
        with open("standard_archive.txt", "r") as vault:
            content = vault.read().strip()
            print(f'SUCCESS: Archive recovered - "{content}"')
            print("STATUS: Normal operations resumed")
    except Exception as e:
        print(f"RESPONSE: Unexpected error - {e}")
        print("STATUS: Crisis handled")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
