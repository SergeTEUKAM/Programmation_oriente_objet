def is_leap_year(year):
    # Les années bissextiles sont toutes des multiples de 4
    if year % 4 != 0:
        return False

    # Les années séculaires ne sont pas bissextiles, hormis 1600, 2000, 2400, etc.
    if year % 100 == 0:
        return year % 400 == 0

    # Tous les autres résultats sont vrais.
    return True
print(is_leap_year(2008))
