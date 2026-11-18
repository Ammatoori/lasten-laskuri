from pathlib import Path

root = Path("_site")
index = root / "index.html"
app = root / "app.js"
sw = root / "sw.js"

html = index.read_text(encoding="utf-8")
field = '<label class="field">Hae tai valitse lääke<input id="search" type="search" placeholder="Hae lääkkeen nimellä..." autocomplete="off"></label>'
assert field in html, "Search field not found in HTML"
index.write_text(html.replace(field, ""), encoding="utf-8")

js = app.read_text(encoding="utf-8")
old = "const q=$('search').value.toLocaleLowerCase('fi').trim();"
assert old in js, "Search handling not found"
js = js.replace(old, "")
old = "&&d.name.toLocaleLowerCase('fi').includes(q)"
assert old in js, "Search filter not found"
js = js.replace(old, "")
old = "$('search').addEventListener('input',selectDrug);"
assert old in js, "Search listener not found"
js = js.replace(old, "")
app.write_text(js, encoding="utf-8")

service_worker = sw.read_text(encoding="utf-8")
assert "lasten-laakelaskuri-v01" in service_worker
sw.write_text(service_worker.replace("lasten-laakelaskuri-v01", "lasten-laakelaskuri-v02"), encoding="utf-8")
