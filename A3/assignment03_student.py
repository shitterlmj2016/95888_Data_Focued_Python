import json
import csv
from pprint import pprint


def create_patient_dictionary(patient_file_name):
    """18 Points for Correctness, 2 Points for Proficiency
    Parses a synthea generated patients.csv file and returns a dictionary of 
    patients where the key is the patient Id and the value is a dictionary 
    containing the following fields.

        Id
        BIRTHDATE
        FIRST
        LAST
        GENDER
    
    Arguments:
        patient_file_name {str} -- file path including name to a synthea 
        patients.csv file
    
    Returns:
        [dict] -- dictionary of all patients in the patients.csv
    """
    with open(patient_file_name) as f:
        reader = csv.DictReader(f, delimiter=',')
        dic = {}
        for line in reader:
            id = line['Id']
            sub_dic = {k: line[k] for k in
                       {'Id',
                        'BIRTHDATE',
                        'FIRST',
                        'LAST',
                        'GENDER'}}
            dic[id] = sub_dic
        return dic


def add_encounters_to_patients(patients, encounters_file_name, resource_name='ENCOUNTERS'):
    """18 Points for Correctness, 2 Points for Proficiency
    Parses a synthea generated encounters file and appends encounters to the
    appropriate patient based on the patient Id. A new key identified by the
    resource_name is added to the patient dictionary as a key. The value of the
    new resource is a dictionary having a key that represents the Encounter Id
    and a dictionary containing the following fields as the value.

        Id
        START
        STOP
        CODE
        DESCRIPTION

    Arguments:
        patients {dict} -- dictionary of patients
        encounters_file_name {str} -- file path including name to a synthea 
        encounters.csv file
    
    Keyword Arguments:
        resource_name {str} -- [description] (default: {'ENCOUNTERS'})
    """
    with open(encounters_file_name) as f:
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            patient_id = line['PATIENT']
            patient = patients[patient_id]
            if resource_name not in patient.keys():
                patient[resource_name] = {}

            id = line['Id']
            sub_dic = {k: line[k] for k in
                       {'Id',
                        'START',
                        'STOP',
                        'CODE',
                        'DESCRIPTION'}}
            patient[resource_name][id] = sub_dic
        return patients


def add_medications_to_patients(patients, medications_file_name, resource_name='MEDICATIONS'):
    """18 Points for Correctness, 2 Points for Proficiency
    Parses a synthea generated medications file and appends medications to the
    appropriate patient based on the patient Id. A new key identified by the
    resource_name is added to the patient dictionary as a key. The value of the
    new resource is a list that contains dictionaries having the following fields.
        ENCOUNTER
        START
        STOP
        CODE
        DESCRIPTION
    
    Arguments:
        patients {dict} -- dictionary of patients
        medications_file_name {str} -- file path including name to a synthea 
        MEDICATIONS.csv file
    
    Keyword Arguments:
        resource_name {str} -- [description] (default: {'MEDICATIONS'})
    """
    with open(medications_file_name) as f:  # ???
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            patient_id = line['PATIENT']
            patient = patients[patient_id]
            if resource_name not in patient.keys():
                patient[resource_name] = {}

            sub_dic = {k: line[k] for k in
                       {'ENCOUNTER',
                        'START',
                        'STOP',
                        'CODE',
                        'DESCRIPTION'}}
            if sub_dic['CODE'] not in patient[resource_name].keys():
                patient[resource_name][sub_dic['CODE']] = []
            patient[resource_name][sub_dic['CODE']].append(sub_dic)
        return patients


def problem1(patients):
    """ 9 Points for Correctness, 1 Point for Proficiency
    Returns a list of distinct medication codes across all patients
    
    Arguments:
        patients {dict} -- dictionary of patients
    
    Returns:
        list -- list of distinct medication codes
    """
    z = set()
    for patient in patients.values():
        if ('MEDICATIONS' in patient.keys()):
            for code in patient['MEDICATIONS'].keys():
                z.add(code)
    return list(z)


def problem2(patients):
    """18 Points for Correctness, 2 Points for Proficiency
    Returns a list of distinct (encounter description, medication description)
    tuples across all patients including only the encounters where medications
    were documented.
    
    Arguments:
        patients {dict} -- dictionary of patients
    
    Returns:
        list -- list of distinct (encounter description, medication description)
        tuples
    """
    z = set()
    for patient in patients.values():
        if ('MEDICATIONS' in patient.keys()):
            for l in patient['MEDICATIONS'].values():
                for map in l:
                    encounter = map['ENCOUNTER']
                    med_description = map['DESCRIPTION']
                    enc_description = patient['ENCOUNTERS'][encounter]['DESCRIPTION']
                    z.add((enc_description, med_description))
    return list(z)


def problem3(medications_path="data/csv/medications.csv", expenses_out="out/expenses.csv"):
    """9 Points for Correctness, 1 Point for Proficiency
    Picks up medications.csv file, notes down the following:
    1. CODE
    2. no. of times appeared
    3. no. of dispenses
    
    Saves a csv file with above 3 rows as header and it's values sorted in decreasing order wrt #of dispenses.
    Eg..
    
    code   no. of times appeared   no. of dispenses
     2               2                   4
     3               5                   2
     4               9                   1

    Arguments:
        medications_path -- path to the medications.csv
        expenses_out -- path to the output csv file
    
    Returns:
        None
    """
    # new or append
    with open(medications_path) as f:
        reader = csv.DictReader(f, delimiter=',')
        dic = {}
        for line in reader:
            code = int(line['CODE'])
            if code not in dic.keys():
                dic[code] = {'appeared': 0, 'dispenses': 0}
            dic[code]['appeared'] += 1
            dic[code]['dispenses'] += int(line['DISPENSES'])

        index = sorted(dic, key=lambda k: dic[k]['dispenses'], reverse=True)
        list = []
        for k in index:
            list.append([k, dic[k]['appeared'], dic[k]['dispenses']])

        with open(expenses_out, 'w', newline='') as csv_file:
            fieldnames = ['code', 'no. of times appeared', 'no. of dispenses']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for item in list:
                writer.writerow({'code': item[0], 'no. of times appeared': item[1], 'no. of dispenses': item[2]})


# do not modify below this line

def write_ndjson(file_name, patients):
    with open(file_name, 'w') as output:
        for patient_id in patients:
            output.write(json.dumps(patients[patient_id], separators=(',', ':')) + "\n")


if __name__ == "__main__":
    # part 1
    patients = create_patient_dictionary('data/csv/patients.csv')
    add_encounters_to_patients(patients, 'data/csv/encounters.csv')
    add_medications_to_patients(patients, 'data/csv/medications.csv')

    write_ndjson('out/assignment03.ndjson', patients)

    # part 2
    codes = problem1(patients)
    print(codes)
    descriptions = problem2(patients)
    print(descriptions)

    # part 3
    problem3("data/csv/medications.csv", "out/expenses.csv")
