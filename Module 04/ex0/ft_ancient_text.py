import os


def read_ancient_text():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    if not os.path.exists(filename):
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...")

    file = open(filename, "r")
    content = file.read()
    file.close()

    print("\nRECOVERED DATA:")
    print(content)

    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    read_ancient_text()
