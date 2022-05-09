def getLegalIdForGivenMarketPlaceId(marketPlaceId):
    return marketPlaceIDtoLegalId[marketPlaceId]


marketPlaceIDtoLegalId = {
    1: 101,
    3: 102,
    4: 103,
    5: 108,
    6: 109,
    7: 115,
    3240: '-',
    35691: 129,
    44571: 131,
    44551: 130,
    111172: 135,
    328451: '-',
    338801: '-',
    338851: '-',
    771770: 133,
    526970: 132,
    104444012: '-',
    338811: '-',
    704403121: 'NULL'
}