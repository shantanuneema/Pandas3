import pandas as pd

# Solution to Problem 1 
def func(x):
    if x[0] % 2 == 0 or x[1].startswith("M"):
        return 0
    else: return x[2]

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees[["employee_id", "name", "salary"]].apply(lambda x: func(x), axis=1)
    return employees[["employee_id", "bonus"]].sort_values("employee_id")

# Solution to Problem 2
def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].apply(lambda x: x[0].upper() + x[1: ].lower())
    return users.sort_values("user_id")

# Solution to Problem 3
def find_diabetes(x):
    lst = x.split(" ")
    if len([v for v in lst if v.startswith("DIAB1")]) > 0:
        return True
    return False

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    s = patients["conditions"].apply(lambda x: find_diabetes(x))
    return patients[s]
