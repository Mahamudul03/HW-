# Odd and Even :
    even_sum: int = sum(n for n in numbers if n % 2 == 0)
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return even_sum, odd_sum

# Example usage
numbers_list = [1, 2, 3, 4, 5, 6, 7,8,9]
even_sum, odd_sum = sum_even_odd(numbers_list)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
