def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("strands must have identical length")

    return sum([1 for letter_a, letter_b in zip(strand_a, strand_b)
                if letter_a != letter_b])
