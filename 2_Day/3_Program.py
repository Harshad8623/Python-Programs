# Random OTP Generator
import random
def generate_otp(length):
    digits = "0123456789"
    otp = ""
    for _ in range(length):
        otp += random.choice(digits)
    return otp
otp_length = int(input("Enter the length of the OTP: "))
otp = generate_otp(otp_length)
print("Generated OTP:", otp)



# Another Simple way using random module
import random
otp_length = int(input("Enter the length of the OTP: "))
otp = ''.join(random.choices('0123456789', k=otp_length))
print("Generated OTP:", otp)


# Anotother Simple way using lambda function
import random
generate_otp_lambda = lambda length: ''.join(random.choices('0123456789', k=length))
otp_length = int(input("Enter the length of the OTP: "))
otp = generate_otp_lambda(otp_length)
print("Generated OTP:", otp)


# Another Simple way using a class
import random
class OTPGenerator:
    def __init__(self, length):
        self.length = length

    def generate_otp(self):
        digits = "0123456789"
        otp = ""
        for _ in range(self.length):
            otp += random.choice(digits)
        return otp
otp_length = int(input("Enter the length of the OTP: "))
otp_generator = OTPGenerator(otp_length)
otp = otp_generator.generate_otp()
print("Generated OTP:", otp)



# Another Simple way using a match case
import random
otp_length = int(input("Enter the length of the OTP: "))
match otp_length:
    case length if length > 0:
        otp = ''.join(random.choices('0123456789', k=length))
        print("Generated OTP:", otp)
    case _:
        print("Invalid input: Length must be a positive integer.")



# Another Simple way using a map function
import random
def generate_otp(length):
    digits = "0123456789"
    otp = ""
    for _ in range(length):
        otp += random.choice(digits)
    return otp
otp_length = int(input("Enter the length of the OTP: "))
otp = map(lambda length: generate_otp(length), [otp_length])
print("Generated OTP:", list(otp)[0])



# Another Simple way using a list comprehension
import random
otp_length = int(input("Enter the length of the OTP: "))
otp = ''.join(random.choice('0123456789') for _ in range(otp_length))
print("Generated OTP:", otp)



# Best way to generate OTP using secrets module
import secrets
def generate_secure_otp(length):
    digits = "0123456789"
    otp = ''.join(secrets.choice(digits) for _ in range(length))
    return otp
otp_length = int(input("Enter the length of the OTP: "))
otp = generate_secure_otp(otp_length)
print("Generated OTP:", otp)