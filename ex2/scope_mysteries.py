from typing import Any, Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return (count)
    return (counter)


def spell_accumulator(initial_power: int) -> Callable:
    count = initial_power

    def add_power(power: int):
        nonlocal count
        count += power
        return (count)
    return (add_power)


def enchantment_factory(enchantment_type: str) -> Callable:
    ench = enchantment_type

    def enchant(item: str):
        return f"{ench} {item}"
    return (enchant)


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any):
        memory[key] = value

    def recall(key: str):
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
    g = enchantment_factory("Frozen")
    print(g("Shield"))
