reports = []

with open('data/day-2-sample.text') as file:
  for row in file.split(' '):
    reports.append(row)

print(reports)
