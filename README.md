# NumPy Analyzer

## Project Overview

NumPy Analyzer is a menu-driven Python application developed using:

- Python Object-Oriented Programming (OOP)
- NumPy Library
- Exception Handling
- Input Validation

This project allows users to create and analyze NumPy arrays through an interactive console menu.

The application supports array creation, mathematical operations, searching, sorting, filtering, statistical analysis, and array manipulation.

---

# Features

## 1. Array Creation

The program supports creating different types of NumPy arrays:

### 1D Array

Example:


[10 20 30 40]


User provides:
- Number of elements
- Values

---

### 2D Array

Example:


[[1 2 3]
[4 5 6]]


User provides:
- Number of rows
- Number of columns
- Values

---

### 3D Array

Example:


[
[[1 2]
[3 4]]

[[5 6]
[7 8]]
]


User provides:
- Depth
- Rows
- Columns
- Values

---

# 2. Array Operations

The project provides:

## Display Array

Shows:

- Array values
- Dimension
- Shape
- Size
- Data type


Example:


Dimension : 2
Shape : (3,3)
Size : 9
Datatype : int64


---

## Indexing

Access individual elements from:

- 1D arrays
- 2D arrays
- 3D arrays


Example:


Enter Row Index : 1
Enter Column Index : 2

Element = 6


---

## Slicing

Extract portions of arrays.

Supported:

- 1D slicing
- 2D slicing
- 3D slicing

Example:


array[1:3]


---

# 3. Mathematical Operations

The application supports:

## Addition

Example:


A + B


---

## Subtraction

Example:


A - B


---

## Multiplication

Example:


A * B


---

## Division

Example:


A / B


Includes division error handling.

---

## Dot Product

Uses:

```python
np.dot()
Matrix Multiplication

Uses:

np.matmul()
4. Combine and Split Arrays
Combine Arrays

Supported operations:

Vertical Stack

Using:

np.vstack()
Horizontal Stack

Using:

np.hstack()
Concatenate

Using:

np.concatenate()
Split Array

Uses:

np.array_split()

Allows dividing an array into multiple parts.

5. Search, Sort and Filter
Search Element

Uses:

np.argwhere()

Finds the position of an element.

Example:

Search value: 5

Found at:
(1,2)
Sorting

Supported:

Ascending Order

Using:

np.sort()
Descending Order

Using:

np.flip()
Filtering

Supported conditions:

Greater than
Less than
Equal to

Example:

Array > 50
6. Aggregate Functions

The project calculates:

Sum

Using:

np.sum()
Mean

Using:

np.mean()
Median

Using:

np.median()
Standard Deviation

Using:

np.std()
Variance

Using:

np.var()
7. Statistical Functions
Minimum Value

Using:

np.min()
Maximum Value

Using:

np.max()
Percentile

Using:

np.percentile()
Correlation Coefficient

Using:

np.corrcoef()
Object-Oriented Programming Concepts Used
Class

Main class:

DataAnalytics
Constructor

Used for initializing the array:

def __init__(self):
    self.array = None
Encapsulation

Private method:

__check_array()

Checks whether an array exists.

Static Method

Example:

line()

Used for printing separators.

Class Method

Example:

title()

Used for displaying project titles.

Input Validation

The project contains two input methods.

get_int()

Used for:

Menu choices
Index values
Searching values

Example:

Enter choice: abc

Output:
Please enter a valid integer.
get_positive_int()

Used for:

Array size
Rows
Columns
Depth
Split parts

Prevents:

-5
0
Error Handling

The project handles:

Invalid Input

Example:

Enter choice: hello

Handled using:

try
except
Invalid Index

Prevents array indexing errors.

Division By Zero

Prevents:

division by zero
Installation

Install NumPy:

pip install numpy
Running The Project

Run:

python numpy_analyzer.py
Main Menu

Example:

===============================

WELCOME TO NUMPY ANALYZER

===============================


1. Create NumPy Array

2. Mathematical Operations

3. Combine / Split Arrays

4. Search / Sort / Filter

5. Aggregate & Statistics

6. Exit

Project Structure
NumPy Analyzer

│
├── numpy_analyzer.py
│
├── README.md
│
└── requirements.txt

Requirements

Python:

3.x

Library:

numpy
Future Improvements

Possible upgrades:

GUI version using Tkinter
Graph plotting
CSV file support
Data visualization
Database connection
Author

Developed as a Python OOP + NumPy project.

License

Educational project.


This README matches your actual project features and is suitable for submission/documentation.
