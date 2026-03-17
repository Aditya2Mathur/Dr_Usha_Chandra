import os
import re

base_dir = r"e:\WebsiteProject(2026)\VarnikaHealthcare"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Determine prefix for relative paths
            rel_path = "" if root == base_dir else "../"
            
            # Find the <ul> under Quick Link
            pattern = r'(<h3[^>]*>.*?Quick Link.*?</h3>\s*<ul[^>]*>)(.*?)(</ul>)'
            
            def replacer(match):
                inner_html = match.group(2)
                if "Skin Clinic Sitapur" not in inner_html:
                    # Append location links with correct relative path
                    addition = f"""
                            <li style="margin-bottom: 12px;"><a href="{rel_path}sitapur/index.html"
                                    style="color: inherit; text-decoration: none;">Skin Clinic Sitapur</a></li>
                            <li style="margin-bottom: 12px;"><a href="{rel_path}shahjahanpur/index.html"
                                    style="color: inherit; text-decoration: none;">Skin Clinic Shahjahanpur</a></li>"""
                    # For subpages, the </ul> indentation might need to be preserved, but adding before </ul> is fine.
                    return match.group(1) + inner_html + addition + "\n                        " + match.group(3)
                return match.group(0)
        
            new_content = re.sub(pattern, replacer, content, flags=re.DOTALL | re.IGNORECASE)
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated footer in {path}")

print("All footers updated with internal linking.")
