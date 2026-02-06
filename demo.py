"""
Demo module for triangle validation.

This module provides functionality to determine if three given sides
can form a valid triangle using the triangle inequality theorem.
"""


def is_triangle(a, b, c):
    """
    Determine if three sides can form a valid triangle.
    
    A valid triangle must satisfy the triangle inequality theorem:
    - The sum of any two sides must be greater than the third side
    
    Args:
        a (float): Length of first side
        b (float): Length of second side
        c (float): Length of third side
    
    Returns:
        bool: True if the sides form a valid triangle, False otherwise
    """
    if ((a + b > c) and
        (a + c > b) and
        (b + c > a)):
        return True
    return False


def main():
    """
    Main function that prompts user for three sides and determines
    if they form a valid triangle.
    """
    print("Enter side 1: ")
    side_1 = int(input())
    
    print("Enter side 2: ")
    side_2 = int(input())
    
    print("Enter side 3: ")
    side_3 = int(input())
    
    if is_triangle(side_1, side_2, side_3):
        print("This is a triangle.")
    else:
        print("This is not a triangle.")


if __name__ == "__main__":
    main()
