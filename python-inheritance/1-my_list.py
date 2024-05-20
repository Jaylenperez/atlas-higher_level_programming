#!/usr/bin/python3

class MyList(list):
    """
    A subclass of list that overrides the default behavior to include a method for printing the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        
        This method iterates over the list, sorts it, and then prints it.
        """
        # Sort the list in place
        self.sort()

        # Print the sorted list
        print(self)


# Example usage
if __name__ == "__main__":
    MyList = __import__('1-my_list').MyList

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
