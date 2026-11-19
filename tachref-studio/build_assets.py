import os

img_dir = r"C:\Users\HP\.gemini\antigravity\scratch\tachref-studio\assets\images"
os.makedirs(img_dir, exist_ok=True)

arts = {
    "dept-web.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <radialGradient id="bg" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#181822" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#08080a" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="iri1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f5d4" stop-opacity="0.85"/>
      <stop offset="30%" stop-color="#7b2cbf" stop-opacity="0.85"/>
      <stop offset="70%" stop-color="#ff007f" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ff9e00" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="wire" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff5e00" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#00e5ff" stop-opacity="0.7"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg)"/>
  <g stroke="rgba(255,255,255,0.06)" stroke-width="1">
    <line x1="150" y1="0" x2="150" y2="600"/>
    <line x1="300" y1="0" x2="300" y2="600"/>
    <line x1="450" y1="0" x2="450" y2="600"/>
    <line x1="600" y1="0" x2="600" y2="600"/>
    <line x1="0" y1="150" x2="800" y2="150"/>
    <line x1="0" y1="300" x2="800" y2="300"/>
    <line x1="0" y1="450" x2="800" y2="450"/>
  </g>
  <g transform="translate(400, 290)">
    <ellipse cx="0" cy="0" rx="230" ry="85" fill="none" stroke="url(#wire)" stroke-width="1.5" stroke-dasharray="6 4" opacity="0.6"/>
    <ellipse cx="0" cy="0" rx="160" ry="160" fill="none" stroke="rgba(255,107,43,0.3)" stroke-width="1"/>
    <polygon points="0,-160 140,-45 110,120 -110,120 -140,-45" fill="url(#iri1)" opacity="0.8" filter="url(#glow)"/>
    <polygon points="0,-160 140,-45 0,25 -140,-45" fill="rgba(255,255,255,0.18)"/>
    <polygon points="0,25 140,-45 110,120" fill="rgba(0,0,0,0.4)"/>
    <polygon points="0,25 -140,-45 -110,120" fill="rgba(0,255,220,0.2)"/>
    <polygon points="0,25 110,120 0,160 -110,120" fill="rgba(255,90,0,0.35)"/>
    <line x1="0" y1="-160" x2="0" y2="160" stroke="#fff" stroke-width="1" opacity="0.7"/>
    <circle cx="0" cy="-160" r="5" fill="#ff5e00" filter="url(#glow)"/>
    <circle cx="140" cy="-45" r="5" fill="#00f5d4" filter="url(#glow)"/>
    <circle cx="-140" cy="-45" r="5" fill="#ff007f" filter="url(#glow)"/>
    <text x="0" y="220" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-family="monospace" font-size="11" letter-spacing="4">[ ARCHITECTURE / NEXT.JS . DISTRIBUTED WEBGPU ]</text>
  </g>
</svg>""",

    "dept-graphic.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <radialGradient id="bg2" cx="60%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#1c101c" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#08080a" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="oil" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff007f" stop-opacity="0.95"/>
      <stop offset="35%" stop-color="#f72585" stop-opacity="0.85"/>
      <stop offset="65%" stop-color="#7209b7" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#4cc9f0" stop-opacity="0.95"/>
    </linearGradient>
    <filter id="chroma">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg2)"/>
  <g transform="translate(400,290)">
    <path d="M -180,0 C -180,-140 180,-140 180,0 C 180,140 -180,140 -180,0 Z" fill="none" stroke="url(#oil)" stroke-width="48" opacity="0.85" filter="url(#chroma)"/>
    <path d="M -120,-60 C -60,-180 120,-120 160,-20 C 200,80 40,160 -80,110 C -160,80 -160,0 -120,-60 Z" fill="none" stroke="#fff" stroke-width="2" stroke-dasharray="10 6" opacity="0.5"/>
    <circle cx="0" cy="0" r="72" fill="#000" stroke="rgba(255,107,43,0.8)" stroke-width="2"/>
    <circle cx="0" cy="0" r="7" fill="#ff5e00"/>
    <text x="0" y="220" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-family="monospace" font-size="11" letter-spacing="4">[ CHROMATIC SPECTRUM / POSTER EDITORIAL . 02 ]</text>
  </g>
</svg>""",

    "dept-branding.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <radialGradient id="bg3" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#181512" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#08080a" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffba08" stop-opacity="0.95"/>
      <stop offset="40%" stop-color="#e85d04" stop-opacity="0.85"/>
      <stop offset="80%" stop-color="#9d0208" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ff0054" stop-opacity="0.85"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg3)"/>
  <g transform="translate(400,290)">
    <polygon points="-90,-160 90,-160 140,80 -40,160" fill="url(#gold)" opacity="0.9"/>
    <polygon points="-90,-160 -40,160 -140,80" fill="rgba(255,255,255,0.12)"/>
    <circle cx="110" cy="-110" r="35" fill="none" stroke="#ffba08" stroke-width="1.5" stroke-dasharray="4 4"/>
    <circle cx="-100" cy="120" r="55" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
    <line x1="-220" y1="0" x2="220" y2="0" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    <line x1="0" y1="-220" x2="0" y2="220" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    <text x="0" y="220" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-family="monospace" font-size="11" letter-spacing="4">[ MONOMARK IDENTITY / KINETIC BRAND SYSTEM ]</text>
  </g>
</svg>""",

    "dept-games.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <radialGradient id="bg4" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0e1a24" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#08080a" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="cyanpurp" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f0ff" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#7000ff" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#ff007b" stop-opacity="0.9"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg4)"/>
  <g transform="translate(400,290)">
    <polygon points="0,-140 120,-70 120,70 0,140 -120,70 -120,-70" fill="url(#cyanpurp)" opacity="0.75"/>
    <polygon points="0,-140 120,-70 0,0 -120,-70" fill="rgba(255,255,255,0.2)"/>
    <polygon points="0,0 120,-70 120,70 0,140" fill="rgba(0,0,0,0.4)"/>
    <circle cx="0" cy="0" r="180" fill="none" stroke="#00f0ff" stroke-width="1" stroke-dasharray="12 8" opacity="0.5"/>
    <line x1="-180" y1="-90" x2="180" y2="90" stroke="#ff007b" stroke-width="1" opacity="0.4"/>
    <text x="0" y="220" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-family="monospace" font-size="11" letter-spacing="4">[ VOID RUNNER ENGINE / THREE.JS . WEBGPU ]</text>
  </g>
</svg>""",

    "dept-uiux.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <radialGradient id="bg5" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#111a1f" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#08080a" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="glass" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(255,255,255,0.4)"/>
      <stop offset="50%" stop-color="rgba(0,245,212,0.3)"/>
      <stop offset="100%" stop-color="rgba(255,107,43,0.3)"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg5)"/>
  <g transform="translate(400,290)">
    <rect x="-160" y="-110" width="260" height="180" rx="16" fill="url(#glass)" stroke="rgba(255,255,255,0.3)" stroke-width="1.5"/>
    <rect x="-100" y="-60" width="260" height="180" rx="16" fill="rgba(15,20,30,0.6)" stroke="rgba(255,107,43,0.5)" stroke-width="1.5"/>
    <circle cx="-70" cy="-35" r="5" fill="#ff5e00"/>
    <circle cx="-50" cy="-35" r="5" fill="#00f5d4"/>
    <line x1="-70" y1="0" x2="60" y2="0" stroke="rgba(255,255,255,0.5)" stroke-width="3" stroke-linecap="round"/>
    <line x1="-70" y1="20" x2="20" y2="20" stroke="rgba(255,255,255,0.2)" stroke-width="2" stroke-linecap="round"/>
    <rect x="-70" y="45" width="80" height="28" rx="6" fill="rgba(255,107,43,0.2)" stroke="#ff5e00" stroke-width="1"/>
    <text x="0" y="220" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-family="monospace" font-size="11" letter-spacing="4">[ SPATIAL ERGONOMICS / DESIGN SYSTEM V3 ]</text>
  </g>
