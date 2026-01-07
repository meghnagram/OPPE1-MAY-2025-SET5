def excel_index(column: str) -> int:
    """Returns the 1-based column index of the excel column.

    Args:
        column (str): The Excel column name (e.g., "A", "Z", "AA", "AB", etc.).

    Returns:
        int: The 1-based column index.
    """
    

    
    index = 0
    for char in column:
        index = index * 26 + (ord(char) - ord('A') + 1)
    return index

# #Another Method:
# def excel_index(column: str) -> int:
    
#     sum=0
#     for i in column:
#         sum =sum*26+ord(i)-64
#     return (sum)

# Convert Excel Column Name to 1-Based Index
# Write a function excel_index that takes an Excel column name (e.g., "A", "Z", "AA", "AB", ..., "ZZZ") and returns its corresponding 1-based index. This function should correctly handle column names beyond "Z", following the Excel column numbering system.

# Example

# excel_column_to_index("A") #1

  
