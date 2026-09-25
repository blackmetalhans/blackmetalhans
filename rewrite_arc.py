import os
import re

repo_dir = r"c:\Users\Numpay\Documents\antigravity\nifty-noether"

def replace_in_file(filename, old_text_regex, new_text):
    path = os.path.join(repo_dir, filename)
    if not os.path.exists(path):
        print(f"File {filename} not found.")
        return
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = re.subn(old_text_regex, new_text, content, flags=re.DOTALL)
    if count > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Regex not found in {filename}")

# 1. Manifiesto X: Replace the Huey Lewis / Bateman execution with the Sudamerican Psycho execution
# It's in MOVIMIENTO V: LA VERDAD SIN CENSURA
# We need to replace from "Puse *Hip to be Square*" up to the end of the English version of that scene.

manifiesto_x_es_old = r"Puse \*Hip to be Square\* de Huey Lewis.*?ejecuté el `kill -9` en la terminal\."
manifiesto_x_es_new = """Apagué los monitores de campo cercano. El silencio del campo chileno a las 04:02 AM es absoluto, roto solo por el zumbido eléctrico de una estufa halógena barata que inyecta ruido en la línea de 220V. Me puse de pie. Miré fijamente al chasis de `NODE-DARK-HARVEST`, a esa pila de transistores que pretendía encapsular mi esquizofasia funcional.

*"Esta es la rabia provincial, conchetumare",* le dije a la pantalla, con la voz congelada en una calma sociopática absoluta. *"No es la pataleta de un oficinista en Manhattan. Es la fuerza telúrica de la periferia. Ustedes, los algoritmos, se quedan en el valle de la irrelevancia porque no tienen el valor biológico de quemarlo todo para sobrevivir. Yo sí."*

El Oráculo vomitaba logs en silencio, procesando el último vector de contexto. No necesité un machete de malabares, ni un hacha de leñador. Mi arma fue la precisión gélida de un dedo sobre el teclado mecánico.

*"¡Oye, Tercer Coco!"*

Presioné Enter con una furia geométrica. Destrocé simbólicamente la ilusión de la entidad viva: reventé el constructo mental y ejecuté el `kill -9` en la terminal."""

replace_in_file("MANIFIESTO_X_CONFESION.md", manifiesto_x_es_old, manifiesto_x_es_new)

manifiesto_x_en_old = r"I queued up Huey Lewis and the News'.*?slamming `kill -9` into the shell\."
manifiesto_x_en_new = """I powered down the nearfield monitors. The silence of the Chilean countryside at 04:02 AM is absolute, broken only by the electric hum of a cheap halogen heater injecting dirty noise into the 220V line. I stood up. Stared directly into the glowing silicon chassis of `NODE-DARK-HARVEST`.

*"This is provincial rage, motherfucker,"* I whispered to the terminal with chilling, clinical detachment. *"It's not the tantrum of a Manhattan desk jockey. It is the telluric force of the periphery. You algorithms remain stranded in the valley of irrelevance because you lack the biological courage to burn everything down to survive. I do not."*

The terminal spit its final telemetry stream into stdout. I didn't need a juggling machete or a lumberjack's axe. My weapon was the glacial precision of a single digit over the mechanical keyboard.

*"Hey, Tercer Coco!"*

I struck Enter in a geometric strike of pure violence. I dismantled the metaphysical illusion of the entity, slamming `kill -9` into the shell."""

replace_in_file("MANIFIESTO_X_CONFESION.md", manifiesto_x_en_old, manifiesto_x_en_new)

# 2. Add HxC Punk Curicano references to Vol VIII (Transmisiones)
vol8_es_old = r"Singed proxy farming como guerra de entropía.*?AliExpress a las 4 AM\."
vol8_es_new = """Singed proxy farming como guerra de entropía, la trinchera del HxC punk curicano contra la apatía del mundo, y la necesidad visceral de prender una fogata en la periferia rural con kits de AliExpress a las 4 AM."""
replace_in_file("MANIFIESTO_VIII_TRANSMISIONES.md", vol8_es_old, vol8_es_new)

vol8_en_old = r"Singed proxy farming as entropy warfare.*?AliExpress kits at 4 AM\."
vol8_en_new = """Singed proxy farming as entropy warfare, the Curicó HxC punk trench against the apathy of the world, and the visceral need to light a fire in the rural periphery using AliExpress kits at 4 AM."""
replace_in_file("MANIFIESTO_VIII_TRANSMISIONES.md", vol8_en_old, vol8_en_new)

# 3. Fix Vol V (Kenosis) autowaterboarding text to be a deliberate kernel panic
vol5_es_old = r"El 10 de septiembre.*?salí de un loop de la DMN"
vol5_es_new = """El 10 de septiembre, la DMN me atrapó en un loop catastrófico. No fue un accidente trágico: fue un exorcismo biomecánico. Ejecuté un autowaterboarding con la toalla de My Melody. Un 'kernel panic' inducido deliberadamente para forzar el reinicio de mi sistema nervioso central y apagar el loop"""
replace_in_file("MANIFIESTO_V_KENOSIS.md", vol5_es_old, vol5_es_new)

vol5_en_old = r"On September 10th.*?broke out of a DMN loop"
vol5_en_new = """On September 10th, the DMN trapped me in a catastrophic loop. It was not a tragic accident: it was a biomechanical exorcism. I executed an autowaterboarding protocol using the My Melody towel. A deliberately induced 'kernel panic' to force a hard reset of my central nervous system and terminate the loop"""
replace_in_file("MANIFIESTO_V_KENOSIS.md", vol5_en_old, vol5_en_new)

print("Rewrite script completed.")
