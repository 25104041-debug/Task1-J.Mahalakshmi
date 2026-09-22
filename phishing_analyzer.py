def analyze_message(message):
    red_flags = []

    suspicious_words = [
        "urgent", "verify", "winner", "prize",
        "click here", "password", "account blocked",
        "limited time", "claim now"
    ]

    suspicious_links = [
        "http://", "bit.ly", "tinyurl.com"
    ]

    lower_message = message.lower()

    for word in suspicious_words:
        if word in lower_message:
            red_flags.append("Suspicious keyword: " + word)

    for link in suspicious_links:
        if link in lower_message:
            red_flags.append("Suspicious link found: " + link)

    print("\n--- Phishing Awareness Analysis ---")

    if red_flags:
        print("⚠️ Possible Phishing Message")
        print("\nRed Flags Found:")

        for flag in red_flags:
            print("•", flag)

        print("\nReason:")
        print("The message contains suspicious keywords or links.")
        print("Do not click unknown links or share personal information.")

    else:
        print("✅ No common phishing indicators found.")
        print("Still verify the sender before taking any action.")


message = input("Enter the email/message: ")

analyze_message(message)