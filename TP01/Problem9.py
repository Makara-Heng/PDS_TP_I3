# Problem 9. Electricity Bill with Progressive Tiers

# a. Write function electricity_bill(kwh)
def electricity_bill(kwh):
    if kwh < 0:
        return None

    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 150)
    tier3 = max(kwh - 200, 0)

    cost = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)
    total = cost + 2000
    vat = total * 0.1
    total += vat

    return round(total)

# b. Print a table
consumptions = [0, 35, 50, 120, 200, 350]

print()
print("Electricity Bill Table")
print("-" * 48)

for kwh in consumptions:
    bill = electricity_bill(kwh)
    usd = bill / 4100

    print(f"{kwh:3} kWh -> {bill:>9} riel (≈ {usd:6.2f} USD)")
print()

# c. Ask user for their monthly consumption
kwh = float(input("Enter your monthly consumption (kWh): "))

bill = electricity_bill(kwh)

if bill is None:
    print("Invalid input! Consumption can't be negative.")
else:
    print(f"Your electricity bill is {bill} riel which is approximately ${bill / 4100:.2f}.")