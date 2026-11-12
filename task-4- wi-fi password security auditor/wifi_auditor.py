import re
import subprocess


def audit_password(wifi_name, password):
    if not password:
        return "OPEN / NO PASSWORD", ["Set a strong WPA2/WPA3 password immediately."]

    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Make it at least 12 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add capital letters (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add small letters (a-z).")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        tips.append("Add numbers (0-9).")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        tips.append("Add special symbols (@, #, $, !).")

    if wifi_name.lower() in password.lower():
        score = max(0, score - 2)
        tips.append("Do not include your Wi-Fi name inside the password.")

    if score <= 2:
        rating = "WEAK"
    elif score <= 4:
        rating = "MEDIUM"
    else:
        rating = "STRONG"

    return rating, tips


def get_saved_wifi_profiles():
    print("Scanning saved Windows Wi-Fi profiles...\n")
    try:
        output = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"],
            text=True,
            stderr=subprocess.DEVNULL
        )
    except Exception:
        print("Could not read system Wi-Fi profiles.")
        return

    profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)

    if not profiles:
        print("No saved Wi-Fi profiles found on this laptop.")
        return

    print("==========================================")
    print("      WI-FI PASSWORD SECURITY REPORT")
    print("==========================================")

    for name in profiles:
        wifi_name = name.strip()
        try:
            details = subprocess.check_output(
                ["netsh", "wlan", "show", "profile", wifi_name, "key=clear"],
                text=True,
                stderr=subprocess.DEVNULL
            )
            key_match = re.search(r"Key Content\s*:\s*(.*)", details)
            password = key_match.group(1).strip() if key_match else ""
        except Exception:
            password = ""

        # Hide the middle of the password so it stays safe in screenshots
        if len(password) > 4:
            masked = password[:2] + "*" * (len(password) - 4) + password[-2:]
        elif password:
            masked = "*" * len(password)
        else:
            masked = "None"

        rating, tips = audit_password(wifi_name, password)

        print(f"\nWi-Fi Name : {wifi_name}")
        print(f"Password   : {masked}")
        print(f"Security   : {rating}")
        if tips:
            print("Tips       :", ", ".join(tips))
        else:
            print("Tips       : Great! Your Wi-Fi password is strong.")

    print("\n==========================================")


def main():
    print("==========================================")
    print("     WI-FI PASSWORD SECURITY AUDITOR")
    print("==========================================")
    get_saved_wifi_profiles()


if __name__ == "__main__":
    main()