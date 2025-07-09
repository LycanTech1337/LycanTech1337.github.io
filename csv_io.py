import csv

def export_to_csv(data, filepath='translator.csv'):
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['english', 'lagu', 'pos', 'image', 'audio'])
        for eng, entry in data.items():
            writer.writerow([eng, entry['lagu'], entry['pos'], entry.get('image', ''), entry.get('audio', '')])
    print(f"Exported to {filepath}")

def import_from_csv(filepath='translator.csv'):
    data = {}
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row['english'].strip().lower()] = {
                'lagu': row['lagu'].strip().lower(),
                'pos': row['pos'].strip().lower(),
                'image': row.get('image', '').strip(),
                'audio': row.get('audio', '').strip()
            }
    print(f"Imported from {filepath}")
    return data