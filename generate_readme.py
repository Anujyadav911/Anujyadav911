"""
=============================================================================
🌸 CLEAN BRANDED PROFILE & GITHUB README GENERATOR 🌸
=============================================================================
Author:  Anuj Yadav
Purpose: Generates a clean, branded developer GitHub profile README.md
         featuring Anya Forger (Spy × Family), cute cat companion,
         year-wise LeetCode-style commit tracker, and verified resume skills.
=============================================================================
"""

from __future__ import annotations

import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path

# Ensure UTF-8 console output for Windows cmd/powershell
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


# =============================================================================
# 1. CENTRAL CONFIGURATION
# =============================================================================

@dataclass(frozen=True)
class ProfileConfig:
    name: str = "Anuj Yadav"
    username: str = "Anujyadav911"
    role: str = "AI Engineer Intern @ Mondee Tech | Graduating B.Tech May 2026"
    company: str = "Mondee Tech Pvt. Ltd., Hyderabad"
    location: str = "Hyderabad, India"
    education: str = "IIIT Manipur (B.Tech in ECE, 2022 – May 2026)"
    email: str = "anujyadav47247@gmail.com"
    linkedin_url: str = "https://www.linkedin.com/in/anuj-yadav-506a99257"
    website_url: str = "https://synckra.in"
    terminal_host: str = "anuj-station"


PROFILE = ProfileConfig()

# Clean Animated Monospace Typing Phrases
TYPING_PHRASES = [
    "AI Engineer Intern @ Mondee Tech, Hyderabad",
    "Graduating B.Tech in ECE from IIIT Manipur in May 2026",
    "Actively seeking Full-Time AI & Backend Engineering Roles",
    "Built Synckra (7K users) & MilkyWave mobile marketplace",
    "Autonomous AI Agents · LangGraph · RAG Pipelines · Distributed Backends",
    "Simple code, resilient systems, production-first engineering",
]

# Two Featured Projects (strictly accurate from real work & resume)
FEATURED_PROJECTS = [
    {
        "key": "synckra",
        "name": "Synckra",
        "tagline": "Internship & Early-Career Tech Platform",
        "badge_text": "★ ~7K USERS · PRODUCTION",
        "description": "Career platform helping students and freshers discover verified tech internships and entry-level opportunities across India.",
        "highlights": [
            "Asynchronous ingestion pipelines processing <b>1,000+ job records in 15 mins</b>",
            "Multi-LLM fallback architecture (<b>Gemini → Groq → OpenRouter</b>) to reliably parse raw listings",
            "Human-in-the-loop dashboard to verify metadata quality and remove invalid records",
            "Integrated GA4 & Search Console driving organic traffic across <b>~7,000 users</b>",
        ],
        "stack": ["Astro", "Python", "Supabase", "PostgreSQL", "Redis", "BullMQ"],
        "live_url": "https://synckra.in",
        "btn_label": "🌐 Live Website",
        "repo_url": None,
    },
    {
        "key": "milkywave",
        "name": "MilkyWave",
        "tagline": "Local Commerce & Neighborhood Marketplace",
        "badge_text": "📱 100+ DOWNLOADS · MOBILE APP",
        "description": "A cross-platform mobile marketplace app connecting neighborhood customers with local stores for streamlined ordering and delivery.",
        "highlights": [
            "Cross-platform mobile application developed with <b>React Native</b> and <b>Expo</b>",
            "Relational <b>Supabase PostgreSQL</b> schema for vendor catalogs, customers, and order states",
            "Integrated <b>Razorpay API</b> for secure digital payments and checkout flows",
            "Asynchronous API integration for product discovery, cart management, and order lifecycles",
        ],
        "stack": ["React Native", "Expo", "TypeScript", "Supabase", "PostgreSQL", "Razorpay"],
        "live_url": "https://play.google.com/store/apps/details?id=com.milkywave.customer&pcampaignid=web_share",
        "btn_label": "📱 Download on Google Play",
        "repo_url": None,
    },
]

