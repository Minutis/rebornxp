import requests

porta_npc_id = 20943


def fetch_npc_html(npc_id: int) -> str:
    request = requests.get(f"https://interlude.wiki/db/npc/{npc_id}.html")
    return request.text


def parse_xp(html: str) -> int:
    xp_index = html.find("Exp:")

    xp = html[xp_index:]
    xp = xp.split(",")[0].replace("Exp: ", "")
    return int(xp)


def parse_hp(html: str) -> int:
    hp_index = html.find("HP:")

    hp = html[hp_index:]
    hp = hp.split(",")[0].replace("HP: ", "")
    return int(hp)


def parse_hp_ratio(html: str) -> float:
    has_ratio = html.find("HP Increase")

    if not has_ratio:
        return 1

    ratio = html[has_ratio:]
    open_pos = ratio.find("(") + 1
    close_pos = ratio.find(")")
    ratio = eval(ratio[open_pos:close_pos].replace("x", ""))

    return ratio


def calculate_ratio(xp: int, hp: int, hp_ratio: float) -> float:
    return xp / (hp * hp_ratio)


def run() -> None:
    html = fetch_npc_html(porta_npc_id)
    xp = parse_xp(html)
    hp = parse_hp(html)
    hp_ratio = parse_hp_ratio(html)
    ratio = calculate_ratio(xp, hp, hp_ratio)
    print(ratio)


run()
