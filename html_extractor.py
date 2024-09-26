import pandas

from bs4 import BeautifulSoup as bs


html_files = [
    # Sumatra
    "aceh1.html",
    "aceh2.html",
    "bengkulu.html",
    "Kepulauan Riau.html",
    "Lampung1.html",
    "Lampung2.html",
    "Riau.html",
    "Sumatera Selatan.html",
    "Sumatera Utara.html",
    "Sumatra Barat.html",
    
    # Jawa
    "Banten.html",
    "Banten2.html",
    "Banten3.html",
    "Banten4.html",
    "Banten5.html",
    "Banten6.html",
    "Daerah Istimewa Yogyakarta1.html",
    "Daerah Istimewa Yogyakarta2.html",
    "jakarta1.html",
    "jakarta2.html",
    "jakarta3.html",
    "jakarta4.html",
    "jakarta5.html",
    "Jawa Barat1.html",
    "Jawa Barat2.html",
    "Jawa Barat3.html",
    "Jawa Barat4.html",
    "Jawa Barat5.html",
    "Jawa Barat6.html",
    "Jawa Barat7.html",
    "Jawa Tengah1.html",
    "Jawa Tengah2.html",
    "Jawa Timur1.html",
    "Jawa Timur2.html",
    "Jawa Timur3.html",
    "Jawa Timur4.html",
    "Jawa Timur5.html",
    
    # Bali
    "Bali1.html",
    "Bali2.html",
    
    # Kalimantan
    "Kalimantan Barat.html",
    "Kalimantan Selatan.html",
    "Kalimantan Tengah.html",
    "Kalimantan Timur.html",
    "Kalimantan Utara.html",
    
    # Sulawesi
    "Gorontalo.html",
    "Sulawesi Barat.html",
    "Sulawesi Selatan.html",
    "Sulawesi Tengah.html",
    "Sulawesi Tenggara1.html",
    "Sulawesi Tenggara2.html",
    "Sulawesi Utara.html",
    
    # NTB (Nusa Tenggara Barat)
    "Nusa Tenggara Barat.html",
    
    # NTT (Nusa Tenggara Timur)
    "Nusa Tenggara Timur.html",
    
    # Papua
    "Papua.html",
    "Papua barat.html"
]


# read list of dental in the html file
def extract_page(html_file):
    with open(html_file, "r") as f:
        html = f.read()
    soup = bs(html, "html.parser")
    
    dental_list = soup.find_all("div", "rllt__details")

    return dental_list

# extract data of each dental list
def get_dental_data(dental: bs):
    data = dental.find_all("div")
    data = [i.text for i in data]

    # remove empty items
    cleaned_data = [item for item in data if item]

    name = cleaned_data[0]

    # validate based on user request
    if 'dental lab' in name.lower():
        validation = "True"
    else:
        validation = "False"

    # separate address and phone number
    if '·' in cleaned_data[2]:
        address, telp_number = [part.strip() for part in cleaned_data[2].split('·')]
    else:
        address = cleaned_data[2]
        telp_number = ""

    result = {
        "nama": name,
        "alamat": address,
        "no. telp": telp_number,
        "valid": validation
    }

    return result

def main(html_files):
    result = []

    counter = len(html_files)

    # loop all html files
    for i, file in enumerate(html_files):
        dental_list = extract_page(file)
        print(f"{i+1}/{counter} | {file}")

        # loop each file
        for dental in dental_list:
            data = get_dental_data(dental)
            result.append(data)
            
        print(f"successfully extracted: {len(result)}")
    
    return result


if __name__ == "__main__":
    result = main(html_files)

    df = pandas.DataFrame(result)

    # set index from 1
    df.index = df.index + 1

    df.to_excel("dental.xlsx")
    print("successfully saved to 'dental.xlsx'")