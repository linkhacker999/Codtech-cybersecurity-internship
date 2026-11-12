import itertools
import string
import time


def brute_force_attack(target_password):
    # Characters to try: small letters (a-z) and numbers (0-9)
    characters = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()

    print("\nStarting Brute Force Simulation...")
    print("Cracking password, please wait...\n")

    # Try passwords from length 1 up to 6
    for length in range(1, 7):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess_password = "".join(guess)

            if guess_password == target_password:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)

                print("====================================")
                print("         PASSWORD CRACKED!")
                print("====================================")
                print("Password Found :", guess_password)
                print("Total Attempts :", attempts)
                print("Time Taken     :", time_taken, "seconds")
                return

    print("Password not cracked (too long or has symbols/uppercase).")


def main():
    print("====================================")
    print("       BRUTE FORCE SIMULATOR")
    print("====================================")
    print("Note: Use a short password (3 or 4 characters) with")
    print("small letters and numbers only (example: cat1 or 2026).\n")

    target = input("Enter a short test password to crack: ")
    brute_force_attack(target)


if __name__ == "__main__":
    main()