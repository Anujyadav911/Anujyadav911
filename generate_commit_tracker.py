"""
Generate GitHub / LeetCode style commit tracker SVGs for 2026, 2025, and 2024.
Matches the exact green contribution grid shown in user's reference image.
"""
import datetime
import sys
from pathlib import Path

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ASSETS_DIR = Path("assets")
ASSETS_DIR.mkdir(exist_ok=True)

# LeetCode / GitHub green shades
GREEN_COLORS = {
    0: "#EBEDF0",  # No contributions
    1: "#9BE9A8",  # Low
    2: "#40C463",  # Medium-low
    3: "#30A14E",  # Medium-high
    4: "#216E39",  # High
}

MONTH_NAMES = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def generate_svg_calendar(year: int, count_str: str, day_levels: dict[str, int]) -> str:
    """
    Builds a clean, branded SVG contribution calendar for a given year.
    day_levels: dict of 'YYYY-MM-DD' -> int (0 to 4)
    """
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    
    # Calculate starting day of week (0 = Monday, 6 = Sunday)
    # GitHub grids usually start with Sunday (weekday() = 6 -> row 0)
    # Let Sunday = row 0, Monday = row 1, ..., Saturday = row 6
    def to_row(dt: datetime.date) -> int:
        return (dt.weekday() + 1) % 7

    # Group days into columns (weeks)
    weeks = []
    curr_week = []
    
    # Pad first week if start_date is not Sunday
    first_row = to_row(start_date)
    for _ in range(first_row):
        curr_week.append(None)
        
    curr = start_date
    while curr <= end_date:
        d_str = curr.strftime("%Y-%m-%d")
        lvl = day_levels.get(d_str, 0)
        curr_week.append((curr, lvl))
        if len(curr_week) == 7:
            weeks.append(curr_week)
            curr_week = []
        curr += datetime.timedelta(days=1)
        
    if curr_week:
        while len(curr_week) < 7:
            curr_week.append(None)
        weeks.append(curr_week)

    cell_size = 10
    cell_gap = 3
    col_width = cell_size + cell_gap
    row_height = cell_size + cell_gap
    
    start_x = 32
    start_y = 42

    cells_svg = []
    month_labels_svg = []
    last_month = -1

    for col_idx, week in enumerate(weeks):
        # Check month label
        for item in week:
            if item is not None:
                dt, _ = item
                if dt.month != last_month and dt.day <= 7:
                    x_pos = start_x + col_idx * col_width
                    month_labels_svg.append(
                        f'<text x="{x_pos}" y="32" font-size="10" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif">{MONTH_NAMES[dt.month - 1]}</text>'
                    )
                    last_month = dt.month
                break

        # Render cells
        for row_idx, item in enumerate(week):
            if item is not None:
                dt, lvl = item
                color = GREEN_COLORS.get(lvl, GREEN_COLORS[0])
                x = start_x + col_idx * col_width
                y = start_y + row_idx * row_height
                date_str = dt.strftime("%b %d, %Y")
                cells_svg.append(
                    f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" rx="2" fill="{color}"><title>{lvl} contributions on {date_str}</title></rect>'
                )

    cells_content = "\n      ".join(cells_svg)
    months_content = "\n      ".join(month_labels_svg)
    
    total_w = start_x + len(weeks) * col_width + 24
    total_h = start_y + 7 * row_height + 34

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" width="100%" height="{total_h}" style="background: transparent; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <filter id="cardShadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000000" flood-opacity="0.06"/>
    </filter>
  </defs>

  <!-- Clean Branded Container Box -->
  <rect x="2" y="2" width="{total_w - 4}" height="{total_h - 4}" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1" filter="url(#cardShadow)" />

  <!-- Header line -->
  <text x="32" y="18" font-size="12" font-weight="600" fill="#0F172A">
    {year} GitHub Activity &#183; <tspan fill="#059669">{count_str} Total Contributions</tspan>
  </text>
  
  <!-- Day Labels (Mon, Wed, Fri) -->
  <text x="12" y="52" font-size="9" fill="#94A3B8">Mon</text>
  <text x="12" y="78" font-size="9" fill="#94A3B8">Wed</text>
  <text x="12" y="104" font-size="9" fill="#94A3B8">Fri</text>

  <!-- Month Labels -->
  <g>
    {months_content}
  </g>

  <!-- Contribution Squares -->
  <g>
    {cells_content}
  </g>

  <!-- Legend at Bottom Right -->
  <g transform="translate({total_w - 170}, {total_h - 18})">
    <text x="0" y="9" font-size="9" fill="#64748B">Less</text>
    <rect x="26" y="1" width="9" height="9" rx="2" fill="{GREEN_COLORS[0]}" />
    <rect x="38" y="1" width="9" height="9" rx="2" fill="{GREEN_COLORS[1]}" />
    <rect x="50" y="1" width="9" height="9" rx="2" fill="{GREEN_COLORS[2]}" />
    <rect x="62" y="1" width="9" height="9" rx="2" fill="{GREEN_COLORS[3]}" />
    <rect x="74" y="1" width="9" height="9" rx="2" fill="{GREEN_COLORS[4]}" />
    <text x="88" y="9" font-size="9" fill="#64748B">More</text>
  </g>
</svg>'''


def main():
    import fetch_contributions
    
    for year, (count, raw_cells) in [
        (2026, fetch_contributions.data_2026),
        (2025, fetch_contributions.data_2025),
        (2024, fetch_contributions.data_2024),
    ]:
        day_dict = {d: int(l) for d, l in raw_cells}
        svg_code = generate_svg_calendar(year, count, day_dict)
        out_path = ASSETS_DIR / f"git_tracker_{year}.svg"
        out_path.write_text(svg_code, encoding="utf-8")
        print(f"Generated {out_path} ({count} contributions)")

if __name__ == "__main__":
    main()
