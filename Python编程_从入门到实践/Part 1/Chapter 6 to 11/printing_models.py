# -*- coding: utf-8 -*-
# cretae by o.c. 2018/7/24
from _for_ex import pt_title

pt_title('printing_models.py'.upper())


def print_model(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design.title())
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_model(unprinted_designs, completed_models)
show_completed_models(completed_models)
print("\n---unprinted designs ---".upper())
show_completed_models(unprinted_designs)