# 1
account = {
    "id": 5681,
    "uid": "45f17b56-bcad-4933-8c73-a37aaa6863b9",
    "account_number": "6733198878",
    "iban": "GB79PNXF20678598570754",
    "bank_name": "AAC CAPITAL PARTNERS LIMITED",
    "routing_number": "007398728",
    "swift_bic": "AACCGB21",
}
print(len(account))


# 2
address = {
    "id": 7973,
    "uid": "42f2ce1d-90ab-4345-9595-0d9f42e6c085",
    "city": "East Monteland",
    "street_name": "Gusikowski Land",
    "street_address": "3230 Daugherty Centers",
    "secondary_address": "Apt. 562",
    "building_number": "58671",
    "mail_box": "PO Box 5313",
    "community": "Paradise Square",
    "zip_code": "58611",
    "zip": "01667",
    "postcode": "00563",
    "time_zone": "America/New_York",
    "street_suffix": "Burg",
    "city_suffix": "mouth",
    "city_prefix": "West",
    "state": "Wisconsin",
    "state_abbr": "NY",
    "country": "Mali",
    "country_code": "MH",
    "latitude": -56.97457993706476,
    "longitude": -104.29509072140858,
    "full_address": "Apt. 982 4820 Leena Rest, Lake Giannaville, MN 09265-3715",
}
for key in ("zip_code", "longitude", "post_code", "street_name", "number_house"):
    print(key in address)


# 3
currencies = {
    "Argentine Peso": 118362.205708,
    "Australian Dollar": 1586.232315,
    "Bahraini Dinar": 423.780164,
    "Botswana Pula": 13168.450636,
    "Brazilian Real": 5954.781483,
    "British Pound": 834.954104,
    "Bruneian Dollar": 1520.451015,
    "Bulgarian Lev": 1955.83,
    "Canadian Dollar": 1430.54405,
    "Chilean Peso": 898463.818465,
    "Chinese Yuan Renminbi": 7171.445692,
    "Colombian Peso": 4447741.922165,
    "Croatian Kuna": 7527.744707,
    "Czech Koruna": 24313.797041,
    "Danish Krone": 7440.613895,
    "Emirati Dirham": 4139.182587,
    "Hong Kong Dollar": 8786.255952,
    "Hungarian Forint": 355958.035747,
    "Icelandic Krona": 143603.932438,
    "Indian Rupee": 84241.767127,
    "Indonesian Rupiah": 16187150.010697,
    "Iranian Rial": 47534006.535121,
    "Israeli Shekel": 3569.191411,
    "Japanese Yen": 129149.364679,
    "Kazakhstani Tenge": 489292.515538,
    "Kuwaiti Dinar": 340.959682,
    "Libyan Dinar": 5196.539901,
    "Malaysian Ringgit": 4717.485104,
    "Mauritian Rupee": 49212.933037,
    "Mexican Peso": 23130.471272,
    "Nepalese Rupee": 134850.008728,
    "New Zealand Dollar": 1703.649473,
    "Norwegian Krone": 9953.078431,
    "Omani Rial": 433.360301,
    "Pakistani Rupee": 198900.635421,
    "Philippine Peso": 57574.278782,
    "Polish Zloty": 4579.273862,
    "Qatari Riyal": 4102.552652,
    "Romanian New Leu": 4946.638369,
    "Russian Ruble": 86197.012666,
    "Saudi Arabian Riyal": 4226.530892,
    "Singapore Dollar": 1520.451015,
    "South African Rand": 17159.831129,
    "South Korean Won": 1355490.097163,
    "Sri Lankan Rupee": 228245.645722,
    "Swedish Krona": 10439.125427,
    "Swiss Franc": 1037.792217,
    "Taiwan New Dollar": 31334.286611,
    "Thai Baht": 37436.518169,
    "Trinidadian Dollar": 7636.35428,
    "Turkish Lira": 15078.75981,
    "US Dollar": 1127.074905,
    "Venezuelan Bolivar": 511082584.868731,
}
if (currency := input()) in currencies:
    print(currencies[currency])
else:
    print(f"Нет данных по {currency}")


# 4
account = {
    "id": 3136,
    "uid": "1359acc6-f07a-4a2a-984e-3fb809982948",
    "account_number": "0847799459",
    "iban": "GB90XTND56373623909314",
    "bank_name": "ABN AMRO HOARE GOVETT CORPORATE FINANCE LTD.",
    "routing_number": "126602476",
    "swift_bic": "BCYPGB2LHGB",
}
keys = list(account)
print(keys)


# 5
d1 = {"India": "Delhi", "Canada": "Ottawa", "United States": "Washington D. C."}
d2 = {"France": "Paris", "Malaysia": "Kuala Lumpur"}
capitals = d1 | d2
print(capitals)
