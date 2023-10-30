import currency_converter

print("Currency Converter")
print("1. USD to BGN")
print("2. BGN to USD")
print("3. EUR to BGN")
print("4. BGN to EUR")
print("5. GBP to BGN")
print("6. BGN to GBP")

choice = int(input("Select an option: "))
amount = float(input("Enter the amount: "))

if choice == 1:
    converted_amount = currency_converter.usd_to_bgn(amount)
    print(f"{amount} USD is equal to {round(converted_amount,2)} BGN")
elif choice == 2:
    converted_amount = currency_converter.bgn_to_usd(amount)
    print(f"{amount} BGN is equal to {round(converted_amount,2)} USD")
elif choice == 3:
    converted_amount = currency_converter.eur_to_bgn(amount)
    print(f"{amount} EUR is equal to {round(converted_amount,2)} BGN")
elif choice == 4:
    converted_amount = currency_converter.bgn_to_eur(amount)
    print(f"{amount} BGN is equal to {round(converted_amount,2)} EUR")
elif choice == 5:
    converted_amount = currency_converter.gbp_to_bgn(amount)
    print(f"{amount} GBP is equal to {round(converted_amount,2)} BGN")
elif choice == 6:
    converted_amount = currency_converter.bgn_to_gbp(amount)
    print(f"{amount} BGN is equal to {round(converted_amount,2)} GBP")
else:
    print("Invalid choice!")
