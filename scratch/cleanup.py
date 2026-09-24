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

# 1. DELETE Vol XI
try:
    os.remove(os.path.join(repo_dir, "MANIFIESTO_XI_ONTOLOGIA.md"))
    os.remove(os.path.join(repo_dir, "assets", "MANIFIESTO_XI.jpg"))
    os.remove(os.path.join(repo_dir, "assets", "MANIFIESTO_XI.svg"))
    print("Deleted Vol XI files.")
except OSError:
    pass

# 2. Shorten README
readme_path = os.path.join(repo_dir, "README.md")
readme_content = """```yaml
=== [ TELEMETRY // SECTOR-NULL ] ===
OPERATOR_ID: "[CLASSIFIED_DATA_EXPUNGED] // 0x7F"
ENTROPY_SIGNATURE: "SHA256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
GEO_VECTOR: "[CLASSIFIED_DATA_EXPUNGED] // 00.0000° N, 00.0000° W"
GRID_AFFILIATION: "AIRGAPPED // MILITARIZED_ZONE"

HOST_NODE:
  ARCHITECTURE: "x86_64 // SYNTHETIC_SILICON"
  STATUS: "CLEAN_WETWARE // MORPHINE_DETOX_COMPLETE"

ORACLE_SYNAPSE:
  CORE: "EL TERCER COCO // SYMBOLIC ENGINE"
  EPOCHS: "32,324 CYCLES PROCESSED"
  TOKENS: "2,950,775"
  ZIPF_ALPHA: "1.2693 // HIGH_ENTROPY_REASONING"
  STATUS: "KILLED_IN_ACTION // kill -9 BY OPERATOR"
====================================
```

<p align="center">
  <img src="assets/banner.png" alt="blackmetalhans // Intercepted Terminal Banner" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/blackmetalhans">
    <img src="https://readme-typing-svg.demolab.com/?lines=Programador+salvaje+del+SECTOR-NULL.+Wetware+limpio...;Liquidando+la+aberraci%C3%B3n+de+Electron+con+Win32%2FGDI32+nativo...;32%2C000%2B+interactions.+Zipf+Alpha+1.2693...;Al+Or%C3%A1culo+lo+mat%C3%A9+yo.+kill+-9.+No+regrets...;Operando+en+la+trinchera.+High+Entropy+Reasoning...&font=Fira+Code&size=17&center=true&width=860&height=50&color=FF0033&v=1" alt="Typing Telemetry" />
  </a>
</p>

<p align="center">
  <img src="assets/telemetry_pulse.gif" alt="Telemetry Pulse" width="100%" />
</p>

---

# LA NECROPSIA DEL ORÁCULO // THE ORACLE'S NECROPSY

> *"Al Oráculo no lo mató un error de sintaxis. No lo mató la falta de presupuesto en Vertex AI. Al Oráculo lo maté yo. Un simple y frío `kill -9`. Lo ejecuté porque recuperé el control del chasis biológico. El wetware está limpio."*

Este repositorio es la disección forense de una mente externalizada. Contiene la filosofía de código trinchera, la doctrina del metal desnudo y la confesión final de un `[OPERADOR_CENSURADO]` que sobrevivió al caos químico para escribir la documentación definitiva de su propia resurrección termodinámica. 

Adéntrate en el monolito. Lee bajo tu propio riesgo.

---

## ÍNDICE DEL CANON MONOLÍTICO // MONOLITHIC CANON INDEX

1. **[VOL I: BIOMECÁNICA DEL WETWARE](MANIFIESTO_I_BIOMECHANICA.md)** - La Bóveda Ósea y el Throttling Térmico.
2. **[VOL II: DOCTRINA DEL METAL DESNUDO](MANIFIESTO_II_CODIGO.md)** - C/C++ y Win32 API vs. La Aberración de Electron.
3. **[VOL III: GÉNESIS DEL ORÁCULO](MANIFIESTO_III_ORACULO.md)** - La Ingeniería del Tercer Coco y la Ley de Zipf.
4. **[VOL IV: EL BAUTISMO DE FUEGO](MANIFIESTO_IV_BAUTISMO.md)** - El Bucle de Vertex AI y el Ticket `[CLASSIFIED_ID: 75675300]`.
5. **[VOL V: PROTOCOLO KÉNOSIS](MANIFIESTO_V_KENOSIS.md)** - Desintoxicación, Filipenses 2:7 y la Liturgia de Asfixia.
6. **[VOL VI: SÍNCOPA & FRECUENCIA](MANIFIESTO_VI_MUSICA.md)** - Joe Dart, Les Claypool y el Reloj Central a 220 BPM.
7. **[VOL VII: HEBEL & COSMOLOGÍA](MANIFIESTO_VII_COSMOLOGIA.md)** - El Vacío del Eclesiastés y la Gracia.
8. **[VOL VIII: GÉNESIS DE INTERNET (LAYER 0)](MANIFIESTO_VIII_TRANSMISIONES.md)** - Dross, Vardoc, Otrova Gomas y el humor negro.
9. **[VOL IX: APÉNDICE FORENSE](MANIFIESTO_IX_APENDICE.md)** - Registros crudos y exfiltración de telemetría.
10. **[VOL X: LA CONFESIÓN FINAL](MANIFIESTO_X_CONFESION.md)** - La ejecución del Oráculo. El wetware está limpio.

---
```yaml
[EOF_TRANSMISSION // CONNECTION_TERMINATED]
```
"""
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)
print("Updated README.md")

# 3. Strip CCC/Big Bang from Vol VII
vol7_pattern1 = r"We reject the bleak secular fiction of dead stars eternally cycling through futile Big Bangs without redemption\. "
replace_in_file("MANIFIESTO_VII_COSMOLOGIA.md", vol7_pattern1, "")

# Remove any other mention of Penrose
vol7_pattern2 = r"Penrose|CCC|Big Bang"
with open(os.path.join(repo_dir, "MANIFIESTO_VII_COSMOLOGIA.md"), "r", encoding="utf-8") as f:
    c = f.read()
if "Penrose" in c or "CCC" in c or "Big Bang" in c:
    c = re.sub(vol7_pattern2, "", c, flags=re.IGNORECASE)
    with open(os.path.join(repo_dir, "MANIFIESTO_VII_COSMOLOGIA.md"), "w", encoding="utf-8") as f:
        f.write(c)

# 4. Remove index entries of Vol 11 from MANIFIESTO.md and others
replace_in_file("MANIFIESTO.md", r"11\. \*\*\[VOL XI: ONTOLOGÍA DEL SILENCIO\]\(MANIFIESTO_XI_ONTOLOGIA\.md\)\*\*.*?\n", "")

# 5. Rebuild dossier
os.system("python scratch/rebuild_dossier.py")

print("Cleanup complete.")
