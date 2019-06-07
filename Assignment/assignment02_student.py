import json
import fhirclient.models.bundle
import fhirclient.models.patient as pa
from pprint import pprint


def get_patient_resource(bundle):
    """ 40 points, 38 for correctness 2 for proficiency
    Parses a FHIR bundle for a patient resource

    Arguments:
        bundle {dict} -- Python dictionary representing a JSON FHIR bundle

    Returns:
        [dict] -- Python dictionary representing the JSON Patient FHIR resource
    """
    entry = bundle['entry']
    for e in entry:
        if e['resource']['resourceType'] == 'Patient':
            return e['resource']


def get_patient_ssn(patient_bundle):
    """ 20 points, 18 for correctness 2 for proficiency
    Parses the patient bundle and returns the social security number as a string
    
    Arguments:

        patient_bundle {dict} -- Python dictionary representing the JSON Patient FHIR resource
    
    Returns:
        string -- the patient's social security number
    """
    id = patient_bundle['identifier']
    for map in id:
        if 'type' in map.keys():
            if map['type']['coding'][0]['code'] == 'SS':
                return map['value']


def get_patient_name(patient_bundle):
    """ 20 points, 18 for correctness 2 for proficiency
    Parses the patient bundle and returns a string formatted as
    <given name(s)> <family name> e.g. John James Doe
    
    Arguments:
        patient_bundle {dict} -- Python dictionary representing the JSON Patient FHIR resource
    
    Returns:
        string -- the formatted patient name
    """
    names = patient_bundle['name']
    for name in names:
        if (name['use'] == 'official'):
            str = ''
            for g in name['given']:
                str += g + ' '
            str += name['family']
            # 'Rita460 Schowalter414'??
    return str


def get_patient_race(patient_resource):
    """ 10 points, 8 for correctness 2 for proficiency
    Parses a Patient resource and returns race details
    
    Arguments:
        patient_resource {dict} -- Python dictionary representing the JSON Patient FHIR resource
    
    Returns:
        tuple -- Tuple containing the system, code, and display
    """
    #pprint(patient_resource['extension'])
    map = patient_resource['extension'][0]['extension'][0]['valueCoding']
    my_tuple = (map['system'], map['code'], map['display'])
    return my_tuple


def get_patient_birth_place(patient_resource):
    """ 10 points, 8 for correctness 2 for proficiency
    Parses a Patient resource and returns birth place
    
    Arguments:
        patient_resource {dict} -- Python dictionary representing the JSON Patient FHIR resource
    
    Returns:
        tuple -- Tuple containing the city, state, and country
    """
    for map in patient_resource['extension']:
        if ('valueAddress' in map):
            birth_place = map['valueAddress']
            my_tuple =(birth_place['city'], birth_place['state'], birth_place['country'])
            return my_tuple



def load_bundle(fhir_bundle_path):
    with open(fhir_bundle_path) as f:
        bundle = json.loads(f.read())
        return bundle


if __name__ == "__main__":
    # bundle = load_bundle('data/fhir/Albina13_Stehr398_a086ee39-c8d2-4cd4-8fe1-f5367e80a370.json')
    #
    # patient = get_patient_resource(bundle)
    # print("***** Patient\n", patient, "\n")
    #
    # ssn = get_patient_ssn(patient)
    # print("***** Patient SSN\n", ssn, "\n")
    #
    # name = get_patient_name(patient)
    # print("***** Patient Name\n", name, "\n")
    #
    # system, code, display = get_patient_race(patient)
    # print("*** Patient Race\n", system, code, display, "\n")
    #
    # birth_place_city, birth_place_state, birth_place_country = get_patient_birth_place(patient)
    # print("*** Patient Birth Place\n", birth_place_city, birth_place_state, birth_place_country, "\n")

    bundle = load_bundle(
        'C:/Users/91593/Desktop/Python/synthea/output/fhir/Devin82_Goodwin327_bf81fdbc-f176-4b27-a50d-aac42654a3d2.json')
    patient = get_patient_resource(bundle)
    ssn = get_patient_ssn(patient)
    print(ssn)
    name = get_patient_name(patient)
    print(name)
    race = get_patient_race(patient)
    print(race)
    city = get_patient_birth_place(patient)
    print(city)
