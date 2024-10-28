#!/usr/bin/env python3
import os
import subprocess
import sys

strain = sys.argv[1]
Platform = sys.argv[2]
genomeSize = sys.argv[3]
file_name = sys.argv[4]

os.environ["PATH"] += ":/Users/pfb2024/PFB_problemsets/PFB_problemsets-1/Genome_Assembly/canu-2.2/bin"
canu_run = "canu"
#os.system(canu_run)
assembly = f"canu -p {strain} -d {strain}-{Platform} genomeSize={genomeSize} -{Platform}-raw {file_name}"
os.system(assembly)



#subprocess.run("canu", "-p" "")