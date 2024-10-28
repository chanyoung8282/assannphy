#!/usr/bin/env python3

import subprocess
import sys,random
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline #MuscleCommandline
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
import matplotlib
import matplotlib.pyplot as plt
import os

# Use: python join_fasta.py infile1.fasta infile2.fasta outfile.fasta
#input_file = ['Xenopus.fasta','Danio.fasta','Dmel.fasta','Homo.fasta','Ostrich.fasta','Synechococcus.fasta']

#output_file = 'combined_Ankit.fasta'                               #Name of the output file
#print ("Output fasta file = ", output_file)

#with open(output_file, "w") as output_handle:
#    for input_file in input_file:
#        for record in SeqIO.parse(input_file, "fasta"):
            # 파일 이름을 ID에 추가하여 고유한 식별자 만들기
#            record.id = f"{input_file.split('.')[0]}_{record.id}"
#            SeqIO.write(record, output_handle, "fasta")

fasta_file = os.path.join(os.getcwd(),'OG0000029.fa')
#fasta_output = 'aligned_sequence1.fasta'
a = f'clustalw2 {fasta_file}'  # -clw 옵션 제거
subprocess.call(a, shell=True)

with open ('ed_Ankit.aln') as aln:
    alignment = AlignIO.read(aln,'fasta')  # 'clustal'을 'fasta'로 변경
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
