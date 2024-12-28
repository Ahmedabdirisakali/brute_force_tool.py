import time
import os

# Midabada Terminal-ka
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Qoraalka hordhaca ah
def introduction():
    os.system('clear')  # Shaashada nadiifi
    print(CYAN + "=" * 70 + RESET)
    print(GREEN + "      TOOLKA AMNIGA BRUTE FORCE (Educational Purposes Only)" + RESET)
    print(YELLOW + "        Created by: Ahmed Abdirisak Ali" + RESET)
    print(RED + "  Fadlan isticmaal si sharci ah iyo ujeeddo waxbarasho oo kaliya" + RESET)
    print(CYAN + "=" * 70 + RESET)

# Liiska boggaga social media ee la tijaabinayo
platforms = ["Facebook", "Twitter", "Google", "YouTube", "TikTok"]

# Function brute force
def brute_force(username, password_file, platform, correct_password):
    try:
        with open(password_file, "r") as file:
            passwords = file.readlines()
    except FileNotFoundError:
        print(RED + "\nFaylka password-ka lama helin! Fadlan hubi waddada faylka." + RESET)
        return False

    print(BLUE + f"\nTijaabinaya '{platform}' isticmaalaha: {username}" + RESET)
    for password in passwords:
        password = password.strip()  # Tirtir firaaqada
        print(YELLOW + f"Isku dayaya password: {password}" + RESET)
        time.sleep(1)  # Hakad yar si loo muujiyo isku day kasta
        
        # Halkan waxaan ku isticmaalaynaa password sax ah
        if password == correct_password:
            print(GREEN + f"\nPassword sax ah waa: {password}" + RESET)
            print(GREEN + f"{platform} account-ka '{username}' waa la galay!" + RESET)
            return True
    print(RED + "\nPassword sax ah lama helin." + RESET)
    return False

# Main program
def main():
    introduction()

    # Dooro bogga
    print(CYAN + "\nDooro bogga aad tijaabinayso:" + RESET)
    for i, platform in enumerate(platforms, 1):
        print(f"{i}. {platform}")
    
    try:
        choice = int(input("\nGali nambarka bogga aad dooratay: "))
    except ValueError:
        print(RED + "Doorasho khaldan! Fadlan ku qor nambar sax ah." + RESET)
        return

    if choice < 1 or choice > len(platforms):
        print(RED + "Doorasho khaldan! Fadlan mar kale isku day." + RESET)
        return

    platform = platforms[choice - 1]

    # Isticmaal username
    username = input(CYAN + f"\nGali username-ka {platform}: " + RESET)

    # Geli waddada faylka password-ka
    password_file = input(YELLOW + "\nGali waddada (path) ee dictionary password-ka: " + RESET)

    # Halkan ku qor password sax ah (Waxaa lagu talinayaa in password sax ah uu noqdo mid loo qoro hal meel)
    correct_password = "#@Eyl@7979"  # Halkan ku beddel password-ka saxda ah

    # Ku orod brute force
    brute_force(username, password_file, platform, correct_password)

# Orodka barnaamijka
if __name__ == "__main__":
    main()

