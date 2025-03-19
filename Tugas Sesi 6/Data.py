name = "Nugraha", "john", "Jane", "Doe"
birtdate = "36","35","33","31"
print('No  | Name    | Age|')

for i, (x,y) in enumerate(zip(name,birtdate), start=1):
    print(f"{i}   | {x:<7} | {y} |")
