from Bio.PDB import Polypeptide
from ssbio.structure.pdbioext import PDBIOExt

def get_pdb_seq(pdb_file):
    '''
    Takes in a structure file and returns a list of the
    structure's sequences
    :param pdb_file: file path of pdb file
    :return: Dictionary of sequence strings with chain IDs as the key
    '''

    my_structure = PDBIOExt(pdb_file)
    model = my_structure.first_model

    structure_seqs = {}

    # loop over each chain of the PDB
    for chain in model:

        chain_it = iter(chain)

        chain_seq = ''
        tracker = 0

        # loop over the residues
        for res in chain.get_residues():
            # NOTE: you can get the residue number too
            res_num = res.id[1]

            # double check if the residue name is a standard residue
            # if it is not a standard residue (ie. selenomethionine),
            # it will be filled in with an X on the next iteration)
            if Polypeptide.is_aa(res, standard=True):
                full_id = res.get_full_id()
                end_tracker = full_id[3][1]
                i_code = full_id[3][2]
                aa = Polypeptide.three_to_one(res.get_resname())

                # tracker to fill in X's
                if end_tracker != (tracker + 1):   # and first == False:
                    if i_code != ' ':
                        chain_seq += aa
                        tracker = end_tracker + 1
                        continue
                    else:
                        chain_seq += 'X' * (end_tracker - tracker - 1)

                chain_seq += aa
                tracker = end_tracker

            else:
                continue

        structure_seqs[chain.get_id()] = chain_seq

    return structure_seqs