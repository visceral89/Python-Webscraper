import os
import requests

# Skapa en lista av heroes namn.
heroes = ["abaddon", "axe", "zuus", "lich"]


# Funktionen download Portraits
def downloadPortraits(heroes_list):
    base_url = (
        "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/"
    )
    dir_name = "img"  # Namnet på mappen

    # Kolla ifall mappen finns, annars skapa den.
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Gör detta för varje "hero" i heroes_list
    for hero in heroes_list:
        image_url = f"{base_url}{hero}.png"
        response = requests.get(image_url)
        # Kolla svarskoden, 200 = ok.
        if response.status_code == 200:
            file_path = os.path.join(dir_name, f"{hero}.png")
            # Special, with skapar en temporär workspace.
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {hero}'s portrait successfully.")
        else:
            print(
                f"Failed to download {hero}'s portrait. Status Code: {response.status_code}"
            )


# Call the function
downloadPortraits(heroes)
