from typing import Any


def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return (count)
    return (counter)


def spell_accumulator(initial_power: int) -> callable:
    count = initial_power

    def add_power(power: int):
        nonlocal count
        count += power
        return (count)
    return (add_power)


def enchantment_factory(enchantment_type: str) -> callable:
    ench = enchantment_type

    def enchant(item: str):
        nonlocal ench
        return f"{ench} {item}"
    return (enchant)


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value: Any):
        nonlocal memory
        memory[key] = value

    def recall(key: str):
        nonlocal memory
        if (memory.get(key, None) is None):
            return ("Memory not found")
        return (memory[key])

    return ({
        "store": store,
        "recall": recall
    })


if (__name__ == "__main__"):
    print("\nTesting mage counter...")
    count = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {count()}")

    print("\nTesting enchantment factory...")
    f = enchantment_factory("Flamming")
    print(f("Sword"))
    f = enchantment_factory("Frozen")
    print(f("Shield"))
