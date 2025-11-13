#!/usr/bin/env python3
"""
Add 'published' column to creations_catalog.csv for website publishing control.
Marks E-00037 and E-00042 as published='yes' for testing.
"""

import csv
import shutil
from datetime import datetime

# Paths
CATALOG_PATH = "/Volumes/2025/SynologyDrive/Operating/Catalogs/creations_catalog.csv"
BACKUP_PATH = f"/Volumes/2025/SynologyDrive/Operating/Catalogs/creations_catalog_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

# Test entries to mark as published
TEST_ENTRIES = ["E-00037", "E-00042"]

def main():
    # Backup original
    print(f"Creating backup: {BACKUP_PATH}")
    shutil.copy2(CATALOG_PATH, BACKUP_PATH)

    # Read all rows
    rows = []
    with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        # Check if 'published' already exists
        if 'published' in fieldnames:
            print("Column 'published' already exists in CSV")
            return

        # Add 'published' to fieldnames
        new_fieldnames = list(fieldnames) + ['published']

        for row in reader:
            # Add published field
            entity_id = row['entity_id']
            if entity_id in TEST_ENTRIES:
                row['published'] = 'yes'
                print(f"✓ Marking {entity_id} as published='yes'")
            else:
                row['published'] = 'no'  # Default to not published
            rows.append(row)

    # Write updated CSV
    with open(CATALOG_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✅ Successfully added 'published' column to {len(rows)} entries")
    print(f"✅ Marked {len(TEST_ENTRIES)} test entries as published='yes'")
    print(f"✅ Backup saved to: {BACKUP_PATH}")

if __name__ == "__main__":
    main()
