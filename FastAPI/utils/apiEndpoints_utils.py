ENDPOINTS = [
    "1ad4899d-fab3-4abd-8df7-025004902932", # tour
    "2b52bb1f-8676-43f2-b883-f673e7015ed9",  # réunion
    "56d437a7-eb0c-4c31-9138-539be94bc490",  # pdl
    "83a1f131-9e23-4c3b-b1c6-e58f33fe7b80",  # pac
    "0c463ef6-c00a-48e2-b50a-d17cfe998b84",  # occitanie
    "cb1ebc9c-73fb-43e8-9386-a7b3cf83a642",  # nor
    "734a4e86-d571-48f6-bdc0-596914066606",  # naq
    "77114c00-9928-49c1-9a1c-5545c10c7101",  # myt
    "4f95a530-d106-4ecd-aa39-1b9d639ee45c",  # mtq
    "b31a1eca-f2ff-495a-9b67-7c0bc281ea57",  # idf
    "838b6af3-74e5-4d51-873d-d359af3f1855",  # hdf
    "338bb298-cc1f-4bfd-adfd-a3c13fbfa393",  # guf
    "f73506d6-a336-4743-827b-64a39d891158",  # glp
    "59956d74-969b-4c42-8ea4-9348f6a70f7a",  # gde
    "6063e108-f8bd-4541-ba67-a5cadac804fb",  # cvl
    "2aefffc5-42f5-4e68-ba85-ba19c13fcb4c",  # cor
    "ab746af8-d21a-42d1-acae-fdfb2e52ecd5",  # bre
    "d92f0184-e9cb-4bc9-81b0-b43fbcf2a0d2",  # bfc
    "5b3c2cee-44b7-48bd-b4e8-439a03ff6cd2",  # ara
]


def filter_activity_data(activity_data: dict) -> dict:
    """Filters the activity data to only include valid columns and split postal code and commune."""
    VALID_COLUMNS = {
        'Nom_du_POI',
        'Categories_de_POI',
        'Latitude',
        'Longitude',
        'Adresse_postale',
        'Code_postal',
        'Commune',
        'Createur_de_la_donnee',
        'SIT_diffuseur',
        'Date_de_mise_a_jour',
        'Contacts_du_POI',
        'Classements_du_POI',
        'Description',
        'URI_ID_du_POI',
    }

    filtered_data = {key: activity_data[key] for key in VALID_COLUMNS if key in activity_data}

    # Split the postal code and commune
    if 'Code_postal_et_commune' in activity_data:
        code_postal, commune = activity_data['Code_postal_et_commune'].split('#', 1)
        filtered_data['Code_postal'] = code_postal.strip()  # Strip whitespace
        filtered_data['Commune'] = commune.strip()  # Strip whitespace
    else:
        filtered_data['Code_postal'] = None
        filtered_data['Commune'] = None

    return filtered_data
