# Reverse a Number
num = int(input("Enter a Number : "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed Number:", reverse)

# Time Complexity : O(log10(n))
# Space Complexity : O(1)

# Another way to reverse a number using String Slicing
num = int(input("Enter a Number : "))
reverse = str(num)[::-1]
print("Reversed Number:", reverse)
# Time Complexity : O(n)
# Space Complexity : O(n) because of string conversion and slicing.