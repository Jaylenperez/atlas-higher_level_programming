#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurences of an element in a list with another element.
    
    Args:
        my_list (list): The initial list.
        search: The element to be replaced.
        replace: The new element to replace with.
        
    Returns:
        list: A new list with all occurrences of 'search' replaced with 'replace'.
    """
    return [replace if x == search else x for x in my_list]

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)
