# your code goes here
def multiplier_of(multiplier):
    def _multiply_with(number):
        return multiplier * number
    return _multiply_with

multiply_with_5 = multiplier_of(5)
multiply_with_5(9)
