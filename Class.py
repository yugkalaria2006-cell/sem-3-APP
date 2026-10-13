""" 
Program: Student Name Input and Display 
Description: 
    This program accepts a student name from the user and displays it on the screen 
    using a simple class. 
 
Input: 
    Student Name (string) 
 
Output: 
    Displays the entered student name. 
 
Author: CRD
""" 
 
 
class Simple: 
    """ 
    A class to accept and display a student's name. 
    """ 
 
    # Class variable 
    var_input = "Chaitnya" 
 
    def input_name(self): 
        """ 
        Accept a student name from the user and store it. 
 
        Prompts the user to enter a student name and stores the input 
        in the instance variable. 
 
        Returns: 
            None 
        """ 
        self.var_input = input("Enter the Student Name: ") 
 
    def show_name(self): 
        """ 
        Display the stored student name. 
 
        Prints the student name entered by the user. 
 
        Returns: 
            None 
        """ 
        print("Student Name:", self.var_input) 
 
 
if __name__ == "__main__": 
    """ 
    Program execution starts here. 
    """ 
    simple = Simple() 
    simple.input_name() 
    simple.show_name()