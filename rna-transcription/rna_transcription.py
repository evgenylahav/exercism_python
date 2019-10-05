"""
this module translates an input DNA strand to an RNA strand
Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

G -> C
C -> G
T -> A
A -> U
"""
from typing import Dict


def get_dna2rna_transform() -> Dict:
    """
    this function returns a translation dictionary of DNA to RNA
    :return: translation dict
    """
    rna_strand = dict()
    rna_strand['G'] = 'C'
    rna_strand['C'] = 'G'
    rna_strand['T'] = 'A'
    rna_strand['A'] = 'U'
    return rna_strand


def is_dna(dna_strand: str) -> bool:
    """
    this function checks that dna_strand actually represents and dna strand

    :param dna_strand:
    :return: True / False
    """
    if not isinstance(dna_strand, str):
        return False

    dna_nucle = 'ACGT'
    for s in dna_strand:
        if s.upper() not in dna_nucle:
            return False

    return True


def to_rna(dna_strand: str) -> str:
    """
    this function transforms an input DNA strand to its complement RNA strand
    :param dna_strand:
    :return: rna_strand
    """

    if not is_dna(dna_strand):
        raise Exception("the input to the function doesn't represent a dna strand")

    dna2rna = get_dna2rna_transform()

    rna_strand = ""

    for s in dna_strand:
        rna_strand += dna2rna[s]

    return rna_strand
