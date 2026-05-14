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
otp = ''.join(random.choices('0123456789', k=otp_length))  # random.choices() returns a list of k elements chosen from the population. We need to join the list to get the OTP as a string.
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
            otp += random.choice(digits) # random.choice() returns a random element from the non-empty sequence. We need to concatenate the chosen digit to the otp string in each iteration.
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



# Number guessing Game
import random
number_to_guess = random.randint(1, 10)
user_guess = int(input("Guess a number between 1 and 10: "))
if user_guess == number_to_guess:
    print("Congratulations! You guessed the correct number.")
else:
    print("Sorry, the correct number was:", number_to_guess)



# random module methods and their use with examples
import random
# random.randint(a, b) - Returns a random integer N such that a <= N <= b
random_integer = random.randint(1, 100)
print("Random Integer between 1 and 100:", random_integer)
# random.choice(seq) - Returns a random element from the non-empty sequence seq
random_element = random.choice(['apple', 'banana', 'cherry'])
print("Randomly chosen element from the list:", random_element)
# random.choices(population, weights=None, k=1) - Returns a list of k elements chosen from the population with optional weights
random_elements = random.choices(['red', 'green', 'blue'], weights=[0.5, 0.3, 0.2], k=5)
print("Randomly chosen elements with weights:", random_elements)
# random.shuffle(x) - Shuffles the sequence x in place
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)
# random.sample(population, k) - Returns a list of k unique elements chosen from the population
random_sample = random.sample(range(1, 50), 5)
print("Random sample of 5 unique numbers between 1 and 50:", random_sample)
# random.random() - Returns a random float in the range [0.0, 1.0)
random_float = random.random()
print("Random float between 0.0 and 1.0:", random_float)
# random.uniform(a, b) - Returns a random float N such that a <= N <= b
random_uniform = random.uniform(1.0, 10.0)
print("Random float between 1.0 and 10.0:", random_uniform)
# random.seed(a=None) - Initializes the random number generator with a seed
random.seed(42)
print("Random integer with seed 42:",   random.randint(1, 100))
# random.getrandbits(n) - Returns a random integer with n random bits
random_bits = random.getrandbits(8)
print("Random integer with 8 random bits:", random_bits)
# random.randrange(start, stop=None, step=1) - Returns a randomly selected element from range(start, stop, step)
random_range = random.randrange(1, 10, 2)
print("Randomly selected element from range(1, 10, 2):", random_range)
# random.getstate() and random.setstate(state) - Get and set the internal state of the random number generator
state = random.getstate()
random.setstate(state)
print("Random integer after setting state:", random.randint(1, 100))
# random.seed() - Resets the random number generator to a random state
random.seed()
print("Random integer after resetting seed:", random.randint(1, 100))