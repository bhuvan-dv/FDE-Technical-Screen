def sort(width: int, height: int, length: int, mass: int) -> str:

    volume = width * height * length

    bulky = volume >= 1_000_000 or (width >= 150 or height >= 150 or length >= 150)
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    return "SPECIAL" if bulky or heavy else "STANDARD"


# ---------------- TESTS ----------------
if __name__ == "__main__":
    test_cases = [
        (100, 100, 100, 10, "STANDARD"),  # Normal case
        (200, 100, 50, 10, "SPECIAL"),    # Bulky due to dimension
        (100, 100, 100, 25, "SPECIAL"),   # Heavy only
        (200, 200, 200, 30, "REJECTED"),  # Both bulky and heavy
        (150, 50, 50, 19, "SPECIAL"),     # Exactly at bulky threshold
        (100, 100, 100, 20, "SPECIAL"),   # Exactly at heavy threshold
        (200, 200, 20, 19, "SPECIAL"),    # Bulky due to large area
        (1, 1, 1_000_000, 5, "SPECIAL"),  # Extremely long package
    ]

    for w, h, l, m, expected in test_cases:
        result = sort(w, h, l, m)
        print(f"sort({w}, {h}, {l}, {m}) = {result} | Expected: {expected}")
