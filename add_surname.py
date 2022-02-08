# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 2/7/2022
#
# Write a function named add_surname that
# takes as a parameter a list of first names. It should use a list comprehension to return a list that contains only
# those names that start with a "K", but with the surname "Kardashian" added to each one, with a space between the
# first and last names.

def add_surname(list_names):
    """ Returns a new list with the names starting with K plus the surname Kardashian."""
    return [x + " Kardashian" for x in list_names if x.startswith("K")]


""" Testing
list_names = ["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]
print(add_surname(list_names))
"""
