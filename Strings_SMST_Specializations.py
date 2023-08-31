# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:18:04 2023

@author: Mandal
"""

def main():
    department_name = "School of Medical Science and Technology"
    print("Welcome to the", department_name)
    
    n = int(input("Enter the number of specializations: "))
    specializations = []

    for i in range(n):
        specialization = input(f"Enter the name of specialization {i + 1}: ")
        specializations.append(specialization)
    
    print("\nDepartment:", department_name)
    print("Specializations:", ", ".join(specializations))

if __name__ == "__main__":
    main()
