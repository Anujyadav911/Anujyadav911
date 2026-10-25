"""
Animated GitHub Profile README Generator
----------------------------------------
Run:
    python generate_readme.py

This creates README.md in the current directory.
Edit the configuration values below before publishing.
"""

from pathlib import Path
from textwrap import dedent


# ============================================================
# 1. PROFILE CONFIGURATION
# ============================================================

USERNAME = "Anujyadav911"
NAME = "Anuj Yadav"
ROLE = "AI Engineer  •  Full-Stack Developer  •  Product Builder"
LOCATION = "Hyderabad, India"
COMPANY = "Mondee Tech"

EMAIL = "anujyadav47247@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/anuj-yadav-506a99257/"

# Replace these with your real links.
SYNCKRA_URL = "https://YOUR-SYNCKRA-WEBSITE.com"
SYNCKRA_REPO_URL = "https://github.com/YOUR-USERNAME/YOUR-SYNCKRA-REPO"
MILKYWAVE_URL = "https://github.com/YOUR-USERNAME/YOUR-MILKYWAVE-REPO"

OUTPUT_FILE = Path("README.md")


# ============================================================
# 2. SMALL REUSABLE HELPERS
# ============================================================

def badge(label: str, message: str, color: str, logo: str = "") -> str:
    """Create a shields.io badge."""
    logo_part = f"&logo={logo}&logoColor=white" if logo else ""
    label = label.replace("-", "--").replace("_", "__").replace(" ", "%20")
    message = message.replace("-", "--").replace("_", "__").replace(" ", "%20")
    return (
        f"![{label}: {message}]"
        f"(https://img.shields.io/badge/{label}-{message}-{color}"
        f"?style=for-the-badge{logo_part})"
    )


def section(title: str, body: str) -> str:
    """Format a README section consistently."""
    return f"\n---\n\n## {title}\n\n{dedent(body).strip()}\n"


def image(url: str, alt: str, height: int | None = None) -> str:
    """Create an HTML image element for GitHub Markdown."""
    height_attr = f' height="{height}"' if height else ""
    return f'<img src="{url}" alt="{alt}"{height_attr} />'


# ============================================================
# 3. ANIMATED HEADER
# ============================================================

def build_header() -> str:
    typing_svg = (
        "https://readme-typing-svg.demolab.com"
        "?font=Fira+Code&weight=600&size=20&duration=2800&pause=700"
        "&color=00F5A0&center=true&vCenter=true&width=760&height=55"
        "&lines=AI+Engineer+%7C+Full-Stack+Developer;"
        "Building+AI-powered+products;"
        "From+idea+to+production;"
        "Python+%7C+LLMs+%7C+Backend+Engineering"
    )

    banner = (
        "https://capsule-render.vercel.app/api"
        "?type=waving&color=0:101827,50:123C69,100:00F5A0"
        "&height=210&section=header&text=ANUJ%20YADAV"
        "&fontSize=48&fontColor=FFFFFF&fontAlignY=38"
        "&desc=Engineering%20ideas%20into%20real%20products"
        "&descSize=16&descAlignY=59&animation=fadeIn"
    )

    return f"""
<div align="center">

{image(banner, "Animated profile banner")}

{image(typing_svg, "Animated introduction")}

<br/>

{badge("PROFILE", "AI ENGINEER", "0d1117", "python")}
{badge("FOCUS", "REAL WORLD PRODUCTS", "123c69")}
{badge("LOCATION", "HYDERABAD INDIA", "146c5b")}

<br/><br/>

<a href="https://github.com/{USERNAME}">
  <img src="https://img.shields.io/badge/GitHub-View%20Profile-181717?style=for-the-badge&logo=github" alt="GitHub profile"/>
</a>
<a href="{LINKEDIN_URL}">
  <img src="https://img.shields.io/badge/LinkedIn-Let's%20Connect-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
</a>
<a href="mailto:{EMAIL}">
  <img src="https://img.shields.io/badge/Email-Say%20Hello-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
</a>

</div>
""".strip()


# ============================================================
# 4. ABOUT ME — PYTHON-INSPIRED TERMINAL
# ============================================================

def build_about() -> str:
    return f"""
### `$ whoami`

```python
class {NAME.replace(" ", "")}:
    role = "{ROLE}"
    company = "{COMPANY}"
    location = "{LOCATION}"

    interests = [
        "LLMs and RAG pipelines",
        "AI agents and model fine-tuning",
        "Backend and distributed systems",
        "Full-stack product engineering",
    ]

    motto = "Build. Ship. Learn. Repeat."


me = {NAME.replace(" ", "")}()
print(me.motto)
```

I build **AI-powered applications and full-stack products** with a focus on useful features,
clean architecture, and production-minded engineering.

Currently working as an **AI Engineer Intern at {COMPANY}**, exploring the intersection
of AI systems, backend engineering, and real-world product development.
""".strip()


# ============================================================
# 5. FEATURED PRODUCTS
# ============================================================

