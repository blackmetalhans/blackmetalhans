import os
import glob

repo_dir = r"c:\Users\Numpay\Documents\antigravity\nifty-noether"
output_file = os.path.join(repo_dir, "DOSSIER_COMPLETO_REPOSITORIO_GEMINI.md")

# Ensure files are concatenated in the right order
files = [
    "MANIFIESTO_I_BIOMECHANICA.md",
    "MANIFIESTO_II_CODIGO.md",
    "MANIFIESTO_III_ORACULO.md",
    "MANIFIESTO_IV_BAUTISMO.md",
    "MANIFIESTO_V_KENOSIS.md",
    "MANIFIESTO_VI_MUSICA.md",
    "MANIFIESTO_VII_COSMOLOGIA.md",
    "MANIFIESTO_VIII_TRANSMISIONES.md",
        "MANIFIESTO_IX_CONFESION.md",
    "MANIFIESTO_X_APENDICE.md",
]

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write("# DOSSIER COMPLETO REPOSITORIO HANS\n\n")
    for f in files:
        filepath = os.path.join(repo_dir, f)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as infile:
                outfile.write(f"\n\n<!-- BEGIN {f} -->\n\n")
                outfile.write(infile.read())
                outfile.write(f"\n\n<!-- END {f} -->\n\n")

print(f"Dossier successfully rebuilt: {output_file}")
