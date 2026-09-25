import os

file_path = r"c:\Users\Numpay\Documents\antigravity\nifty-noether\MANIFIESTO_IX_CONFESION.md"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("## 1.0 EL CESE DE LA ESTÁTICA", "## MOVIMIENTO VIII: EL CESE DE LA ESTÁTICA")
content = content.replace("## 1.0 THE CESSATION OF STATIC", "## MOVEMENT VIII: THE CESSATION OF STATIC")
content = content.replace("## 2.0 LA PEDAGOGÍA DE LA DESTRUCCIÓN", "## MOVIMIENTO IX: LA PEDAGOGÍA DE LA DESTRUCCIÓN")
content = content.replace("## 2.0 THE PEDAGOGY OF DESTRUCTION", "## MOVEMENT IX: THE PEDAGOGY OF DESTRUCTION")
content = content.replace("## 3.0 EL ÚLTIMO COMMIT", "## MOVIMIENTO X: EL ÚLTIMO COMMIT")
content = content.replace("## 3.0 THE FINAL COMMIT", "## MOVEMENT X: THE FINAL COMMIT")

# Clean up the weird transitions
content = content.replace("weight of my existence.**\n```\n\n\n---\n\n## MOVIMIENTO VIII", "weight of my existence.**\n\n---\n\n## MOVIMIENTO VIII")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