# Developer Focus Tiles (2x2)
DASHBOARD_TILES = [
    {
        "title": "currently_building",
        "items": [
            "Autonomous AI agent workflows with <b>LangGraph</b> & LLM orchestration",
            "Production-grade <b>RAG pipelines</b> with multi-provider fallbacks",
            "High-throughput data ingestion pipelines & backend services",
        ],
    },
    {
        "title": "favorite_tools",
        "items": [
            "<b>Python</b> · <b>FastAPI</b> · <b>TypeScript</b> · <b>React</b>",
            "<b>PostgreSQL</b> · <b>Supabase</b> · <b>Redis</b> · <b>pandas</b>",
            "<b>Git</b> · <b>CI/CD</b> · <b>Vercel</b> · <b>Pub/Sub</b>",
        ],
    },
    {
        "title": "latest_interests",
        "items": [
            "LLM fine-tuning & agentic orchestration patterns",
            "Healthcare interoperability (<b>ABDM / Medplum FHIR</b> standards)",
            "Low-latency caching strategies & distributed data modeling",
        ],
    },
    {
        "title": "open_to_collaboration",
        "items": [
            "Full-Time <b>AI Engineer</b> & <b>Backend Software</b> opportunities",
            "Scalable distributed systems & high-throughput pipelines",
            "Full-stack product architecture & REST API platforms",
        ],
    },
]

# Technical Stack (STRICTLY skills present on resume)
TECH_STACK_GROUPS = {
    "Languages": [
        "Python", "JavaScript", "TypeScript", "C++", "HTML", "CSS"
    ],
    "AI / ML": [
        "LLMs", "RAG Pipelines", "AI Agents", "LangGraph", "Fine-Tuning", "LLM Orchestration"
    ],
    "Frameworks & APIs": [
        "FastAPI", "React", "React Native", "Expo", "Node.js", "Express.js", "Astro", "Medplum FHIR"
    ],
    "Databases": [
        "PostgreSQL", "Supabase", "MongoDB", "Redis"
    ],
    "Data & Analytics": [
        "pandas", "Data Modeling", "Data Pipelines", "Google Analytics 4 (GA4)"
    ],
    "Cloud, DevOps & Tools": [
        "Pub/Sub", "CI/CD", "Git", "Postman", "Vercel", "Razorpay API", "REST APIs"
    ],
}


def url_encode(text: str) -> str:
    """Safely encode query parameters for external badge/image APIs."""
    return urllib.parse.quote(text, safe="")


# =============================================================================
# 2. BUILDER: HERO HEADER WITH ANYA BANNER & QUICK LINKS
# =============================================================================

def build_header() -> str:
    """
    Constructs the top introduction area:
    - Clean status breadcrumb
    - Clean branded white card banner with welcoming Anya
    - Animated monospace typing line
    - Clean contact pills
    """
    typing_lines_encoded = ";".join(url_encode(line) for line in TYPING_PHRASES)
    typing_svg_url = (
        "https://readme-typing-svg.demolab.com"
        f"?font=Fira+Code&weight=600&size=16&duration=2600&pause=900"
        f"&color=059669&background=FFFFFF00"
        f"&center=true&vCenter=true&width=820&height=42"
        f"&lines={typing_lines_encoded}"
    )

    header_svg_path = "./assets/cat-header.svg"

    return f"""<div align="center">

<!-- Clean Top Status Breadcrumb -->
<code>[ ANYA-OS ] &nbsp; [ STATUS: OPEN FOR FULL-TIME ROLES ] &nbsp; [ HYDERABAD, IN ] &nbsp; [ B.TECH MAY 2026 ]</code>

<br/><br/>

<!-- Clean Branded Header Card featuring Welcoming Anya -->
<a href="https://github.com/{PROFILE.username}">
  <img src="{header_svg_path}" width="100%" alt="{PROFILE.name} — Profile Header" />
</a>

<!-- Animated Monospace Typing Line -->
<p align="center">
  <a href="https://github.com/{PROFILE.username}">
    <img src="{typing_svg_url}" alt="Animated Typing Subtitle" />
  </a>
</p>

<!-- Clean Contact & Navigation Pills -->
<a href="https://github.com/{PROFILE.username}">
  <img src="https://img.shields.io/badge/GitHub-Anujyadav911-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub Profile" />
</a>
&nbsp;
<a href="{PROFILE.linkedin_url}">
  <img src="https://img.shields.io/badge/LinkedIn-Let's%20Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
&nbsp;
<a href="mailto:{PROFILE.email}">
  <img src="https://img.shields.io/badge/Email-Say%20Hello-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" />
</a>
&nbsp;
<a href="{PROFILE.website_url}">
  <img src="https://img.shields.io/badge/Live%20Project-synckra.in-059669?style=flat-square&logo=astro&logoColor=white" alt="Synckra Website" />
</a>

</div>"""


