import re

with open("app.py", "r", encoding="utf-8") as f:
    app_code = f.read()

# 1. Extract WOTD_LIST
wotd_match = re.search(r'WOTD_LIST = \[\n.*?\]\n', app_code, re.DOTALL)
wotd_code = wotd_match.group(0) if wotd_match else ""

# 2. Extract QUOTES
quotes_match = re.search(r'QUOTES = \[\n.*?\]\n', app_code, re.DOTALL)
quotes_code = quotes_match.group(0) if quotes_match else ""

# 3. Extract THEMES
themes_match = re.search(r'THEMES = \{\n.*?\}\n\n', app_code, re.DOTALL)
themes_code = themes_match.group(0) if themes_match else ""

# 4. Extract LOGIN_THEME
login_match = re.search(r'LOGIN_THEME = \{\n.*?\}\n', app_code, re.DOTALL)
login_code = login_match.group(0) if login_match else ""

config_code = f"\"\"\"Configuration data for Linguistix\"\"\"\n\n{wotd_code}\n{quotes_code}\n{themes_code}\n{login_code}\n"
with open("config.py", "w", encoding="utf-8") as f:
    f.write(config_code)

# 5. Extract CSS Block
css_match = re.search(r'st\.markdown\(f\"\"\"\n<style>\n.*?</style>\n\"\"\", unsafe_allow_html=True\)', app_code, re.DOTALL)
css_block = css_match.group(0) if css_match else ""

s1 = 'st.markdown(f\"\"\"'
s2 = '\"\"\", unsafe_allow_html=True)'
css_body = css_block.replace(s1, '').replace(s2, '')
ui_styles_code = f"def get_main_css(theme):\n    return f\"\"\"\n{css_body}\n\"\"\"\n"

with open("views/ui_styles.py", "w", encoding="utf-8") as f:
    f.write(ui_styles_code)

# Now, remove them from app.py and replace with imports
new_app_code = app_code.replace(wotd_code, "").replace(quotes_code, "").replace(themes_code, "").replace(login_code, "")

new_app_code = new_app_code.replace(css_block, "st.markdown(get_main_css(theme), unsafe_allow_html=True)")

# add imports at the top
imports = "from config import WOTD_LIST, QUOTES, THEMES, LOGIN_THEME\nfrom views.ui_styles import get_main_css\n"
new_app_code = imports + new_app_code

with open("app.py", "w", encoding="utf-8") as f:
    f.write(new_app_code)

print("Refactoring complete.")
