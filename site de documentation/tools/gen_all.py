# -*- coding: utf-8 -*-
"""Import all banks then write exos/*.md and js/exercises.js"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import gen_exos  # noqa: F401 — DATA + helpers
import gen_exos_ch2  # noqa: F401
import gen_exos_ch3  # noqa: F401
import gen_exos_ch4  # noqa: F401
import gen_exos_ch5  # noqa: F401
import gen_exos_ch6  # noqa: F401
import gen_exos_ch7_8  # noqa: F401
import gen_exos_ch9_10  # noqa: F401
import gen_exos_ch11_13  # noqa: F401

from gen_exos import DATA, EXOS, JS, dump_md


def dump_js():
    os.makedirs(os.path.dirname(JS), exist_ok=True)
    payload = {}
    for key, info in DATA.items():
        payload[key] = {
            "title": info["title"],
            "theoretical": info["theoretical"],
            "practical": info["practical"],
        }
        assert len(info["theoretical"]) == 20, (key, "theory", len(info["theoretical"]))
        assert len(info["practical"]) == 20, (key, "prac", len(info["practical"]))
    text = "window.EXERCISES = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"
    with open(JS, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    os.makedirs(EXOS, exist_ok=True)
    for key, info in DATA.items():
        dump_md(key, info)
        print("md", info["file"], len(info["theoretical"]), len(info["practical"]))
    dump_js()
    print("js", JS)
    print("chapters", list(DATA.keys()))


if __name__ == "__main__":
    main()