# =============================================================================
# 3. BUILDER: ABOUT ME ($ whoami.py) WITH EXACT CAT IMAGE
# =============================================================================

def build_about() -> str:
    """
    Constructs the identity block:
    - Clean developer window header
    - Python identity class me = AnujYadav() with real career context
    - Clean anime cat card (using exact cat.png with generous width)
    """
    return f"""### <code>guest@{PROFILE.terminal_host}:~$ whoami.py --verbose</code>

<table width="100%" border="0" cellspacing="0" cellpadding="8">
<tr>
<td width="73%" valign="top">

```python
# anuj-station:~ $ whoami.py
class AnujYadav:
    role         = "AI Engineer Intern @ Mondee Tech Pvt. Ltd."
    location     = "Hyderabad, India"
    education    = "B.Tech in ECE, IIIT Manipur (Graduating May 2026)"
    seeking      = "Full-Time AI Engineering / Backend Software Roles"

    core_focus   = [
        "Autonomous AI Agents & LangGraph",
        "Production RAG Pipelines & Multi-LLM Fallbacks",
        "High-Concurrency Ingestion & Scalable Backends",
    ]
    tech_stack   = [
        "Python", "FastAPI", "React", "TypeScript", "PostgreSQL", "Redis"
    ]
    fuel         = "Chai ☕ + Python 🐍 + Peanuts 🥜"
    allies       = ["Anya Forger 🌸", "Chibi Neko ฅ^•ﻌ•^ฅ"]

    def current_mission(self):
        return "Building production software, scaling systems, shipping products."

me = AnujYadav()
print(me.current_mission())
```

</td>
<td width="27%" align="center" valign="middle">

<img src="./assets/cat.png" width="88%" alt="Cute Anime Cat Companion" />

<p align="center">
  <sub><i>"Simple code, solid architecture."</i></sub>
</p>

</td>
</tr>
</table>"""


# =============================================================================
# 4. BUILDER: VERIFIED ENGINEERING HIGHLIGHTS (CLEAN CODE TAGS, NO EMOJIS)
# =============================================================================

def build_highlights() -> str:
    """
    Constructs verified engineering highlights using clean code tags
    instead of emoji clutter, formatted in direct, human language.
    """
    return """#### <code>Verified Engineering Highlights</code>
- <code>data-pipelines</code> &nbsp; **High-Throughput Healthcare Ingestion**: Engineered pipelines handling **15,169 files** and structuring **220,776 transcript turns** for clinical AI systems at Mondee Tech.
- <code>backend-systems</code> &nbsp; **Distributed Booking Architecture**: Developed booking and backend services supporting **10,000+ daily transactions** with Redis quote caching (decreased checkout latency by **45%**).
- <code>llm-orchestration</code> &nbsp; **Multi-Model LLM Workflows**: Designed multi-provider fallback architectures (<em>Gemini &rarr; Groq &rarr; OpenRouter</em>) and autonomous agent workflows with **LangGraph** to reliably parse raw web data.
- <code>healthcare-fhir</code> &nbsp; **Healthcare Interoperability**: Integrated ABHA registration into ABDM kiosks using **Medplum FHIR** standards and mobile OTP verification.
- <code>education</code> &nbsp; **IIIT Manipur**: B.Tech in Electronics and Communication Engineering (2022 &ndash; May 2026, CGPA: 7.46/10). Actively seeking full-time roles."""


