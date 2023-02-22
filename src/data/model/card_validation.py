class CardValidation:
    def validate_credit_card(card_number):
        card_number = str(card_number)
        if len(card_number) < 13 or len(card_number) > 16:
            return "Invalid card length"
        if card_number.startswith('4'):
            card_type = "VISA"
        elif card_number.startswith('5'):
            card_type = "MasterCard"
        elif card_number.startswith('37'):
            card_type = "American Express"
        elif card_number.startswith('6'):
            card_type = "Discover"
        else:
            return "Invalid card type"

        # Implement the Luhn algorithm
        sum = 0
        num_digits = len(card_number)
        oddeven = num_digits & 1
        for count in range(0, num_digits):
            digit = int(card_number[count])
            if not ((count & 1) ^ oddeven):
                digit = digit * 2
            if digit > 9:
                digit = digit - 9
            sum = sum + digit
        if (sum % 10) == 0:
            return f"{card_type} card is valid"
        else:
            return f"{card_type} card is invalid"

    # Request for a credit card number
    card_number = input("Enter a credit card number: ")

    # Get the credit card type and validity status
    result = validate_credit_card(card_number)
    print(result)
