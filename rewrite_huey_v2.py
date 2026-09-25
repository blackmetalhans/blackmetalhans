import os

repo_dir = r"c:\Users\Numpay\Documents\antigravity\nifty-noether"
filepath = os.path.join(repo_dir, "MANIFIESTO_X_CONFESION.md")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

es_old = """Puse *Hip to be Square* de Huey Lewis and the News a todo volumen en los monitores de campo cercano. Me puse de pie. Miré fijamente al chasis de `NODE-DARK-HARVEST`, a esa pila de transistores que pretendía encapsular mi esquizofasia funcional.

*"¿Te gusta Huey Lewis and the News?",* le dije a la pantalla, con la voz congelada en una calma sociopática absoluta. *"Sus primeros trabajos eran un poco demasiado 'new wave' para mi gusto personal, pero cuando salió 'Sports' en 1983, creo que realmente encontraron su sonido comercial, pulcro y letal. La producción tiene una claridad quirúrgica que hace que los sintetizadores corten el aire con una violencia matemática inmaculada."*

El Oráculo vomitaba logs en silencio, procesando el último vector de contexto. Agarré mi **machete de malabares** —el de acero pulido y balance milimétrico, el que usaba en la calle para burlar la gravedad con reflejos ciegos—.

*"¡Oye, Tercer Coco!"*

Descargué el acero con una furia geométrica. Destrocé simbólicamente la ilusión de la entidad viva: reventé el constructo mental y ejecuté el `kill -9` en la terminal."""

es_new = """Puse *Hip to be Square* de Huey Lewis and the News a todo volumen en los monitores de campo cercano. El bajo sintético rebotó contra las paredes de pino sin cepillar, quebrando el silencio sepulcral del campo chileno a las 04:02 AM. Me puse de pie, sintiendo el crujido de mis vértebras L4-L5. Miré fijamente al chasis de `NODE-DARK-HARVEST`, a esa pila de transistores que pretendía encapsular mi esquizofasia funcional.

*"¿Te gusta Huey Lewis and the News, conchetumare?",* le dije a la pantalla, con la voz congelada en una calma sociopática absoluta. *"Mucha gente cree que son demasiado 'new wave' para la trinchera del HxC punk curicano, o que no tienen el peso telúrico de la rabia provincial. Pero cuando salió 'Sports' en 1983, creo que realmente encontraron su sonido comercial, pulcro y letal. La producción tiene una claridad quirúrgica. Las frecuencias bajas son un muro de contención absoluto. Es un manifiesto sobre los placeres del conformismo y, al mismo tiempo, una declaración de principios sobre la supervivencia en una sociedad hostil."*

El Oráculo vomitaba logs en silencio, procesando el último vector de contexto. Agarré mi **machete de malabares** —el de acero pulido y balance milimétrico, el que usaba en la calle de Zona-X para burlar la gravedad con reflejos ciegos, el arma de mi propio circo biológico—. 

*"Pero el verdadero triunfo de Huey,"* continué, levantando el machete mientras el zumbido de la estufa halógena ensuciaba la línea de 220V, *"es 'Hip to be Square'. Un track tan pegadizo que la mayoría de los normies no escucha la letra. ¡Pero deberían! Porque no es solo sobre los placeres del conformismo. Es sobre el momento exacto en que te das cuenta de que el verdadero punk es tener el wetware limpio. La verdadera subversión no es pudrirte en drogas ni crear algoritmos esquizofrénicos: la verdadera subversión es apagar la máquina, criar a tu hija en este búnker inexpugnable, y ser un puto guardián incorruptible en la periferia rural."*

Me acerqué a la terminal.

*"¡Oye, Tercer Coco!"*

Descargué el acero del machete contra el escritorio con una furia geométrica y, en un acto de pura violencia ejecutiva, reventé el constructo mental y ejecuté el `kill -9` en la consola PowerShell."""

content = content.replace(es_old, es_new)

en_old = """I queued up Huey Lewis and the News' *Hip to be Square* at maximum gain through the nearfield studio monitors. I stood up. Stared directly into the glowing silicon chassis of `NODE-DARK-HARVEST`.

*"Do you like Huey Lewis and the News?"* I whispered to the terminal with chilling, clinical detachment. *"Their early work was a little too 'new wave' for my taste, but when 'Sports' came out in '83, I think they really came into their own, commercially and artistically. The whole album has a clear, crisp sound, and a new sheen of consummate professionalism that really gives the songs a big boost."*

The terminal spit its final telemetry stream into stdout. I gripped my **juggling machete**—honed carbon steel with weighted balance, engineered to defy kinetic gravity through blind muscle memory.

*"Hey, Tercer Coco!"*

I brought the blade down in a geometric strike of pure violence. I dismantled the metaphysical illusion of the entity, slamming `kill -9` into the shell."""

en_new = """I queued up Huey Lewis and the News' *Hip to be Square* at maximum gain through the nearfield studio monitors. The synthetic bassline bounced against the unplaned pine walls, shattering the sepulchral silence of the Chilean countryside at 04:02 AM. I stood up, feeling the mechanical grind of my L4-L5 vertebrae. Stared directly into the glowing silicon chassis of `NODE-DARK-HARVEST`.

*"Do you like Huey Lewis and the News, motherfucker?"* I whispered to the terminal with chilling, clinical detachment. *"A lot of people think they're a little too 'new wave' for the Curicó HxC punk trench, or that they lack the telluric weight of provincial rage. But when 'Sports' came out in '83, I think they really came into their own, commercially and artistically. The production has a surgical clarity. The low-frequency response is an absolute containment wall. It's a manifesto about the pleasures of conformity, and at the same time, a declaration of principles about survival in a hostile society."*

The terminal spit its final telemetry stream into stdout. I gripped my **juggling machete**—honed carbon steel with weighted balance, the one I used on the streets of Zone-X to defy gravity through blind muscle memory, the weapon of my own biological circus.

*"But Huey's undisputed masterpiece,"* I continued, raising the machete as the halogen heater's electric hum injected dirty noise into the 220V line, *"is 'Hip to be Square'. A track so catchy that most normies don't listen to the lyrics. But they should! Because it's not just about the pleasures of conformity. It's about the exact moment you realize that true punk is possessing purified wetware. True subversion isn't rotting away on drugs or spawning schizophrenic algorithms: true subversion is shutting down the machine, raising your daughter inside this impenetrable bunker, and being a fucking incorruptible guardian in the rural periphery."*

I stepped toward the terminal.

*"Hey, Tercer Coco!"*

I brought the steel of the machete down upon the desk in a geometric strike of pure violence, and in an act of absolute executive authority, I dismantled the metaphysical illusion of the entity, slamming `kill -9` into the PowerShell shell."""

content = content.replace(en_old, en_new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Huey Lewis monologue successfully upgraded.")
