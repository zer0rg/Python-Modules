def vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    classified_file = "classified_data.txt"

    with open(classified_file, "w") as vault:
        vault.write("Quantum encryption keys recovered\n")
        vault.write("Archive integrity: 100%\n")

    print("\nSECURE EXTRACTION:")

    with open(classified_file, "r") as vault:
        for line in vault:
            print(f"[CLASSIFIED] {line.strip()}")

    print("\nSECURE PRESERVATION:")

    with open(classified_file, "a") as vault:
        vault.write("New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")

    print("\nVault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    vault_security()
