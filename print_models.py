def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print("Printing models: "+current_designs)
        completed_models.append(current_designs)
def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)