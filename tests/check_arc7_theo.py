"""Contrôles ciblés : python tests/check_arc7_theo.py (sans SDK Ren'Py)."""

import ast
from pathlib import Path
import re
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "game/arcs/arc_7/arc_7_theo.rpy").read_text(encoding="utf-8-sig")
expected = {"kung_pow", "film_reporte", "apres_million"}
blocks = re.findall(
    r'^    if (renpy\.loadable\("(images/scenes/cg/theo/arc7_theo_[^"]+)"\)):\n'
    r'        scene expression ([^\n]+)\n'
    r'    else:\n((?:        show [^\n]+\n)+)    with dissolve',
    source,
    re.MULTILINE,
)
assert len(blocks) == 3, "Trois CG facultatives avec un repli explicite sont attendues"
assert {Path(path).stem.removeprefix("arc7_theo_") for _, path, _, _ in blocks} == expected

for condition, path, expression, fallback in blocks:
    for available in (False, True):
        renpy = SimpleNamespace(loadable=lambda candidate: available and candidate == path)
        im = SimpleNamespace(Scale=lambda *args: args)
        if eval(condition, {"renpy": renpy}):
            assert eval(expression, {"im": im}) == (path, 1920, 1080)
        else:
            assert "show ilona " in fallback, "Ilona doit rester visible sans CG"
            if not path.endswith("apres_million.jpg"):
                assert "show theo " in fallback, "Le couple doit rester visible sans CG"
        assert bool(eval(condition, {"renpy": renpy})) == available

flashback = source.split('systeme "Avant ce soir du 6 décembre,', 1)[1]
flashback = flashback.split('systeme "Retour au 6 décembre,', 1)[0]
assert "show ilona tokyo neutral" in flashback
assert "show ilona short" not in flashback, "Pas de cheveux courts en août/octobre"
assert len(re.findall(r"^    menu:", source, re.MULTILINE)) == 1
choices = re.findall(r'^        (".*"):$', source, re.MULTILINE)
assert [ast.literal_eval(choice) for choice in choices] == [
    "Proposer de décaler les sponsors et d'annuler le live.",
    "Maintenir le live, alléger le reste.",
]
assert re.findall(r"^            jump (\w+)$", source, re.MULTILINE) == [
    "ending_neutre", "bad_ending",
]
print("OK : CG présentes/absentes, coiffure des flashbacks, menu et destinations.")
