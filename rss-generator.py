from bs4 import BeautifulSoup
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import datetime

# Load your HTML file
with open("index.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Map section anchors to editorial categories
section_map = {
    "incident": "Incident",
    "case": "Case",
    "community": "Community"
}

# Find all timeline cards and track their section
cards = []
current_section = None

for tag in soup.find_all(["section", "h2"]):
    if tag.name == "h2" and tag.get("id") in section_map:
        current_section = tag.get("id")
    elif tag.name == "section" and "timeline-card" in tag.get("class", []):
        cards.append((current_section, tag))

# Sort cards: Case → Incident → Community
priority_order = ["case", "incident", "community"]

# Group and reverse each section
sorted_cards = []
for section in priority_order:
    group = [c for c in cards if c[0] == section]
    sorted_cards.extend(group[::-1])  # Newest first within group

cards = sorted_cards

# Build RSS feed
rss = Element("rss", version="2.0")
channel = SubElement(rss, "channel")

SubElement(channel, "title").text = "Iryna Watch Updates"
SubElement(channel, "link").text = "https://irynawatch.netlify.app/"
SubElement(channel, "description").text = "Updates to the Iryna murder case timeline."
SubElement(channel, "lastBuildDate").text = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

for section_id, card in cards:
    h3 = card.find("h3")
    p = card.find("p")
    small = card.find("small")

    if h3 and p:
        title = h3.get_text(strip=True)
        description = p.get_text(strip=True)
        if small:
            description += f" <em>{small.get_text(strip=True)}</em>"

        # Extract date from title
        try:
            date_str = title.split(" - ")[0].strip()
            pub_date = datetime.datetime.strptime(date_str, "%b %d, %Y").strftime("%a, %d %b %Y %H:%M:%S GMT")
        except Exception:
            pub_date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

        # Build RSS item
        item = SubElement(channel, "item")
        SubElement(item, "title").text = title
        SubElement(item, "link").text = f"https://irynawatch.netlify.app/#{section_id}"
        SubElement(item, "description").text = f"Category: {section_map.get(section_id, 'Unknown')}. {description}"
        SubElement(item, "pubDate").text = pub_date
        SubElement(item, "guid").text = title.replace(" ", "-").lower()

# Save RSS XML
rss_xml = parseString(tostring(rss)).toprettyxml(indent="  ")
with open("rss.xml", "w", encoding="utf-8") as f:
    f.write(rss_xml)

print("✅ RSS feed generated as rss.xml")