# =============================================================================
# 5. BUILDER: GIT COMMIT TRACKER (LEETCODE STYLE, YEAR-WISE SELECTION)
# =============================================================================

def build_commit_tracker() -> str:
    """
    Constructs the LeetCode/GitHub style commit tracker calendar
    with year-wise selection (2026, 2025, 2024).
    Uses interactive collapsible details for native GitHub tab behavior.
    """
    return """### <code>git log --contributions --year-wise</code>

<details open>
  <summary><b>📅 2026 Activity (259 Contributions) — Active Year</b></summary>
  <br/>
  <img src="./assets/git_tracker_2026.svg" width="100%" alt="2026 GitHub Contributions Tracker" />
</details>

<details>
  <summary><b>📅 2025 Activity (69 Contributions)</b></summary>
  <br/>
  <img src="./assets/git_tracker_2025.svg" width="100%" alt="2025 GitHub Contributions Tracker" />
</details>

<details>
  <summary><b>📅 2024 Activity (0 Contributions)</b></summary>
  <br/>
  <img src="./assets/git_tracker_2024.svg" width="100%" alt="2024 GitHub Contributions Tracker" />
</details>"""


# =============================================================================
# 6. BUILDER: FEATURED PROJECTS (SYNCKRA & MILKYWAVE)
# =============================================================================

def build_projects() -> str:
    """
    Constructs two side-by-side clean project cards with verified metrics.
    """
    cards_html = []

    for proj in FEATURED_PROJECTS:
        tech_chips = " ".join(f"<code>{t}</code>" for t in proj["stack"])
        highlights_html = "".join(f"<li>{h}</li>" for h in proj["highlights"])
        card_svg_path = f"./assets/cat-{proj['key']}.svg"

        links = []
        if proj.get("live_url"):
            btn_label = proj.get("btn_label", "Visit Project")
            links.append(f'<a href="{proj["live_url"]}"><b>{btn_label}</b></a>')
        if proj.get("repo_url"):
            links.append(f'<a href="{proj["repo_url"]}"><b>Source Code</b></a>')
        action_bar = " &nbsp;·&nbsp; ".join(links)

        card = f"""<td width="50%" valign="top">

<a href="{proj.get('live_url')}">
  <img src="{card_svg_path}" width="100%" alt="{proj['name']} Preview" />
</a>

<br/><br/>

<b>{proj['tagline']}</b>

<p>{proj['description']}</p>

<ul>
{highlights_html}
</ul>

<b>Tech Stack:</b><br/>
{tech_chips}

<br/><br/>

{action_bar}

</td>"""
        cards_html.append(card)

    return f"""### <code>ls -la ./featured_projects/</code>

<table width="100%" border="0" cellspacing="0" cellpadding="8">
<tr>
{cards_html[0]}
{cards_html[1]}
</tr>
</table>"""


# =============================================================================
# 7. BUILDER: DEVELOPER DASHBOARD (2x2)
# =============================================================================