def build_projects() -> str:
    return f"""
<table>
<tr>
<td width="50%" valign="top">

<h3>🌐 Synckra</h3>

<b>Internship & Fresher Job Platform</b>

A career platform helping students discover internships and entry-level opportunities.

<br/><br/>

<img src="https://img.shields.io/badge/~7,000-Users-00C896?style=for-the-badge" alt="Approximately 7000 users"/>

- Modern web experience built with Astro
- Supabase and PostgreSQL data layer
- Redis and BullMQ background processing
- SEO and search discoverability focus

<br/>

<b>Stack</b><br/>
<code>Astro</code> <code>PostgreSQL</code> <code>Supabase</code>
<code>Redis</code> <code>BullMQ</code> <code>Vercel</code>

<br/><br/>

<a href="{SYNCKRA_URL}">🚀 Live Product</a>
&nbsp;·&nbsp;
<a href="{SYNCKRA_REPO_URL}">💻 Repository</a>

</td>
<td width="50%" valign="top">

<h3>📱 MilkyWave</h3>

<b>Local Commerce & Delivery Platform</b>

A mobile application concept focused on connecting customers with local shops and supporting ordering workflows.

<br/><br/>

<img src="https://img.shields.io/badge/MOBILE-APPLICATION-7C3AED?style=for-the-badge" alt="Mobile application"/>

- Mobile experience built with Expo
- Supabase backend integration
- Customer and shop-related workflows
- API-driven application architecture

<br/>

<b>Stack</b><br/>
<code>React Native</code> <code>Expo</code> <code>TypeScript</code>
<code>Supabase</code> <code>PostgreSQL</code>

<br/><br/>

<a href="{MILKYWAVE_URL}">💻 Explore Repository</a>

</td>
</tr>
</table>

> **Product mindset:** Build for people, measure what matters, and keep improving.
""".strip()


# ============================================================
# 6. TECH STACK
# ============================================================

def build_stack() -> str:
    groups = {
        "Languages": [
            ("Python", "3776AB", "python"),
            ("C++", "00599C", "cplusplus"),
            ("JavaScript", "F7DF1E", "javascript"),
            ("TypeScript", "3178C6", "typescript"),
        ],
        "AI / Machine Learning": [
            ("Hugging Face", "FFD21E", "huggingface"),
            ("PyTorch", "EE4C2C", "pytorch"),
            ("LangChain", "1C3C3C", "langchain"),
            ("OpenAI", "412991", "openai"),
        ],
        "Backend / Data": [
            ("FastAPI", "009688", "fastapi"),
            ("Node.js", "339933", "nodedotjs"),
            ("PostgreSQL", "4169E1", "postgresql"),
            ("Redis", "DC382D", "redis"),
            ("MongoDB", "47A248", "mongodb"),
        ],
        "Frontend / Tools": [
            ("React", "20232A", "react"),
            ("Next.js", "000000", "nextdotjs"),
            ("Docker", "2496ED", "docker"),
            ("Git", "F05032", "git"),
        ],
    }

    parts = []
    for heading, technologies in groups.items():
        badges = " ".join(
            badge(name, name, color, logo)
            for name, color, logo in technologies
        )
        parts.append(f"**{heading}**\n\n{badges}")

    return "\n\n".join(parts)


# ============================================================
# 7. LIVE GITHUB ANALYTICS
# ============================================================

def build_analytics() -> str:
    return f"""
<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&hide_border=true&theme=tokyonight&rank_icon=github" alt="GitHub stats"/>
<img width="49%" src="https://github-readme-stats.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&hide_border=true&theme=tokyonight" alt="Most used languages"/>

<br/><br/>

<img width="70%" src="https://streak-stats.demolab.com?user={USERNAME}&theme=tokyonight&hide_border=true" alt="GitHub contribution streak"/>

<br/><br/>

<img src="https://komarev.com/ghpvc/?username={USERNAME}&style=for-the-badge&color=00C896&label=PROFILE+VIEWS" alt="Profile views"/>

</div>
""".strip()


# ============================================================
# 8. CONTACT + FOOTER
# ============================================================

def build_contact() -> str:
    footer_wave = (
        "https://capsule-render.vercel.app/api"
        "?type=waving&color=0:00F5A0,100:101827&height=100&section=footer"
    )

    return f"""
<div align="center">

### Let's build something meaningful.

<a href="https://github.com/{USERNAME}">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"/>
</a>
<a href="{LINKEDIN_URL}">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
</a>
<a href="mailto:{EMAIL}">
  <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
</a>

<br/><br/>

<code>while learning:</code>
<br/>
<code> &nbsp; build() → ship() → improve()</code>

<br/><br/>

{image(footer_wave, "Animated footer wave")}

</div>
""".strip()


# ============================================================
# 9. ASSEMBLE README
# ============================================================

def generate_readme() -> str:
    sections = [
        build_header(),
        section("`01` &nbsp; About Me", build_about()),
        section("`02` &nbsp; Featured Products", build_projects()),
        section("`03` &nbsp; Tech Stack", build_stack()),
        section("`04` &nbsp; GitHub Analytics", build_analytics()),
        section("`05` &nbsp; Connect", build_contact()),
    ]
    return "\n\n".join(sections) + "\n"


def main() -> None:
    content = generate_readme()
    OUTPUT_FILE.write_text(content, encoding="utf-8")
    print(f"✅ Generated {OUTPUT_FILE.resolve()}")
    print("Next steps:")
    print("1. Replace placeholder project URLs in this script.")
    print("2. Review README.md in a Markdown preview.")
    print("3. Commit README.md to your profile repository.")


if __name__ == "__main__":
    main()
