def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def new_func(spell1, spell2):
        return tuple(spell1(), spell2())
    return new_func


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    pass


def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


def spell_sequence(spells: list[callable]) -> callable:
    pass


# spell_combiner(spell1, spell2) - Combine two spells:
# • Return a new function that calls both spells with the same arguments
# • The combined spell should return a tuple of both results
# • Example: combined = spell_combiner(fireball, heal)