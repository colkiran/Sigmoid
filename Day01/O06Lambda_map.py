
from calendar import month_abbr

print(list(month_abbr))

print("-" * 60)

months = ['nov', 'jul', 'apr',  'dec', 'jan', 'oct', 'feb', 'sep', 'jun', 'mar', 'may', 'aug']

print(f"Unsorted Months :{months}")

sorted_months = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print("-" * 60)

print(f"Sorted Months :{sorted_months}")