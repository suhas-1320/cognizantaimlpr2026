"""
Application entry point
"""

import random


def generate_otp():
    """
    Generate a random OTP
    """
    import random

    otp = random.randint(100000, 999999)
    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print(f"Your OTP is: {otp}")
