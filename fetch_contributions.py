import urllib.request
import re
from pathlib import Path

def fetch_year(year):
    url = f"https://github.com/users/Anujyadav911/contributions?to={year}-12-31"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("utf-8")
        
        # Total count
        m_count = re.search(r'([0-9,]+)\s+contributions', html)
        count = m_count.group(1) if m_count else "0"
        
        # Extract td items
        pattern = r'<td[^>]*data-date="([^"]+)"[^>]*data-level="([^"]+)"[^>]*>'
        matches = re.findall(pattern, html)
        if not matches:
            # Alternate order
            pattern2 = r'<td[^>]*data-level="([^"]+)"[^>]*data-date="([^"]+)"[^>]*>'
            matches2 = re.findall(pattern2, html)
            matches = [(d, l) for l, d in matches2]
            
        print(f"Year {year}: {count} contributions, {len(matches)} days recorded")
        return count, matches
    except Exception as e:
        print(f"Year {year} error: {e}")
        return "0", []

data_2026 = fetch_year(2026)
data_2025 = fetch_year(2025)
data_2024 = fetch_year(2024)
