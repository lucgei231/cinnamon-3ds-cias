import qrcode

URLS = {
    "qr-undertale.png": "https://raw.githubusercontent.com/lucgei231/cinnamon-3ds-cias/main/undertale-3ds.cia",
    "qr-deltarune.png": "https://raw.githubusercontent.com/lucgei231/cinnamon-3ds-cias/main/deltarune-3ds.cia",
}

for name, url in URLS.items():
    img = qrcode.make(url, box_size=12, border=2)
    img.save(name)
    print(f"{name} <- {url}")
