'''sys 
os 
math
datetime'''
import sys
import os
import datetime
import math

def separate_section(title):
    print("\n" + "="*20 + " " + title + " " + "="*20)

# =====================================================================
# 1. THE SYS MODULE
# =====================================================================
separate_section("1. sys Module")
# The sys module provides access to some variables used or maintained by the
# interpreter and to functions that interact strongly with the interpreter.

# 1.1 sys.argv - Command Line Arguments
print("sys.argv (Arguments passed to script):", sys.argv)

# 1.2 sys.platform - Platform Identifier
print("sys.platform (Operating System):", sys.platform)

# 1.3 sys.version - Python Version
print("sys.version (Python Version):", sys.version)

# 1.4 sys.path - Module Search Paths
print("\nFirst 3 search paths in sys.path:")
for path in sys.path[:3]:
    print(f"  - {path}")

# 1.5 sys.getsizeof() - Memory Footprint of Objects
num = 42
text = "Hello, World!"
lst = [1, 2, 3, 4, 5]
tup = (1, 2, 3, 4, 5)
print(f"\nMemory consumption (getsizeof):")
print(f"  Integer (42): {sys.getsizeof(num)} bytes")
print(f"  String ('Hello, World!'): {sys.getsizeof(text)} bytes")
print(f"  List [1, 2, 3, 4, 5]: {sys.getsizeof(lst)} bytes")
print(f"  Tuple (1, 2, 3, 4, 5): {sys.getsizeof(tup)} bytes")


# =====================================================================
# 2. THE OS MODULE
# =====================================================================
separate_section("2. os Module")
# The os module provides a portable way of using operating system dependent functionality.

# 2.1 os.getcwd() - Get Current Working Directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# 2.2 os.listdir() - List Directory Contents
print("\nFirst 5 files/folders in the current directory:")
entries = os.listdir(cwd)
# for entry in entries[:5]:
print(f"  - {entries}")

# 2.3 os.path methods - Joining, Existence, Types, Splitting
print("\nPath Operations (os.path):")
# Joining paths safely (handles platform-specific backslash or slash)
example_path = os.path.join(cwd, "some_folder", "test_file.txt")
print("  Joined Path:", example_path)

# Checking if path exists, is file, or is directory
print("  Does current directory exist?:", os.path.exists(cwd))
print("  Is current directory a folder?:", os.path.isdir(cwd))
print("  Is this script a file?:", os.path.isfile(__file__))


# 2.4 os.mkdir() & os.rmdir() - Directory management
temp_dir = os.path.join(cwd, "temp_demo_dir")
print("\nCreating/Deleting Directories:")
if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)
    print(f"  Created directory: {temp_dir}")
if os.path.exists(temp_dir):
    os.rmdir(temp_dir)
    print(f"  Removed directory: {temp_dir}")

print (os.name)


# =====================================================================
# 3. THE DATETIME MODULE
# =====================================================================
separate_section("3. datetime Module")
# The datetime module supplies classes for manipulating dates and times.

# 3.1 Getting Current Date and Time
now = datetime.datetime.now()
print("Current Date & Time (datetime.now()):", now)

# 3.2 Date Objects (Year, Month, Day)
today = datetime.date.today()
print("Today's Date (date.today()):", today)
print(f"Year: {today.year}, Month: {today.month}, Day: {today.day}")

# 3.3 Creating Specific Dates and Times
specific_datetime = datetime.datetime(2025, 12, 25, 18, 30, 0)
print("Specific Date/Time (Christmas 2025 6:30 PM):", specific_datetime)

# 3.4 Formatting Dates to Strings (strftime)
print("\nFormatted Dates (strftime):")
print("  YYYY-MM-DD format:", now.strftime("%Y-%m-%d"))
print("  Friendly weekday/month format:", now.strftime("%A, %d %B %Y"))
print("  12-Hour format with AM/PM:", now.strftime("%I:%M:%S %p"))

# 3.5 Parsing Strings to Dates (strptime)
date_string = "2026-07-15 14:45:00"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("\nParsing Strings (strptime):")
print("  Input string:", date_string)
print("  Parsed datetime object:", repr(parsed_datetime))

# 3.6 Timedelta - Date Arithmetic and Durations
print("\nDate Arithmetic (timedelta):")
today_date = datetime.date.today()
ten_days = datetime.timedelta(days=10)
future_date = today_date + ten_days
past_date = today_date - ten_days

print("  Today:", today_date)
print("  In 10 days:", future_date)
print("  10 days ago:", past_date)


# =====================================================================
# 4. THE MATH MODULE
# =====================================================================
separate_section("4. math Module")
# The math module provides access to mathematical functions defined by the C standard.

# 4.1 Constants
print("Math Constants:")
print("  math.pi (Pi):", math.pi)
print("  math.e (Euler's number):", math.e)
print("  math.tau (Tau = 2 * Pi):", math.tau)

# 4.2 Numeric Representations (ceil, floor, trunc, fabs)
val = -5.67
print("\nRounding & Absolute Values:")
print(f"  Original value: {val}")
print(f"  math.ceil({val}) (Smallest integer >= val):", math.ceil(val))
print(f"  math.floor({val}) (Largest integer <= val):", math.floor(val))
print(f"  math.trunc({val}) (Truncates decimal part):", math.trunc(val))
print(f"  math.fabs({val}) (Absolute value as float):", math.fabs(val))

# 4.3 Operations (factorial, gcd, isclose)
print("\nMathematical Operations:")
print("  math.factorial(5) (5! = 5*4*3*2*1):", math.factorial(5))
print("  math.gcd(24, 36) (Greatest Common Divisor):", math.gcd(24, 36))


# 4.4 Power & Logarithmic Functions
print("\nPower & Logarithmic Functions:")
print("  math.sqrt(64) (Square root):", math.sqrt(64))
print("  math.pow(2, 5) (2 raised to power of 5):", math.pow(2, 5))

# 4.5 Trigonometry & Angle Conversion
print("\nTrigonometry:")
angle_deg = 45
angle_rad = math.radians(angle_deg)
print(f"  Converting {angle_deg}° to radians: {angle_rad:.4f} radians")
print(f"  math.sin(math.radians(45)) (Sine of 45°):", math.sin(angle_rad))
print(f"  math.cos(math.radians(45)) (Cosine of 45°):", math.cos(angle_rad))
print(f"  Converting {angle_rad:.4f} radians back to degrees: {math.degrees(angle_rad)}°")