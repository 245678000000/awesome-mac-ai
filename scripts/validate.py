#!/usr/bin/env python3
"""
Validation script for Awesome Mac AI dataset.
Ensures data/apps.json follows the required schema.
"""

import json
import sys
from pathlib import Path

REQUIRED_KEYS = [
    "id",
    "name",
    "primary_type",
    "surfaces",
    "capabilities",
    "platforms",
    "status",
    "recommendation",
    "verified_at"
]

VALID_STATUSES = ["active", "beta", "experimental", "legacy", "deprecated", "transitioned"]
VALID_RECOMMENDATIONS = ["S", "A", "B"]

def main():
    root = Path(__file__).resolve().parent.parent
    data_file = root / "data" / "apps.json"
    
    if not data_file.exists():
        print(f"❌ Error: {data_file} not found!")
        sys.exit(1)
        
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            apps = json.load(f)
    except Exception as e:
        print(f"❌ JSON Parse Error: {e}")
        sys.exit(1)
        
    if not isinstance(apps, list):
        print("❌ Error: data/apps.json must contain a JSON array!")
        sys.exit(1)
        
    seen_ids = set()
    errors = []
    
    for idx, app in enumerate(apps):
        app_name = app.get("name", f"Index {idx}")
        
        # Check required fields
        for key in REQUIRED_KEYS:
            if key not in app:
                errors.append(f"[{app_name}] Missing required field: '{key}'")
                
        # Check ID uniqueness
        app_id = app.get("id")
        if app_id:
            if app_id in seen_ids:
                errors.append(f"[{app_name}] Duplicate ID: '{app_id}'")
            seen_ids.add(app_id)
            
        # Check status
        status = app.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(f"[{app_name}] Invalid status: '{status}'. Must be one of {VALID_STATUSES}")
            
        # Check recommendation
        rec = app.get("recommendation")
        if rec and rec not in VALID_RECOMMENDATIONS:
            errors.append(f"[{app_name}] Invalid recommendation: '{rec}'. Must be one of {VALID_RECOMMENDATIONS}")
            
    if errors:
        print(f"❌ Found {len(errors)} validation errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
        
    print(f"✅ Successfully validated {len(apps)} entries in data/apps.json! All checks passed.")

if __name__ == "__main__":
    main()
