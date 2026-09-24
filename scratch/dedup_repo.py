import os
import re

repo_dir = r"c:\Users\Numpay\Documents\antigravity\nifty-noether"

def replace_in_file(filename, pattern, replacement, flags=re.DOTALL):
    path = os.path.join(repo_dir, filename)
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = re.sub(pattern, replacement, content, flags=flags)
    
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No match found in {filename}")


# VOL II: Remove Genesis section since it's redundant now
vol2_pattern = r"## 0\.0 GÉNESIS DEL AUTODIDACTA: ABRIL DE 2026 EN EL SECTOR-NULL.*?## 1\.0"
vol2_replacement = r"## 1.0"
replace_in_file("MANIFIESTO_II_CODIGO.md", vol2_pattern, vol2_replacement)


# VOL VII: Prune the My Melody towel paragraph
vol7_pattern = r"Quince años de caos químico.*?respiratory drive\."
vol7_replacement = r"Quince años de caos químico fueron desmantelados no por voluntad moral, sino por un reseteo biológico violento (documentado en la Liturgia de la Kénosis). La adicción severa es una máquina de demolición perfecta: reduce al portador a una masa temblorosa de reflejos condicionados.\n\nFifteen consecutive years of multi-substance chemical chaos were dismantled not by moral sovereignty, but by a violent biological reset (documented in the Liturgy of Kenosis). Advanced addiction operates as an immaculate kinetic demolition rig: it reduces the biological host to a convulsing network of conditioned reflexes."
replace_in_file("MANIFIESTO_VII_COSMOLOGIA.md", vol7_pattern, vol7_replacement)

# VOL X: Prune My Melody redundancy
vol10_pattern = r"No fue un retiro espiritual ni una terapia.*?autonomic overload\."
vol10_replacement = r"No fue un retiro espiritual. Fue el vaciamiento biológico de la Kénosis: el choque osmótico y térmico que colapsó la Default Mode Network por sobrecarga autonómica.\n\nIt was no pastoral retreat. It was the biological evacuation of Kenosis: the osmotic and thermal shock that collapsed the Default Mode Network from autonomic overload."
replace_in_file("MANIFIESTO_X_CONFESION.md", vol10_pattern, vol10_replacement)


# VOL IX: Remove My Melody Citation completely
vol9_pattern = r"#### Cita 22 // Citation 22: El Experimento de la Toalla.*?El wetware funciona\.\"\n```\n\n---"
vol9_replacement = r""
replace_in_file("MANIFIESTO_IX_APENDICE.md", vol9_pattern, vol9_replacement)


# Rebuild dossier
os.system("python scratch/rebuild_dossier.py")
print("Done deduping.")
