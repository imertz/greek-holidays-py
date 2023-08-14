# Greek Holidays 🇬🇷

A python package to easily get the fixed and movable holidays for Greece in any given year.

## Installation

```bash
pip install greek-holidays
```

## Usage

Here's a quick start guide on how to use the greekHolidays function.

```python
from greek_holidays import greek_holidays

holidays = greek_holidays(2023)
print(holidays)

# holidays: [{'date': '2017-01-01', 'name': 'Πρωτοχρονιά'}, {'date': '2017-01-06', 'name': 'Θεοφάνεια'}, {'date': '2017-01-27', 'name': 'Καθαρά Δευτέρα'}, {'date': '2017-03-14', 'name': 'Μεγάλη Παρασκευή'}, {'date': '2017-03-17', 'name': 'Δευτέρα του Πάσχα'}, {'date': '2017-03-25', 'name': 'Ευαγγελισμός της Θεοτόκου'}, {'date': '2017-05-01', 'name': 'Εργατική Πρωτομαγιά'}, {'date': '2017-05-05', 'name': 'Αγίου Πνεύματος'}, {'date': '2017-08-15', 'name': 'Κοίμηση της Θεοτόκου'}, {'date': '2017-10-28', 'name': 'Ημέρα του Όχι'}, {'date': '2017-12-25', 'name': 'Χριστούγεννα'}, {'date': '2017-12-26', 'name': 'Επόμενη των Χριστουγέννων'}]
```

This will return an array of objects, each having a **date** and **name** in Greek.

## Features

- Retrieve all national holidays of Greece for a given year.
- Includes both fixed date holidays and movable holidays based on the Orthodox Easter.
- Automatically removes Labour Day (Εργατική Πρωτομαγιά) if it falls on a weekend or coincides with another holiday.

