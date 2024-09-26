import requests
import pandas as pd

from fake_useragent import UserAgent as ua


provinsi_indonesia = [
    # Sumatra
    "Aceh",
    "Bengkulu",
    "Jambi",
    "Kepulauan Riau",
    "Lampung",
    "Riau",
    "Sumatra Barat",
    "Sumatra Selatan",
    "Sumatra Utara",
    # Jawa
    "Banten",
    "DKI Jakarta",
    "Jawa Barat",
    "Jawa Tengah",
    "Jawa Timur",
    "Daerah Istimewa Yogyakarta",
    # Kalimantan
    "Kalimantan Barat",
    "Kalimantan Tengah",
    "Kalimantan Selatan",
    "Kalimantan Timur",
    "Kalimantan Utara",
    # Sulawesi
    "Gorontalo",
    "Sulawesi Barat",
    "Sulawesi Selatan",
    "Sulawesi Tengah",
    "Sulawesi Tenggara",
    "Sulawesi Utara",
    # Bali
    "Bali",
    # NTB (Nusa Tenggara Barat)
    "Nusa Tenggara Barat",
    # NTT (Nusa Tenggara Timur)
    "Nusa Tenggara Timur",
    # Papua
    "Papua",
    "Papua Barat"
]

headers = {
    "User-Agent": ua().random
}
def get_page(url):
    response = requests.get(url)
    print(f"{response.status_code}: {url}")
    return response.text


if __name__ == "__main__":
    url = "https://www.google.com/maps/search/dental+lab+di+dki+jakarta"

    

    html = get_page(url)

    print(headers)
    with open("google.html", "w") as f:
        f.write(html)