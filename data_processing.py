import json
import statistics
import random 

def read_imsitu_space():
    imsitu = json.load(open("imsitu_space.json"))

    nouns = imsitu["nouns"]
    verbs = imsitu["verbs"]

    random_key = random.choice(list(nouns.keys()))
    random_value = nouns[random_key]

    print(random_key)
    print(random_value)

    #
    #for key, value in nouns.items():
    #    print(key)
    #    print(value)
    #    break
    print(type(nouns))

def cr

def read_imsitu_train():
    train = json.load(open("train.json"))

    print(len(train))

    pressing_images = {k: v for k, v in train.items() if k.startswith('pressing')}
    pressing_values = list(pressing_images.values())
    print(len(pressing_values))
    print(pressing_values[0])

def read_imsitu_dev():
    dev = json.load(open("dev.json"))

    print(len(dev))

    pressing_images = {k: v for k, v in dev.items() if k.startswith('pressing')}
    pressing_values = list(pressing_images.values())
    print(len(pressing_values))
    print(pressing_values[0])


def read_imsitu_test():
    test = json.load(open("test.json"))
    for key, value in test.items():
        print(key)
        print(value)
        break
    print(len(test))

    pressing_images = {k: v for k, v in test.items() if k.startswith('pressing')}
    pressing_values = list(pressing_images.values())
    print(len(pressing_values))
    print(pressing_values[0])

def replace_data(entry):
    # Initialize variables for the target verb and agent
    agents = []

    target_verb = entry['verb']

    # Iterate over the frames in the data
    concepts = []
    for frame in entry['frames']:
        
        if 'agent' not in frame:
            current_agent = "NA"
        else:
            current_agent = frame['agent']
        agents.append(current_agent)

        current_concepts = entry.values()
        if current_agent != "NA":
            current_concepts.remove(current_agent)
        
        concepts.extend(current_concepts)

    # Find the most common agent 
    agent = statistics.mode(agents) 

    # Remove duplicates
    concepts = set(concepts)
    
    # Create the modified dictionary
    modified_dict = {'target': target_verb, 'agent': agent, 'concepts': concepts}

example = {'frames': [{'item': 'n03931044', 'place': '', 'agent': 'n10287213'}, {'item': 'n03720163', 'place': 'n08588294', 'agent': 'n10287213'}, {'item': 'n03210940', 'place': '', 'agent': 'n10287213'}], 'verb': 'pressing'}

read_imsitu_space()
