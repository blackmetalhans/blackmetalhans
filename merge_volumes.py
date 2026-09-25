import os
import re

repo_dir = r"c:\Users\Numpay\Documents\antigravity\nifty-noether"

ix_path = os.path.join(repo_dir, "MANIFIESTO_IX_ONTOLOGIA.md")
x_path = os.path.join(repo_dir, "MANIFIESTO_X_CONFESION.md")
xi_path = os.path.join(repo_dir, "MANIFIESTO_XI_APENDICE.md")

# 1. Read IX and extract content
with open(ix_path, 'r', encoding='utf-8') as f:
    ix_content = f.read()

# Extract everything after the SVG header (split by ``` or ---)
parts = ix_content.split("---", 1)
if len(parts) > 1:
    ix_text = "---" + parts[1]
else:
    ix_text = ix_content

# 2. Append to X
with open(x_path, 'r', encoding='utf-8') as f:
    x_content = f.read()

# Replace the "kill -9" references inside VII just in case
vii_path = os.path.join(repo_dir, "MANIFIESTO_VII_COSMOLOGIA.md")
with open(vii_path, 'r', encoding='utf-8') as f:
    vii_content = f.read()
vii_content = vii_content.replace("(`kill -9`)", "(el apagón definitivo)")
vii_content = vii_content.replace("(`kill -9`)", "(el apagón definitivo)")
with open(vii_path, 'w', encoding='utf-8') as f:
    f.write(vii_content)

# We also want to replace 'PARTE IX:' with 'EPÍLOGO:' inside the appended text
ix_text = ix_text.replace("PARTE IX: ONTOLOGÍA DEL SILENCIO", "EPÍLOGO: ONTOLOGÍA DEL SILENCIO")
ix_text = ix_text.replace("PART IX: ONTOLOGY OF SILENCE", "EPILOGUE: ONTOLOGY OF SILENCE")

x_content_updated = x_content + "\n\n" + ix_text

# Write updated X (which we will save as IX)
new_ix_path = os.path.join(repo_dir, "MANIFIESTO_IX_CONFESION.md")
with open(new_ix_path, 'w', encoding='utf-8') as f:
    # Update headers inside Confesion
    content = x_content_updated.replace("PARTE X:", "PARTE IX:")
    content = content.replace("PART X:", "PART IX:")
    content = content.replace("RELAY_10", "RELAY_09")
    content = content.replace("VOL_10", "VOL_09")
    f.write(content)

# 3. Rename XI to X
new_x_path = os.path.join(repo_dir, "MANIFIESTO_X_APENDICE.md")
with open(xi_path, 'r', encoding='utf-8') as f:
    xi_content = f.read()

xi_content = xi_content.replace("PARTE XI:", "PARTE X:")
xi_content = xi_content.replace("PART XI:", "PART X:")
xi_content = xi_content.replace("RELAY_11", "RELAY_10")
xi_content = xi_content.replace("VOL_11", "VOL_10")

with open(new_x_path, 'w', encoding='utf-8') as f:
    f.write(xi_content)

# 4. Remove old files
os.remove(ix_path)
os.remove(x_path)
os.remove(xi_path)

print("Files successfully merged and renamed to 10 volumes.")

# Update rebuild_dossier.py
rebuild_script = os.path.join(repo_dir, "rebuild_dossier.py")
with open(rebuild_script, 'r', encoding='utf-8') as f:
    script_content = f.read()

script_content = script_content.replace('"MANIFIESTO_IX_ONTOLOGIA.md",\n', '')
script_content = script_content.replace('"MANIFIESTO_X_CONFESION.md",', '"MANIFIESTO_IX_CONFESION.md",')
script_content = script_content.replace('"MANIFIESTO_XI_APENDICE.md",', '"MANIFIESTO_X_APENDICE.md",')

with open(rebuild_script, 'w', encoding='utf-8') as f:
    f.write(script_content)

print("Rebuild script updated.")
