# Project : NumPy Analyzer
# Developed Using :
# • Python OOP
# • NumPy


import numpy as np


class DataAnalytics:
    """
    NumPy Analyzer
    Menu Driven Project using OOP and NumPy
    """

    
                                                                        # Constructor


    def __init__(self):
        self.array = None

    
                                                                # Private Method (Encapsulation)
    
    def __check_array(self):
        """
        Checks whether array exists.
        """

        if self.array is None:
            print("\nCreate an array first.\n")
            return False

        return True

    

                                                                 # Static Method
    

    @staticmethod
    def line():
        print("=" * 60)

    

                                                # Class Method
    

    @classmethod
    def title(cls):

        cls.line()

        print("            NUMPY ANALYZER")

        cls.line()

                                                # Safe Integer Input

    @staticmethod
    def get_int(message):

        while True:

            try:
                return int(input(message))

            except ValueError:

                print("Please enter a valid integer.")
                                            # Positive Integer Input

    def get_positive_int(self, message):

        while True:

            value = self.get_int(message)

            if value > 0:
                return value

            print("Please enter a positive integer.")

    
                                                # Read Elements
    
    def read_elements(self, total):

        while True:

            try:

                values = list(
                    map(
                        int,
                        input(
                            f"Enter {total} elements separated by space : "
                        ).split()
                    )
                )

                if len(values) != total:
                    print(
                        f"You must enter exactly {total} values."
                    )
                    continue

                return values

            except ValueError:

                print("Invalid input.")

    

                                             # Main Menu
    

    def menu(self):

        while True:

            self.welcome()

            print("1. Create NumPy Array")
            print("2. Mathematical Operations")
            print("3. Combine / Split Arrays")
            print("4. Search / Sort / Filter")
            print("5. Aggregate & Statistics")
            print("6. Exit")

            self.line()

            choice = self.get_int(
                "Enter your choice : "
            )

            if choice == 1:
                self.create_array()

            elif choice == 2:
                self.math_operations()

            elif choice == 3:
                self.combine_split()

            elif choice == 4:
                self.search_sort_filter()

            elif choice == 5:
                self.statistics_menu()

            elif choice == 6:
                if self.confirm_exit():
                    self.goodbye() 
                    break

            else:

                print("\nInvalid Choice.\n")

        

                                                # Create NumPy Array
    

    def create_array(self):

        while True:

            self.line()

            print("CREATE NUMPY ARRAY")
            self.line()

            print("1. Create 1D Array")
            print("2. Create 2D Array")
            print("3. Create 3D Array")
            print("4. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:
                self.create_1d()

            elif choice == 2:
                self.create_2d()

            elif choice == 3:
                self.create_3d()

            elif choice == 4:
                return

            else:
                print("Invalid Choice.")

    

                                             # Create 1D Array
    

    def create_1d(self):

        size = self.get_positive_int("Enter number of elements : ")

        values = self.read_elements(size)

        self.array = np.array(values)

        print("\n1D Array Created Successfully")
        print(self.array)

        self.array_operations()

    

                                             # Create 2D Array
    

    def create_2d(self):

        rows = self.get_positive_int("Enter number of rows : ")
        cols = self.get_positive_int("Enter number of columns : ")

        total = rows * cols

        values = self.read_elements(total)

        self.array = np.array(values).reshape(rows, cols)

        print("\n2D Array Created Successfully")
        print(self.array)

        self.array_operations()

    

                                                # Create 3D Array
    

    def create_3d(self):

        depth = self.get_positive_int("Enter depth : ")
        rows = self.get_positive_int("Enter rows : ")
        cols = self.get_positive_int("Enter columns : ")

        total = depth * rows * cols

        values = self.read_elements(total)

        self.array = np.array(values).reshape(depth, rows, cols)

        print("\n3D Array Created Successfully")
        print(self.array)

        self.array_operations()

                                                 # display / slicing / index 
    
    def array_operations(self):

        while True:

            self.line()

            print("ARRAY OPERATIONS")

            self.line()

            print("1. Display Array")
            print("2. Indexing")
            print("3. Slicing")
            print("4. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:
                self.display_array()

            elif choice == 2:
                self.indexing()

            elif choice == 3:
                self.slicing()

            elif choice == 4:
                break

            else:
                print("Invalid Choice.")

    
                                                # Display Array
    
    def display_array(self):

        if not self.__check_array():
            return

        self.line()

        print("ARRAY")

        self.line()

        print(self.array)

        print("\nDimension :", self.array.ndim)
        print("Shape :", self.array.shape)
        print("Size :", self.array.size)
        print("Data Type :", self.array.dtype)


                                                # Indexing
    
    def indexing(self):

        if not self.__check_array():
            return

        print("\nCurrent Array\n")
        print(self.array)

        if self.array.ndim == 1:

            index = self.get_int("Enter index : ")

            try:
                print("Element =", self.array[index])

            except IndexError:
                print("Invalid Index.")

        elif self.array.ndim == 2:

            row = self.get_int("Enter Row Index : ")
            col = self.get_int("Enter Column Index : ")

            try:

                print("Element =", self.array[row][col])

                print("\nSelected Row")
                print(self.array[row])

                print("\nSelected Column")
                print(self.array[:, col])

            except IndexError:
                print("Invalid Index.")

        else:

            depth = self.get_int("Enter Depth Index : ")
            row = self.get_int("Enter Row Index : ")
            col = self.get_int("Enter Column Index : ")

            try:

                print("Element =", self.array[depth][row][col])

            except IndexError:
                print("Invalid Index.")

    
    # Slicing
    
    def slicing(self):

        if not self.__check_array():
            return

        print("\nCurrent Array\n")
        print(self.array)

        try:

            if self.array.ndim == 1:

                start = self.get_int("Start Index : ")
                end = self.get_int("End Index : ")

                print("\nSliced Array")
                print(self.array[start:end])

            elif self.array.ndim == 2:

                rs = self.get_int("Row Start : ")
                re = self.get_int("Row End : ")

                cs = self.get_int("Column Start : ")
                ce = self.get_int("Column End : ")

                print("\nSliced Array")
                print(self.array[rs:re, cs:ce])

            else:

                ds = self.get_int("Depth Start : ")
                de = self.get_int("Depth End : ")

                rs = self.get_int("Row Start : ")
                re = self.get_int("Row End : ")

                cs = self.get_int("Column Start : ")
                ce = self.get_int("Column End : ")

                print("\nSliced Array")
                print(self.array[ds:de, rs:re, cs:ce])

        except Exception:

            print("Invalid Slice.")

        
    # Mathematical Operations Menu
    
    def math_operations(self):

        if not self.__check_array():
            return

        while True:

            self.line()
            print("MATHEMATICAL OPERATIONS")
            self.line()

            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Dot Product")
            print("6. Matrix Multiplication")
            print("7. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:
                self.addition()

            elif choice == 2:
                self.subtraction()

            elif choice == 3:
                self.multiplication()

            elif choice == 4:
                self.division()

            elif choice == 5:
                self.dot_product()

            elif choice == 6:
                self.matrix_multiplication()

            elif choice == 7:
                break

            else:
                print("Invalid Choice.")

    
    # Read Second Array
    
    def second_array(self):

        total = self.array.size

        print("\nEnter values for second array")

        values = self.read_elements(total)

        return np.array(values).reshape(self.array.shape)

    
    # Addition
    
    def addition(self):

        second = self.second_array()

        print("\nFirst Array")
        print(self.array)

        print("\nSecond Array")
        print(second)

        print("\nResult")
        print(self.array + second)

    
    # Subtraction
    
    def subtraction(self):

        second = self.second_array()

        print("\nFirst Array")
        print(self.array)

        print("\nSecond Array")
        print(second)

        print("\nResult")
        print(self.array - second)

    
    # Multiplication
    
    def multiplication(self):

        second = self.second_array()

        print("\nFirst Array")
        print(self.array)

        print("\nSecond Array")
        print(second)

        print("\nResult")
        print(self.array * second)

    
    # Division
    
    def division(self):

        second = self.second_array()

        try:

            print("\nFirst Array")
            print(self.array)

            print("\nSecond Array")
            print(second)

            print("\nResult")
            print(self.array / second)

        except ZeroDivisionError:
            print("Division by zero is not possible.")

    
    # Dot Product
    
    def dot_product(self):

        if self.array.ndim != 2:
            print("\nDot Product requires a 2D array.")
            return

        rows = self.array.shape[0]
        cols = self.array.shape[1]

        print("\nEnter Second Matrix")

        values = self.read_elements(rows * cols)

        second = np.array(values).reshape(rows, cols)

        print("\nFirst Matrix")
        print(self.array)

        print("\nSecond Matrix")
        print(second)

        print("\nDot Product")
        print(np.dot(self.array, second.T))


    # Matrix Multiplication

    def matrix_multiplication(self):

        if self.array.ndim != 2:
            print("\nMatrix Multiplication requires a 2D array.")
            return

        cols = self.array.shape[1]

        rows2 = self.get_int("Rows of second matrix : ")
        cols2 = self.get_int("Columns of second matrix : ")

        if rows2 != cols:

            print("\nMatrix multiplication cannot be performed.")
            return

        values = self.read_elements(rows2 * cols2)

        second = np.array(values).reshape(rows2, cols2)

        print("\nFirst Matrix")
        print(self.array)

        print("\nSecond Matrix")
        print(second)

        print("\nResult")
        print(np.matmul(self.array, second))

        
    # Combine / Split Menu
    
    def combine_split(self):

        if not self.__check_array():
            return

        while True:

            self.line()
            print("COMBINE / SPLIT ARRAYS")
            self.line()

            print("1. Combine Arrays")
            print("2. Split Array")
            print("3. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:
                self.combine_arrays()

            elif choice == 2:
                self.split_array()

            elif choice == 3:
                break

            else:
                print("Invalid Choice.")

    
    # Combine Arrays
    
    def combine_arrays(self):

        print("\nCurrent Array")
        print(self.array)

        print("\nEnter another array of same shape.")

        total = self.array.size

        values = self.read_elements(total)

        second = np.array(values).reshape(self.array.shape)

        while True:

            self.line()
            print("COMBINE OPTIONS")
            self.line()

            print("1. Vertical Stack")
            print("2. Horizontal Stack")
            print("3. Concatenate")
            print("4. Back")

            choice = self.get_int("Enter your choice : ")

            try:

                if choice == 1:

                    print("\nVertical Stack\n")
                    print(np.vstack((self.array, second)))

                elif choice == 2:

                    print("\nHorizontal Stack\n")
                    print(np.hstack((self.array, second)))

                elif choice == 3:

                    print("\nConcatenated Array\n")
                    print(np.concatenate((self.array, second)))

                elif choice == 4:
                    break

                else:
                    print("Invalid Choice.")

            except ValueError:

                print("\nThese arrays cannot be combined using this operation.")

    
    # Split Array
    
    def split_array(self):

        print("\nCurrent Array")
        print(self.array)

        parts = self.get_int("\nEnter number of parts : ")

        try:

            result = np.array_split(self.array, parts)

            self.line()

            print("SPLIT RESULT")

            self.line()

            for i, item in enumerate(result, start=1):

                print(f"\nPart {i}")
                print(item)

        except Exception:

            print("Unable to split the array.")

        
    # Search / Sort / Filter Menu
    
    def search_sort_filter(self):

        if not self.__check_array():
            return

        while True:

            self.line()
            print("SEARCH / SORT / FILTER")
            self.line()

            print("1. Search Element")
            print("2. Sort Array")
            print("3. Filter Array")
            print("4. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:
                self.search_element()

            elif choice == 2:
                self.sort_array()

            elif choice == 3:
                self.filter_array()

            elif choice == 4:
                break

            else:
                print("Invalid Choice.")

    
    # Search Element
    
    def search_element(self):

        print("\nCurrent Array")
        print(self.array)

        value = self.get_int("\nEnter element to search : ")

        position = np.argwhere(self.array == value)

        if len(position) == 0:

            print("\nElement not found.")

        else:

            print("\nElement Found At:")

            for pos in position:
                print(tuple(pos))

    
    # Sort Array
    
    def sort_array(self):

        while True:

            self.line()

            print("SORT MENU")

            self.line()

            print("1. Ascending Order")
            print("2. Descending Order")
            print("3. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:

                print("\nSorted Array (Ascending)\n")
                print(np.sort(self.array))

            elif choice == 2:

                print("\nSorted Array (Descending)\n")

                if self.array.ndim == 1:
                    print(np.sort(self.array)[::-1])

                else:
                    print(np.flip(np.sort(self.array), axis=-1))

            elif choice == 3:
                break

            else:
                print("Invalid Choice.")

    
                                                # Filter Array
    
    def filter_array(self):

        while True:

            self.line()

            print("FILTER MENU")

            self.line()

            print("1. Greater Than")
            print("2. Less Than")
            print("3. Equal To")
            print("4. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 4:
                break

            value = self.get_int("Enter value : ")

            if choice == 1:

                result = self.array[self.array > value]

                print("\nFiltered Array")
                print(result)

            elif choice == 2:

                result = self.array[self.array < value]

                print("\nFiltered Array")
                print(result)

            elif choice == 3:

                result = self.array[self.array == value]

                print("\nFiltered Array")
                print(result)

            else:

                print("Invalid Choice.")

                                                # Aggregate & Statistics Menu
    
    def statistics_menu(self):

        if not self.__check_array():
            return

        while True:

            self.line()
            print("AGGREGATE & STATISTICS")
            self.line()

            print("1. Aggregate Functions")
            print("2. Statistical Functions")
            print("3. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:
                self.aggregate_functions()

            elif choice == 2:
                self.statistical_functions()

            elif choice == 3:
                break

            else:
                print("Invalid Choice.")

    
                                                # Aggregate Functions
    
    def aggregate_functions(self):

        while True:

            self.line()
            print("AGGREGATE FUNCTIONS")
            self.line()

            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:

                print("\nArray")
                print(self.array)

                print("\nSum =", np.sum(self.array))

            elif choice == 2:

                print("\nArray")
                print(self.array)

                print("\nMean =", np.mean(self.array))

            elif choice == 3:

                print("\nArray")
                print(self.array)

                print("\nMedian =", np.median(self.array))

            elif choice == 4:

                print("\nArray")
                print(self.array)

                print("\nStandard Deviation =", np.std(self.array))

            elif choice == 5:

                print("\nArray")
                print(self.array)

                print("\nVariance =", np.var(self.array))

            elif choice == 6:
                break

            else:
                print("Invalid Choice.")

       
                                                # Statistical Functions
    def statistical_functions(self):

        while True:

            self.line()
            print("STATISTICAL FUNCTIONS")
            self.line()

            print("1. Minimum")
            print("2. Maximum")
            print("3. Percentile")
            print("4. Correlation Coefficient")
            print("5. Back")

            choice = self.get_int("Enter your choice : ")

            if choice == 1:
                self.minimum_value()

            elif choice == 2:
                self.maximum_value()

            elif choice == 3:
                self.percentile_value()

            elif choice == 4:
                self.correlation()

            elif choice == 5:
                break

            else:
                print("Invalid Choice.")

                                                # Minimum Value
    def minimum_value(self):

        print("\nCurrent Array\n")
        print(self.array)

        print("\nMinimum Value :", np.min(self.array))

                                             # Maximum Value
    def maximum_value(self):

        print("\nCurrent Array\n")
        print(self.array)

        print("\nMaximum Value :", np.max(self.array))

                                             # Percentile
    def percentile_value(self):

        print("\nCurrent Array\n")
        print(self.array)

        percentile = self.get_int("Enter Percentile (0-100) : ")

        if percentile < 0 or percentile > 100:

            print("Percentile must be between 0 and 100.")
            return

        result = np.percentile(self.array, percentile)

        print(f"\n{percentile}th Percentile :", result)

                                                # Correlation Coefficient
    def correlation(self):

        if self.array.ndim != 2:

            print("\nCorrelation Coefficient requires a 2D array.")
            return

        if self.array.shape[0] < 2:

            print("\nAt least two rows are required.")
            return

        print("\nCurrent Array\n")
        print(self.array)

        print("\nCorrelation Coefficient Matrix\n")

        try:

            result = np.corrcoef(self.array)

            print(result)

        except Exception as e:

            print("Unable to calculate correlation.")
            print(e)

       
                                                # Display Current Array
    def show_current_array(self):

        if not self.__check_array():
            return

        self.line()
        print("CURRENT ARRAY")
        self.line()

        print(self.array)

        print("\nDimension :", self.array.ndim)
        print("Shape     :", self.array.shape)
        print("Size      :", self.array.size)
        print("Datatype  :", self.array.dtype)

                                             # Pause Program
    @staticmethod
    def pause():

        input("\nPress Enter to continue...")

                                                # Clear Screen
    @staticmethod
    def clear():

        print("\n" * 5)

                                             # Welcome Screen
    @classmethod
    def welcome(cls):

        cls.line()

        print("      WELCOME TO NUMPY ANALYZER")

        print("        OOP + NUMPY PROJECT")

        cls.line()

                                             # Goodbye Message
    @staticmethod
    def goodbye():

        print("\nThank You For Using NumPy Analyzer.")

        print("Project Completed Successfully.")

        print("Good Bye!")


                                             # Confirm Exit
    def confirm_exit(self):

        while True:

            choice = input("Are you sure you want to exit? (Y/N): ").strip().upper()

            if choice == "Y":
                return True

            elif choice == "N":
                return False

            else:
                print("Please enter Y or N.")

                                             # Print Section Header
    def header(self, title):

        self.line()
        print(title.center(60))
        self.line()

                                             # Reset Current Array
    def reset_array(self):

        self.array = None

        print("\nCurrent array has been cleared.")


                                            # Main Function

def main():

    analyzer = DataAnalytics()

    analyzer.menu()


# Program Starts Here

if __name__ == "__main__":

    main()