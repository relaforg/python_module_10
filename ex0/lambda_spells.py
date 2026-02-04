def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda a: a["power"], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return (list(filter(lambda m: m["power"] >= min_power, mages)))


def spell_transformer(spells: list[str]) -> list[str]:
    return (map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if (not len(mages)):
        avg = 0
    else:
        avg = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)

    return ({
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": avg
    })


if (__name__ == "__main__"):
    artifacts = [{'name': 'Shadow Blade', 'power': 107, 'type': 'focus'},
                 {'name': 'Wind Cloak', 'power': 93, 'type': 'weapon'},
                 {'name': 'Wind Cloak', 'power': 67, 'type': 'armor'},
                 {'name': 'Storm Crown', 'power': 114, 'type': 'armor'}]
    mages = [{'name': 'Luna', 'power': 55, 'element': 'earth'},
             {'name': 'Sage', 'power': 69, 'element': 'ice'},
             {'name': 'Luna', 'power': 76, 'element': 'fire'},
             {'name': 'Morgan', 'power': 86, 'element': 'earth'},
             {'name': 'Alex', 'power': 86, 'element': 'earth'}]
    spells = ['tsunami', 'darkness', 'meteor', 'tornado']

    print("\nTesting artifact sorter...")
    artifacts = artifact_sorter(artifacts)
    print(f"{artifacts[0]['name']} ({artifacts[0]['power']} power) comes "
          f"before {artifacts[1]['name']} ({artifacts[1]['power']} power)")
    print("\nTesting spell transformer...")
    spells = spell_transformer(spells)
    for i in spells:
        print(i, end=" ")
    print()