</svg>""",

    "dept-robotics.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <radialGradient id="bg6" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#1f140e" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#08080a" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="mech" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff6b2b" stop-opacity="0.9"/>
      <stop offset="60%" stop-color="#ff9e00" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#3a86ff" stop-opacity="0.8"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg6)"/>
  <g transform="translate(400,290)">
    <circle cx="0" cy="0" r="130" fill="none" stroke="url(#mech)" stroke-width="2" stroke-dasharray="8 8"/>
    <circle cx="0" cy="0" r="70" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <circle cx="0" cy="0" r="26" fill="#ff6b2b" opacity="0.8"/>
    <line x1="0" y1="0" x2="110" y2="-90" stroke="#fff" stroke-width="5" stroke-linecap="round"/>
    <circle cx="110" cy="-90" r="12" fill="#08080a" stroke="#ff6b2b" stroke-width="3"/>
    <line x1="110" y1="-90" x2="180" y2="-30" stroke="#ff9e00" stroke-width="4" stroke-linecap="round"/>
    <circle cx="180" cy="-30" r="8" fill="#00f5d4"/>
    <text x="0" y="220" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-family="monospace" font-size="11" letter-spacing="4">[ KINEMATIC AUTOMATION / ROS2 . EMBEDDED ]</text>
  </g>
</svg>""",

    "dept-creative-tech.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%">
  <defs>
    <radialGradient id="bg7" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#181024" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#08080a" stop-opacity="1"/>
    </radialGradient>
    <linearGradient id="holo" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff00c8" stop-opacity="0.85"/>
      <stop offset="30%" stop-color="#3a86ff" stop-opacity="0.85"/>
      <stop offset="70%" stop-color="#00f5d4" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#ffbe0b" stop-opacity="0.85"/>
    </linearGradient>
    <filter id="glow7">
      <feGaussianBlur stdDeviation="10" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="url(#bg7)"/>
  <g transform="translate(400,290)">
    <ellipse cx="0" cy="0" rx="200" ry="70" fill="none" stroke="url(#holo)" stroke-width="3" transform="rotate(-25)"/>
    <ellipse cx="0" cy="0" rx="200" ry="70" fill="none" stroke="url(#holo)" stroke-width="3" transform="rotate(35)"/>
    <ellipse cx="0" cy="0" rx="200" ry="70" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" transform="rotate(95)"/>
    <circle cx="0" cy="0" r="32" fill="#fff" opacity="0.9" filter="url(#glow7)"/>
    <text x="0" y="220" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-family="monospace" font-size="11" letter-spacing="4">[ GENERATIVE SYSTEMS / NEURAL SHADERS . EXPERIMENTAL ]</text>
  </g>
