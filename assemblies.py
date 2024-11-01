#!/usr/bin/env python3
import os
from pathlib import Path

# Canu 경로 설정
os.environ["PATH"] += ":/Users/pfb2024/PFB_problemsets/PFB_problemsets-1/Genome_Assembly/canu-2.2/bin"

def run_assemblies(assemblies_list):
    os.environ["PATH"] += ":/Users/pfb2024/PFB_problemsets/PFB_problemsets-1/Genome_Assembly/canu-2.2/bin"
    
    for assembly in assemblies_list:
        command = f"canu -p {assembly['strain']} -d {assembly['strain']}-{assembly['platform']} " \
                 f"genomeSize={assembly['genome_size']} -{assembly['platform']}-raw {assembly['file']} "
        
        print(f"Starting assembly for {assembly['strain']}...")
        os.system(command)
        

def get_contig_files(assemblies_list):
    contig_files = {}
    
    for assembly in assemblies_list:
        directory = f"{assembly['strain']}-{assembly['platform']}"
        contig_path = Path(directory) / f"{assembly['strain']}.contigs.fasta"
        
        if contig_path.exists():
            contig_files[assembly['strain']] = str(contig_path)
        else:
            print(f"Warning: Contig file not found for {assembly['strain']}")
    
    return contig_files

 # Assembly 실행
    run_assemblies(assemblies)
    # Assembly 완료 후 contig 파일 경로 반환
    contig_files = get_contig_files(assemblies)
    
    
    print("\nCompleted assemblies:")
    for strain, contig_path in contig_files.items():
        print(f"{strain}: {contig_path}")