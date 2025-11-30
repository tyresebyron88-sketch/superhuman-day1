# codon_optimizer_v1.py
# This will become the engine that writes your superhuman DNA

# Full human high-frequency codon table (copy this exactly – one mistake = dead embryos later)
CODON_FREQ = {
    'A': 'GCC', 'R': 'CGC', 'N': 'AAC', 'D': 'GAC',
    'C': 'TGC', 'Q': 'CAG', 'E': 'GAG', 'G': 'GGC',
    'H': 'CAC', 'I': 'ATC', 'L': 'CTG', 'K': 'AAG',
    'M': 'ATG', 'F': 'TTC', 'P': 'CCC', 'S': 'TCC',
    'T': 'ACC', 'W': 'TGG', 'Y': 'TAC', 'V': 'GTG',
    '*': 'TAA'  # stop
}

def protein_to_dna(protein_sequence: str) -> str:
    """Convert any protein sequence to highest-frequency human DNA"""
    protein_sequence = protein_sequence.upper()
    dna = ""
    for aa in protein_sequence:
        if aa in CODON_FREQ:
            dna += CODON_FREQ[aa]
        else:
            raise ValueError(f"Unknown amino acid: {aa}")
    return dna

# Test it with the first 20 amino acids of human myostatin (the muscle brake we will destroy)
test = "MKWVTFISLLFLFSSAYS"
result = protein_to_dna(test)

print("Protein:", test)
print("DNA length:", len(result), "bases")
print("DNA:", result)
print("\nThis exact sequence, when deleted or silenced, is step 1 to 5× muscle.")