</svg>""",

    "project-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117"/>
      <stop offset="50%" stop-color="#161b22"/>
      <stop offset="100%" stop-color="#ff5e00" stop-opacity="0.3"/>
    </linearGradient>
    <linearGradient id="iriP1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f5d4"/>
      <stop offset="50%" stop-color="#7b2cbf"/>
      <stop offset="100%" stop-color="#ff007f"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#p1)"/>
  <g transform="translate(400,250)">
    <polygon points="-120,-90 120,-90 160,80 -80,80" fill="none" stroke="url(#iriP1)" stroke-width="2"/>
    <circle cx="0" cy="0" r="80" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <circle cx="30" cy="-20" r="6" fill="#ff5e00"/>
    <text x="0" y="160" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-family="monospace" font-size="12" letter-spacing="3">KAIROS NEURAL OS // WEB PLATFORM</text>
  </g>
</svg>""",

    "project-2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <linearGradient id="p2" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#120c18"/>
      <stop offset="100%" stop-color="#7209b7" stop-opacity="0.4"/>
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#p2)"/>
  <g transform="translate(400,250)">
    <rect x="-140" y="-80" width="280" height="160" fill="none" stroke="#f72585" stroke-width="2" rx="8"/>
    <path d="M -140,-80 L 140,80 M -140,80 L 140,-80" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    <circle cx="0" cy="0" r="50" fill="#7209b7" opacity="0.5"/>
    <text x="0" y="160" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-family="monospace" font-size="12" letter-spacing="3">SYNTHESIS // BRAND IDENTITY SYSTEM</text>
  </g>
</svg>""",

    "project-3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <defs>
    <radialGradient id="p3" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#002b36"/>
      <stop offset="100%" stop-color="#08080a"/>
    </radialGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#p3)"/>
  <g transform="translate(400,250)">
    <circle cx="0" cy="0" r="100" fill="none" stroke="#00f0ff" stroke-width="2" stroke-dasharray="6 4"/>
    <circle cx="0" cy="0" r="60" fill="none" stroke="#ff5e00" stroke-width="1.5"/>
    <polygon points="0,-40 35,20 -35,20" fill="#00f0ff" opacity="0.7"/>
    <text x="0" y="160" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-family="monospace" font-size="12" letter-spacing="3">AETHER VOID ENGINE // 3D BROWSER GAME</text>
  </g>
</svg>""",

    "project-4.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0e1416"/>
  <g transform="translate(400,250)">
    <circle cx="0" cy="0" r="90" fill="none" stroke="#ff9e00" stroke-width="2"/>
    <line x1="-120" y1="0" x2="120" y2="0" stroke="#ff5e00" stroke-width="2" stroke-dasharray="5 5"/>
    <line x1="0" y1="-120" x2="0" y2="120" stroke="#ff5e00" stroke-width="2" stroke-dasharray="5 5"/>
    <rect x="-40" y="-40" width="80" height="80" fill="rgba(255,107,43,0.3)" stroke="#fff" stroke-width="1"/>
    <text x="0" y="160" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-family="monospace" font-size="12" letter-spacing="3">CHRONOS ROVER // ROBOTICS &amp; TELEMETRY</text>
  </g>