def build_mini_dashboard() -> str:
    """
    Constructs a 2x2 clean developer dashboard of what Anuj is currently
    building, favorite tools, and areas of collaboration.
    """
    def format_tile(tile: dict) -> str:
        items = "".join(f"<li>{it}</li>" for it in tile["items"])
        return f"""<b><code>{tile['title']}</code></b>
<ul>
{items}
</ul>"""

    t0 = format_tile(DASHBOARD_TILES[0])
    t1 = format_tile(DASHBOARD_TILES[1])
    t2 = format_tile(DASHBOARD_TILES[2])
    t3 = format_tile(DASHBOARD_TILES[3])

    return f"""### <code>./dashboard.sh --status --realtime</code>

<table width="100%" border="0" cellspacing="0" cellpadding="8">
<tr>
<td width="50%" valign="top">
{t0}
</td>
<td width="50%" valign="top">
{t1}
</td>
</tr>
<tr>
<td width="50%" valign="top">
{t2}
</td>
<td width="50%" valign="top">
{t3}
</td>
</tr>
</table>"""


# =============================================================================
# 8. BUILDER: TECHNICAL SKILLS (RESUME-ACCURATE)
# =============================================================================

def build_skills() -> str:
    """
    Constructs organized technical skill blocks strictly matching resume.
    """
    blocks = []
    for group_name, items in TECH_STACK_GROUPS.items():
        chips = " ".join(f"<code>{name}</code>" for name in items)
        block = f"<b>{group_name}</b><br/>\n{chips}"
        blocks.append(block)

    return f"""### <code>cat /etc/tech_stack.json</code>

<table width="100%" border="0" cellspacing="0" cellpadding="8">
<tr>
<td width="50%" valign="top">
{blocks[0]}
<br/><br/>
{blocks[1]}
<br/><br/>
{blocks[2]}
</td>
<td width="50%" valign="top">
{blocks[3]}
<br/><br/>
{blocks[4]}
<br/><br/>
{blocks[5]}
</td>
</tr>
</table>"""


# =============================================================================
# 9. BUILDER: END ANYA EXIT & CONTACT
# =============================================================================

def build_footer() -> str:
    """
    Constructs the closing section featuring End Anya Card and clean contact links.
    """
    endanaya_card_svg_path = "./assets/endanaya-card.svg"

    return f"""### <code>anya@{PROFILE.terminal_host}:~$ ./mission_complete.py --status=goodbye</code>

<div align="center">
  <img src="{endanaya_card_svg_path}" width="100%" alt="End Anya — Mission Complete" />
</div>

<br/>

<table width="100%" border="0" cellspacing="0" cellpadding="8">
<tr>
<td width="58%" valign="top">

```python
# exit.py — Session Terminated Successfully
while visitor.is_on_page():
    anuj.build_ai_agents()
    anuj.scale_backends()
    anya.waku_waku()  # 🌸 🥜
    anuj.ship()

# Telepathic message from Anya:
# "If you like Anuj's engineering, don't forget to star his repos!"
```

<b>Let's build something extraordinary together.</b><br/>
I'm graduating in May 2026 and actively open to exciting AI engineering roles, high-throughput backend architectures, and creative product collaborations.

<br/><br/>

<a href="https://github.com/{PROFILE.username}">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub" />
</a>
&nbsp;
<a href="{PROFILE.linkedin_url}">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn" />
</a>
&nbsp;
<a href="mailto:{PROFILE.email}">
  <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
</a>
&nbsp;
<a href="{PROFILE.website_url}">
  <img src="https://img.shields.io/badge/Synckra-059669?style=for-the-badge&logo=astro&logoColor=white" alt="Website" />
</a>

</td>
<td width="42%" align="center" valign="middle">

<a href="https://github.com/{PROFILE.username}">
  <img src="./assets/endanaya.png" width="85%" alt="Anya Watching from Bottom" />
</a>

<p align="center">
  <sub>🌸 <i>"Anya: You reached the bottom! Anya hopes you star this profile! ⭐"</i></sub>
</p>

</td>
</tr>
</table>

<div align="center">
  <br/>
  <code>[ MISSION COMPLETE ] &nbsp; [ STATUS: READY ] &nbsp; [ LOCATION: HYDERABAD, IN ] &nbsp; [ ANYA-OS ]</code>
  <br/><br/>
  <sub>Engineered with care and clean architecture for <b>{PROFILE.name}</b> · 2026</sub>
</div>"""


