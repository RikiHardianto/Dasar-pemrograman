name = "Nugraha", "john", "Jane", "Doe"
birtdate = "1989-09-13","1990-01-01","1992-02-02","1994-03-03"
print('No     | Name     | birtdate  |')

for i, (x,y) in enumerate(zip(name,birtdate), start=1):
    print(f"{i}   | {x:<7} | {y} |")
