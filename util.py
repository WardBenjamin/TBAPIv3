def gen_model(class_name, json):
    print('class ' + class_name + ":")
    print('    def __init__(self, json):')
    for key in json:
        print("        self." + key + " = json.get('" + key + "')")
