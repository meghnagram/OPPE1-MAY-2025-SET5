
def expand_sum_of_products(expr: str) -> str:
    '''
    Given a string expression of the form "(a+b)(c+d)", expand it into
    a sum of products string "a*c + a*d + b*c + b*d".

    Examples:
    >>> expand_sum_of_products("(a+b)(c+d)")
    "a*c + a*d + b*c + b*d"
    >>> expand_sum_of_products("(x+y)(z+w)")
    "x*z + x*w + y*z + y*w"
    >>> expand_sum_of_products("(1+5)(10+12)")
    "1*10 + 1*12 + 5*10 + 5*12"

    Args:
        expr (str): A string representation of a polynomial expression.

    Returns:
        str: A formatted string with expanded sum of products.
    '''
    
    
    terms = expr.replace(' ','').strip("()").split(")(")
    a,b = terms[0].split('+')
    c,d = terms[1].split('+')

    return f"{a}*{c} + {a}*{d} + {b}*{c} + {b}*{d}"

# #Another Method


# def expand_sum_of_products(expr: str) -> str:
  
   
#     l=[]
#     s=''
#     for i in expr:
#         if i.isalnum()==True:
#             s=s+i
#         else:
#             l.append(s)
#             s=""
#     a=l[1]
#     b=l[2]
#     c=l[4]
#     d=l[5]
            
#     s=f"{a}*{c} + {a}*{d} + {b}*{c} + {b}*{d}"
#     return(s)       

#   Expand Sum of Products
# Write a function expand_sum_of_products(expr: str) -> str that takes a string representation of a product of sum of two terms in the form "(a+b)(c+d)", and expands it into the sum of products in the form "a*c + a*d + b*c + b*d". The output should be a properly formatted string of the expanded form.

# The input can have spaces in between the symbols and operators. The spacing and ordering of the terms should be exacty as given in the format.

# There will be always + sign between the values in a term.

# Example

# >>> expand_sum_of_products("(a+b)(c+d)")
# "a*c + a*d + b*c + b*d"
# >>> expand_sum_of_products("(x+y)(z+w)")
# "x*z + x*w + y*z + y*w"
# >>> expand_sum_of_products("(1+5)(10+12)")
# "1*10 + 1*12 + 5*10 + 5*12"
            
