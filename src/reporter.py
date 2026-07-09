from collections import Counter

def build_report(records, pages_scraped):
    lines = []

    lines.append("# Catalog Scraping Report")
    lines.append("")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Pages scraped: {pages_scraped}")
    lines.append(f"- Total books: {len(records)}")
    lines.append("")
    lines.append("")
    lines.append("## Ratings")

    
    ratings = [item["rating"] for item in records]
    rating_count = Counter(ratings)
    for value, count in rating_count.items():
        lines.append(f"- {value}: {count}")

    lines.append("")
    lines.append("")
    lines.append("## Availability")


    availability = [item["availability"] for item in records]
    availability_count = Counter(availability)
    for value, count in availability_count.items():
        lines.append(f"- {value}: {count}")

    lines.append("")
    lines.append("")
    lines.append("## Sample Records")
    
    for record in records[:5]:
        lines.append(f"- {record}")

    return "\n".join(lines)

