# counting even numbers in range
# by yara

start = int(input("please enter the start number: "))
end = int(input("please enter the end number: "))

count_even = 0

for num in range(start + 1, end - 1):
    if num % 2 == 0:
        print(num)
        count_even += 1

print("\nthe count of even numbers is {}".format(count_even))

# end of code
