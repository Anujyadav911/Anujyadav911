"""
=============================================================================
🌸 CLEAN BRANDED TERMINAL & ANYA ASSETS GENERATOR 🌸
=============================================================================
Author:  Anuj Yadav
Purpose: Generates clean, branded white/light cards featuring Anya Forger
         (Spy × Family), cute cat assets, and modern developer aesthetics.
=============================================================================
"""

import base64
import sys
from pathlib import Path

# Ensure UTF-8 console output for Windows cmd/powershell
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ASSETS_DIR = Path("assets")
ASSETS_DIR.mkdir(exist_ok=True)

# Clean Branded Color Palette (Modern, Crisp White Card with Slate / Emerald / Rose accents)
COLOR_BG = "#FFFFFF"
COLOR_HEADER_BG = "#F8FAFC"
COLOR_BORDER = "#E2E8F0"
COLOR_TEXT_PRIMARY = "#0F172A"       # Deep slate
COLOR_TEXT_SECONDARY = "#334155"     # Slate 700
COLOR_TEXT_MUTED = "#64748B"         # Slate 500
COLOR_EMERALD = "#059669"            # Clean GitHub / Tech Emerald
COLOR_EMERALD_BG = "#ECFDF5"
COLOR_EMERALD_BORDER = "#A7F3D0"
COLOR_ROSE = "#E11D48"               # Anya Rose
COLOR_ROSE_BG = "#FFF1F2"
COLOR_ROSE_BORDER = "#FECDD3"
COLOR_INDIGO = "#4F46E5"
COLOR_INDIGO_BG = "#EEF2FF"
COLOR_INDIGO_BORDER = "#C7D2FE"


