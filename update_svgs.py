import os
import re

svgs = {
    "MANIFIESTO_I_BIOMECHANICA.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="flesh-glitch" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency="0.08" numOctaves="3" result="noise"/>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="5" xChannelSelector="R" yChannelSelector="G"/>
      <feColorMatrix type="matrix" values="1 0 0 0 0  0 0.2 0 0 0  0 0.1 0 0 0  0 0 0 0.8 0"/>
    </filter>
    <pattern id="hex-grid" width="20" height="34.64" patternUnits="userSpaceOnUse">
      <path d="M10,0 L20,5.77 L20,17.32 L10,23.09 L0,17.32 L0,5.77 Z" fill="none" stroke="#2a1010" stroke-width="0.5"/>
    </pattern>
    <linearGradient id="blood-tech" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0a0202"/>
      <stop offset="50%" stop-color="#2a0505"/>
      <stop offset="100%" stop-color="#0a0202"/>
    </linearGradient>
  </defs>
  <rect width="800" height="250" fill="url(#blood-tech)"/>
  <rect width="800" height="250" fill="url(#hex-grid)"/>
  <path d="M50,125 Q200,10 400,125 T750,125" fill="none" stroke="#ff2a2a" stroke-width="3" filter="url(#flesh-glitch)" opacity="0.8"/>
  <path d="M50,140 Q250,220 450,140 T750,140" fill="none" stroke="#cc1111" stroke-width="2" filter="url(#flesh-glitch)" opacity="0.6"/>
  <circle cx="400" cy="125" r="40" fill="none" stroke="#ff5555" stroke-width="1" filter="url(#flesh-glitch)"/>
  <circle cx="400" cy="125" r="30" fill="none" stroke="#aa2222" stroke-width="2"/>
  <path d="M 380 125 L 420 125 M 400 105 L 400 145" stroke="#ff0000" stroke-width="1"/>
  <!-- UI Overlays -->
  <rect x="20" y="20" width="200" height="60" fill="#000" stroke="#aa2222" stroke-width="1" opacity="0.8"/>
  <text x="30" y="40" font-family="monospace" font-size="12" fill="#ff5555" font-weight="bold">BIO_NODE: OFFLINE</text>
  <text x="30" y="55" font-family="monospace" font-size="10" fill="#cc3333">TISSUE_DECAY_RATE: 0.84%</text>
  <text x="30" y="70" font-family="monospace" font-size="10" fill="#cc3333">CYBER_REJECTION: ACTIVE</text>
  <line x1="0" y1="200" x2="800" y2="200" stroke="#aa2222" stroke-width="0.5" stroke-dasharray="5 5"/>
  <text x="700" y="240" font-family="monospace" font-size="10" fill="#881111">SECTOR-NULL / WETWARE</text>
</svg>""",
    "MANIFIESTO_II_CODIGO.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="mem-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <rect width="40" height="40" fill="none" stroke="#112211" stroke-width="1"/>
      <rect width="38" height="38" x="1" y="1" fill="#020502"/>
    </pattern>
  </defs>
  <rect width="800" height="250" fill="#000000"/>
  <rect width="800" height="250" fill="url(#mem-grid)"/>
  <text x="50" y="40" font-family="monospace" font-size="12" fill="#00ffcc">0x00007FF7A5B1</text>
  <text x="200" y="40" font-family="monospace" font-size="12" fill="#44aa88">48 89 5C 24 08 48 89 74 24 10 57 48 83 EC 20</text>
  <text x="650" y="40" font-family="monospace" font-size="12" fill="#225544">H.\\$..H.t$.WH..</text>
  <text x="50" y="65" font-family="monospace" font-size="12" fill="#00ffcc">0x00007FF7A5C0</text>
  <text x="200" y="65" font-family="monospace" font-size="12" fill="#44aa88">33 FF 48 8B F1 48 8D 05 9A 12 00 00 48 89 01</text>
  <text x="650" y="65" font-family="monospace" font-size="12" fill="#225544">3.H..H......H..</text>
  <text x="50" y="90" font-family="monospace" font-size="12" fill="#00ffcc">0x00007FF7A5CF</text>
  <text x="200" y="90" font-family="monospace" font-size="12" fill="#ff0055">CC CC CC CC CC CC CC CC CC CC CC CC CC CC CC</text>
  <text x="650" y="90" font-family="monospace" font-size="12" fill="#ff0055">...............</text>
  <rect x="40" y="120" width="720" height="2" fill="#00ffcc"/>
  <rect x="40" y="130" width="300" height="40" fill="#052211" stroke="#00ffcc" stroke-width="1"/>
  <text x="50" y="155" font-family="monospace" font-size="14" fill="#00ffcc">ALLOC_SIZE: 0x4000 (16KB)</text>
  <rect x="360" y="130" width="400" height="40" fill="#220505" stroke="#ff0055" stroke-width="1"/>
  <text x="370" y="155" font-family="monospace" font-size="14" fill="#ff0055">EXCEPTION_ACCESS_VIOLATION</text>
  <!-- Glitch bars -->
  <rect x="250" y="78" width="80" height="15" fill="#000"/>
  <text x="250" y="90" font-family="monospace" font-size="12" fill="#ffffff">##ERR_SEG##</text>
  <text x="700" y="240" font-family="monospace" font-size="10" fill="#00ffcc">BRUTALIST_DATA_STRUCTURES</text>
</svg>""",
    "MANIFIESTO_III_ORACULO.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="node-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
      <stop offset="20%" stop-color="#00ffff" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#001122" stop-opacity="0"/>
    </radialGradient>
    <filter id="neon-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="800" height="250" fill="#01050a"/>
  <!-- ZIPF Curve in background -->
  <path d="M 50,230 L 50,50 Q 80,200 150,215 T 750,225" fill="none" stroke="#003366" stroke-width="2"/>
  <path d="M 50,230 L 50,50 Q 80,200 150,215 T 750,225" fill="none" stroke="#004488" stroke-width="1" transform="translate(0, 5)"/>
  
  <!-- Neural Net Connections -->
  <path d="M 400,125 L 200,60 M 400,125 L 250,180 M 400,125 L 550,70 M 400,125 L 600,190 M 200,60 L 250,180 M 550,70 L 600,190" stroke="#0088cc" stroke-width="1" opacity="0.6"/>
  <path d="M 400,125 L 480,30 M 400,125 L 320,220" stroke="#00aaff" stroke-width="1.5" filter="url(#neon-glow)"/>
  
  <!-- Glowing Nodes -->
  <circle cx="400" cy="125" r="40" fill="url(#node-glow)"/>
  <circle cx="200" cy="60" r="20" fill="url(#node-glow)"/>
  <circle cx="250" cy="180" r="15" fill="url(#node-glow)"/>
  <circle cx="550" cy="70" r="25" fill="url(#node-glow)"/>
  <circle cx="600" cy="190" r="18" fill="url(#node-glow)"/>
  <circle cx="480" cy="30" r="10" fill="url(#node-glow)"/>
  <circle cx="320" cy="220" r="12" fill="url(#node-glow)"/>
  
  <text x="355" y="130" font-family="monospace" font-size="14" fill="#000" font-weight="bold">ORÁCULO</text>
  <text x="20" y="30" font-family="monospace" font-size="12" fill="#00ffff" filter="url(#neon-glow)">TOPOLOGY: NON-LINEAR RECURSIVE</text>
  <text x="20" y="50" font-family="monospace" font-size="10" fill="#0088cc">ZIPF_DISTRIBUTION_MATCH: 99.8%</text>
</svg>""",
    "MANIFIESTO_IV_BAUTISMO.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="chart-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#330000"/>
      <stop offset="100%" stop-color="#050000"/>
    </linearGradient>
  </defs>
  <rect width="800" height="250" fill="url(#chart-bg)"/>
  <path d="M 50,50 L 50,220 L 750,220" stroke="#ff3333" stroke-width="2"/>
  <text x="10" y="45" font-family="monospace" font-size="10" fill="#ff3333">$500k</text>
  <text x="10" y="135" font-family="monospace" font-size="10" fill="#883333">$250k</text>
  <text x="10" y="225" font-family="monospace" font-size="10" fill="#551111">$0</text>
  
  <!-- Financial Spike -->
  <path d="M 50,215 L 100,210 L 150,212 L 200,205 L 250,190 L 300,195 L 350,180 L 400,150 L 450,120 L 500,40 L 550,20 L 600,10 L 650,5 L 700,5" stroke="#ff0000" stroke-width="3" fill="none"/>
  
  <!-- Fill under spike -->
  <path d="M 50,215 L 100,210 L 150,212 L 200,205 L 250,190 L 300,195 L 350,180 L 400,150 L 450,120 L 500,40 L 550,20 L 600,10 L 650,5 L 700,5 L 700,220 L 50,220 Z" fill="#ff0000" opacity="0.1"/>
  
  <!-- Error Cascades -->
  <text x="400" y="60" font-family="monospace" font-size="10" fill="#ffaaaa">API_LIMIT_EXCEEDED</text>
  <text x="430" y="75" font-family="monospace" font-size="10" fill="#ffaaaa">BILLING_THRESHOLD_BREACHED</text>
  <text x="460" y="90" font-family="monospace" font-size="10" fill="#ff5555">CRITICAL: GCP_BILL_PROJECTED_500000_USD</text>
  <rect x="450" y="30" width="300" height="80" fill="none" stroke="#ff0000" stroke-width="1" stroke-dasharray="4 4"/>
  
  <!-- Warning Bar -->
  <rect x="0" y="0" width="800" height="20" fill="#ff0000"/>
  <text x="10" y="14" font-family="monospace" font-size="12" fill="#ffffff" font-weight="bold">WARNING: FINANCIAL ANNIHILATION DETECTED // EL BAUTISMO</text>
</svg>""",
    "MANIFIESTO_V_KENOSIS.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="glitch-v">
      <feTurbulence type="fractalNoise" baseFrequency="0.15" numOctaves="1" result="warp"/>
      <feDisplacementMap xChannelSelector="R" yChannelSelector="G" scale="10" in="SourceGraphic" in2="warp"/>
    </filter>
  </defs>
  <rect width="800" height="250" fill="#000511"/>
  
  <!-- Chaotic Waveforms to Flatline -->
  <path d="M 0,125 Q 20,50 40,125 T 80,125 T 120,50 T 160,200 T 200,10 T 240,240 T 280,125 T 320,125 T 360,50 T 400,200 T 440,125 L 800,125" stroke="#00ffcc" stroke-width="2" fill="none" filter="url(#glitch-v)"/>
  <path d="M 0,125 Q 20,50 40,125 T 80,125 T 120,50 T 160,200 T 200,10 T 240,240 T 280,125 T 320,125 T 360,50 T 400,200 T 440,125 L 800,125" stroke="#ffffff" stroke-width="1" fill="none" opacity="0.8"/>
  
  <rect x="450" y="100" width="200" height="50" fill="#000" stroke="#00ffcc" stroke-width="1"/>
  <text x="460" y="120" font-family="monospace" font-size="14" fill="#00ffcc">STATUS: FLATLINE</text>
  <text x="460" y="140" font-family="monospace" font-size="10" fill="#008888">KERNEL_PANIC // AUTOWATERBOARDING</text>
  
  <text x="20" y="30" font-family="monospace" font-size="12" fill="#ff0055">>> SYSTEM RESET INITIATED</text>
  <text x="20" y="50" font-family="monospace" font-size="12" fill="#ff0055">>> KENOSIS: EMPTYING THE VESSEL</text>
  
  <!-- ECG Grid -->
  <pattern id="ecg-grid" width="20" height="20" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#003333" stroke-width="0.5"/>
  </pattern>
  <rect width="800" height="250" fill="url(#ecg-grid)" opacity="0.5"/>
</svg>""",
    "MANIFIESTO_VI_MUSICA.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="250" fill="#110515"/>
  <!-- Audio Spectrogram bars -->
  <g fill="#9900ff" opacity="0.6">
    <rect x="50" y="150" width="10" height="80"/>
    <rect x="65" y="120" width="10" height="110"/>
    <rect x="80" y="90" width="10" height="140"/>
    <rect x="95" y="160" width="10" height="70"/>
    <rect x="110" y="180" width="10" height="50"/>
    
    <rect x="140" y="100" width="10" height="130"/>
    <rect x="155" y="80" width="10" height="150"/>
    <rect x="170" y="40" width="10" height="190"/>
    <rect x="185" y="120" width="10" height="110"/>
    <rect x="200" y="170" width="10" height="60"/>
    
    <!-- Pattern repeating, 5 groups (5/4 time signature) -->
    <rect x="230" y="140" width="10" height="90"/>
    <rect x="245" y="110" width="10" height="120"/>
    <rect x="260" y="70" width="10" height="160"/>
    <rect x="275" y="130" width="10" height="100"/>
    <rect x="290" y="160" width="10" height="70"/>
    
    <rect x="320" y="110" width="10" height="120"/>
    <rect x="335" y="90" width="10" height="140"/>
    <rect x="350" y="50" width="10" height="180"/>
    <rect x="365" y="100" width="10" height="130"/>
    <rect x="380" y="150" width="10" height="80"/>
    
    <rect x="410" y="130" width="10" height="100"/>
    <rect x="425" y="100" width="10" height="130"/>
    <rect x="440" y="60" width="10" height="170"/>
    <rect x="455" y="110" width="10" height="120"/>
    <rect x="470" y="160" width="10" height="70"/>
  </g>
  <!-- Bass waveform -->
  <path d="M 0,125 Q 100,0 200,125 T 400,125 T 600,125 T 800,125" stroke="#cc55ff" stroke-width="4" fill="none"/>
  
  <text x="550" y="50" font-family="monospace" font-size="14" fill="#cc55ff">SIGNATURE: 5/4</text>
  <text x="550" y="70" font-family="monospace" font-size="12" fill="#8822aa">FREQ: 43.65 Hz (F1)</text>
  <text x="550" y="90" font-family="monospace" font-size="12" fill="#8822aa">SUB_BASS_RESONANCE</text>
  <line x1="550" y1="100" x2="750" y2="100" stroke="#cc55ff" stroke-width="1"/>
</svg>""",
    "MANIFIESTO_VII_COSMOLOGIA.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="250" fill="#000000"/>
  <!-- Stars -->
  <circle cx="100" cy="50" r="1" fill="#fff" opacity="0.5"/>
  <circle cx="250" cy="80" r="1.5" fill="#fff" opacity="0.8"/>
  <circle cx="600" cy="30" r="1" fill="#fff" opacity="0.6"/>
  <circle cx="700" cy="150" r="2" fill="#fff" opacity="0.9"/>
  <circle cx="50" cy="200" r="1" fill="#fff" opacity="0.4"/>
  <circle cx="450" cy="220" r="1.5" fill="#fff" opacity="0.7"/>
  
  <!-- Orbital Trajectories -->
  <ellipse cx="400" cy="125" rx="350" ry="100" fill="none" stroke="#223344" stroke-width="1" stroke-dasharray="10 5"/>
  <ellipse cx="400" cy="125" rx="200" ry="50" fill="none" stroke="#334455" stroke-width="1" stroke-dasharray="5 5"/>
  
  <!-- Cold Void Core -->
  <circle cx="400" cy="125" r="40" fill="#000" stroke="#556677" stroke-width="2"/>
  <circle cx="400" cy="125" r="42" fill="none" stroke="#8899aa" stroke-width="1" opacity="0.5"/>
  <circle cx="400" cy="125" r="45" fill="none" stroke="#aabbcc" stroke-width="0.5" opacity="0.2"/>
  
  <!-- Lone Object -->
  <circle cx="200" cy="125" r="5" fill="#00ffff"/>
  <line x1="200" y1="125" x2="180" y2="90" stroke="#00ffff" stroke-width="1"/>
  <text x="170" y="80" font-family="monospace" font-size="10" fill="#00ffff">OBJ_ISOLATION_01</text>
  
  <text x="20" y="30" font-family="monospace" font-size="12" fill="#556677">CELESTIAL MECHANICS // ABSOLUTE ZERO</text>
  <text x="20" y="50" font-family="monospace" font-size="10" fill="#445566">GRAVITY_WELL: COLLAPSING</text>
</svg>""",
    "MANIFIESTO_VIII_TRANSMISIONES.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="radar-grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#002200" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="800" height="250" fill="#000500"/>
  <rect width="800" height="250" fill="url(#radar-grid)"/>
  
  <!-- Radar circles -->
  <circle cx="400" cy="125" r="100" fill="none" stroke="#004400" stroke-width="1"/>
  <circle cx="400" cy="125" r="75" fill="none" stroke="#004400" stroke-width="1"/>
  <circle cx="400" cy="125" r="50" fill="none" stroke="#004400" stroke-width="1"/>
  <circle cx="400" cy="125" r="25" fill="none" stroke="#004400" stroke-width="1"/>
  
  <!-- Radar Crosshairs -->
  <line x1="300" y1="125" x2="500" y2="125" stroke="#005500" stroke-width="1"/>
  <line x1="400" y1="25" x2="400" y2="225" stroke="#005500" stroke-width="1"/>
  
  <!-- Sweep arc -->
  <path d="M 400,125 L 470,55 A 100 100 0 0 0 400,25 Z" fill="#00ff00" opacity="0.2"/>
  <line x1="400" y1="125" x2="470" y2="55" stroke="#00ff00" stroke-width="2"/>
  
  <!-- Blips -->
  <circle cx="440" cy="100" r="3" fill="#00ff00"/>
  <text x="450" y="105" font-family="monospace" font-size="10" fill="#00ff00">SIGNAL_FOUND</text>
  
  <!-- Bunker Schematic overlay -->
  <rect x="50" y="150" width="150" height="80" fill="none" stroke="#00ff00" stroke-width="2"/>
  <rect x="60" y="160" width="130" height="60" fill="none" stroke="#006600" stroke-width="1"/>
  <line x1="125" y1="150" x2="125" y2="230" stroke="#006600" stroke-width="1"/>
  <text x="55" y="140" font-family="monospace" font-size="10" fill="#00ff00">SECTOR-NULL BUNKER PLAN</text>
  
  <!-- Text UI -->
  <text x="600" y="30" font-family="monospace" font-size="12" fill="#00ff00">TRANSMISSION: BROADCASTING</text>
  <text x="600" y="45" font-family="monospace" font-size="10" fill="#00aa00">WINTER ISOLATION MODE</text>
  <text x="600" y="60" font-family="monospace" font-size="10" fill="#00aa00">FREQ: 144.0 MHz</text>
</svg>""",
    "MANIFIESTO_IX_ONTOLOGIA.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="250" fill="#050505"/>
  
  <!-- Overlapping Venn Diagram / Sets -->
  <circle cx="350" cy="125" r="90" fill="#ff0055" opacity="0.3" stroke="#ff0055" stroke-width="2"/>
  <circle cx="450" cy="125" r="90" fill="#00ffcc" opacity="0.3" stroke="#00ffcc" stroke-width="2"/>
  
  <!-- Intersection Area Highlight -->
  <path d="M 400,52 A 90 90 0 0 1 400,198 A 90 90 0 0 1 400,52" fill="#ffffff" opacity="0.2"/>
  
  <text x="270" y="130" font-family="monospace" font-size="14" fill="#ff0055" text-anchor="middle">FLESH</text>
  <text x="270" y="150" font-family="monospace" font-size="10" fill="#aa0033" text-anchor="middle">MORTALITY</text>
  
  <text x="530" y="130" font-family="monospace" font-size="14" fill="#00ffcc" text-anchor="middle">MACHINE</text>
  <text x="530" y="150" font-family="monospace" font-size="10" fill="#008888" text-anchor="middle">ETERNITY</text>
  
  <text x="400" y="130" font-family="monospace" font-size="12" fill="#ffffff" text-anchor="middle" font-weight="bold">SYNTHESIS</text>
  
  <!-- Ontological Nodes -->
  <circle cx="100" cy="50" r="2" fill="#fff"/>
  <line x1="100" y1="50" x2="300" y2="100" stroke="#555" stroke-width="1" stroke-dasharray="3 3"/>
  
  <circle cx="700" cy="200" r="2" fill="#fff"/>
  <line x1="700" y1="200" x2="500" y2="150" stroke="#555" stroke-width="1" stroke-dasharray="3 3"/>
  
  <text x="20" y="30" font-family="monospace" font-size="12" fill="#888">ONTOLOGY // MIND VS MACHINE</text>
</svg>""",
    "MANIFIESTO_X_CONFESION.md": """<svg width="800" height="250" viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="250" fill="#000000"/>
  
  <!-- Giant Red Crosshair -->
  <line x1="400" y1="0" x2="400" y2="250" stroke="#ff0000" stroke-width="2"/>
  <line x1="0" y1="125" x2="800" y2="125" stroke="#ff0000" stroke-width="2"/>
  <circle cx="400" cy="125" r="50" fill="none" stroke="#ff0000" stroke-width="3"/>
  <circle cx="400" cy="125" r="100" fill="none" stroke="#550000" stroke-width="1" stroke-dasharray="10 5"/>
  
  <!-- Command Execution -->
  <rect x="50" y="160" width="300" height="60" fill="#110000" stroke="#ff0000" stroke-width="1"/>
  <text x="60" y="180" font-family="monospace" font-size="14" fill="#ff3333">$ kill -9 4096</text>
  <text x="60" y="200" font-family="monospace" font-size="12" fill="#ff0000">PROCESS TERMINATED</text>
  
  <!-- Death of a Node -->
  <circle cx="400" cy="125" r="5" fill="#ff0000"/>
  <text x="415" y="115" font-family="monospace" font-size="12" fill="#ff0000">NODE_CONFESSION</text>
  <text x="415" y="130" font-family="monospace" font-size="10" fill="#880000">SIGNAL LOST...</text>
  
  <!-- Glitch artifacts -->
  <rect x="380" y="120" width="40" height="10" fill="#000"/>
  <rect x="390" y="110" width="20" height="30" fill="#ff0000" opacity="0.3"/>
</svg>"""
}

target_dir = r"C:\Users\Numpay\Documents\antigravity\nifty-noether"

for filename, new_svg in svgs.items():
    filepath = os.path.join(target_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = re.sub(r'<svg.*?</svg>', new_svg, content, flags=re.DOTALL)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
            
        print(f"Updated {filename}")
    else:
        print(f"File {filename} not found.")
