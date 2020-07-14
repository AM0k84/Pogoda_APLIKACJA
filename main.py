from requests import get                 # metoda get z biblioteki requests sluzy do pobierania danych z jakiejs strony
from json import loads                   #  json sluzy do obslugi jsona a metoda loads obsluzy nam pobranego stringa
                                         # i zamieni na jsona w postaci slownika / listy slownikow
from terminaltables import AsciiTable    # pozwala nam na wyswietlenie jsona w formie tabelki (wiecej info w dokumentacji biblioteki)

cities = ["Katowice", "Kraków", "Warszawa"]         # lista w ktorej okreslam jakie miasta beda mnie interesowaly

# tutaj zgodnie z dokumentacja terminaltables tworze liste list z 'etykietami' tabelki
rows = [
    ["Data Pomiaru", "Miasto", "Godzina Pomiaru", "Temperatura"]
]

def main():
    url = "https://danepubliczne.imgw.pl/api/data/synop"  # do zmiennej przypisuje adres (dzieki api mozemy sie komunikować)

    # wysyłam zapytanie do serwera korzystajac z metody get z biblioteki requests
    # print(get(url))  # to wyprintuje tatus odpowiedzi serwera <Response [200]>
    # 2xx wszystko jest ok
    # 3xx przekierowanie
    # 4xx uzytkownik cos zepsul
    # 5xx cos nie dziala po stonie serwera

    response = get(url)               # odpowiedz serwera przypisana do zmiennej response

    # print(response.text)            # text uzyty na response pozwoli wyprintowac nam cala zawartosc w postaci stringa
    # print(loads(response.text))     # tutaj uzylismy loads z biblioteki json aby wyswietlic to jako liste slownikow

    json_dict = loads(response.text)  # przypisuje pobranego jsona z lista slownikow do zmiennej dict

    # for elem in json_dict:          # tutaj wypisuje sobie wszystkie slowniki
    #     print(elem)

    for elem in json_dict:              # tutaj iteruje po slowniku
        if elem["stacja"] in cities:    # i jesli klucz wystepuje w liscie miast
    # i moge np wypisac print(elem) lub stworzyc tabele za pomoca terminaltables
    #czyli dodaje do rows jako druga liste aby potem wyswietlic w tabeli
            rows.append([
                elem["data_pomiaru"],
                elem["stacja"],
                elem["godzina_pomiaru"],
                elem["temperatura"]
            ])
    # tworzę obiekt tabelki i jako argument przekazuje rows
    table = AsciiTable(rows)
    print(table.table)

if __name__ == "__main__":
    print(f"AKTUALNA POGODA 2020 by AM0k_(Lukasz_Chalinski)")
    main()