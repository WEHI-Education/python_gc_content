import sys
"""
Reads a FASTA file and calculates the average GC content of all sequences.

Usage: python gc_content.py <fasta_file>
"""

def calculate_gc_content(sequence):
    """
    Calculate the GC content of a nucleotide sequence.
    
    Args:
    sequence (str): A DNA sequence.
    
    Returns:
    float: The GC content percentage.
    """
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_content = (g_count + c_count) / len(sequence) * 100 if len(sequence) > 0 else 0
    return gc_content

def read_fasta(filename):
    """
    Read sequences from a FASTA file and concatenate them into one large sequence.
    
    Args:
    filename (str): Path to the FASTA file.
    
    Returns:
    str: A concatenated string of all sequences in the FASTA file.
    """
    full_sequence = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line.startswith(">"):
                full_sequence.append(line)

    return "".join(full_sequence)

def main():
    if len(sys.argv) != 2:
        print("Usage: python gc_content.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    full_sequence = read_fasta(fasta_file)
    gc_content = calculate_gc_content(full_sequence)
    print(f"Overall GC Content: {gc_content:.2f}%")

if __name__ == "__main__":
    main()
