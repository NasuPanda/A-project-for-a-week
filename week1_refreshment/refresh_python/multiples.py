def solution(number):
    # If the number is negative, return 0
    if number < 0:
        return 0

    sum = 0

    # Sum of all the multiples of 3 or 5 *below* the number
    for i in range(1, number):
        if i % 5 == 0:
            sum = sum + i
        elif i % 3 == 0:
            sum = sum + i

    return sum
