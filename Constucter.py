"""
Program: Constructor Demonstration
Description:
    This program demonstrates the behavior of constructors and destructors
    in Python. It also illustrates that Python does not support constructor
    overloading. If multiple constructors are defined, the last one overrides
    the previous ones.

Input:
    None

Output:
    Displays a message when the object is destroyed.

Author: CRD
"""


class DemoConstructor:
    """
    A class to demonstrate constructors and destructors in Python.

    Note:
        Python does not support constructor overloading. Therefore,
        the second __init__() method replaces the first one.
    """

    def __init__(self, name):
        """
        Initialize the object with a name.

        Args:
            name (str): Name of the object.

        Returns:
            None
        """
        self.name = name

    def __init__(self):
        """
        Default constructor.

        Note:
            This constructor overrides the previous __init__(name)
            constructor. As a result, the 'name' attribute is not created.

        Returns:
            None
        """
        pass

    def show_name(self):
        """
        Display the stored name.

        Returns:
            None
        """
        print("Name:", self.name)

    def run(self):
        """
        Execute the main functionality of the class.

        Returns:
            None
        """
        pass

    def __del__(self):
        """
        Destructor.

        Called automatically when the object is about to be destroyed.

        Returns:
            None
        """
        print("I am deleting class")


if __name__ == "__main__":
    """
    Program execution starts here.
    """
    demo_constructor = DemoConstructor()
    demo_constructor.run()