def get_b64(filename: str) -> str:
    """Load image as base64 string if present."""
    p = ASSETS_DIR / filename
    if p.exists():
        with open(p, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""


# =============================================================================
# 1. HERO TERMINAL HEADER (WHITE BRANDED CARD + RESTORED OLD CODE + WAKU WAKU)
# =============================================================================

def generate_header_svg() -> str:
    """
    Constructs the clean, branded Hero Header:
    - Clean white card (#FFFFFF) with refined subtle shadow & border
    - Titlebar: anya@anuj-station:~ (zsh) — [ 🌸 WAKU WAKU! ✧ ANYA-OS v3.5 ]
    - Prompt: guest@anuj-station:~$ ./welcome_guest.sh --enthusiasm=MAX
    - Name: ANUJ YADAV (bold, clean slate #0F172A, NO flower)
    - Subtitle: AI Engineer · Full-Stack Developer · Product Architect
    - Restored Old Code Specs:
      AI_CORE: LLMs · RAG Pipelines · AI Agents · LangGraph · Fine-Tuning
      STACK:   Python • FastAPI • TypeScript • React • PostgreSQL • Redis
      MISSION: Building production systems & scaling platforms (~7K users)
      STATUS:  Ready to innovate 🚀 Powered by chai ☕ & peanuts 🥜  TERM: READY_ █
    - Welcoming Anya on the right with 'WAKU WAKU! ✧' speech bubble
    """
    anaya_b64 = get_b64("anaya_clean.png")
    if not anaya_b64:
        anaya_b64 = get_b64("anaya_header.png")

    image_element = ""
    if anaya_b64:
        image_element = f'''
        <g class="anya-float">
          <!-- Subtle Glow Aura behind Anya -->
          <circle cx="95" cy="100" r="75" fill="{COLOR_ROSE}" opacity="0.08" filter="url(#roseBlur)" />
          
          <!-- Anya Image -->
          <image href="data:image/png;base64,{anaya_b64}" x="10" y="8" width="170" height="186" preserveAspectRatio="xMidYMid meet" />
          
          <!-- Waku Waku Speech Bubble -->
          <g class="welcome-bubble" transform="translate(95, 6)">
            <rect width="105" height="26" rx="6" fill="{COLOR_ROSE_BG}" stroke="{COLOR_ROSE_BORDER}" stroke-width="1.2" filter="url(#cardShadow)" />
            <polygon points="12,26 18,32 22,26" fill="{COLOR_ROSE_BG}" />
            <text x="52" y="17" font-size="10.5" font-family="'Fira Code', monospace" font-weight="700" fill="{COLOR_ROSE}" text-anchor="middle">WAKU WAKU! &#10023;</text>
          </g>
        </g>
        '''
    else:
        image_element = f'''
        <g class="anya-float">
          <rect width="170" height="150" rx="10" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" stroke-width="1.2" />
          <text x="85" y="75" font-size="20" fill="{COLOR_ROSE}" text-anchor="middle">( &#728;&#8226;&#768;&#7447;&#8226;&#769;&#728; )</text>
          <text x="85" y="105" font-size="12" fill="{COLOR_ROSE}" font-weight="bold" text-anchor="middle">WAKU WAKU! &#10023;</text>
        </g>
        '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 250" width="100%" height="250" style="background: transparent; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <!-- Soft Card Shadow -->
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#000000" flood-opacity="0.06"/>
    </filter>

    <filter id="roseBlur" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="12" />
    </filter>
  </defs>

  <style>
    .term-title {{ font-size: 11.5px; fill: #64748B; font-weight: 600; letter-spacing: 0.3px; font-family: 'Fira Code', monospace; }}
    .status-text {{ font-size: 11px; fill: {COLOR_EMERALD}; font-weight: 700; font-family: 'Fira Code', monospace; }}
    .prompt {{ font-size: 12.5px; fill: #475569; font-weight: 600; font-family: 'Fira Code', monospace; }}
    .name-title {{ font-size: 30px; font-weight: 800; fill: {COLOR_TEXT_PRIMARY}; letter-spacing: 0.5px; }}
    .role-text {{ font-size: 14px; fill: #475569; font-weight: 600; }}
    .meta-label {{ font-size: 11px; fill: #64748B; font-weight: 700; font-family: 'Fira Code', monospace; }}
    .meta-val {{ font-size: 11px; fill: #0F172A; font-weight: 500; font-family: 'Fira Code', monospace; }}
    .meta-val-green {{ font-size: 11px; fill: {COLOR_EMERALD}; font-weight: 600; font-family: 'Fira Code', monospace; }}
    .meta-val-rose {{ font-size: 11px; fill: {COLOR_ROSE}; font-weight: 600; font-family: 'Fira Code', monospace; }}
    
    @keyframes anyaFloat {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-6px); }}
    }}
    @keyframes pulseDot {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.4; transform: scale(0.85); }}
    }}
    @keyframes cursorBlink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}

    .anya-float {{ animation: anyaFloat 4s ease-in-out infinite; }}
    .pulse {{ animation: pulseDot 2s ease-in-out infinite; transform-origin: 755px 19px; }}
    .cursor {{ animation: cursorBlink 0.9s infinite; }}
  </style>

  <!-- Clean Branded Container Box -->
  <rect x="2" y="2" width="876" height="246" rx="12" fill="{COLOR_BG}" stroke="{COLOR_BORDER}" stroke-width="1.2" filter="url(#cardShadow)" />

  <!-- Clean Titlebar -->
  <path d="M 2 12 Q 2 2 12 2 L 868 2 Q 878 2 878 12 L 878 38 L 2 38 Z" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" stroke-width="0.8" />
  
  <!-- Window Control Buttons -->
  <circle cx="22" cy="20" r="5.5" fill="#EF4444" />
  <circle cx="40" cy="20" r="5.5" fill="#F59E0B" />
  <circle cx="58" cy="20" r="5.5" fill="#10B981" />

  <!-- Titlebar Title -->
  <text x="80" y="24" class="term-title">anya@anuj-station:~ (zsh) &#8212; [ &#127800; WAKU WAKU! &#10023; ANYA-OS v3.5 ]</text>

  <!-- Status Beacon in Titlebar -->
  <circle cx="755" cy="20" r="4" fill="{COLOR_EMERALD}" class="pulse" />
  <text x="766" y="24" class="status-text">ONLINE</text>
  <text x="824" y="24" font-size="11" fill="#64748B" font-family="'Fira Code', monospace">[HYD, IN]</text>

  <!-- ================================================================= -->
  <!-- LEFT: DEVELOPER CONSOLE & RESTORED OLD CODE METRICS               -->
  <!-- ================================================================= -->
  <g transform="translate(28, 52)">
    <!-- Terminal Command Line -->
    <text x="0" y="16" class="prompt">guest@anuj-station:~$ <tspan fill="{COLOR_TEXT_PRIMARY}">./welcome_guest.sh --enthusiasm=MAX</tspan></text>

    <!-- Clean Name (NO Flower) -->
    <text x="0" y="52" class="name-title">ANUJ YADAV</text>

    <!-- Role / Professional Identity -->
    <text x="0" y="76" class="role-text">AI Engineer <tspan fill="{COLOR_EMERALD}">&#183;</tspan> Full-Stack Developer <tspan fill="{COLOR_EMERALD}">&#183;</tspan> Product Architect</text>

    <!-- Restored Old Code Specs Matrix -->
    <g transform="translate(0, 95)">
      <!-- Line 1: AI_CORE -->
      <text x="0" y="15" class="meta-label">AI_CORE:</text>
      <text x="75" y="15" class="meta-val-green">LLMs &#183; RAG Pipelines &#183; AI Agents &#183; LangGraph &#183; Fine-Tuning</text>

      <!-- Line 2: STACK -->
      <text x="0" y="35" class="meta-label">STACK:</text>
      <text x="75" y="35" class="meta-val">Python <tspan fill="#94A3B8">&#8226;</tspan> FastAPI <tspan fill="#94A3B8">&#8226;</tspan> TypeScript <tspan fill="#94A3B8">&#8226;</tspan> React <tspan fill="#94A3B8">&#8226;</tspan> PostgreSQL <tspan fill="#94A3B8">&#8226;</tspan> Redis</text>

      <!-- Line 3: MISSION -->
      <text x="0" y="55" class="meta-label">MISSION:</text>
      <text x="75" y="55" class="meta-val">Building production systems &amp; scaling platforms (<tspan fill="{COLOR_EMERALD}">~7K users</tspan>)</text>

      <!-- Line 4: STATUS (Chai + Peanuts + Ready) -->
      <text x="0" y="75" class="meta-label">STATUS:</text>
      <text x="75" y="75" class="meta-val-rose">Ready to innovate 🚀 Powered by chai ☕ &amp; peanuts 🥜</text>

      <text x="445" y="75" class="meta-label">TERM:</text>
      <text x="490" y="75" class="meta-val-green">READY_</text>
      <rect x="542" y="65" width="6" height="12" fill="{COLOR_EMERALD}" class="cursor" />
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- RIGHT: WELCOMING ANYA WITH 'WAKU WAKU!' SPEECH BUBBLE             -->
  <!-- ================================================================= -->
  <g transform="translate(640, 42)">
    {image_element}
  </g>
</svg>'''


# =============================================================================
# 2. FEATURED PROJECT CARDS (SYNCKRA & MILKYWAVE)
# =============================================================================

def generate_synckra_card_svg() -> str:
    """Clean branded card for Synckra with white background and verified metrics."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 130" width="100%" height="130" style="background: transparent; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="cardShadowProj" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
  </defs>

  <rect x="2" y="2" width="396" height="126" rx="8" fill="{COLOR_BG}" stroke="{COLOR_BORDER}" stroke-width="1.2" filter="url(#cardShadowProj)" />
  
  <!-- Clean Titlebar -->
  <path d="M 2 8 Q 2 2 8 2 L 392 2 Q 398 2 398 8 L 398 26 L 2 26 Z" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" stroke-width="0.8" />
  <circle cx="14" cy="14" r="3.5" fill="#EF4444" />
  <circle cx="24" cy="14" r="3.5" fill="#F59E0B" />
  <circle cx="34" cy="14" r="3.5" fill="#10B981" />
  <text x="46" y="17" font-size="10" fill="#64748B" font-family="'Fira Code', monospace">synckra.in &#8212; [LIVE PLATFORM]</text>
  
  <!-- Users Badge -->
  <rect x="295" y="6" width="96" height="16" rx="4" fill="{COLOR_EMERALD_BG}" stroke="{COLOR_EMERALD_BORDER}" stroke-width="1" />
  <text x="343" y="17.5" font-size="9" fill="{COLOR_EMERALD}" font-weight="700" font-family="'Fira Code', monospace" text-anchor="middle">&#10029; ~7K USERS</text>

  <!-- Left: Mini Branded Emblem -->
  <g transform="translate(14, 38)">
    <rect width="64" height="66" rx="6" fill="{COLOR_EMERALD_BG}" stroke="{COLOR_EMERALD_BORDER}" stroke-width="1" />
    <text x="32" y="32" font-size="12" fill="{COLOR_EMERALD}" font-weight="700" font-family="'Fira Code', monospace" text-anchor="middle">SYNC</text>
    <text x="32" y="48" font-size="9" fill="{COLOR_TEXT_MUTED}" font-family="'Fira Code', monospace" text-anchor="middle">.in</text>
  </g>

  <!-- Right: Project Details -->
  <text x="90" y="50" font-size="15" fill="{COLOR_TEXT_PRIMARY}" font-weight="700">Synckra</text>
  <text x="90" y="66" font-size="11" fill="{COLOR_INDIGO}" font-weight="600">Internship &amp; Early-Career Platform</text>
  <text x="90" y="82" font-size="9.5" fill="{COLOR_TEXT_MUTED}" font-family="'Fira Code', monospace">Astro &#183; Python &#183; Supabase &#183; PostgreSQL &#183; Redis</text>
  
  <!-- Metric chips -->
  <rect x="90" y="93" width="135" height="18" rx="3" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" />
  <text x="96" y="105.5" font-size="9" fill="{COLOR_EMERALD}" font-weight="600" font-family="'Fira Code', monospace">1K+ records / 15m</text>
  
  <rect x="232" y="93" width="145" height="18" rx="3" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" />
  <text x="238" y="105.5" font-size="9" fill="{COLOR_TEXT_SECONDARY}" font-weight="600" font-family="'Fira Code', monospace">Multi-LLM fallbacks</text>
</svg>'''


def generate_milkywave_card_svg() -> str:
    """Clean branded card for MilkyWave with white background and verified metrics."""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 130" width="100%" height="130" style="background: transparent; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="cardShadowMw" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000000" flood-opacity="0.05"/>
    </filter>
  </defs>

  <rect x="2" y="2" width="396" height="126" rx="8" fill="{COLOR_BG}" stroke="{COLOR_BORDER}" stroke-width="1.2" filter="url(#cardShadowMw)" />
  
  <!-- Clean Titlebar -->
  <path d="M 2 8 Q 2 2 8 2 L 392 2 Q 398 2 398 8 L 398 26 L 2 26 Z" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" stroke-width="0.8" />
  <circle cx="14" cy="14" r="3.5" fill="#EF4444" />
  <circle cx="24" cy="14" r="3.5" fill="#F59E0B" />
  <circle cx="34" cy="14" r="3.5" fill="#10B981" />
  <text x="46" y="17" font-size="10" fill="#64748B" font-family="'Fira Code', monospace">milkywave.app &#8212; [MOBILE APP]</text>
  
  <!-- Downloads Badge -->
  <rect x="275" y="6" width="116" height="16" rx="4" fill="{COLOR_INDIGO_BG}" stroke="{COLOR_INDIGO_BORDER}" stroke-width="1" />
  <text x="333" y="17.5" font-size="9" fill="{COLOR_INDIGO}" font-weight="700" font-family="'Fira Code', monospace" text-anchor="middle">100+ DOWNLOADS</text>

  <!-- Left: Mini Branded Emblem -->
  <g transform="translate(14, 38)">
    <rect width="64" height="66" rx="6" fill="{COLOR_INDIGO_BG}" stroke="{COLOR_INDIGO_BORDER}" stroke-width="1" />
    <text x="32" y="32" font-size="12" fill="{COLOR_INDIGO}" font-weight="700" font-family="'Fira Code', monospace" text-anchor="middle">MILK</text>
    <text x="32" y="48" font-size="9" fill="{COLOR_TEXT_MUTED}" font-family="'Fira Code', monospace" text-anchor="middle">wave</text>
  </g>

  <!-- Right: Project Details -->
  <text x="90" y="50" font-size="15" fill="{COLOR_TEXT_PRIMARY}" font-weight="700">MilkyWave</text>
  <text x="90" y="66" font-size="11" fill="{COLOR_INDIGO}" font-weight="600">Local Commerce &amp; Delivery Platform</text>
  <text x="90" y="82" font-size="9.5" fill="{COLOR_TEXT_MUTED}" font-family="'Fira Code', monospace">React Native &#183; Expo &#183; TypeScript &#183; Supabase &#183; Razorpay</text>
  
  <!-- Metric chips -->
  <rect x="90" y="93" width="138" height="18" rx="3" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" />
  <text x="96" y="105.5" font-size="9" fill="{COLOR_INDIGO}" font-weight="600" font-family="'Fira Code', monospace">Razorpay API Checkout</text>
  
  <rect x="235" y="93" width="145" height="18" rx="3" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" />
  <text x="241" y="105.5" font-size="9" fill="{COLOR_EMERALD}" font-weight="600" font-family="'Fira Code', monospace">Real-time Order State</text>
</svg>'''


# =============================================================================
# 3. END ANYA CARD (WHITE BRANDED CARD + RESTORED FUNNY TELEPATHIC TEXT)
# =============================================================================

def generate_endanaya_card_svg() -> str:
    """
    Constructs the Clean Branded Footer Card featuring Anya holding Chimera
    with the RESTORED FUNNY TELEPATHIC REPORT TEXT:
    - Clean white card (#FFFFFF) with subtle shadow
    - Titlebar: anya@station:~$ ./mission_complete.py --status=goodbye  [STANDBY]
    - End Anya portrait on the left
    - Funny Telepathic dialogue box on the right:
      "Anya saw you scrolled all the way to the end! ⭐"
      "That means you're super interested in Anuj's work!"
      ✔ Systems online           ✔ High-throughput backends
      ✔ AI agents ready          ✔ Waku waku level: 100%
      🥜 Don't forget to star this repo! Anya will remember! 🥜
    """
    endanaya_b64 = get_b64("endanaya.png")
    if not endanaya_b64:
        endanaya_b64 = get_b64("endanaya_card.png")

    image_element = ""
    if endanaya_b64:
        image_element = f'''
        <g class="end-float">
          <!-- Subtle Glow behind Anya -->
          <circle cx="114" cy="110" r="85" fill="{COLOR_ROSE}" opacity="0.08" />
          
          <!-- Anya Photo inside clean rounded frame -->
          <rect x="14" y="14" width="232" height="212" rx="10" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" stroke-width="1" />
          <image href="data:image/png;base64,{endanaya_b64}" x="16" y="16" width="228" height="208" preserveAspectRatio="xMidYMid slice" clip-path="url(#anyaEndClip)" />
        </g>
        '''
    else:
        image_element = f'''
        <g class="end-float">
          <rect x="14" y="14" width="232" height="212" rx="10" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" stroke-width="1" />
          <text x="130" y="110" font-size="28" fill="{COLOR_ROSE}" text-anchor="middle">( &#3665;&#8226;&#768;&#12609;&#8226;&#769;&#3665; )</text>
          <text x="130" y="140" font-size="13" fill="{COLOR_TEXT_MUTED}" text-anchor="middle">Mission Complete</text>
        </g>
        '''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 250" width="100%" height="250" style="background: transparent; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="endCardShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#000000" flood-opacity="0.06"/>
    </filter>

    <clipPath id="anyaEndClip">
      <rect x="16" y="16" width="228" height="208" rx="8" />
    </clipPath>
  </defs>

  <style>
    @keyframes endFloat {{
      0%, 100% {{ transform: translateY(0px); }}
      50% {{ transform: translateY(-5px); }}
    }}
    @keyframes beaconBlink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0.3; }}
    }}
    .end-float {{ animation: endFloat 4s ease-in-out infinite; }}
    .beacon {{ animation: beaconBlink 1.5s infinite; }}
  </style>

  <!-- Clean Branded Container Box -->
  <rect x="2" y="2" width="756" height="246" rx="12" fill="{COLOR_BG}" stroke="{COLOR_BORDER}" stroke-width="1.2" filter="url(#endCardShadow)" />

  <!-- Clean Titlebar -->
  <path d="M 2 12 Q 2 2 12 2 L 748 2 Q 758 2 758 12 L 758 34 L 2 34 Z" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" stroke-width="0.8" />
  <circle cx="20" cy="18" r="5" fill="#EF4444" />
  <circle cx="36" cy="18" r="5" fill="#F59E0B" />
  <circle cx="52" cy="18" r="5" fill="#10B981" />
  <text x="70" y="22" font-size="11.5" fill="#64748B" font-family="'Fira Code', monospace">anya@station:~$ ./mission_complete.py --status=goodbye</text>
  
  <circle cx="675" cy="18" r="4" fill="{COLOR_ROSE}" class="beacon" />
  <text x="686" y="22" font-size="10.5" fill="{COLOR_ROSE}" font-weight="700" font-family="'Fira Code', monospace">STANDBY</text>

  <!-- Left: End Anya Photo Card -->
  <g transform="translate(10, 24)">
    {image_element}
  </g>

  <!-- Right: Restored Funny Telepathic Dialogue Box -->
  <g transform="translate(285, 46)">
    <rect width="455" height="180" rx="10" fill="{COLOR_HEADER_BG}" stroke="{COLOR_BORDER}" stroke-width="1" />
    
    <text x="20" y="28" font-size="13" fill="{COLOR_ROSE}" font-weight="700">🌸 Anya Forger [Telepathic Report]:</text>
    
    <text x="20" y="52" font-size="12" fill="{COLOR_TEXT_PRIMARY}" font-weight="600">"Anya saw you scrolled all the way to the end! ⭐"</text>
    <text x="20" y="72" font-size="11.5" fill="{COLOR_TEXT_MUTED}">"That means you're super interested in Anuj's work!"</text>
    
    <line x1="20" y1="86" x2="435" y2="86" stroke="{COLOR_BORDER}" stroke-width="1" />

    <!-- Terminal Highlights -->
    <text x="20" y="108" font-size="11.5" fill="{COLOR_EMERALD}" font-weight="600" font-family="'Fira Code', monospace">&#10004; Systems online</text>
    <text x="200" y="108" font-size="11.5" fill="{COLOR_INDIGO}" font-weight="600" font-family="'Fira Code', monospace">&#10004; High-throughput backends</text>
    
    <text x="20" y="128" font-size="11.5" fill="#0284C7" font-weight="600" font-family="'Fira Code', monospace">&#10004; AI agents ready</text>
    <text x="200" y="128" font-size="11.5" fill="{COLOR_ROSE}" font-weight="600" font-family="'Fira Code', monospace">&#10004; Waku waku level: 100%</text>

    <!-- Bottom Action Pill -->
    <rect x="20" y="142" width="415" height="26" rx="5" fill="{COLOR_ROSE_BG}" stroke="{COLOR_ROSE_BORDER}" stroke-width="0.8" />
    <text x="227" y="159" font-size="11" fill="{COLOR_ROSE}" font-weight="700" text-anchor="middle">🥜 Don't forget to star this repo! Anya will remember! 🥜</text>
  </g>
</svg>'''


def main():
    # 1. Hero Header Banner
    header_content = generate_header_svg()
    (ASSETS_DIR / "cat-header.svg").write_text(header_content, encoding="utf-8")
    (ASSETS_DIR / "anya-header.svg").write_text(header_content, encoding="utf-8")

    # 2. Featured Project Cards
    (ASSETS_DIR / "cat-synckra.svg").write_text(generate_synckra_card_svg(), encoding="utf-8")
    (ASSETS_DIR / "cat-milkywave.svg").write_text(generate_milkywave_card_svg(), encoding="utf-8")

    # 3. End Anya Card (with funny telepathic text)
    (ASSETS_DIR / "endanaya-card.svg").write_text(generate_endanaya_card_svg(), encoding="utf-8")

    print("Successfully generated assets with restored old code and funny telepathic text!")


if __name__ == "__main__":
    main()
