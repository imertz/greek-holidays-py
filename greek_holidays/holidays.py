import datetime


def calculate_movable_holidays(year):
    e = 10
    if year > 1600:
        year2 = year // 100
        e = 10 + year2 - 16 - (year2 - 16) // 4
    if year < 1583:
        e = 0

    a = year % 19
    b = (19 * a + 15) % 30
    c = (year + year // 4 + b) % 7
    L = b - c
    p = L + e
    day = 1 + (p + 27 + (p + 6) // 40) % 31
    month = 3 + (p + 26) // 30 - 1

    pascha = datetime.date(year, month, day)
    kathara_deftera = pascha - datetime.timedelta(days=48)
    meg_paraskevi = pascha - datetime.timedelta(days=2)
    meg_savvato = pascha - datetime.timedelta(days=1)
    deft_pascha = pascha + datetime.timedelta(days=1)
    agiou_pnefmatos = pascha + datetime.timedelta(days=50)

    return [
        {"date": kathara_deftera.strftime("%Y-%m-%d"), "name": "Καθαρά Δευτέρα"},
        {"date": meg_paraskevi.strftime("%Y-%m-%d"), "name": "Μεγάλη Παρασκευή"},
        {"date": meg_savvato.strftime("%Y-%m-%d"), "name": "Μεγάλο Σάββατο"},
        {"date": pascha.strftime("%Y-%m-%d"), "name": "Κυριακή του Πάσχα"},
        {"date": deft_pascha.strftime("%Y-%m-%d"), "name": "Δευτέρα του Πάσχα"},
        {"date": agiou_pnefmatos.strftime("%Y-%m-%d"), "name": "Αγίου Πνεύματος"},
    ]


def greek_holidays(year):
    fixed_holidays = [
        {"date": datetime.date(year, 1, 1).strftime("%Y-%m-%d"), "name": "Πρωτοχρονιά"},
        {"date": datetime.date(year, 1, 6).strftime("%Y-%m-%d"), "name": "Θεοφάνεια"},
        {
            "date": datetime.date(year, 3, 25).strftime("%Y-%m-%d"),
            "name": "Ευαγγελισμός της Θεοτόκου",
        },
        {
            "date": datetime.date(year, 5, 1).strftime("%Y-%m-%d"),
            "name": "Εργατική Πρωτομαγιά",
        },
        {
            "date": datetime.date(year, 8, 15).strftime("%Y-%m-%d"),
            "name": "Κοίμηση της Θεοτόκου",
        },
        {
            "date": datetime.date(year, 10, 28).strftime("%Y-%m-%d"),
            "name": "Ημέρα του Όχι",
        },
        {
            "date": datetime.date(year, 12, 25).strftime("%Y-%m-%d"),
            "name": "Χριστούγεννα",
        },
        {
            "date": datetime.date(year, 12, 26).strftime("%Y-%m-%d"),
            "name": "Επόμενη των Χριστουγέννων",
        },
    ]

    movable_holidays = calculate_movable_holidays(year)

    all_holidays = fixed_holidays + movable_holidays
    all_holidays.sort(key=lambda x: x["date"])

    return all_holidays
