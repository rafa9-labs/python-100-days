
# 197 list comprehension -----------------------------------
def fn1():
    numbers = [1,2,3]
    new_list = [n+1 for n in numbers]
    print(new_list)

def fn2():
    name = 'Angela'
    letters_list = [l for l in name]
    print(letters_list)
    
def fn3():
    l_n = range(1, 5)
    l_2n = [n*2 for n in l_n]
    print(l_2n)
    
        
def fn4():
    names = ['aaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaa']
    short_names = [name.upper() for name in names if len(name) <= 4]
    print(short_names)

# 199 dict comprehension ------------------------------------------------

def fn5():
    import random
    names = ["dog", "cat", "bob", "tic", "ana"]
    dict_grades =  {name: random.randint(1, 100) for name in names}
    print(dict_grades)
    
    passed_grades = {name:grade for (name, grade) in dict_grades.items() if grade > 50}
    print(passed_grades)

# 200 iterate through Pandas DataFrame ------------------------------------

def fn6():
    import random
    names = ["dog", "cat", "bob", "tic", "ana"]
    dict_grades =  {name: random.randint(1, 100) for name in names}
    
    import pandas as pd
    df_student = pd.DataFrame(
        list(dict_grades.items()),
        columns=["student", "grade"])
    
    # Loop through each of the rows in the data frame
    for (inx, row) in df_student.iterrows():
        if row.student == "dog":
            print("hi student no %s! %s you had a grade of %s" % (inx+1, row.student, row.grade))


if __name__ == "__main__": 
    # fn1()
    # fn2()
    # fn3()
    # fn4()
    # fn5()
    fn6()
    