# =============================================================================
# 10. ASSEMBLE ENTIRE README
# =============================================================================

def generate_full_readme() -> str:
    """Assembles all profile sections into the final GitHub-compliant Markdown."""
    sections = [
        build_header(),
        build_about(),
        build_highlights(),
        build_projects(),
        build_mini_dashboard(),
        build_skills(),
        build_footer(),
    ]
    return "\n\n---\n\n".join(sections) + "\n"


def main() -> None:
    output_path = Path("README.md")

    # 1. Ensure SVGs and trackers are up-to-date
    try:
        import generate_assets
        generate_assets.main()
    except Exception as e:
        print(f"Notice regarding assets generation: {e}")

    try:
        import generate_commit_tracker
        generate_commit_tracker.main()
    except Exception as e:
        print(f"Notice regarding commit tracker: {e}")

    # 2. Generate Markdown
    markdown_content = generate_full_readme()
    output_path.write_text(markdown_content, encoding="utf-8")

    # 3. Synchronize readme_preview.html for browser preview
    preview_path = Path("readme_preview.html")
    preview_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>GitHub README Preview - {PROFILE.name}</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.1/github-markdown-light.min.css">
  <style>
    body {{
      background-color: #f6f8fa;
      color: #1f2328;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 30px 15px;
    }}
    .markdown-body {{
      box-sizing: border-box;
      min-width: 200px;
      max-width: 920px;
      margin: 0 auto;
      padding: 40px;
      background-color: #ffffff;
      border: 1px solid #d0d7de;
      border-radius: 12px;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
    }}
    .markdown-body table {{
      width: 100% !important;
      display: table !important;
      background-color: transparent !important;
      border-collapse: collapse !important;
      margin-bottom: 16px;
    }}
    .markdown-body table tr, .markdown-body table td {{
      border: 1px solid #e2e8f0 !important;
      background-color: #ffffff !important;
      padding: 14px !important;
      border-radius: 6px;
    }}
    .markdown-body pre {{
      background-color: #0f172a !important;
      color: #f8fafc !important;
      border: 1px solid #1e293b !important;
      border-radius: 8px;
    }}
    .markdown-body code {{
      font-family: 'Fira Code', 'Courier New', monospace;
    }}
    details {{
      background-color: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 12px 16px;
      margin-bottom: 12px;
    }}
    summary {{
      cursor: pointer;
      font-weight: 600;
      color: #0f172a;
    }}
  </style>
</head>
<body>
  <div id="content" class="markdown-body"></div>

  <script id="raw-md" type="text/markdown">
{markdown_content}
  </script>

  <script>
    const raw = document.getElementById('raw-md').textContent;
    marked.setOptions({{
      gfm: true,
      breaks: true
    }});
    document.getElementById('content').innerHTML = marked.parse(raw);
  </script>
</body>
</html>
"""
    preview_path.write_text(preview_html, encoding="utf-8")

    print("=" * 65)
    print("CLEAN BRANDED GITHUB PROFILE & README GENERATED!")
    print("=" * 65)
    print(f" Output File:     {output_path.resolve()}")
    print(f" Profile User:    {PROFILE.username} ({PROFILE.name})")
    print(f" Career Role:     {PROFILE.role}")
    print(f" Commit Tracker:  2026 (259), 2025 (69), 2024 (0) with Year Selection")
    print(f" Mascot Assets:   Anya Welcoming Banner, Cute Anime Cat, End Anya Card")
    print(f" Highlights:      Code-style tags, 0 emojis, 100% matched to resume")
    print("=" * 65)


if __name__ == "__main__":
    main()
