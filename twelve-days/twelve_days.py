def recite(start_verse, end_verse):
    ans = []
    for i in range(start_verse, end_verse+1):
        gift = ""
        for j in range(i, 0, -1):
            if j == 1:
                gift += f" and a {gift_text(j)}."
            else:
                gift += f" {count_text(j)} {gift_text(j)},"
        if gift.startswith(" and"):
            gift = gift.replace("and ", "")
        ans.append(f"On the {roman_text(i)} day of Christmas my true love gave to me:{gift}")
    return ans


def gift_text(num):
    values = [
        "",
        "Partridge in a Pear Tree",
        "Turtle Doves",
        "French Hens",
        "Calling Birds",
        "Gold Rings",
        "Geese-a-Laying",
        "Swans-a-Swimming",
        "Maids-a-Milking",
        "Ladies Dancing",
        "Lords-a-Leaping",
        "Pipers Piping",
        "Drummers Drumming"
    ]
    return values[num]


def roman_text(num):
    values = [
        "",
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"
    ]
    return values[num]


def count_text(num):
    values = [
        "",
        "a",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve"
    ]
    return values[num]
