def create_archive():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    filename = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")

    file = open(filename, "w")

    entries = [
        "[ENTRY 001] New quantum algorithm discovered\n",
        "[ENTRY 002] Efficiency increased by 347%\n",
        "[ENTRY 003] Archived by Data Archivist trainee\n",
    ]

    for entry in entries:
        file.write(entry)
        print(entry.strip())

    file.close()

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    create_archive()
