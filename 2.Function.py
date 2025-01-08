# Sum even and odd numbers 
def sum_even_odd(numbers):
    even_sum = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return even_sum, odd_sum
numbers_list = [1, 2, 3, 4, 5, 6]
even_sum, odd_sum = sum_even_odd(numbers_list)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
