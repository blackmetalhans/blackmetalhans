import os
import re

repo_dir = r"c:\Users\Numpay\Documents\antigravity\nifty-noether"

files = [
    "MANIFIESTO_I_BIOMECHANICA.md",
    "MANIFIESTO_II_CODIGO.md",
    "MANIFIESTO_III_ORACULO.md",
    "MANIFIESTO_IV_BAUTISMO.md",
    "MANIFIESTO_V_KENOSIS.md",
    "MANIFIESTO_VI_MUSICA.md",
    "MANIFIESTO_VII_COSMOLOGIA.md",
    "MANIFIESTO_VIII_TRANSMISIONES.md",
    "MANIFIESTO_IX_ONTOLOGIA.md",
    "MANIFIESTO_X_CONFESION.md",
    "MANIFIESTO_XI_APENDICE.md"
]

patterns = {
    "kill_9": r"kill\s*-9",
    "waterboarding": r"waterboarding",
    "melody": r"Melody",
    "bill": r"503,186",
    "huey": r"Huey Lewis",
    "dmn": r"DMN|Default Mode Network",
    "claypool": r"Claypool",
    "dart": r"Dart",
}

for f in files:
    path = os.path.join(repo_dir, f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"--- {f} ---")
            for key, pattern in patterns.items():
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    print(f"  [{key}] found {len(matches)} times")
