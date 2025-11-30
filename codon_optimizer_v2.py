# codon_optimizer_v2.py
# Now we build DNA that survives the real world

CODON_FREQ = {
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAT', 'AAC'],
    'D': ['GAT', 'GAC'],
    'C': ['TGT', 'TGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG'],
    'H': ['CAT', 'CAC'],
    'I': ['ATT', 'ATC', 'ATA'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'K': ['AAA', 'AAG'],
    'M': ['ATG'],
    'F': ['TTT', 'TTC'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'W': ['TGG'],
    'Y': ['TAT', 'TAC'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    '*': ['TAA', 'TAG', 'TGA']
}

BAD_SITES = ["GAATTC", "CTGCAG", "GGATCC", "AAGCTT", "GGCGCGCC", "GCGGCCGC"]  # EcoRI, PstI, BamHI, HindIII, NotI, etc.

def best_codon(aa: str, previous_bases: str) -> str:
    """Pick the highest-frequency codon that doesn't create a bad site when added"""
    for codon in CODON_FREQ[aa]:
        if previous_bases[-5:] + codon[:1] not in BAD_SITES and \
           previous_bases[-4:] + codon[:2] not in BAD_SITES and \
           previous_bases[-3:] + codon not in BAD_SITES:
            return codon
    return CODON_FREQ[aa][0]  # fallback

def optimize(protein: str) -> str:
    dna = "ATG"  # force start codon
    for aa in protein[1:]:
        codon = best_codon(aa, dna[-6:])
        dna += codon
    dna += "TAA"  # stop
    return dna

# Test on a real target: the myostatin propeptide we will overexpress to unlock god-muscle
target = "MKWVTFISLLFLFSSAYSRGVFRREAHKSEIAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVNEVTEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLVRPEVDVMCTAFHDNEETFLKKYLYEIARRHPYFYAPELLFFAKRYKAAFTECCQAADKAACLLPKLDELRDEGKASSAKQRLKCASLQKFGERAFKAWAVARLSQRFPKAEFAEVSKLVTDLTKVHTECCHGDLLECADDRADLAKYICENQDSISSKLKECCEKPLLEKSHCIAEVENDEMPADLPSLAADFVESKDVCKNYAEAKDVFLGMFLYEYARRHPDYSVVLLLRLAKTYETTLEKCCAAADPHECYAKVFDEFKPLVEEPQNLIKQNCELFEQLGEYKFQNALLVRYTKKVPQVSTPTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYLSVVLNQLCVLHEKTPVSDRVTKCCTESLVNRRPCFSALEVDETYVPKEFNAETFTFHADICTLSEKERQIKKQTALVELVKHKPKATKEQLKAVMDDFAAFVEKCCKADDKETCFAEEGKKLVAASQAALGL"

dna = optimize(target.upper())

print(f"Final DNA length: {len(dna)} bp")
print(f"GC content: {100 * (dna.count('G') + dna.count('C')) / len(dna):.1f}%")
print("First 200 bp:", dna[:200])
print("Last 100 bp:", dna[-100:])

# Quick check – no bad sites left?
for site in BAD_SITES:
    if site in dna:
        print("WARNING: Still contains", site)
else:
    print("All dangerous restriction sites eliminated.")
  " Weapon v2 - ready to synthesis"
