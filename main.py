import contact_book
import calculator
import email_sender
import weather_app
import crypto_price

while True:
    print("\n===== MAIN MENU =====")
    print("1. Contact Book")
    print("2. Calculator")
    print("3. Send Email")
    print("4. Weather App")
    print("5. Crypto Price")
    print("6. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        contact_book.main()
    elif choice == "2":
        calculator.main()
    elif choice == "3":
        email_sender.send_email()
    elif choice == "4":
        weather_app.get_weather()
    elif choice == "5":
        crypto_price.get_crypto_price()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
