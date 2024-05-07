#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if the index is within the range of both lists
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)
                continue

            # Check if the elements are integers or floats
            if not (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
                print("wrong type")
                result.append(0)
                continue

            # Perform division
            if my_list_2[i] == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(my_list_1[i] / my_list_2[i])
        except Exception as e:
            print(f"An error occurred: {e}")
            result.append(0)
        finally:
            # This block will execute regardless of whether an exception was raised or not
            pass

    return result