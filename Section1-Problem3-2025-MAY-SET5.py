def repeat_second_half(t: tuple) -> tuple:
    '''
    Given a tuple, return a new tuple where the second half is repeated 
    after the first half. If the tuple has an odd number of elements, 
    include the middle element in the first half.

    Examples:
    >>> repeat_second_half((1, 2, 3, 4, 5))
    (1, 2, 3, 4, 5, 4, 5)
    >>> repeat_second_half((10, 20, 30, 40))
    (10, 20, 30, 40, 30, 40)
    >>> repeat_second_half(('a', 'b', 'c', 'd', 'e', 'f'))
    ('a', 'b', 'c', 'd', 'e', 'f', 'e', 'f')
    >>> repeat_second_half((1, 2, 3))
    (1, 2, 3, 3)

    Args:
        t (tuple): A tuple with at least two elements

    Returns:
        tuple: A new tuple with repeated second half
    '''
    
    
    n = len(t)
    mid = (n + 1) // 2
    return t + t[mid:]
    


# #Another Method:

# def repeat_second_half(t: tuple) -> tuple:
#     s=list(t)
#     r=[]
#     divide=int(len(s)/2)
    
#     c=divide
        
#     for i in range(divide):
#         r.append(s[-c])
#         c=c-1
#     return(tuple(s+r))

# Repeat Second Half of a Tuple
# Write a function repeat_second_half(t) that takes a tuple t and returns a new tuple where the second half of the original tuple is repeated after the first half. If the tuple has an odd number of elements, the middle element should be included in the first half.

# Constraints

# The input tuple will contain at least two elements.
# The elements in the tuple can be of any type (integers, strings, etc.).
# NOTE: This is a function type question; you don't have to take input or print the output, just have to complete the required function definition.

# Example

# >>> repeat_second_half((1, 2, 3, 4, 5))
# (1, 2, 3, 4, 5, 4, 5)
# >>> repeat_second_half((10, 20, 30, 40))
# (10, 20, 30, 40, 30, 40)
# >>> repeat_second_half(('a', 'b', 'c', 'd', 'e', 'f'))
# ('a', 'b', 'c', 'd', 'e', 'f', 'd', 'e', 'f')
# >>> repeat_second_half((1, 2, 3))
# (1, 2, 3, 3)


