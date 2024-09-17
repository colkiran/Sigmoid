
import O21Oops21

def withdraw(tmp, amt):
    print(f"You can withdraw only Rs. {amt} per day...")

O21Oops21.HDFC.withdraw = withdraw

hdfc = O21Oops21.HDFC()
hdfc.withdraw(2000)


