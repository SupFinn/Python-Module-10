def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts ,key=lambda item: item["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }

def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
    ]

    spells = ["fireball", "heal", "shield"]
    
    print("\nTesting artifact sorter...")
    sa = artifact_sorter(artifacts)
    print(f"{sa[0]['name']} ({sa[0]['power']} power) "
          f"comes before {sa[1]['name']} ({sa[1]['power']} power)")

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))


if __name__ == "__main__":
    main()