from functools import wraps
from datetime import datetime
from inspect import signature


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Casting", func.__name__)
        t1 = datetime.now()
        result = func(*args, **kwargs)
        print(f"Spell completed in {(datetime.now() - t1).total_seconds()} "
              "seconds")
        return (result)
    return (wrapper)


def power_validator(min_power: int):
    def decorator(func):
        sig = signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind_partial(*args, **kwargs)
            if bound.arguments["power"] < min_power:
                return ("Insufficient power for this spell")
            return (func(*args, **kwargs))
        return (wrapper)
    return (decorator)


def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return (func(*args, **kwargs))
                except Exception:
                    print("Spell failed, retrying... (attempt "
                          f"{i + 1}/{max_attempts})")
            return ("Spell casting failed after max_attempts attempts")
        return (wrapper)
    return (decorator)


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return all(c.isalpha() or c == " " for c in name) and len(name) >= 3

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


if (__name__ == "__main__"):
    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        return ("Fireball cast!")

    print("Result:", fireball())
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("wizard"))
    print(MageGuild.validate_mage_name("wizard_0"))
    print(MageGuild().cast_spell("Lightning", 15))
    print(MageGuild().cast_spell("Lightning", 9))
