from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if (operation == "add"):
        return (reduce(operator.add, spells))
    elif (operation == "multiply"):
        return (reduce(operator.mul, spells, 1))
    elif (operation == "max"):
        return (reduce(max, spells))
    elif (operation == "min"):
        return (reduce(min, spells))
    return (0)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return ({
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lighting_enchant": partial(base_enchantment, power=50,
                                    element="lightning")
    })


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if (n == 0):
        return (0)
    if (n == 1):
        return (1)
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


@singledispatch
def spell_dispatcher(a: Any) -> Callable:
    return (lambda: f"{type(a)} not supported")


@spell_dispatcher.register
def _(a: int):
    return (lambda: f"{type(a)} deals {a} damages")


@spell_dispatcher.register
def _(a: str):
    return (lambda: f"{type(a)} add {a} enchant")


@spell_dispatcher.register
def _(a: list):
    return (lambda: f"{type(a)} casting all {a} spells")


if (__name__ == "__main__"):
    print("\nTesting spell reducer...")
    spell_powers = [48, 27, 21, 32, 35, 15]
    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    print("\nTesting memoized fibonacci...")
    print("fib(10):", memoized_fibonacci(10))
    print("fib(15):", memoized_fibonacci(15))
