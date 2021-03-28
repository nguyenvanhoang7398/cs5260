from utils_io import *


data = load_from_pickle("CrossNER_NOUN_PRON.pickle")

for domain, domain_data in data.items():
    domain_nouns = [x[0].lower() for x in domain_data["NOUN"]]
    domain_pronouns = [x[0].lower() for x in domain_data["PRON"]]
    domain_concepts = sorted(list(set(domain_nouns + domain_pronouns)))
    save_list_as_text(domain_concepts, os.path.join("data", "{}.entities.txt".format(domain)))

pass
