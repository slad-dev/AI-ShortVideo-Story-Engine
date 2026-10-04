"""
Pipeline Utility: Parse Storyboard Markdown into structured JSON
Useful for feeding narration into Edge-TTS or sending prompts to Image Generation APIs.
"""

import re
import json
import sys

def parse_markdown_storyboard(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Simple regex parser for markdown table rows
    table_pattern = re.compile(r'\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|')
    
    scenes = []
    lines = content.splitlines()
    in_table = False
    
    for line in lines:
        if "时间" in line and "旁白" in line:
            in_table = True
            continue
        if in_table and line.strip().startswith("|") and not line.strip().startswith("|--"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 4:
                scene = {
                    "time": parts[0],
                    "visual_description": parts[1],
                    "narration": parts[2],
                    "subtitles": parts[3],
                    "camera_motion": parts[4] if len(parts) > 4 else "static"
                }
                scenes.append(scene)
        elif in_table and not line.strip().startswith("|"):
            in_table = False
            
    return scenes

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = parse_markdown_storyboard(sys.argv[1])
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print("Usage: python parse_storyboard.py <path_to_storyboard.md>")
