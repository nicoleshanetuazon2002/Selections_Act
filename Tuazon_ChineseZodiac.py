print("Welcome to Chinese Zodiac Sign Calculator!")
print()
def chinese_zodiac(year):
    zodiac_signs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]
    start_year = 1956
    year_index = (year - start_year) % 12
    return zodiac_signs[year_index]

year = int(input("Enter a year: "))
zodiac = chinese_zodiac(year)
print(f"The Chinese zodiac sign for the year {year} is {zodiac}.")
