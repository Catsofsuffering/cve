import os
import yaml

# 设置项目根目录和输出文件路径
root_dir = "."
output_file = "mkdocs.yml"

# 基本的 mkdocs 配置信息
config = {
    "site_name": "CVE Documentation",
    "site_description": "A documentation site for CVEs from 1999 to 2024.",
    "site_author": "Peony",
    "site_url": "https://peonycsa.com/cve",
    "repo_url": "https://github.com/Catsofsuffering/cve",
    "repo_name": "cve",
    "theme": {
        "name": "material",
        "palette": {
            "scheme": "default",
            "primary": "indigo",
            "accent": "indigo"
        },
        "features": [
            "navigation.tabs",
            "search.highlight",
            "toc.integrate"
        ],
        "language": "en"
    },
    "markdown_extensions": [
        {"toc": {"permalink": True}},
        "footnotes",
        "codehilite",
        "admonition"
    ],
    "plugins": [
        "search"
    ],
    "extra_css": [
        "stylesheets/extra.css"
    ],
    "extra_javascript": [
        "https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"
    ],
    "nav": [
        {"Home": "index.md"}
    ]
}

# 遍历 1999 到 2024 的年份文件夹并生成导航结构
years = list(range(1999, 2025))
for year in years:
    year_dir = os.path.join(root_dir, str(year))
    if os.path.isdir(year_dir):
        year_nav = []
        # 遍历年份文件夹中的 Markdown 文件
        for md_file in sorted(os.listdir(year_dir)):
            if md_file.endswith(".md"):
                file_name = os.path.splitext(md_file)[0]
                # 添加到该年份的导航条目
                year_nav.append({file_name.replace('_', ' ').title(): f"{year}/{md_file}"})
        
        # 如果该年份有 Markdown 文件，添加到主导航中
        if year_nav:
            config["nav"].append({str(year): year_nav})

# 将生成的配置写入 mkdocs.yml 文件
with open(output_file, "w", encoding="utf-8") as f:
    yaml.dump(config, f, allow_unicode=True, sort_keys=False)

print(f"Generated {output_file} successfully.")
