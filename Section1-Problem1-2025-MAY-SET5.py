

def point_position_relative_to_line(a, b, c, x, y) -> int:
    '''
    Determine the position of point (x, y) relative to the line ax + by + c = 0.

    Returns:
    +1 if the point is above the line,
    -1 if the point is below the line,
    0 if the point is on the line.

    Examples:
    >>> point_position_relative_to_line(1, -1, 0, 2, 1)
    1
    >>> point_position_relative_to_line(-1, -1, -1, 0, 0)
    -1
    >>> point_position_relative_to_line(2, -1, -4, 2, 0)
    0

    Args:
        a : Coefficient of x in line equation
        b : Coefficient of y in line equation
        c : Constant term in line equation
        x : x-coordinate of the point
        y : y-coordinate of the point

    Returns:
        int: +1, -1, or 0 based on the position of the point relative to the line
    '''
    
    
    position = a * x + b * y + c
    if position > 0:
        return 1
    elif position < 0:
        return -1
    else:
        return 0
    

# #Another Method:



# def point_position_relative_to_line(a, b, c, x, y) -> int:
#     sum=a*x+b*y+c 
#     if sum==0:
#         return(0)
#     if sum<0:
#         return(-1)
#     if sum>0:
#         return(+1)

# Position of a Point Relative to a Line
# Write a function point_position_relative_to_line(a, b, c, x, y) -> int that determines the position of a point (x, y) with respect to a line described by the equation ax + by + c = 0.

# The function should return:

# +1 if the point is above the line
# -1 if the point is below the line
# 0 if the point is on the line
# Note:

# A point (x, y) is considered on the line if substituting x and y into the equation results in 0.
# A point is above the line if the value of ax + by + c > 0 and below the line if ax + by + c < 0.
# Example

# >>> point_position_relative_to_line(1, -1, 0, 2, 1)
# 1
# >>> point_position_relative_to_line(-1, -1, -1, 0, 0)
# -1
# >>> point_position_relative_to_line(2, -1, -4, 2, 0)
# 0


