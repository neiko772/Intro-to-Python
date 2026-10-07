# Ewok Data tracker - Created by Neiko
ewok_data = {
    "name": "Neiko",
    "age": 16,
    "weapon": "spear",
    "rank": "warrior"
}

print("Ewok Name:", ewok_data["name"])
print("Ewok Age:", ewok_data["age"])
print("Ewok Weapon:", ewok_data["weapon"])
print("Ewok Rank:", ewok_data["rank"])

ewok_data["weapon"] = "bow and arrow" # updating the weapon
ewok_data["rank"] = "chief" # updating the rank
ewok_data["homeland"] = "earth" # adding a new attribute for homeland

print("\nUpdated Ewok Data:")
for key, value in ewok_data.items():
    print(f"{key}: {value}")

ewok_tribe = {
    "neiko": ewok_data,
    "tristan": {
        "name": "tristan",
        "age": 16,
        "weapon": "sword",
        "rank": "warrior",
        "homeland": "earth"
    }
}

print("\nEwok Tribe Data:")
for ewok_name, ewok_info in ewok_tribe.items():
    print(f"\nEwok Name: {ewok_name}")
    for key, value in ewok_info.items():
        print(f"{key}: {value}")