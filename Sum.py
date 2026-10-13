"""
Program: Sum of Two Numbers
Description:
    This program accepts two integer values from the user and calculates
    their sum using a class.

Input:
    Two integer values.

Output:
    Displays the sum of the two entered numbers.

Author: CRD
"""


class SumOfTwoNumbers:
    """
    A class to accept two numbers and calculate their sum.
    """

    # Class variables
    no_1 = 25
    no_2 = 35

    def input_values(self):
        """
        Accept two integer values from the user.

        Prompts the user to enter two numbers and stores them
        in the instance variables.

        Returns:
            None
        """
        self.no_1 = int(input("Enter First No : "))
        self.no_2 = int(input("Enter Second No : "))

    def sum_of_two_numbers(self):
        """
        Calculate and display the sum of two numbers.

        Returns:
            None
        """
        total = self.no_1 + self.no_2
        print("Sum:", total)


if __name__ == "__main__":
    """
    Program execution starts here.
    """
    sum_of_numbers = SumOfTwoNumbers()
    sum_of_numbers.input_values()
    sum_of_numbers.sum_of_two_numbers()
