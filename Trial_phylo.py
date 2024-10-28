#!/usr/bin/env python3

import subprocess
import sys,random
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline#MuscleCommandline
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib
import matplotlib.pyplot as plt
import os

# Use: python join_fasta.py infile1.fasta infile2.fasta outfile.fasta
input_file = ['OG0000029.fa']

output_file = 'OG0000029.fasta'                               #Name of the output file
print ("Output fasta file = ", output_file)

with open(output_file, "w") as output_handle:
    for input_file in input_file:
        for record in SeqIO.parse(input_file, "fasta"):
            SeqIO.write(record, output_handle, "fasta")

fasta_file = os.path.join(os.getcwd(),'OG0000029.fasta')
fasta_output = 'OG0000029.aln'
a = f'clustalw2 {fasta_file}'
subprocess.call(a, shell=True) # This line is used to make sure that variable a runs in the command line

with open ('OG0000029.aln') as aln:
    alignment = AlignIO.read(aln,'clustal')
    print(type(alignment))
    calculator = DistanceCalculator('identity')
    distance_matrix = calculator.get_distance(alignment)
    print(distance_matrix)
    constructor = DistanceTreeConstructor(calculator)
    tree = constructor.build_tree(alignment)
    tree.rooted = True
    print(tree)
    Phylo.write(tree, 'tree.xml', 'phyloxml')
    tree_view = Phylo.draw(tree)
