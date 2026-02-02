# ---------------------------------------------------------------------------------------------------------------------------------------
# with open("a_file.txt") as file:
#     file.read()
    
# Traceback (most recent call last):
#   File "c:\Users\rafa\projects\python-100-days\day_30_errors_exceptions_json\main.py", line 1, in <module>
#     with open("a_file.txt") as file:
#          ^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'

# Simple try and except
# try:
#     with open("a_file.txt") as file:
#         file.read()
# except:
#     print("There was an error.")
    
# We can specify the actual errors we have.
# try: 
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["false key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is a error i made up")

# BMI calculator
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should not be above 3 meters.")
bmi = weight / height ** 2
print(bmi)


# ---------------------------------------------------------------------------------------------------------------------------------------
# a_dict =  {"key": "value"}
# a_value = a_dict["non_existent_key"]

# PS C:\Users\rafa\projects\python-100-days> & C:/Users/rafa/AppData/Local/Programs/Python/Python312/python.exe c:/Users/rafa/projects/python-100-days/day_30_errors_exceptions_json/main.py
# Traceback (most recent call last):
#   File "c:\Users\rafa\projects\python-100-days\day_30_errors_exceptions_json\main.py", line 12, in <module>
#     a_value = a_dict["non_existent_key"]
#               ~~~~~~^^^^^^^^^^^^^^^^^^^^
# KeyError: 'non_existent_key'
# ---------------------------------------------------------------------------------------------------------------------------------------
# fruit_list = [1,2,3,4]
# fruit = fruit_list[4]

# PS C:\Users\rafa\projects\python-100-days> & C:/Users/rafa/AppData/Local/Programs/Python/Python312/python.exe c:/Users/rafa/projects/python-100-days/day_30_errors_exceptions_json/main.py
# Traceback (most recent call last):
#   File "c:\Users\rafa\projects\python-100-days\day_30_errors_exceptions_json\main.py", line 22, in <module>
#     fruit = fruit_list[4]
#             ~~~~~~~~~~^^^
# IndexError: list index out of range
# ---------------------------------------------------------------------------------------------------------------------------------------
# text = "abc"
# print(text + 5)

# PS C:\Users\rafa\projects\python-100-days> & C:/Users/rafa/AppData/Local/Programs/Python/Python312/python.exe c:/Users/rafa/projects/python-100-days/day_30_errors_exceptions_json/main.py
# Traceback (most recent call last):
#   File "c:\Users\rafa\projects\python-100-days\day_30_errors_exceptions_json\main.py", line 32, in <module>
#     print(text + 5)
#           ~~~~~^~~
# TypeError: can only concatenate str (not "int") to str
# ---------------------------------------------------------------------------------------------------------------------------------------

# Everything that can go wrong will eventually go wrong.