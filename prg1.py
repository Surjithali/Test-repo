import secrets

def generate_otp(length=6):
    """Generate a secure OTP."""
    otp = ''.join(secrets.choice('0123456789') for _ in range(length))
    return otp

def main():
    print("Welcome to OTP Generator!")
    length = int(input("Enter the length of OTP you want to generate: "))
    otp = generate_otp(length)
    print("Your generated OTP is:", otp)

if __name__ == "__main__":
    main()