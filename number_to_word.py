one_digit_words = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}

teens = {
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen",
    17: "seventeen", 18: "eighteen", 19: "nineteen"
}

tens_words = {
    2: "twenty", 3: "thirty", 4: "forty",
    5: "fifty", 6: "sixty", 7: "seventy",
    8: "eighty", 9: "ninety"
}

large_units = [
    "", "thousand", "million", "billion",
    "trillion", "quadrillion", "quintillion"
]


def three_digit_to_words(num):
    """Convert a number from 0–999 into words."""
    words = []

    hundred = num // 100
    remainder = num % 100

    if hundred:
        words.append(one_digit_words[hundred] + " hundred")

    if remainder:
        if hundred:
            words.append("and")

        if remainder < 10:
            words.append(one_digit_words[remainder])
        elif remainder < 20:
            words.append(teens[remainder])
        else:
            tens = remainder // 10
            ones = remainder % 10

            if ones:
                words.append(tens_words[tens] + " " + one_digit_words[ones])
            else:
                words.append(tens_words[tens])

    return " ".join(words)


def converter(n):
    if n == "0":
        return "Zero"

    word = []

    if n.startswith('-'):
        word.append("Negative")
        n = n[1:]

    num = int(n)

    parts = []
    unit_index = 0

    while num > 0:
        chunk = num % 1000
        if chunk != 0:
            chunk_words = three_digit_to_words(chunk)
            if large_units[unit_index]:
                chunk_words += " " + large_units[unit_index]
            parts.append(chunk_words)
        num //= 1000
        unit_index += 1

    result = " ".join(reversed(parts))
    return " ".join(word + [result]).strip().capitalize()


if __name__ == "__main__":
    while True:
        try:
            n = input("Enter a number (or 'exit'): ").strip()
            if n.lower() == "exit":
                break
            int(n)  # validate input
            print(f"{n} --> {converter(n)}")
        except ValueError:
            print("Error: Invalid Number!")
