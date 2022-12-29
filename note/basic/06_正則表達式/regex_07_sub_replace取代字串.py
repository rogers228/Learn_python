def update_devmode():
    # re.sub(pattern, replacement, string, count=0, flags=0)

    with open(FULLNAME_BASE_HTML, "r", encoding='utf-8') as f:
        source = f.read()
    # print(source)
    devmode = 'all.min' if DEVELOPMENT else 'all'
    # print(devmode)
    html =  re.sub(r"javascript\/(.+)\.js\?version", 
        f'javascript/{devmode}.js?version', 
        source, count=1, flags=0)
    # print(html)

    with open(FULLNAME_BASE_HTML, "w", encoding='utf-8') as f:
        f.write(html)