</svg>""",

    "project-5.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#141118"/>
  <g transform="translate(400,250)">
    <ellipse cx="0" cy="0" rx="140" ry="70" fill="none" stroke="#ff007f" stroke-width="2" transform="rotate(-15)"/>
    <ellipse cx="0" cy="0" rx="140" ry="70" fill="none" stroke="#00f5d4" stroke-width="2" transform="rotate(30)"/>
    <text x="0" y="160" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-family="monospace" font-size="12" letter-spacing="3">HYPERION SPATIAL // UI/UX DESIGN SYSTEM</text>
  </g>
</svg>""",

    "project-6.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0d131a"/>
  <g transform="translate(400,250)">
    <polygon points="0,-110 95,-55 95,55 0,110 -95,55 -95,-55" fill="none" stroke="#3a86ff" stroke-width="2"/>
    <circle cx="0" cy="0" r="50" fill="none" stroke="#ffbe0b" stroke-width="1.5" stroke-dasharray="6 4"/>
    <text x="0" y="160" text-anchor="middle" fill="rgba(255,255,255,0.6)" font-family="monospace" font-size="12" letter-spacing="3">LUMEN AUDIOVISUAL // CREATIVE CODE</text>
  </g>
</svg>""",

    "lab-1.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#080b0f"/>
  <g transform="translate(400,250)">
    <circle cx="0" cy="0" r="120" fill="none" stroke="#ff5e00" stroke-width="1" stroke-dasharray="4 6"/>
    <line x1="-150" y1="0" x2="150" y2="0" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <line x1="0" y1="-150" x2="0" y2="150" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <polygon points="0,-70 60,35 -60,35" fill="none" stroke="#00f5d4" stroke-width="2"/>
    <text x="0" y="160" text-anchor="middle" fill="#ff5e00" font-family="monospace" font-size="12" letter-spacing="3">EXP_01: INVERSE KINEMATICS ACTUATOR</text>
  </g>
</svg>""",

    "lab-2.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0c0914"/>
  <g transform="translate(400,250)">
    <ellipse cx="0" cy="0" rx="140" ry="70" fill="none" stroke="#ff00c8" stroke-width="2" transform="rotate(45)"/>
    <ellipse cx="0" cy="0" rx="140" ry="70" fill="none" stroke="#7000ff" stroke-width="2" transform="rotate(-45)"/>
    <circle cx="0" cy="0" r="10" fill="#fff"/>
    <text x="0" y="160" text-anchor="middle" fill="#ff00c8" font-family="monospace" font-size="12" letter-spacing="3">EXP_02: QUANTUM RAYMARCHING SHADERS</text>
  </g>
</svg>""",

    "lab-3.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0a1210"/>
  <g transform="translate(400,250)">
    <polygon points="0,-90 78,-45 78,45 0,90 -78,45 -78,-45" fill="none" stroke="#00f5d4" stroke-width="2"/>
    <circle cx="0" cy="0" r="45" fill="rgba(0,245,212,0.15)"/>
    <text x="0" y="160" text-anchor="middle" fill="#00f5d4" font-family="monospace" font-size="12" letter-spacing="3">EXP_03: PROCEDURAL TERRAIN VOXEL MESH</text>
  </g>
</svg>""",

    "logo.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 48" width="200" height="48">
  <g transform="translate(4, 8)">
    <!-- Tech diamond brand icon -->
    <polygon points="16,0 32,16 16,32 0,16" fill="none" stroke="#ffffff" stroke-width="2.5"/>
    <polygon points="16,6 26,16 16,26 6,16" fill="#ff5e00"/>
    <circle cx="16" cy="16" r="2.5" fill="#ffffff"/>
  </g>
  <text x="46" y="29" fill="#ffffff" font-family="'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="18" letter-spacing="2">TACHREF</text>
  <text x="146" y="29" fill="#ff5e00" font-family="'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="18" letter-spacing="2">®</text>
</svg>"""
}

for filename, content in arts.items():
    path = os.path.join(img_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
print(f"Generated {len(arts)} assets successfully in {img_dir}")
