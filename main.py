from requests import get
from json import loads
from terminaltables import AsciiTable

CITIES = ['Gdańsk', 'Warszawa']

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    # print(response.text)
    # print(loads(response.text))
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Ciśnienie']
    ]
    for row in loads(response.text):
        if row['stacja'] in CITIES:
            # print(row)
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie'],
            ])
    table = AsciiTable(rows)
    print(table.table)

    pass

if __name__ == '__main__':
    print('Pogodynka 2020')
    main()