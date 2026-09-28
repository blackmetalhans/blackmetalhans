import os
import re
import random

base_dir = r'c:\Users\Numpay\Documents\antigravity\nifty-noether'

manifestos = [
    'MANIFIESTO_I_BIOMECHANICA.md',
    'MANIFIESTO_II_CODIGO.md',
    'MANIFIESTO_III_ORACULO.md',
    'MANIFIESTO_IV_BAUTISMO.md',
    'MANIFIESTO_V_KENOSIS.md',
    'MANIFIESTO_VI_MUSICA.md',
    'MANIFIESTO_VII_COSMOLOGIA.md',
    'MANIFIESTO_VIII_TRANSMISIONES.md',
    'MANIFIESTO_IX_ONTOLOGIA.md',
    'MANIFIESTO_X_CONFESION.md',
    'MANIFIESTO_XI_APENDICE.md'
]

def generate_cypherpunk_svg(title, index):
    colors = ['#00FF41', '#FF5500', '#00E5FF', '#FF003C', '#F4C430']
    primary_color = colors[index % len(colors)]
    
    # Generate some fake hex telemetry
    hex_data = ' '.join([f'{random.randint(0, 255):02X}' for _ in range(12)])
    
    svg = f'''<svg width="800" height="220" viewBox="0 0 800 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="grid_{index}" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1A1A1A" stroke-width="1"/>
    </pattern>
    <pattern id="dot_{index}" width="10" height="10" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1" fill="#2A2A2A"/>
    </pattern>
    <linearGradient id="grad_{index}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#050505"/>
      <stop offset="100%" stop-color="#111111"/>
    </linearGradient>
  </defs>
  
  <!-- Backgrounds -->
  <rect width="800" height="220" fill="url(#grad_{index})"/>
  <rect width="800" height="220" fill="url(#grid_{index})"/>
  <rect width="800" height="220" fill="url(#dot_{index})" opacity="0.5"/>
  
  <!-- Tech Borders & Crosshairs -->
  <rect x="10" y="10" width="780" height="200" fill="none" stroke="#333" stroke-width="2"/>
  <rect x="15" y="15" width="770" height="190" fill="none" stroke="#222" stroke-width="1"/>
  <path d="M 5 20 L 15 20 M 20 5 L 20 15 M 795 20 L 785 20 M 780 5 L 780 15" stroke="{primary_color}" stroke-width="2"/>
  <path d="M 5 200 L 15 200 M 20 215 L 20 205 M 795 200 L 785 200 M 780 215 L 780 205" stroke="{primary_color}" stroke-width="2"/>
  
  <!-- Waveform / Telemetry Graph -->
  <path d="M 30,150 L 150,150 L 180,80 L 220,180 L 260,110 L 290,150 L 500,150 L 520,100 L 550,150 L 770,150" stroke="{primary_color}" stroke-width="1.5" fill="none" stroke-linejoin="bevel"/>
  <path d="M 30,160 L 770,160" stroke="#222" stroke-width="1" stroke-dasharray="4 4"/>
  <path d="M 30,110 L 770,110" stroke="#222" stroke-width="1" stroke-dasharray="2 6"/>
  
  <!-- Overlay UI Elements -->
  <rect x="30" y="30" width="250" height="25" fill="#111" stroke="{primary_color}" stroke-width="1"/>
  <text x="40" y="47" font-family="monospace" font-size="12" fill="{primary_color}" font-weight="bold">SYS.OP // VOL_{index:02d} // {title}</text>
  
  <text x="30" y="80" font-family="monospace" font-size="10" fill="#666">[METRICS] BUFFER: 0x{hex_data[:8]}</text>
  <text x="30" y="95" font-family="monospace" font-size="10" fill="#666">[LINK] UPLINK SECURE | LATENCY: {random.randint(2, 14)}ms</text>
  
  <!-- Hex Dump -->
  <text x="600" y="40" font-family="monospace" font-size="10" fill="#555">MEM DUMP:</text>
  <text x="600" y="55" font-family="monospace" font-size="10" fill="{primary_color}">{hex_data}</text>
  <text x="600" y="70" font-family="monospace" font-size="10" fill="{primary_color}">{hex_data[::-1]}</text>
  
  <!-- Status Indicator -->
  <circle cx="750" cy="185" r="4" fill="{primary_color}">
    <animate attributeName="opacity" values="1;0;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="690" y="188" font-family="monospace" font-size="10" fill="#888">NODE ACTIVE</text>
</svg>'''
    return svg

for i, m in enumerate(manifestos):
    m_path = os.path.join(base_dir, m)
    if os.path.exists(m_path):
        with open(m_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 1. Update SVGs
        svg_pattern = r'<div align="center">\s*<svg.*?</svg>\s*</div>'
        title = m.replace('MANIFIESTO_', '').replace('.md', '').split('_')[-1]
        new_svg_block = f'<div align="center">\n{generate_cypherpunk_svg(title, i+1)}\n</div>'
        
        if re.search(svg_pattern, content, flags=re.DOTALL):
            content = re.sub(svg_pattern, new_svg_block, content, flags=re.DOTALL)
        else:
            # Try just matching SVG if div isn't there
            fallback_pattern = r'<svg.*?</svg>'
            if re.search(fallback_pattern, content, flags=re.DOTALL):
                content = re.sub(fallback_pattern, new_svg_block, content, flags=re.DOTALL)
            else:
                # Insert at top below image if present
                content = re.sub(r'(!\[.*?\]\(.*?\)\n)', r'\1\n' + new_svg_block + '\n', content)

        # 2. Aggressive deduplication
        if 'CONFESION' not in m and 'KENOSIS' not in m:
            content = re.sub(r'(?i)mis últimos 15 años', 'el ciclo previo', content)
            content = re.sub(r'(?i)15 años', 'el ciclo previo', content)
            content = re.sub(r'(?i)15 years', 'the prior cycle', content)
            content = re.sub(r'(?i)abril 2026', 'el inicio del registro', content)
            content = re.sub(r'(?i)April 2026', 'the inception of the ledger', content)
            content = re.sub(r'(?i)adicción', 'corrupción de sistema', content)
            content = re.sub(r'(?i)addiction', 'systemic corruption', content)
            content = re.sub(r'(?i)drogas', 'agentes de degradación térmica', content)
            content = re.sub(r'(?i)toalla', 'el disipador térmico improvisado', content)
            content = re.sub(r'(?i)towel', 'the improvised thermal sink', content)
            
        with open(m_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Rebuild Dossier
dossier_path = os.path.join(base_dir, 'DOSSIER_COMPLETO_REPOSITORIO_GEMINI.md')
dossier_content = '# DOSSIER COMPLETO REPOSITORIO GEMINI\n\n'

for m in manifestos:
    m_path = os.path.join(base_dir, m)
    if os.path.exists(m_path):
        with open(m_path, 'r', encoding='utf-8') as f:
            dossier_content += f.read() + '\n\n---\n\n'

with open(dossier_path, 'w', encoding='utf-8') as f:
    f.write(dossier_content)

print('Deduplication, SVG upgrades, and Dossier rebuild complete.')
