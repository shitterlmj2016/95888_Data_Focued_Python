import os
import json
import csv
import argparse
import fhirclient.models.bundle as bu
import fhirclient.models.claim as cl

"""In this assignment you will generate a set of synthetic healthcare data 
using the synthea tool discussed in class. For the purposes of the assignment
you can generate as few or as many patients as you'd like. You'll submit
your python file to canvas and the grader will run your code on their dataset.

DO NOT change any of the function signatures. You only need to implement the 
function bodies below the docstring replacing pass with your implementation.
Keep in mind that the arguments and return values are specified in the
docstring.
"""


def parse_claims_into_csv(bundle_path, output_path, claims_file_name):
    """18 Points for Correctness, 2 Points for Proficiency
    Reads a directory of fhir bundles, parses fhir bundles into
    fhirclient bundle objects, parses out claims data, writes claims data to a
    csv file.

    Hint : translate relative to absolute paths 
    Hint : walk the subdirectory to find files
    Hint : call parse_bundle_for_file
    Hint : call get_claims_from_bundle
    Hint : call write_claims_to_csv
    Arguments:
        bundle_path {String} -- path to the fhir data directory for this assignment e.g. ~/assignments/data/fhir
        output_path {String} -- path to the output directory for this assignment e.g. ~/assignments/out
        claims_file_name {String} -- claims file name e.g. claims.csv
    """
    files = os.listdir(bundle_path)
    claims = []
    for file in files:
        if not os.path.isdir(file):
            path = bundle_path + "/" + file
            #print(path)
            my_bundle = parse_bundle_for_file(path)
            claims += get_claims_from_bundle(my_bundle)
            write_claims_to_csv(claims, output_path, claims_file_name)

    # my_bundle = parse_bundle_for_file(os.path.abspath(bundle_path))
    #
    # claims = get_claims_from_bundle(my_bundle)
    #
    # write_claims_to_csv(claims, os.path.abspath(output_path), claims_file_name)


def parse_bundle_for_file(fhir_bundle_path):
    """18 Points for Correctness, 2 Points for Proficiency
    Reads a fhir bundle file and returns a fhir bundle class object
    
    Arguments:
        fhir_bundle_path {String} -- path to a fhir bundle
    
    Returns:
        fhirclient.models.bundle.Bundle -- fhir bundle class object for the
        fhir bundle file passed into the function
    """

    with open(fhir_bundle_path, 'r', encoding='UTF-8') as f:
        bundle = bu.Bundle(json.load(f))
        return bundle


def get_claims_from_bundle(bundle):
    """18 Points for Correctness, 2 Points for Proficiency
    Extracts a fhir claim resource from a FHIR bundle containing a claim

    Arguments:
        bundle {fhirclient.models.bundle.Bundle} -- fhir bundle representing a
        single synthea fhir file

    Returns:
        list -- list of all fhir fhirclient.models.claim.Claim resources 
        contained within a single fhir bundle
    """
    list = []
    for i in bundle.entry:
        rs = i.resource
        if isinstance(rs, cl.Claim):
            list.append(rs)
    return list


def write_claims_to_csv(claims, output_path, claims_file_name, new_file=True):
    """18 Points for Correctness, 2 Points for Proficiency
    Writes information contained within a list of claims to a csv file
    at the specified path

    Ex: must match exact format with no spaces between fields
    status,use,billable_period_start,billable_period_end,total,currency

    Arguments:
        claims {list} -- List of fhirclient.models.claim.Claim objects
        output_path {String} -- path to the output directory for this assignment e.g. ~/assignments/out
        claims_file_name {String} -- claims file name e.g. claims.csv
        new_file {Boolean} -- indicates if a csv file should be created or updated
    """
    output_path = output_path + "/" + claims_file_name

    if new_file:
        file = open(output_path, 'w', newline='')
    else:
        file = open(output_path, 'a+', newline='')
    csv_write = csv.writer(file)

    if new_file:
        csv_head = ['status', 'use', 'billable_period_start', 'billable_period_end', 'total', 'currency']
        csv_write.writerow(csv_head)

    for i in claims:
        csv_write.writerow(get_csv_values_from_claim(i))

    file.close()


def get_csv_values_from_claim(claim):
    """18 Points for Correctness, 2 Points for Proficiency
    Takes a fhirclient.models.claim.Claim object and returns a list of 
    strings for the following attributes

    status
    use
    billable_period_start as an iso string
    billable_period_end as an iso string
    total
    currency

    Ex: must match exact format with no spaces between fields
    active,complete,2009-06-22T06:16:39-04:00,2009-06-22T06:31:39-04:00,255.0,USD

    Arguments:
        claim {fhirclient.models.claim.Claim} -- fhir Claim object

    Returns:
        list -- list of String values
    """
    list = [];
    list.append(claim.status)
    list.append(claim.use)  # ????
    list.append(claim.billablePeriod.start.isostring)
    list.append(claim.billablePeriod.end.isostring)
    list.append(str(claim.total.value))
    list.append(claim.total.currency)
    return list


# DO NOT MODIFY BELOW THIS LINE

def get_parsed_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fhir", default="data/fhir/",
                        help="path to the fhir data directory for this assignment e.g. ~/assignments/data/fhir")
    parser.add_argument("-o", "--output", default="out/",
                        help="path to the output directory for this assignment e.g. ~/assignments/out")
    return parser.parse_args()


if __name__ == "__main__":
    parsed_args = get_parsed_args()
    parse_claims_into_csv(parsed_args.fhir, parsed_args.output, 'claims.csv')
    # bundle = parse_bundle_for_file(
    #     'C:\\Users\\91593\\Desktop\\Python\\synthea\\output\\fhir\\Devin82_Goodwin327_bf81fdbc-f176-4b27-a50d-aac42654a3d2.json')
    # list = get_claims_from_bundle(bundle)
    # write_claims_to_csv(list, 'C:\\Users\\91593\\Desktop', 'test.csv')
