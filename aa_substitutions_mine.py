from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

amino_acids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N',
               'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

def aa_count(sequence):
    """ includes the amino acid counts, arg/lys ratio and
        acidic residue counts
    """
    count = ProteinAnalysis(sequence).count_amino_acids()
    count_list = [count[aa] for aa in amino_acids]
    arg_to_lys = float(count['R'])/count['K'] if count['K'] else 'N/A'
    acid_res = count['D'] + count['E']
    all_counts = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t\
{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t\
{19}\t{20}\t{21}".format(*(count_list+[arg_to_lys]+[acid_res]))
    return all_counts


def aa_percent(sequence):
    """ includes the aliphatic index followed by amino acid percent values
    """
    percent = ProteinAnalysis(sequence).get_amino_acids_percent()
    aliphatic_index = percent['A'] + 2.9 * percent['V'] + 3.9 * (percent['I']
        + percent['L'])
    percent_list = ["{:.5f}".format(percent[aa]) for aa in amino_acids]
    all_percents = "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t\
{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t\
{19}\t{20}".format(*([aliphatic_index] + percent_list))
    return all_percents


def aroma(sequence):
    aromaticity = ProteinAnalysis(sequence).aromaticity()
    return aromaticity


def flex(sequence):
    """ Returns a list of scores for each residue and not a single score for
    the whole protein.
    """
    flexibility = ProteinAnalysis(sequence).flexibility()
    return flexibility


def gravy(sequence):
    if 'X' or '*' in sequence:
        sequence = sequence.replace('X', '')
        sequence = sequence.replace('*', '')
        g = ProteinAnalysis(sequence).gravy()
    else:
        g = ProteinAnalysis(sequence).gravy()
    return g

for gene in prot_seqs:
    gene = str(gene[0]).strip()
        query_prot_seq = str(prot_seqs["{}".format(gene)].seq)
        print "{}\t".format(gene), "{}\t".format(gene),\
            aa_percent(query_prot_seq), '\t', aa_count(query_prot_seq), '\t',\
            aroma(query_prot_seq), '\t', gravy(query_prot_seq)
        for hit in results_list:
            target_id = hit[1]
            target_prot_seq = str(prot_seqs["{}".format(target_id)].seq)
            print "{}\t".format(gene), "{}\t".format(target_id),\
                aa_percent(target_prot_seq), '\t', aa_count(target_prot_seq),\
                '\t', aroma(target_prot_seq), '\t', gravy(target_prot_seq)              
               
            
