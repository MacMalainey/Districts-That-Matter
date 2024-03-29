'''
'K'onstants for parsing and identifying data within the Canadian 2021 Census dataset

This is just a general combination of the fields, indentifiers, and formats required to parse the data for out use case.
Not all data in this document may be necessary as per record there tends to be multiple ways to identify different pieces of data.
However, for completeness and documentation sake we provide the means to easily utilize any method a developer may wish to use BUT NOT ALL DATA.

Fulfills FR25
'''
import re

class K_DATA_FIELDS:
    '''
    Indices for each data field
    '''
    CENSUS_YEAR = 0
    DGUID = 1
    ALT_GEO_CODE = 2
    GEO_LEVEL = 3
    GEO_NAME = 4
    TNR_SF = 5
    TNR_LF = 6
    DATA_QUALITY_FLAG = 7
    CHARACTERISTIC_ID = 8
    CHARACTERISTIC_NAME = 9
    CHARACTERISTIC_NOTE = 10
    C1_COUNT_TOTAL = 11
    C1_SYMBOL = 12
    C2_COUNT_MEN = 13
    C2_SYMBOL = 14
    C3_COUNT_WOMEN = 15
    C3_SYMBOL = 16
    C10_RATE_TOTAL = 17
    C10_SYMBOL = 18
    C11_RATE_MEN = 19
    C11_SYMBOL = 20
    C12_RATE_WOMEN = 21
    C12_SYMBOL = 22

    HEADER_FIELDS = [
        "CENSUS_YEAR",
        "DGUID",
        "ALT_GEO_CODE",
        "GEO_LEVEL",
        "GEO_NAME",
        "TNR_SF",
        "TNR_LF",
        "DATA_QUALITY_FLAG",
        "CHARACTERISTIC_ID",
        "CHARACTERISTIC_NAME",
        "CHARACTERISTIC_NOTE",
        "C1_COUNT_TOTAL",
        "SYMBOL",
        "C2_COUNT_MEN+",
        "SYMBOL",
        "C3_COUNT_WOMEN+",
        "SYMBOL",
        "C10_RATE_TOTAL",
        "SYMBOL",
        "C11_RATE_MEN+",
        "SYMBOL",
        "C12_RATE_WOMEN+",
        "SYMBOL",
    ]

class K_GEO_LEVELS:
    '''
    Geographic level specifiers
    '''
    DA = "Dissemination area"
    CSD = "Census subdivision"


class K_DGUID_TYPES:
    '''
    Region type code as found in a region's DGUID
    '''
    ADMINISTRATIVE = 'A'
    STATISTICAL = 'S'

class K_DGUID_SCHEMAS:
    '''
    Region schema code as found in a region's DGUID
    '''
    DA = "0512" # Dissemination Area
    CS = "0005" # Census Subdivision

K_DGUID_FORMAT = re.compile(r"^(\d{4})(A|S)(\d{4})(\d{1,12})$")
'''
DGUID format for parsing
Format: VVVVTSSSSGGGGGGGGGGGG

V - Vintage (year)
T - Type
S - Schema (specific type)
G - Unique ID (1-12 chars)

References
- https://www150.statcan.gc.ca/n1/pub/92f0138m/92f0138m2019001-eng.htm
- https://www12.statcan.gc.ca/census-recensement/2021/ref/dict/az/Definition-eng.cfm?ID=geo055
'''

K_DA_ID_FORMAT = re.compile(r"^(\d{2})(\d{2})(\d{4})")
'''
DA ID format for parsing
Format: PPDDUUUU

P - Province Code
D - District Code
U - Unique ID for province and district

References
- https://www12.statcan.gc.ca/census-recensement/2021/ref/dict/az/definition-eng.cfm?ID=geo021
'''

K_DATA_CHARACTERISTIC_IDS = [
    1,      # Population, 2021 (1)
    2,      # Population, 2016 (1)
    3,      # Population percentage change, 2016 to 2021
    4,      # Total private dwellings (2)
    5,      # Private dwellings occupied by usual residents (3)
    6,      # Population density per square kilometre
    7,      # Land area in square kilometres
    8,      # Total - Age groups of the population - 100% data
    9,      #   0 to 14 years
    10,     #	    0 to 4 years
    11,     #	    5 to 9 years
    12,     #	    10 to 14 years
    13,     #	  15 to 64 years
    14,     #	    15 to 19 years
    15,     #	    20 to 24 years
    16,     #	    25 to 29 years
    17,     #	    30 to 34 years
    18,     #	    35 to 39 years
    19,     #	    40 to 44 years
    20,     #	    45 to 49 years
    21,     #	    50 to 54 years
    22,     #	    55 to 59 years
    23,     #	    60 to 64 years
    24,     #	  65 years and over
    25,     #	    65 to 69 years
    26,     #	    70 to 74 years
    27,     #	    75 to 79 years
    28,     #	    80 to 84 years
    29,     #	    85 years and over
    30,     #	      85 to 89 years
    31,     #	      90 to 94 years
    32,     #	      95 to 99 years
    33,     #	      100 years and over
    34,     #	Total - Distribution (%) of the population by broad age groups - 100% data
    35,     #	  0 to 14 years
    36,     #	  15 to 64 years
    37,     #	  65 years and over
    38,     #	    85 years and over
    39,     #	Average age of the population
    40,     #	Median age of the population
    41,     #	Total - Occupied private dwellings by structural type of dwelling - 100% data
    42,     #	  Single-detached house
    43,     #	  Semi-detached house
    44,     #	  Row house
    45,     #	  Apartment or flat in a duplex
    46,     #	  Apartment in a building that has fewer than five storeys
    47,     #	  Apartment in a building that has five or more storeys
    48,     #	  Other single-attached house
    49,     #	  Movable dwelling (4)
    50,     #	Total - Private households by household size - 100% data
    51,     #	  1 person
    52,     #	  2 persons
    53,     #	  3 persons
    54,     #	  4 persons
    55,     #	  5 or more persons
    56,     #	Number of persons in private households
    57,     #	Average household size
    58,     #	Total - Marital status for the total population aged 15 years and over - 100% data
    59,     #	  Married or living common-law
    60,     #	    Married
    61,     #	    Living common-law
    62,     #	      Living common law - Never married
    63,     #	      Living common law - Separated
    64,     #	      Living common law - Divorced
    65,     #	      Living common law - Widowed
    66,     #	  Not married and not living common-law
    67,     #	    Not married and not living common law - Never married
    68,     #	    Not married and not living common law - Separated
    69,     #	    Not married and not living common law - Divorced
    70,     #	    Not married and not living common law - Widowed
    71,     #	Total - Census families in private households by family size - 100% data (5)
    72,     #	  2 persons
    73,     #	  3 persons
    74,     #	  4 persons
    75,     #	  5 or more persons
    76,     #	Average size of census families
    77,     #	Average number of children in census families with children (6)
    78,     #	Total number of census families in private households - 100% data
    79,     #	  Total couple families
    80,     #	    Married couples
    81,     #	      With children (6)
    82,     #	      Without children
    83,     #	    Common-law couples
    84,     #	      With children (6)
    85,     #	      Without children
    86,     #	  Total one-parent families
    87,     #	    in which the parent is a woman+
    88,     #	    in which the parent is a man+
    89,     #	Total - Persons in private households - 100% data
    90,     #	  Total - Persons in census families
    91,     #	    Married spouses or common-law partners
    92,     #	    Parents in one-parent families
    93,     #	    Children (6)
    94,     #	      In a two-parent family
    95,     #	      In a one-parent family
    96,     #	  Total - Persons not in census families in private households - 100% data
    97,     #	    Living alone
    98,     #	    Living with other relatives (7)
    99,     #	    Living with non-relatives only
    100,    #	Total - Household type - 100% data
    101,    #	  One-census-family households without additional persons
    102,    #	    Couple-family households
    103,    #	      With children (6)
    104,    #	      Without children
    105,    #	    One-parent-family households
    106,    #	  Multigenerational households (8)
    107,    #	  Multiple-census-family households (9)
    108,    #	  One-census-family households with additional persons (9)
    109,    #	  Two-or-more-person non-census-family households 
    110,    #	  One-person households
    111,    #	Total - Income statistics in 2020 for the population aged 15 years and over in private households - 100% data (10)
    112,    #	  Number of total income recipients aged 15 years and over in private households in 2020 - 100% data
    113,    #	    Median total income in 2020 among recipients ($)
    114,    #	  Number of after-tax income recipients aged 15 years and over in private households in 2020 - 100% data
    115,    #	    Median after-tax income in 2020 among recipients ($)
    116,    #	  Number of market income recipients aged 15 years and over in private households in 2020 - 100% data
    117,    #	    Median market income in 2020 among recipients ($)
    118,    #	  Number of employment income recipients aged 15 years and over in private households in 2020 - 100% data
    119,    #	    Median employment income in 2020 among recipients ($)
    120,    #	  Number of government transfers recipients aged 15 years and over in private households in 2020 - 100% data
    121,    #	    Median government transfers in 2020 among recipients ($)
    122,    #	  Number of employment insurance benefits recipients aged 15 years and over in private households in 2020 - 100% data
    123,    #	    Median employment insurance benefits in 2020 among recipients ($)
    124,    #	  Number of COVID-19 emergency and recovery benefits recipients aged 15 years and over in private households in 2020 - 100% data
    125,    #	    Median COVID-19 emergency and recovery benefits in 2020 among recipients ($)
    126,    #	Total - Income statistics in 2020 for the population aged 15 years and over in private households - 25% sample data (11)
    127,    #	  Number of total income recipients aged 15 years and over in private households in 2020 - 25% sample data
    128,    #	    Average total income in 2020 among recipients ($)
    129,    #	  Number of after-tax income recipients aged 15 years and over in private households in 2020 - 25% sample data
    130,    #	    Average after-tax income in 2020 among recipients ($)
    131,    #	  Number of market income recipients aged 15 years and over in private households in 2020 - 25% sample data
    132,    #	    Average market income in 2020 among recipients ($)
    133,    #	  Number of employment income recipients aged 15 years and over in private households in 2020 - 25% sample data
    134,    #	    Average employment income in 2020 among recipients ($)
    135,    #	  Number of government transfers recipients aged 15 years and over in private households in 2020 - 25% sample data
    136,    #	    Average government transfers in 2020 among recipients ($)
    137,    #	  Number of employment insurance benefits recipients aged 15 years and over in private households in 2020 - 25% sample data
    138,    #	    Average employment insurance benefits in 2020 among recipients ($)
    139,    #	  Number of COVID-19 emergency and recovery benefits recipients aged 15 years and over in private households in 2020 - 25% sample data
    140,    #	    Average COVID-19 emergency and recovery benefits in 2020 among recipients ($)
    141,    #	Total - Employment income statistics in 2020 for the population aged 15 years and over in private households - 25% sample data (12)
    142,    #	  Number of employment income recipients in 2020 who worked full-year full-time in 2020 - 25% sample data (13)
    143,    #	    Median employment income in 2020 for full-year full-time workers in 2020 ($) (14)
    144,    #	    Average employment income in 2020 for full-year full-time workers in 2020 ($) (15)
    145,    #	  Number of employment income recipients in 2020 who worked part-year or part-time in 2020 - 25% sample data (16)
    146,    #	    Median employment income in 2020 of those who worked part-year or part-time in 2020 ($)
    147,    #	    Average employment income in 2020 of those who worked part-year or part-time in 2020 ($)
    148,    #	Composition of total income in 2020 of the population aged 15 years and over in private households (%) - 25% sample data (17)
    149,    #	  Market income (%) (18)
    150,    #	    Employment income (%) (19)
    151,    #	  Government transfers (%) (20)
    152,    #	    Employment insurance benefits (%)
    153,    #	    COVID-19 - Government income support and benefits (%)
    154,    #	      COVID-19 - Emergency and recovery benefits (%)
    155,    #	Total - Total income groups in 2020 for the population aged 15 years and over in private households - 100% data (21)
    156,    #	  Without total income
    157,    #	  With total income
    158,    #	    Under $10,000 (including loss)
    159,    #	    $10,000 to $19,999
    160,    #	    $20,000 to $29,999
    161,    #	    $30,000 to $39,999
    162,    #	    $40,000 to $49,999
    163,    #	    $50,000 to $59,999
    164,    #	    $60,000 to $69,999
    165,    #	    $70,000 to $79,999
    166,    #	    $80,000 to $89,999
    167,    #	    $90,000 to $99,999
    168,    #	    $100,000 and over
    169,    #	      $100,000 to $149,999
    170,    #	      $150,000 and over
    171,    #	Total - After-tax income groups in 2020 for the population aged 15 years and over in private households - 100% data (22)
    172,    #	  Without after-tax income
    173,    #	  With after-tax income
    174,    #	    Under $10,000 (including loss)
    175,    #	    $10,000 to $19,999
    176,    #	    $20,000 to $29,999
    177,    #	    $30,000 to $39,999
    178,    #	    $40,000 to $49,999
    179,    #	    $50,000 to $59,999
    180,    #	    $60,000 to $69,999
    181,    #	    $70,000 to $79,999
    182,    #	    $80,000 to $89,999
    183,    #	    $90,000 to $99,999
    184,    #	    $100,000 and over
    185,    #	      $100,000 to $124,999
    186,    #	      $125,000 and over
    187,    #	Total - Employment income groups in 2020 for the population aged 15 years and over in private households - 100% data (19)
    188,    #	  Without employment income
    189,    #	  With employment income
    190,    #	    Under $5,000 (including loss)
    191,    #	    $5,000 to $9,999
    192,    #	    $10,000 to $19,999
    193,    #	    $20,000 to $29,999
    194,    #	    $30,000 to $39,999
    195,    #	    $40,000 to $49,999
    196,    #	    $50,000 to $59,999
    197,    #	    $60,000 to $69,999
    198,    #	    $70,000 to $79,999
    199,    #	    $80,000 to $89,999
    200,    #	    $90,000 to $99,999
    201,    #	    $100,000 and over
    202,    #	      $100,000 to $124,999
    203,    #	      $125,000 and over
    204,    #	Total - Income statistics in 2019 for the population aged 15 years and over in private households - 100% data (23)
    205,    #	  Number of total income recipients aged 15 years and over in private households in 2019 - 100% data
    206,    #	    Median total income in 2019 among recipients ($)
    207,    #	  Number of after-tax income recipients aged 15 years and over in private households in 2019 - 100% data
    208,    #	    Median after-tax income in 2019 among recipients ($)
    209,    #	  Number of market income recipients aged 15 years and over in private households in 2019 - 100% data
    210,    #	    Median market income in 2019 among recipients ($)
    211,    #	  Number of employment income recipients aged 15 years and over in private households in 2019 - 100% data
    212,    #	    Median employment income in 2019 among recipients ($)
    213,    #	  Number of government transfers recipients aged 15 years and over in private households in 2019 - 100% data
    214,    #	    Median government transfers in 2019 among recipients ($)
    215,    #	  Number of employment insurance benefits recipients aged 15 years and over in private households in 2019 -100% data
    216,    #	    Median employment insurance benefits in 2019 among recipients ($)
    217,    #	Total - Income statistics in 2019 for the population aged 15 years and over in private households - 25% sample data (24)
    218,    #	  Number of total income recipients aged 15 years and over in private households in 2019 - 25% sample data
    219,    #	    Average total income in 2019 among recipients ($)
    220,    #	  Number of after-tax income recipients aged 15 years and over in private households in 2019 - 25% sample data
    221,    #	    Average after-tax income in 2019 among recipients ($)
    222,    #	  Number of market income recipients aged 15 years and over in private households in 2019 - 25% sample data
    223,    #	    Average market income in 2019 among recipients ($)
    224,    #	  Number of employment income recipients aged 15 years and over in private households in 2019 - 25% sample data
    225,    #	    Average employment income in 2019 among recipients ($)
    226,    #	  Number of government transfers recipients aged 15 years and over in private households in 2019 - 25% sample data
    227,    #	    Average government transfers in 2019 among recipients ($)
    228,    #	  Number of employment insurance benefits recipients aged 15 years and over in private households in 2019 - 25% sample data
    229,    #	    Average employment insurance benefits in 2019 among recipients ($)
    230,    #	Total - Employment income statistics in 2019 for the population aged 15 years and over in private households - 25% sample data (25)
    231,    #	  Number of employment income recipients in 2019 who worked full-year full-time in 2020 - 25% sample data (13)
    232,    #	    Median employment income in 2019 for full-year full-time workers in 2020 ($) (14)
    233,    #	    Average employment income in 2019 for full-year full-time workers in 2020 ($) (15)
    234,    #	  Number of employment income recipients in 2019 who worked part-year or part-time in 2020 - 25% sample data (16)
    235,    #	    Median employment income in 2019 of those who worked part-year or part-time in 2020 ($)
    236,    #	    Average employment income in 2019 of those who worked part-year or part-time in 2020 ($)
    237,    #	Composition of total income in 2019 of the population aged 15 years and over in private households (%) - 25% sample data
    238,    #	  Market income (%)
    239,    #	    Employment income (%)
    240,    #	  Government transfers (%)
    241,    #	    Employment insurance benefits (%)
    242,    #	Total - Income statistics for private households - 100% data (26)
    243,    #	  Median total income of household in 2020 ($)
    244,    #	  Median after-tax income of household in 2020 ($)
    245,    #	    Total - Income statistics for one-person private households - 100% data
    246,    #	      Median total income of one-person households in 2020 ($)
    247,    #	      Median after-tax income of one-person households in 2020 ($)
    248,    #	    Total - Income statistics for two-or-more-persons private households - 100% data
    249,    #	      Median total income of two-or-more-person households in 2020 ($)
    250,    #	      Median after-tax income of two-or-more-person households in 2020 ($)
    251,    #	Total - Income statistics for private households - 25% sample data (27)
    252,    #	  Average total income of household in 2020 ($)
    253,    #	  Average after-tax income of household in 2020 ($)
    254,    #	    Total - Income statistics for one-person private households - 25% sample data
    255,    #	      Average total income of one-person households in 2020 ($)
    256,    #	      Average after-tax income of one-person households in 2020 ($)
    257,    #	    Total - Income statistics for two-or-more-persons private households - 25% sample data
    258,    #	      Average total income of two-or-more-person households in 2020 ($)
    259,    #	      Average after-tax income of two-or-more-person households in 2020 ($)
    260,    #	Total - Household total income groups in 2020 for private households - 100% data (21)
    261,    #	  Under $5,000
    262,    #	  $5,000 to $9,999
    263,    #	  $10,000 to $14,999
    264,    #	  $15,000 to $19,999
    265,    #	  $20,000 to $24,999
    266,    #	  $25,000 to $29,999
    267,    #	  $30,000 to $34,999
    268,    #	  $35,000 to $39,999
    269,    #	  $40,000 to $44,999
    270,    #	  $45,000 to $49,999
    271,    #	  $50,000 to $59,999
    272,    #	  $60,000 to $69,999
    273,    #	  $70,000 to $79,999
    274,    #	  $80,000 to $89,999
    275,    #	  $90,000 to $99,999
    276,    #	  $100,000 and over
    277,    #	    $100,000 to $124,999
    278,    #	    $125,000 to $149,999
    279,    #	    $150,000 to $199,999
    280,    #	    $200,000 and over
    281,    #	Total - Household after-tax income groups in 2020 for private households - 100% data (22)
    282,    #	  Under $5,000
    283,    #	  $5,000 to $9,999
    284,    #	  $10,000 to $14,999
    285,    #	  $15,000 to $19,999
    286,    #	  $20,000 to $24,999
    287,    #	  $25,000 to $29,999
    288,    #	  $30,000 to $34,999
    289,    #	  $35,000 to $39,999
    290,    #	  $40,000 to $44,999
    291,    #	  $45,000 to $49,999
    292,    #	  $50,000 to $59,999
    293,    #	  $60,000 to $69,999
    294,    #	  $70,000 to $79,999
    295,    #	  $80,000 to $89,999
    296,    #	  $90,000 to $99,999
    297,    #	  $100,000 and over
    298,    #	    $100,000 to $124,999
    299,    #	    $125,000 to $149,999
    300,    #	    $150,000 and over
    301,    #	Total - Income statistics for economic families in private households - 100% data (28)
    302,    #	  Median total income of economic family in 2020 ($)
    303,    #	  Median after-tax income of economic family in 2020 ($)
    304,    #	  Average family size of economic families
    305,    #	Total - Income statistics for couple-only economic families in private households - 100% data
    306,    #	  Median total income of couple-only economic families in 2020 ($)
    307,    #	  Median after-tax income of couple-only economic families in 2020 ($)
    308,    #	  Average family size of couple-only economic families
    309,    #	Total - Income statistics for couple-with-children economic families in private households - 100% data
    310,    #	  Median total income of couple-with-children economic families  in 2020 ($)
    311,    #	  Median after-tax income of couple-with-children economic families in 2020 ($)
    312,    #	  Average family size of couple-with-children economic families
    313,    #	Total - Income statistics for one-parent economic families in private households - 100% data
    314,    #	  Median total income of one-parent economic families in 2020 ($)
    315,    #	  Median after-tax income of one-parent economic families in 2020 ($)
    316,    #	  Average family size of one-parent economic families
    317,    #	Total - Income statistics for persons aged 15 years and over not in economic families in private households - 100% data (29)
    318,    #	  Median total income in 2020 ($) (30)
    319,    #	  Median after-tax income in 2020 ($) (30)
    320,    #	Total - Income statistics for economic families in private households - 25% sample data (31)
    321,    #	  Average total income of economic family in 2020 ($)
    322,    #	  Average after-tax income of economic family in 2020 ($)
    323,    #	Total - Income statistics for couple-only economic families in private households - 25% sample data
    324,    #	  Average total income of couple-only economic families in 2020 ($)
    325,    #	  Average after-tax income of couple-only economic families in 2020 ($)
    326,    #	Total - Income statistics for couple-with-children economic families in private households - 25% sample data
    327,    #	  Average total income of couple-with-children economic families in 2020 ($)
    328,    #	  Average after-tax income of couple-with-children economic families in 2020 ($)
    329,    #	Total - Income statistics for one-parent economic families in private households - 25% sample data
    330,    #	  Average total income of one-parent economic families in 2020 ($)
    331,    #	  Average after-tax income of one-parent economic families in 2020 ($)
    332,    #	Total - Income statistics for persons aged 15 years and over not in economic families in private households - 25% sample data (32)
    333,    #	  Average total income in 2020 ($) (30)
    334,    #	  Average after-tax income in 2020 ($) (30)
    335,    #	Total - LIM low-income status in 2020 for the population in private households - 100% data (33)
    336,    #	  0 to 17 years
    337,    #	    0 to 5 years
    338,    #	  18 to 64 years
    339,    #	  65 years and over
    340,    #	In low income based on the Low-income measure, after tax (LIM-AT)
    341,    #	  0 to 17 years
    342,    #	    0 to 5 years
    343,    #	  18 to 64 years
    344,    #	  65 years and over
    345,    #	Prevalence of low income based on the Low-income measure, after tax (LIM-AT) (%)
    346,    #	  0 to 17 years (%)
    347,    #	    0 to 5 years (%)
    348,    #	  18 to 64 years (%)
    349,    #	  65 years and over (%)
    350,    #	Total - LICO low-income status in 2020 for the population in private households to whom the low-income concept is applicable - 100% data (33)
    351,    #	  0 to 17 years
    352,    #	    0 to 5 years
    353,    #	  18 to 64 years
    354,    #	  65 years and over
    355,    #	In low income based on the Low-income cut-offs, after tax (LICO-AT)
    356,    #	  0 to 17 years
    357,    #	    0 to 5 years
    358,    #	  18 to 64 years
    359,    #	  65 years and over
    360,    #	Prevalence of low income based on the Low-income cut-offs, after tax (LICO-AT) (%)
    361,    #	  0 to 17 years (%)
    362,    #	    0 to 5 years (%)
    363,    #	  18 to 64 years (%)
    364,    #	  65 years and over (%)
    365,    #	Total - Adjusted after-tax economic family income decile group for the population in private households - 100% data (34)
    366,    #	  In bottom half of the distribution
    367,    #	    In bottom decile
    368,    #	    In second decile
    369,    #	    In third decile
    370,    #	    In fourth decile
    371,    #	    In fifth decile
    372,    #	  In top half of the distribution
    373,    #	    In sixth decile
    374,    #	    In seventh decile
    375,    #	    In eighth decile
    376,    #	    In ninth decile
    377,    #	    In top decile
    378,    #	Total - Inequality measures for the population in private households - 100% data (35)
    379,    #	  Gini index on adjusted household total income
    380,    #	  Gini index on adjusted household market income
    381,    #	  Gini index on adjusted household after-tax income
    382,    #	  P90/P10 ratio on adjusted household after-tax income
    383,    #	Total - Knowledge of official languages for the total population excluding institutional residents - 100% data (36)
    384,    #	  English only
    385,    #	  French only
    386,    #	  English and French
    387,    #	  Neither English nor French
    388,    #	Total - First official language spoken for the total population excluding institutional residents - 100% data (37)
    389,    #	  English
    390,    #	  French
    391,    #	  English and French
    392,    #	  Neither English nor French
    393,    #	Total - Mother tongue for the total population excluding institutional residents - 100% data (38)
    394,    #	  Single responses
    395,    #	    Official languages
    396,    #	      English
    397,    #	      French
    398,    #	    Non-official languages
    399,    #	      Indigenous languages (39)
    400,    #	        Algonquian languages
    401,    #	          Blackfoot
    402,    #	          Cree-Innu languages
    403,    #	            Atikamekw
    404,    #	            Cree languages
    405,    #	              Ililimowin (Moose Cree)
    406,    #	              Inu Ayimun (Southern East Cree)
    407,    #	              Iyiyiw-Ayimiwin (Northern East Cree)
    408,    #	              Nehinawewin (Swampy Cree)
    409,    #	              Nehiyawewin (Plains Cree)
    410,    #	              Nihithawiwin (Woods Cree)
    411,    #	              Cree, n.o.s.
    412,    #	            Innu (Montagnais)
    413,    #	            Naskapi
    414,    #	          Eastern Algonquian languages
    415,    #	            Mi'kmaq
    416,    #	            Wolastoqewi (Malecite)
    417,    #	          Ojibway-Potawatomi languages
    418,    #	            Anicinabemowin (Algonquin)
    419,    #	            Oji-Cree
    420,    #	            Ojibway languages
    421,    #	              Anishinaabemowin (Chippewa)
    422,    #	              Daawaamwin (Odawa)
    423,    #	              Saulteau (Western Ojibway)
    424,    #	              Ojibway, n.o.s.
    425,    #	          Algonquian languages, n.i.e.
    426,    #	        Athabaskan languages
    427,    #	          Northern Athabaskan languages
    428,    #	            Dakelh (Carrier)
    429,    #	            Dane-zaa (Beaver)
    430,    #	            Dene, n.o.s.
    431,    #	            Gwich'in
    432,    #	            Slavey-Hare languages
    433,    #	              Deh Gah Ghotie Zhatie (South Slavey)
    434,    #	              Satuotine Yati (North Slavey)
    435,    #	              Slavey, n.o.s.
    436,    #	            Tahltan languages
    437,    #	              Kaska (Nahani)
    438,    #	              Tahltan
    439,    #	            Tlicho (Dogrib)
    440,    #	            Tse'khene (Sekani)
    441,    #	            Tsilhqot'in (Chilcotin)
    442,    #	            Tsuu T'ina (Sarsi)
    443,    #	            Tutchone languages
    444,    #	              Northern Tutchone
    445,    #	              Southern Tutchone
    446,    #	              Tutchone, n.o.s.
    447,    #	            Wetsuwet'en-Babine
    448,    #	          Tlingit
    449,    #	          Athabaskan languages, n.i.e.
    450,    #	        Haida
    451,    #	        Inuktut (Inuit) languages
    452,    #	          Inuinnaqtun (Inuvialuktun)
    453,    #	            Inuinnaqtun
    454,    #	            Inuvialuktun
    455,    #	          Inuktitut
    456,    #	          Inuktut (Inuit) languages, n.i.e.
    457,    #	        Iroquoian languages
    458,    #	          Cayuga
    459,    #	          Mohawk
    460,    #	          Oneida
    461,    #	          Iroquoian languages, n.i.e.
    462,    #	        Ktunaxa (Kutenai)
    463,    #	        Michif
    464,    #	        Salish languages
    465,    #	          Halkomelem
    466,    #	          Lillooet
    467,    #	          Ntlakapamux (Thompson)
    468,    #	          Secwepemctsin (Shuswap)
    469,    #	          Squamish
    470,    #	          Straits
    471,    #	          Syilx (Okanagan)
    472,    #	          Salish languages, n.i.e.
    473,    #	        Siouan languages
    474,    #	          Assiniboine
    475,    #	          Dakota
    476,    #	          Stoney
    477,    #	          Siouan languages, n.i.e.
    478,    #	        Tsimshian languages
    479,    #	          Gitxsan (Gitksan)
    480,    #	          Nisga'a
    481,    #	          Tsimshian
    482,    #	        Wakashan languages
    483,    #	          Haisla
    484,    #	          Heiltsuk
    485,    #	          Kwak'wala (Kwakiutl)
    486,    #	          Nuu-chah-nulth (Nootka)
    487,    #	          Wakashan languages, n.i.e.
    488,    #	        Indigenous languages, n.i.e.
    489,    #	        Indigenous languages, n.o.s.
    490,    #	      Non-Indigenous languages
    491,    #	        Afro-Asiatic languages
    492,    #	          Berber languages
    493,    #	            Kabyle
    494,    #	            Tamazight
    495,    #	            Berber languages, n.i.e.
    496,    #	          Chadic languages
    497,    #	            Hausa
    498,    #	            Mina
    499,    #	          Coptic
    500,    #	          Cushitic languages
    501,    #	            Bilen
    502,    #	            Oromo
    503,    #	            Somali
    504,    #	            Cushitic languages, n.i.e.
    505,    #	          Semitic languages
    506,    #	            Amharic
    507,    #	            Arabic
    508,    #	            Aramaic languages
    509,    #	              Assyrian Neo-Aramaic
    510,    #	              Chaldean Neo-Aramaic
    511,    #	              Aramaic, n.o.s.
    512,    #	            Harari
    513,    #	            Hebrew
    514,    #	            Maltese
    515,    #	            Tigrigna
    516,    #	            Semitic languages, n.i.e.
    517,    #	        Austro-Asiatic languages
    518,    #	          Khmer (Cambodian)
    519,    #	          Vietnamese
    520,    #	          Austro-Asiatic languages, n.i.e
    521,    #	        Austronesian languages
    522,    #	          Bikol
    523,    #	          Bisaya, n.o.s.
    524,    #	          Cebuano
    525,    #	          Fijian
    526,    #	          Hiligaynon
    527,    #	          Ilocano
    528,    #	          Indonesian
    529,    #	          Kankanaey
    530,    #	          Kinaray-a
    531,    #	          Malagasy languages
    532,    #	            Merina
    533,    #	            Malagasy, n.o.s.
    534,    #	          Malay
    535,    #	          Pampangan (Kapampangan, Pampango)
    536,    #	          Pangasinan
    537,    #	          Tagalog (Pilipino, Filipino)
    538,    #	          Waray-Waray
    539,    #	          Austronesian languages, n.i.e.
    540,    #	        Creole languages
    541,    #	          Haitian Creole
    542,    #	          Jamaican English Creole
    543,    #	          Krio
    544,    #	          Morisyen
    545,    #	          Sango
    546,    #	          Creole, n.o.s.
    547,    #	          Creole languages, n.i.e.
    548,    #	        Dravidian languages
    549,    #	          Kannada
    550,    #	          Malayalam
    551,    #	          Tamil
    552,    #	          Telugu
    553,    #	          Tulu
    554,    #	          Dravidian languages, n.i.e.
    555,    #	        Georgian
    556,    #	        Hmong-Mien languages
    557,    #	        Indo-European languages
    558,    #	          Albanian
    559,    #	          Armenian
    560,    #	          Balto-Slavic languages
    561,    #	            Baltic languages
    562,    #	              Latvian
    563,    #	              Lithuanian
    564,    #	            Slavic languages
    565,    #	              Belarusian
    566,    #	              Bulgarian
    567,    #	              Czech
    568,    #	              Macedonian
    569,    #	              Polish
    570,    #	              Russian
    571,    #	              Rusyn
    572,    #	              Serbo-Croatian
    573,    #	                Bosnian
    574,    #	                Croatian
    575,    #	                Serbian
    576,    #	                Serbo-Croatian, n.i.e.
    577,    #	              Slovak
    578,    #	              Slovene (Slovenian)
    579,    #	              Ukrainian
    580,    #	              Slavic languages, n.i.e.
    581,    #	          Celtic languages
    582,    #	            Irish
    583,    #	            Scottish Gaelic
    584,    #	            Welsh
    585,    #	            Celtic languages, n.i.e.
    586,    #	          Germanic languages
    587,    #	            Frisian
    588,    #	            High German languages
    589,    #	              German
    590,    #	              Pennsylvania German
    591,    #	              Swiss German
    592,    #	              Yiddish
    593,    #	            Low Saxon-Low Franconian languages
    594,    #	              Afrikaans
    595,    #	              Dutch
    596,    #	              Low German, n.o.s.
    597,    #	              Low Saxon
    598,    #	              Plautdietsch
    599,    #	              Vlaams (Flemish)
    600,    #	            Scandinavian languages
    601,    #	              Danish
    602,    #	              Icelandic
    603,    #	              Norwegian
    604,    #	              Swedish
    605,    #	            Germanic languages, n.i.e.
    606,    #	          Greek
    607,    #	          Indo-Iranian languages
    608,    #	            Indo-Aryan languages
    609,    #	              Assamese
    610,    #	              Bengali
    611,    #	              Gujarati
    612,    #	              Hindi
    613,    #	              Kacchi
    614,    #	              Kashmiri
    615,    #	              Konkani
    616,    #	              Marathi
    617,    #	              Nepali
    618,    #	              Oriya languages
    619,    #	                Odia
    620,    #	                Oriya, n.o.s.
    621,    #	              Punjabi (Panjabi)
    622,    #	              Rohingya
    623,    #	              Sindhi
    624,    #	              Sinhala (Sinhalese)
    625,    #	              Urdu
    626,    #	              Indo-Aryan languages, n.i.e.
    627,    #	            Iranian languages
    628,    #	              Baluchi
    629,    #	              Kurdish
    630,    #	              Parsi
    631,    #	              Pashto
    632,    #	              Persian languages
    633,    #	                Dari
    634,    #	                Iranian Persian
    635,    #	                Persian (Farsi), n.o.s.
    636,    #	              Iranian languages, n.i.e.
    637,    #	            Indo-Iranian languages, n.i.e.
    638,    #	          Italic (Romance) languages
    639,    #	            Catalan
    640,    #	            Italian
    641,    #	            Portuguese
    642,    #	            Romanian
    643,    #	            Spanish
    644,    #	            Italic (Romance) languages, n.i.e.
    645,    #	          Indo-European languages, n.i.e.
    646,    #	        Japanese
    647,    #	        Korean
    648,    #	        Mongolian
    649,    #	        Niger-Congo languages
    650,    #	          Akan (Twi)
    651,    #	          Bamanankan
    652,    #	          Edo
    653,    #	          ษw้
    654,    #	          Fulah (Pular, Pulaar, Fulfulde)
    655,    #	          Ga
    656,    #	          Ganda
    657,    #	          Gikuyu
    658,    #	          Igbo
    659,    #	          Kinyarwanda (Rwanda)
    660,    #	          Lingala
    661,    #	          Luba-Kasai
    662,    #	          M๒or้
    663,    #	          Mwani
    664,    #	          Ndebele
    665,    #	          Rundi (Kirundi)
    666,    #	          Shona
    667,    #	          Soninke
    668,    #	          Sotho-Tswana languages
    669,    #	          Swahili
    670,    #	          Wojenaka
    671,    #	          Wolof
    672,    #	          Yoruba
    673,    #	          Niger-Congo languages, n.i.e.
    674,    #	        Nilo-Saharan languages
    675,    #	          Dinka
    676,    #	          Nuer
    677,    #	          Nilo-Saharan languages, n.i.e.
    678,    #	          African, n.o.s.
    679,    #	        Sign languages
    680,    #	          American Sign Language
    681,    #	          Quebec Sign Language
    682,    #	          Sign languages, n.i.e.
    683,    #	        Sino-Tibetan languages
    684,    #	          Chinese languages
    685,    #	            Hakka
    686,    #	            Mandarin
    687,    #	            Min Dong
    688,    #	            Min Nan (Chaochow, Teochow, Fukien, Taiwanese)
    689,    #	            Wu (Shanghainese)
    690,    #	            Yue (Cantonese)
    691,    #	            Chinese, n.o.s.
    692,    #	            Chinese languages, n.i.e.
    693,    #	          Tibeto-Burman languages
    694,    #	            Burmese
    695,    #	            Kuki-Chin languages
    696,    #	            Karenic languages
    697,    #	              S'gaw Karen
    698,    #	              Karenic languages, n.i.e.
    699,    #	            Tibetan
    700,    #	            Tibeto-Burman languages, n.i.e.
    701,    #	          Sino-Tibetan languages, n.i.e.
    702,    #	        Tai-Kadai languages
    703,    #	          Lao
    704,    #	          Thai
    705,    #	          Tai-Kadai languages, n.i.e.
    706,    #	        Turkic languages
    707,    #	          Azerbaijani
    708,    #	          Kazakh
    709,    #	          Turkish
    710,    #	          Uyghur
    711,    #	          Uzbek
    712,    #	          Turkic languages, n.i.e.
    713,    #	        Uralic languages
    714,    #	          Estonian
    715,    #	          Finnish
    716,    #	          Hungarian
    717,    #	        Other languages, n.i.e.
    718,    #	  Multiple responses
    719,    #	    English and French
    720,    #	    English and non-official language(s)
    721,    #	    French and non-official language(s)
    722,    #	    English, French and non-official language(s)
    723,    #	    Multiple non-official languages
    724,    #	Total - All languages spoken at home for the total population excluding institutional residents - 100% data (40)
    725,    #	  English
    726,    #	  French
    727,    #	  Non-official language
    728,    #	    Indigenous (39)
    729,    #	    Non-Indigenous
    730,    #	  English and French
    731,    #	  English and non-official language(s)
    732,    #	  French and non-official language(s)
    733,    #	  English, French and non-official language(s)
    734,    #	  Multiple non-official languages
    735,    #	Total - Language spoken most often at home for the total population excluding institutional residents - 100% data (41)
    736,    #	  Single responses
    737,    #	    Official languages
    738,    #	      English
    739,    #	      French
    740,    #	    Non-official languages
    741,    #	      Indigenous languages (39)
    742,    #	        Algonquian languages
    743,    #	          Blackfoot
    744,    #	          Cree-Innu languages
    745,    #	            Atikamekw
    746,    #	            Cree languages
    747,    #	              Ililimowin (Moose Cree)
    748,    #	              Inu Ayimun (Southern East Cree)
    749,    #	              Iyiyiw-Ayimiwin (Northern East Cree)
    750,    #	              Nehinawewin (Swampy Cree)
    751,    #	              Nehiyawewin (Plains Cree)
    752,    #	              Nihithawiwin (Woods Cree)
    753,    #	              Cree, n.o.s.
    754,    #	            Innu (Montagnais)
    755,    #	            Naskapi
    756,    #	          Eastern Algonquian languages
    757,    #	            Mi'kmaq
    758,    #	            Wolastoqewi (Malecite)
    759,    #	          Ojibway-Potawatomi languages
    760,    #	            Anicinabemowin (Algonquin)
    761,    #	            Oji-Cree
    762,    #	            Ojibway languages
    763,    #	              Anishinaabemowin (Chippewa)
    764,    #	              Daawaamwin (Odawa)
    765,    #	              Saulteau (Western Ojibway)
    766,    #	              Ojibway, n.o.s.
    767,    #	          Algonquian languages, n.i.e.
    768,    #	        Athabaskan languages
    769,    #	          Northern Athabaskan languages
    770,    #	            Dakelh (Carrier)
    771,    #	            Dane-zaa (Beaver)
    772,    #	            Dene, n.o.s.
    773,    #	            Gwich'in
    774,    #	            Slavey-Hare languages
    775,    #	              Deh Gah Ghotie Zhatie (South Slavey)
    776,    #	              Satuotine Yati (North Slavey)
    777,    #	              Slavey, n.o.s.
    778,    #	            Tahltan languages
    779,    #	              Kaska (Nahani)
    780,    #	              Tahltan
    781,    #	            Tlicho (Dogrib)
    782,    #	            Tse'khene (Sekani)
    783,    #	            Tsilhqot'in (Chilcotin)
    784,    #	            Tsuu T'ina (Sarsi)
    785,    #	            Tutchone languages
    786,    #	              Northern Tutchone
    787,    #	              Southern Tutchone
    788,    #	              Tutchone, n.o.s.
    789,    #	            Wetsuwet'en-Babine
    790,    #	          Tlingit
    791,    #	          Athabaskan languages, n.i.e.
    792,    #	        Haida
    793,    #	        Inuktut (Inuit) languages
    794,    #	          Inuinnaqtun (Inuvialuktun)
    795,    #	            Inuinnaqtun
    796,    #	            Inuvialuktun
    797,    #	          Inuktitut
    798,    #	          Inuktut (Inuit) languages, n.i.e.
    799,    #	        Iroquoian languages
    800,    #	          Cayuga
    801,    #	          Mohawk
    802,    #	          Oneida
    803,    #	          Iroquoian languages, n.i.e.
    804,    #	        Ktunaxa (Kutenai)
    805,    #	        Michif
    806,    #	        Salish languages
    807,    #	          Halkomelem
    808,    #	          Lillooet
    809,    #	          Ntlakapamux (Thompson)
    810,    #	          Secwepemctsin (Shuswap)
    811,    #	          Squamish
    812,    #	          Straits
    813,    #	          Syilx (Okanagan)
    814,    #	          Salish languages, n.i.e.
    815,    #	        Siouan languages
    816,    #	          Assiniboine
    817,    #	          Dakota
    818,    #	          Stoney
    819,    #	          Siouan languages, n.i.e.
    820,    #	        Tsimshian languages
    821,    #	          Gitxsan (Gitksan)
    822,    #	          Nisga'a
    823,    #	          Tsimshian
    824,    #	        Wakashan languages
    825,    #	          Haisla
    826,    #	          Heiltsuk
    827,    #	          Kwak'wala (Kwakiutl)
    828,    #	          Nuu-chah-nulth (Nootka)
    829,    #	          Wakashan languages, n.i.e.
    830,    #	        Indigenous languages, n.i.e.
    831,    #	        Indigenous languages, n.o.s.
    832,    #	      Non-Indigenous languages
    833,    #	        Afro-Asiatic languages
    834,    #	          Berber languages
    835,    #	            Kabyle
    836,    #	            Tamazight
    837,    #	            Berber languages, n.i.e.
    838,    #	          Chadic languages
    839,    #	            Hausa
    840,    #	            Mina
    841,    #	          Coptic
    842,    #	          Cushitic languages
    843,    #	            Bilen
    844,    #	            Oromo
    845,    #	            Somali
    846,    #	            Cushitic languages, n.i.e.
    847,    #	          Semitic languages
    848,    #	            Amharic
    849,    #	            Arabic
    850,    #	            Aramaic languages
    851,    #	              Assyrian Neo-Aramaic
    852,    #	              Chaldean Neo-Aramaic
    853,    #	              Aramaic, n.o.s.
    854,    #	            Harari
    855,    #	            Hebrew
    856,    #	            Maltese
    857,    #	            Tigrigna
    858,    #	            Semitic languages, n.i.e.
    859,    #	        Austro-Asiatic languages
    860,    #	          Khmer (Cambodian)
    861,    #	          Vietnamese
    862,    #	          Austro-Asiatic languages, n.i.e
    863,    #	        Austronesian languages
    864,    #	          Bikol
    865,    #	          Bisaya, n.o.s.
    866,    #	          Cebuano
    867,    #	          Fijian
    868,    #	          Hiligaynon
    869,    #	          Ilocano
    870,    #	          Indonesian
    871,    #	          Kankanaey
    872,    #	          Kinaray-a
    873,    #	          Malagasy languages
    874,    #	            Merina
    875,    #	            Malagasy, n.o.s.
    876,    #	          Malay
    877,    #	          Pampangan (Kapampangan, Pampango)
    878,    #	          Pangasinan
    879,    #	          Tagalog (Pilipino, Filipino)
    880,    #	          Waray-Waray
    881,    #	          Austronesian languages, n.i.e.
    882,    #	        Creole languages
    883,    #	          Haitian Creole
    884,    #	          Jamaican English Creole
    885,    #	          Krio
    886,    #	          Morisyen
    887,    #	          Sango
    888,    #	          Creole, n.o.s.
    889,    #	          Creole languages, n.i.e.
    890,    #	        Dravidian languages
    891,    #	          Kannada
    892,    #	          Malayalam
    893,    #	          Tamil
    894,    #	          Telugu
    895,    #	          Tulu
    896,    #	          Dravidian languages, n.i.e.
    897,    #	        Georgian
    898,    #	        Hmong-Mien languages
    899,    #	        Indo-European languages
    900,    #	          Albanian
    901,    #	          Armenian
    902,    #	          Balto-Slavic languages
    903,    #	            Baltic languages
    904,    #	              Latvian
    905,    #	              Lithuanian
    906,    #	            Slavic languages
    907,    #	              Belarusian
    908,    #	              Bulgarian
    909,    #	              Czech
    910,    #	              Macedonian
    911,    #	              Polish
    912,    #	              Russian
    913,    #	              Rusyn
    914,    #	              Serbo-Croatian
    915,    #	                Bosnian
    916,    #	                Croatian
    917,    #	                Serbian
    918,    #	                Serbo-Croatian, n.i.e.
    919,    #	              Slovak
    920,    #	              Slovene (Slovenian)
    921,    #	              Ukrainian
    922,    #	              Slavic languages, n.i.e.
    923,    #	          Celtic languages
    924,    #	            Irish
    925,    #	            Scottish Gaelic
    926,    #	            Welsh
    927,    #	            Celtic languages, n.i.e.
    928,    #	          Germanic languages
    929,    #	            Frisian
    930,    #	            High German languages
    931,    #	              German
    932,    #	              Pennsylvania German
    933,    #	              Swiss German
    934,    #	              Yiddish
    935,    #	            Low Saxon-Low Franconian languages
    936,    #	              Afrikaans
    937,    #	              Dutch
    938,    #	              Low German, n.o.s.
    939,    #	              Low Saxon
    940,    #	              Plautdietsch
    941,    #	              Vlaams (Flemish)
    942,    #	            Scandinavian languages
    943,    #	              Danish
    944,    #	              Icelandic
    945,    #	              Norwegian
    946,    #	              Swedish
    947,    #	            Germanic languages, n.i.e.
    948,    #	          Greek
    949,    #	          Indo-Iranian languages
    950,    #	            Indo-Aryan languages
    951,    #	              Assamese
    952,    #	              Bengali
    953,    #	              Gujarati
    954,    #	              Hindi
    955,    #	              Kacchi
    956,    #	              Kashmiri
    957,    #	              Konkani
    958,    #	              Marathi
    959,    #	              Nepali
    960,    #	              Oriya languages
    961,    #	                Odia
    962,    #	                Oriya, n.o.s.
    963,    #	              Punjabi (Panjabi)
    964,    #	              Rohingya
    965,    #	              Sindhi
    966,    #	              Sinhala (Sinhalese)
    967,    #	              Urdu
    968,    #	              Indo-Aryan languages, n.i.e.
    969,    #	            Iranian languages
    970,    #	              Baluchi
    971,    #	              Kurdish
    972,    #	              Parsi
    973,    #	              Pashto
    974,    #	              Persian languages
    975,    #	                Dari
    976,    #	                Iranian Persian
    977,    #	                Persian (Farsi), n.o.s.
    978,    #	              Iranian languages, n.i.e.
    979,    #	            Indo-Iranian languages, n.i.e.
    980,    #	          Italic (Romance) languages
    981,    #	            Catalan
    982,    #	            Italian
    983,    #	            Portuguese
    984,    #	            Romanian
    985,    #	            Spanish
    986,    #	            Italic (Romance) languages, n.i.e.
    987,    #	          Indo-European languages, n.i.e.
    988,    #	        Japanese
    989,    #	        Korean
    990,    #	        Mongolian
    991,    #	        Niger-Congo languages
    992,    #	          Akan (Twi)
    993,    #	          Bamanankan
    994,    #	          Edo
    995,    #	          �w�
    996,    #	          Fulah (Pular, Pulaar, Fulfulde)
    997,    #	          Ga
    998,    #	          Ganda
    999,    #	          Gikuyu
    1000,   #	          Igbo
    1001,   #	          Kinyarwanda (Rwanda)
    1002,   #	          Lingala
    1003,   #	          Luba-Kasai
    1004,   #	          M�or�
    1005,   #	          Mwani
    1006,   #	          Ndebele
    1007,   #	          Rundi (Kirundi)
    1008,   #	          Shona
    1009,   #	          Soninke
    1010,   #	          Sotho-Tswana languages
    1011,   #	          Swahili
    1012,   #	          Wojenaka
    1013,   #	          Wolof
    1014,   #	          Yoruba
    1015,   #	          Niger-Congo languages, n.i.e.
    1016,   #	        Nilo-Saharan languages
    1017,   #	          Dinka
    1018,   #	          Nuer
    1019,   #	          Nilo-Saharan languages, n.i.e.
    1020,   #	          African, n.o.s.
    1021,   #	        Sign languages
    1022,   #	          American Sign Language
    1023,   #	          Quebec Sign Language
    1024,   #	          Sign languages, n.i.e.
    1025,   #	        Sino-Tibetan languages
    1026,   #	          Chinese languages
    1027,   #	            Hakka
    1028,   #	            Mandarin
    1029,   #	            Min Dong
    1030,   #	            Min Nan (Chaochow, Teochow, Fukien, Taiwanese)
    1031,   #	            Wu (Shanghainese)
    1032,   #	            Yue (Cantonese)
    1033,   #	            Chinese, n.o.s.
    1034,   #	            Chinese languages, n.i.e.
    1035,   #	          Tibeto-Burman languages
    1036,   #	            Burmese
    1037,   #	            Kuki-Chin languages
    1038,   #	            Karenic languages
    1039,   #	              S'gaw Karen
    1040,   #	              Karenic languages, n.i.e.
    1041,   #	            Tibetan
    1042,   #	            Tibeto-Burman languages, n.i.e.
    1043,   #	          Sino-Tibetan languages, n.i.e.
    1044,   #	        Tai-Kadai languages
    1045,   #	          Lao
    1046,   #	          Thai
    1047,   #	          Tai-Kadai languages, n.i.e.
    1048,   #	        Turkic languages
    1049,   #	          Azerbaijani
    1050,   #	          Kazakh
    1051,   #	          Turkish
    1052,   #	          Uyghur
    1053,   #	          Uzbek
    1054,   #	          Turkic languages, n.i.e.
    1055,   #	        Uralic languages
    1056,   #	          Estonian
    1057,   #	          Finnish
    1058,   #	          Hungarian
    1059,   #	        Other languages, n.i.e.
    1060,   #	  Multiple responses
    1061,   #	    English and French
    1062,   #	    English and non-official language(s)
    1063,   #	    French and non-official language(s)
    1064,   #	    English, French and non-official language(s)
    1065,   #	    Multiple non-official languages
    1066,   #	Total - Other language(s) spoken regularly at home for the total population excluding institutional residents - 100% data (42)
    1067,   #	  None
    1068,   #	  English
    1069,   #	  French
    1070,   #	  Non-official language
    1071,   #	    Indigenous (39)
    1072,   #	    Non-Indigenous
    1073,   #	  English and French
    1074,   #	  English and non-official language(s)
    1075,   #	  French and non-official language(s)
    1076,   #	  English, French and non-official language(s)
    1077,   #	  Multiple non-official languages
    1078,   #	Total - Knowledge of languages for the population in private households - 25% sample data (43)
    1079,   #	  Official languages
    1080,   #	    English
    1081,   #	    French
    1082,   #	  Non-official languages
    1083,   #	    Indigenous languages (39)
    1084,   #	      Algonquian languages
    1085,   #	        Blackfoot
    1086,   #	        Cree-Innu languages
    1087,   #	          Atikamekw
    1088,   #	          Cree languages
    1089,   #	            Ililimowin (Moose Cree)
    1090,   #	            Inu Ayimun (Southern East Cree)
    1091,   #	            Iyiyiw-Ayimiwin (Northern East Cree)
    1092,   #	            Nehinawewin (Swampy Cree)
    1093,   #	            Nehiyawewin (Plains Cree)
    1094,   #	            Nihithawiwin (Woods Cree)
    1095,   #	            Cree, n.o.s.
    1096,   #	          Innu (Montagnais)
    1097,   #	          Naskapi
    1098,   #	        Eastern Algonquian languages
    1099,   #	          Mi'kmaq
    1100,   #	          Wolastoqewi (Malecite)
    1101,   #	        Ojibway-Potawatomi languages
    1102,   #	          Anicinabemowin (Algonquin)
    1103,   #	          Oji-Cree
    1104,   #	          Ojibway languages
    1105,   #	            Anishinaabemowin (Chippewa)
    1106,   #	            Daawaamwin (Odawa)
    1107,   #	            Saulteau (Western Ojibway)
    1108,   #	            Ojibway, n.o.s.
    1109,   #	        Algonquian languages, n.i.e.
    1110,   #	      Athabaskan languages
    1111,   #	        Northern Athabaskan languages
    1112,   #	          Dakelh (Carrier)
    1113,   #	          Dane-zaa (Beaver)
    1114,   #	          Dene, n.o.s.
    1115,   #	          Gwich'in
    1116,   #	          Slavey-Hare languages
    1117,   #	            Deh Gah Ghotie Zhatie (South Slavey)
    1118,   #	            Satuotine Yati (North Slavey)
    1119,   #	            Slavey, n.o.s.
    1120,   #	          Tahltan languages
    1121,   #	            Kaska (Nahani)
    1122,   #	            Tahltan
    1123,   #	          Tlicho (Dogrib)
    1124,   #	          Tse'khene (Sekani)
    1125,   #	          Tsilhqot'in (Chilcotin)
    1126,   #	          Tsuu T'ina (Sarsi)
    1127,   #	          Tutchone languages
    1128,   #	            Northern Tutchone
    1129,   #	            Southern Tutchone
    1130,   #	            Tutchone, n.o.s.
    1131,   #	          Wetsuwet'en-Babine
    1132,   #	        Tlingit
    1133,   #	        Athabaskan languages, n.i.e.
    1134,   #	      Haida
    1135,   #	      Inuktut (Inuit) languages
    1136,   #	        Inuinnaqtun (Inuvialuktun)
    1137,   #	          Inuinnaqtun
    1138,   #	          Inuvialuktun
    1139,   #	        Inuktitut
    1140,   #	        Inuktut (Inuit) languages, n.i.e.
    1141,   #	      Iroquoian languages
    1142,   #	        Cayuga
    1143,   #	        Mohawk
    1144,   #	        Oneida
    1145,   #	        Iroquoian languages, n.i.e.
    1146,   #	      Ktunaxa (Kutenai)
    1147,   #	      Michif
    1148,   #	      Salish languages
    1149,   #	        Halkomelem
    1150,   #	        Lillooet
    1151,   #	        Ntlakapamux (Thompson)
    1152,   #	        Secwepemctsin (Shuswap)
    1153,   #	        Squamish
    1154,   #	        Straits
    1155,   #	        Syilx (Okanagan)
    1156,   #	        Salish languages, n.i.e.
    1157,   #	      Siouan languages
    1158,   #	        Assiniboine
    1159,   #	        Dakota
    1160,   #	        Stoney
    1161,   #	        Siouan languages, n.i.e.
    1162,   #	      Tsimshian languages
    1163,   #	        Gitxsan (Gitksan)
    1164,   #	        Nisga'a
    1165,   #	        Tsimshian
    1166,   #	      Wakashan languages
    1167,   #	        Haisla
    1168,   #	        Heiltsuk
    1169,   #	        Kwak'wala (Kwakiutl)
    1170,   #	        Nuu-chah-nulth (Nootka)
    1171,   #	        Wakashan languages, n.i.e.
    1172,   #	      Indigenous languages, n.i.e.
    1173,   #	      Indigenous languages, n.o.s.
    1174,   #	    Non-Indigenous languages
    1175,   #	      Afro-Asiatic languages
    1176,   #	        Berber languages
    1177,   #	          Kabyle
    1178,   #	          Tamazight
    1179,   #	          Berber languages, n.i.e.
    1180,   #	        Chadic languages
    1181,   #	          Hausa
    1182,   #	          Mina
    1183,   #	        Coptic
    1184,   #	        Cushitic languages
    1185,   #	          Bilen
    1186,   #	          Oromo
    1187,   #	          Somali
    1188,   #	          Cushitic languages, n.i.e.
    1189,   #	        Semitic languages
    1190,   #	          Amharic
    1191,   #	          Arabic
    1192,   #	          Aramaic languages
    1193,   #	            Assyrian Neo-Aramaic
    1194,   #	            Chaldean Neo-Aramaic
    1195,   #	            Aramaic, n.o.s.
    1196,   #	          Harari
    1197,   #	          Hebrew
    1198,   #	          Maltese
    1199,   #	          Tigrigna
    1200,   #	          Semitic languages, n.i.e.
    1201,   #	      Austro-Asiatic languages
    1202,   #	        Khmer (Cambodian)
    1203,   #	        Vietnamese
    1204,   #	        Austro-Asiatic languages, n.i.e
    1205,   #	      Austronesian languages
    1206,   #	        Bikol
    1207,   #	        Bisaya, n.o.s.
    1208,   #	        Cebuano
    1209,   #	        Fijian
    1210,   #	        Hiligaynon
    1211,   #	        Ilocano
    1212,   #	        Indonesian
    1213,   #	        Kankanaey
    1214,   #	        Kinaray-a
    1215,   #	        Malagasy languages
    1216,   #	          Merina
    1217,   #	          Malagasy, n.o.s.
    1218,   #	        Malay
    1219,   #	        Pampangan (Kapampangan, Pampango)
    1220,   #	        Pangasinan
    1221,   #	        Tagalog (Pilipino, Filipino)
    1222,   #	        Waray-Waray
    1223,   #	        Austronesian languages, n.i.e.
    1224,   #	      Creole languages
    1225,   #	        Haitian Creole
    1226,   #	        Jamaican English Creole
    1227,   #	        Krio
    1228,   #	        Morisyen
    1229,   #	        Sango
    1230,   #	        Creole, n.o.s.
    1231,   #	        Creole languages, n.i.e.
    1232,   #	      Dravidian languages
    1233,   #	        Kannada
    1234,   #	        Malayalam
    1235,   #	        Tamil
    1236,   #	        Telugu
    1237,   #	        Tulu
    1238,   #	        Dravidian languages, n.i.e.
    1239,   #	      Georgian
    1240,   #	      Hmong-Mien languages
    1241,   #	      Indo-European languages
    1242,   #	        Albanian
    1243,   #	        Armenian
    1244,   #	        Balto-Slavic languages
    1245,   #	        Baltic languages
    1246,   #	            Latvian
    1247,   #	            Lithuanian
    1248,   #	          Slavic languages
    1249,   #	            Belarusian
    1250,   #	            Bulgarian
    1251,   #	            Czech
    1252,   #	            Macedonian
    1253,   #	            Polish
    1254,   #	            Russian
    1255,   #	            Rusyn
    1256,   #	            Serbo-Croatian
    1257,   #	              Bosnian
    1258,   #	              Croatian
    1259,   #	              Serbian
    1260,   #	              Serbo-Croatian, n.i.e.
    1261,   #	            Slovak
    1262,   #	            Slovene (Slovenian)
    1263,   #	            Ukrainian
    1264,   #	            Slavic languages, n.i.e.
    1265,   #	        Celtic languages
    1266,   #	          Irish
    1267,   #	          Scottish Gaelic
    1268,   #	          Welsh
    1269,   #	          Celtic languages, n.i.e.
    1270,   #	        Germanic languages
    1271,   #	          Frisian
    1272,   #	          High German languages
    1273,   #	            German
    1274,   #	            Pennsylvania German
    1275,   #	            Swiss German
    1276,   #	            Yiddish
    1277,   #	          Low Saxon-Low Franconian languages
    1278,   #	            Afrikaans
    1279,   #	            Dutch
    1280,   #	            Low German, n.o.s.
    1281,   #	            Low Saxon
    1282,   #	            Plautdietsch
    1283,   #	            Vlaams (Flemish)
    1284,   #	          Scandinavian languages
    1285,   #	            Danish
    1286,   #	            Icelandic
    1287,   #	            Norwegian
    1288,   #	            Swedish
    1289,   #	          Germanic languages, n.i.e.
    1290,   #	        Greek
    1291,   #	        Indo-Iranian languages
    1292,   #	          Indo-Aryan languages
    1293,   #	            Assamese
    1294,   #	            Bengali
    1295,   #	            Gujarati
    1296,   #	            Hindi
    1297,   #	            Kacchi
    1298,   #	            Kashmiri
    1299,   #	            Konkani
    1300,   #	            Marathi
    1301,   #	            Nepali
    1302,   #	            Oriya languages
    1303,   #	              Odia
    1304,   #	              Oriya, n.o.s.
    1305,   #	            Punjabi (Panjabi)
    1306,   #	            Rohingya
    1307,   #	            Sindhi
    1308,   #	            Sinhala (Sinhalese)
    1309,   #	            Urdu
    1310,   #	            Indo-Aryan languages, n.i.e.
    1311,   #	          Iranian languages
    1312,   #	            Baluchi
    1313,   #	            Kurdish
    1314,   #	            Parsi
    1315,   #	            Pashto
    1316,   #	            Persian languages
    1317,   #	              Dari
    1318,   #	              Iranian Persian
    1319,   #	              Persian (Farsi), n.o.s.
    1320,   #	            Iranian languages, n.i.e.
    1321,   #	          Indo-Iranian languages, n.i.e.
    1322,   #	        Italic (Romance) languages
    1323,   #	          Catalan
    1324,   #	          Italian
    1325,   #	          Portuguese
    1326,   #	          Romanian
    1327,   #	          Spanish
    1328,   #	          Italic (Romance) languages, n.i.e.
    1329,   #	        Indo-European languages, n.i.e.
    1330,   #	      Japanese
    1331,   #	      Korean
    1332,   #	      Mongolian
    1333,   #	      Niger-Congo languages
    1334,   #	        Akan (Twi)
    1335,   #	        Bamanankan
    1336,   #	        Edo
    1337,   #	        �w�
    1338,   #	        Fulah (Pular, Pulaar, Fulfulde)
    1339,   #	        Ga
    1340,   #	        Ganda
    1341,   #	        Gikuyu
    1342,   #	        Igbo
    1343,   #	        Kinyarwanda (Rwanda)
    1344,   #	        Lingala
    1345,   #	        Luba-Kasai
    1346,   #	        M�or�
    1347,   #	        Mwani
    1348,   #	        Ndebele
    1349,   #	        Rundi (Kirundi)
    1350,   #	        Shona
    1351,   #	        Soninke
    1352,   #	        Sotho-Tswana languages
    1353,   #	        Swahili
    1354,   #	        Wojenaka
    1355,   #	        Wolof
    1356,   #	        Yoruba
    1357,   #	        Niger-Congo languages, n.i.e.
    1358,   #	      Nilo-Saharan languages
    1359,   #	        Dinka
    1360,   #	        Nuer
    1361,   #	        Nilo-Saharan languages, n.i.e.
    1362,   #	        African, n.o.s.
    1363,   #	      Sign languages
    1364,   #	        American Sign Language
    1365,   #	        Quebec Sign Language
    1366,   #	        Sign languages, n.i.e.
    1367,   #	      Sino-Tibetan languages
    1368,   #	        Chinese languages
    1369,   #	          Hakka
    1370,   #	          Mandarin
    1371,   #	          Min Dong
    1372,   #	          Min Nan (Chaochow, Teochow, Fukien, Taiwanese)
    1373,   #	          Wu (Shanghainese)
    1374,   #	          Yue (Cantonese)
    1375,   #	          Chinese, n.o.s.
    1376,   #	          Chinese languages, n.i.e.
    1377,   #	        Tibeto-Burman languages
    1378,   #	          Burmese
    1379,   #	          Kuki-Chin languages
    1380,   #	          Karenic languages
    1381,   #	            S'gaw Karen
    1382,   #	            Karenic languages, n.i.e.
    1383,   #	          Tibetan
    1384,   #	          Tibeto-Burman languages, n.i.e.
    1385,   #	        Sino-Tibetan languages, n.i.e.
    1386,   #	      Tai-Kadai languages
    1387,   #	        Lao
    1388,   #	        Thai
    1389,   #	        Tai-Kadai languages, n.i.e.
    1390,   #	      Turkic languages
    1391,   #	        Azerbaijani
    1392,   #	        Kazakh
    1393,   #	        Turkish
    1394,   #	        Uyghur
    1395,   #	        Uzbek
    1396,   #	        Turkic languages, n.i.e.
    1397,   #	      Uralic languages
    1398,   #	        Estonian
    1399,   #	        Finnish
    1400,   #	        Hungarian
    1401,   #	      Other languages, n.i.e.
    1402,   #	Total - Indigenous identity for the population in private households - 25% sample data (44)
    1403,   #	  Indigenous identity (45)
    1404,   #	    Single Indigenous responses (46)
    1405,   #	      First Nations (North American Indian)
    1406,   #	      M�tis
    1407,   #	      Inuk�(Inuit)
    1408,   #	    Multiple Indigenous responses (47)
    1409,   #	    Indigenous responses not included elsewhere (48)
    1410,   #	  Non-Indigenous identity
    1411,   #	Total - Registered or Treaty Indian status for the population in private households - 25% sample data (44)
    1412,   #	  Registered or Treaty Indian (49)
    1413,   #	  Not a Registered or Treaty Indian
    1414,   #	Total - Private households by tenure - 25% sample data (50)
    1415,   #	  Owner
    1416,   #	  Renter
    1417,   #	  Dwelling provided by the local government, First Nation or Indian band
    1418,   #	Total - Occupied private dwellings by condominium status - 25% sample data (51)
    1419,   #	  Condominium
    1420,   #	  Not condominium
    1421,   #	Total - Occupied private dwellings by number of bedrooms - 25% sample data (52)
    1422,   #	  No bedrooms
    1423,   #	  1 bedroom
    1424,   #	  2 bedrooms
    1425,   #	  3 bedrooms
    1426,   #	  4 or more bedrooms
    1427,   #	Total - Occupied private dwellings by number of rooms - 25% sample data (53)
    1428,   #	  1 to 4 rooms
    1429,   #	  5 rooms
    1430,   #	  6 rooms
    1431,   #	  7 rooms
    1432,   #	  8 or more rooms
    1433,   #	Average number of rooms per dwelling
    1434,   #	Total - Private households by number of persons per room - 25% sample data (54)
    1435,   #	  One person or fewer per room
    1436,   #	  More than one person per room
    1437,   #	Total - Private households by housing suitability - 25% sample data (55)
    1438,   #	  Suitable
    1439,   #	  Not suitable
    1440,   #	Total - Occupied private dwellings by period of construction - 25% sample data (56)
    1441,   #	  1960 or before
    1442,   #	  1961 to 1980
    1443,   #	  1981 to 1990
    1444,   #	  1991 to 2000
    1445,   #	  2001 to 2005
    1446,   #	  2006 to 2010
    1447,   #	  2011 to 2015
    1448,   #	  2016 to 2021 (57)
    1449,   #	Total - Occupied private dwellings by dwelling condition - 25% sample data (58)
    1450,   #	  Only regular maintenance and minor repairs needed
    1451,   #	  Major repairs needed
    1452,   #	Total - Private households by number of household maintainers - 25% sample data (59)
    1453,   #	  One-maintainer household
    1454,   #	  Two-maintainer household
    1455,   #	  Three-or-more-maintainer household
    1456,   #	Total - Private households by age of primary household maintainers - 25% sample data (60)
    1457,   #	  15 to 24 years
    1458,   #	  25 to 34 years
    1459,   #	  35 to 44 years
    1460,   #	  45 to 54 years
    1461,   #	  55 to 64 years
    1462,   #	  65 to 74 years
    1463,   #	  75 to 84 years
    1464,   #	  85 years and over
    1465,   #	Total - Owner and tenant households with household total income greater than zero, in non-farm, non-reserve private dwellings by shelter-cost-to-income ratio - 25% sample data (61)
    1466,   #	  Spending less than 30% of income on shelter costs
    1467,   #	  Spending 30% or more of income on shelter costs
    1468,   #	    30% to less than 100%
    1469,   #	Total - Occupied private dwellings by housing indicators - 25% sample data (62)
    1470,   #	  Total - Households 'spending 30% or more of income on shelter costs' or 'not suitable' or 'major repairs needed'
    1471,   #	    Spending 30% or more of income on shelter costs only
    1472,   #	    Not suitable only
    1473,   #	    Major repairs needed only
    1474,   #	    'Spending 30% or more of income on shelter costs' and 'not suitable'
    1475,   #	    'Spending 30% or more of income on shelter costs' and 'major repairs needed'
    1476,   #	    'Not suitable' and 'major repairs needed'
    1477,   #	    'Spending 30% or more of income on shelter costs' and 'not suitable' and 'major repairs needed'
    1478,   #	  Acceptable housing
    1479,   #	Total - Owner and tenant households with household total income greater than zero and shelter-cost-to-income ratio less than 100%, in non-farm, non-reserve private dwellings - 25% sample data (63)
    1480,   #	  In core need
    1481,   #	  Not in core need
    1482,   #	Total - Owner households in non-farm, non-reserve private dwellings - 25% sample data
    1483,   #	  % of owner households with a mortgage (64)
    1484,   #	  % of owner households spending 30% or more of its income on shelter costs (61)
    1485,   #	  % in core housing need (63)
    1486,   #	  Median monthly shelter costs for owned dwellings ($) (65)
    1487,   #	  Average monthly shelter costs for owned dwellings ($) (65)
    1488,   #	  Median value of dwellings ($) (66)
    1489,   #	  Average value of dwellings ($) (66)
    1490,   #	Total - Tenant households in non-farm, non-reserve private dwellings - 25% sample data
    1491,   #	  % of tenant households in subsidized housing (67)
    1492,   #	  % of tenant households spending 30% or more of its income on shelter costs (61)
    1493,   #	  % in core housing need (63)
    1494,   #	  Median monthly shelter costs for rented dwellings ($) (65)
    1495,   #	  Average monthly shelter costs for rented dwellings ($) (65)
    1496,   #	Total - Households living in a dwelling provided by the local government, First Nation or Indian band in non-farm private dwellings - 25% sample data
    1497,   #	  % of households living in a dwelling provided by the local government, First Nation or Indian band spending more than 30% on shelter costs (61)
    1498,   #	  Median monthly shelter costs for dwellings provided by local government, First Nation or Indian band ($) (65)
    1499,   #	  Average monthly shelter costs for dwellings provided by local government, First Nation or Indian band ($) (65)
    1500,   #	Total - Indigenous ancestry for the population in private households - 25% sample data (68)
    1501,   #	  Indigenous ancestry (only) (69)
    1502,   #	    Single Indigenous ancestry (only) (70)
    1503,   #	      First Nations (North American Indian) single ancestry
    1504,   #	      M�tis single ancestry
    1505,   #	      Inuit single ancestry
    1506,   #	    Multiple Indigenous ancestries (only) (71)
    1507,   #	      First Nations (North American Indian) and M�tis ancestry only
    1508,   #	      First Nations (North American Indian) and Inuit ancestry only
    1509,   #	      M�tis and Inuit ancestry only
    1510,   #	      First Nations (North American Indian) and M�tis and Inuit ancestry only
    1511,   #	  Indigenous and non-Indigenous ancestries (72)
    1512,   #	    Single Indigenous and non-Indigenous ancestries (73)
    1513,   #	      First Nations (North American Indian) and non-Indigenous ancestry only
    1514,   #	      M�tis and non-Indigenous ancestry only
    1515,   #	      Inuit and non-Indigenous ancestry only
    1516,   #	    Multiple Indigenous and non-Indigenous ancestries (74)
    1517,   #	      First Nations (North American Indian) and M�tis and non-Indigenous ancestry only
    1518,   #	      First Nations (North American Indian) and Inuit and non-Indigenous ancestry only
    1519,   #	      M�tis and Inuit and non-Indigenous ancestry only
    1520,   #	      First Nations (North American Indian) and M�tis and Inuit and non-Indigenous ancestry only
    1521,   #	  Non-Indigenous ancestry only (75)
    1522,   #	Total - Citizenship for the population in private households - 25% sample data (76)
    1523,   #	  Canadian citizens (77)
    1524,   #	    Canadian citizens aged under 18
    1525,   #	    Canadian citizens aged 18 and over
    1526,   #	  Not Canadian citizens (78)
    1527,   #	Total - Immigrant status and period of immigration for the population in private households - 25% sample data (79)
    1528,   #	  Non-immigrants (80)
    1529,   #	  Immigrants (81)
    1530,   #	    Before 1980
    1531,   #	    1980 to 1990
    1532,   #	    1991 to 2000
    1533,   #	    2001 to 2010
    1534,   #	    2011 to 2021 (82)
    1535,   #	      2011 to 2015
    1536,   #	      2016 to 2021
    1537,   #	  Non-permanent residents (83)
    1538,   #	Total - Age at immigration for the immigrant population in private households - 25% sample data (84)
    1539,   #	  Under 5 years
    1540,   #	  5 to 14 years
    1541,   #	  15 to 24 years
    1542,   #	  25 to 44 years
    1543,   #	  45 years and over
    1544,   #	Total - Place of birth for the immigrant population in private households - 25% sample data (85)
    1545,   #	  Americas
    1546,   #	    Brazil
    1547,   #	    Colombia
    1548,   #	    El Salvador
    1549,   #	    Guyana
    1550,   #	    Haiti
    1551,   #	    Jamaica
    1552,   #	    Mexico
    1553,   #	    Peru
    1554,   #	    Trinidad and Tobago
    1555,   #	    United States of America
    1556,   #	    Other places of birth in Americas
    1557,   #	  Europe
    1558,   #	    Bosnia and Herzegovina
    1559,   #	    Croatia
    1560,   #	    France
    1561,   #	    Germany
    1562,   #	    Greece
    1563,   #	    Hungary
    1564,   #	    Italy
    1565,   #	    Netherlands
    1566,   #	    Poland
    1567,   #	    Portugal
    1568,   #	    Romania
    1569,   #	    Russian Federation
    1570,   #	    Serbia (86)
    1571,   #	    Ukraine
    1572,   #	    United Kingdom (87)
    1573,   #	    Other places of birth in Europe
    1574,   #	  Africa
    1575,   #	    Algeria
    1576,   #	    Congo, Democratic Republic of the
    1577,   #	    Egypt
    1578,   #	    Eritrea
    1579,   #	    Ethiopia
    1580,   #	    Morocco
    1581,   #	    Nigeria
    1582,   #	    Somalia
    1583,   #	    South Africa, Republic of
    1584,   #	    Other places of birth in Africa
    1585,   #	  Asia
    1586,   #	    Afghanistan
    1587,   #	    Iran (88)
    1588,   #	    Iraq
    1589,   #	    Lebanon
    1590,   #	    Syria (89)
    1591,   #	    Turkey
    1592,   #	    China (90)
    1593,   #	    Hong Kong (91)
    1594,   #	    Korea, South (92)
    1595,   #	    Taiwan
    1596,   #	    Philippines
    1597,   #	    Viet Nam
    1598,   #	    Bangladesh
    1599,   #	    India
    1600,   #	    Pakistan
    1601,   #	    Sri Lanka
    1602,   #	    Other places of birth in Asia
    1603,   #	  Oceania and other places of birth (93)
    1604,   #	Total - Place of birth for the recent immigrant population in private households - 25% sample data (94)
    1605,   #	  Americas
    1606,   #	    Brazil
    1607,   #	    Colombia
    1608,   #	    Haiti
    1609,   #	    Jamaica
    1610,   #	    Mexico
    1611,   #	    United States of America
    1612,   #	    Venezuela (95)
    1613,   #	    Other places of birth in Americas
    1614,   #	  Europe
    1615,   #	    France
    1616,   #	    Germany
    1617,   #	    Ireland (96)
    1618,   #	    Italy
    1619,   #	    Russian Federation
    1620,   #	    Ukraine
    1621,   #	    United Kingdom (87)
    1622,   #	    Other places of birth in Europe
    1623,   #	  Africa
    1624,   #	    Algeria
    1625,   #	    Burundi
    1626,   #	    Cameroon
    1627,   #	    Congo, Democratic Republic of the
    1628,   #	    C�te d'Ivoire
    1629,   #	    Egypt
    1630,   #	    Eritrea
    1631,   #	    Ethiopia
    1632,   #	    Morocco
    1633,   #	    Nigeria
    1634,   #	    Somalia
    1635,   #	    South Africa, Republic of
    1636,   #	    Sudan (97)
    1637,   #	    Tunisia
    1638,   #	    Other places of birth in Africa
    1639,   #	  Asia
    1640,   #	    Afghanistan
    1641,   #	    Bangladesh
    1642,   #	    China (90)
    1643,   #	    Hong Kong (91)
    1644,   #	    India
    1645,   #	    Iran (88)
    1646,   #	    Iraq
    1647,   #	    Israel
    1648,   #	    Japan
    1649,   #	    Jordan
    1650,   #	    Korea, South (92)
    1651,   #	    Lebanon
    1652,   #	    Nepal
    1653,   #	    Pakistan
    1654,   #	    Philippines
    1655,   #	    Saudi Arabia
    1656,   #	    Sri Lanka
    1657,   #	    Syria (89)
    1658,   #	    Turkey
    1659,   #	    United Arab Emirates
    1660,   #	    Viet Nam
    1661,   #	    Other places of birth in Asia
    1662,   #	  Oceania and other (93)
    1663,   #	    Australia
    1664,   #	    Other places of birth (98)
    1665,   #	Total - Generation status for the population in private households - 25% sample data (99)
    1666,   #	  First generation (100)
    1667,   #	  Second generation (101)
    1668,   #	  Third generation or more (102)
    1669,   #	Total - Admission category and applicant type for the immigrant population in private households who were admitted between 1980 and 2021 - 25% sample data (103)
    1670,   #	  Economic immigrants (104)
    1671,   #	    Principal applicants (105)
    1672,   #	    Secondary applicants (106)
    1673,   #	  Immigrants sponsored by family (107)
    1674,   #	  Refugees (108)
    1675,   #	  Other immigrants (109)
    1676,   #	Total - Pre-admission experience for the immigrant population in private households who were admitted between 1980 and 2021 - 25% sample data (110)
    1677,   #	  Asylum claim before admission (111)
    1678,   #	  Work permits only before admission (112)
    1679,   #	  Study permits only before admission (113)
    1680,   #	  Work and study permits before admission (114)
    1681,   #	  Other permits before admission (115)
    1682,   #	  No pre-admission experience (116)
    1683,   #	Total - Visible minority for the population in private households - 25% sample data (117)
    1684,   #	  Total visible minority population (118)
    1685,   #	    South Asian
    1686,   #	    Chinese
    1687,   #	    Black
    1688,   #	    Filipino
    1689,   #	    Arab
    1690,   #	    Latin American
    1691,   #	    Southeast Asian
    1692,   #	    West Asian
    1693,   #	    Korean
    1694,   #	    Japanese
    1695,   #	    Visible minority, n.i.e. (119)
    1696,   #	    Multiple visible minorities
    1697,   #	  Not a visible minority (120)
    1698,   #	Total - Ethnic or cultural origin for the population in private households - 25% sample data (121)
    1699,   #	  Canadian
    1700,   #	  English
    1701,   #	  Irish
    1702,   #	  Scottish
    1703,   #	  French, n.o.s. (122)
    1704,   #	  German
    1705,   #	  Chinese
    1706,   #	  Italian
    1707,   #	  Indian (India)
    1708,   #	  Ukrainian
    1709,   #	  Dutch
    1710,   #	  Polish
    1711,   #	  Qu�b�cois
    1712,   #	  British Isles, n.o.s. (123)
    1713,   #	  Filipino
    1714,   #	  French Canadian
    1715,   #	  Caucasian (White), n.o.s. (124)
    1716,   #	  First Nations (North American Indian), n.o.s. (125)
    1717,   #	  M�tis
    1718,   #	  European, n.o.s. (126)
    1719,   #	  Russian
    1720,   #	  Norwegian
    1721,   #	  Welsh
    1722,   #	  Portuguese
    1723,   #	  American
    1724,   #	  Spanish
    1725,   #	  Swedish
    1726,   #	  Hungarian
    1727,   #	  Acadian
    1728,   #	  Pakistani
    1729,   #	  African, n.o.s. (127)
    1730,   #	  Jewish
    1731,   #	  Punjabi
    1732,   #	  Vietnamese
    1733,   #	  Arab, n.o.s. (128)
    1734,   #	  Greek
    1735,   #	  Jamaican
    1736,   #	  Asian, n.o.s. (129)
    1737,   #	  Cree, n.o.s. (130)
    1738,   #	  Korean
    1739,   #	  Romanian
    1740,   #	  Lebanese
    1741,   #	  Iranian
    1742,   #	  Christian, n.i.e. (131)
    1743,   #	  Danish
    1744,   #	  North American Indigenous, n.o.s. (132)
    1745,   #	  Sikh
    1746,   #	  Austrian
    1747,   #	  Belgian
    1748,   #	  Haitian
    1749,   #	  Hindu
    1750,   #	  Mexican
    1751,   #	  Mennonite
    1752,   #	  Swiss
    1753,   #	  Finnish
    1754,   #	  Sri Lankan
    1755,   #	  Croatian
    1756,   #	  Japanese
    1757,   #	  South Asian, n.o.s. (133)
    1758,   #	  Mi'kmaq, n.o.s. (134)
    1759,   #	  Northern European, n.o.s. (135)
    1760,   #	  Muslim
    1761,   #	  Egyptian
    1762,   #	  Latin, Central or South American, n.o.s. (136)
    1763,   #	  Tamil
    1764,   #	  Icelandic
    1765,   #	  Colombian
    1766,   #	  Moroccan
    1767,   #	  Czech
    1768,   #	  Syrian
    1769,   #	  Guyanese
    1770,   #	  Afghan
    1771,   #	  Black, n.o.s. (137)
    1772,   #	  Serbian
    1773,   #	  Ojibway
    1774,   #	  Newfoundlander
    1775,   #	  Hong Konger
    1776,   #	  Ontarian
    1777,   #	  Persian
    1778,   #	  Trinidadian/Tobagonian
    1779,   #	  Turkish
    1780,   #	  Inuit, n.o.s. (138)
    1781,   #	  Bangladeshi
    1782,   #	  Algerian
    1783,   #	  Brazilian
    1784,   #	  Nigerian
    1785,   #	  Armenian
    1786,   #	  Slovak
    1787,   #	  Eastern European, n.o.s. (139)
    1788,   #	  Somali
    1789,   #	  Taiwanese
    1790,   #	  Iraqi
    1791,   #	  Salvadorean
    1792,   #	  African Caribbean
    1793,   #	  East or Southeast Asian, n.o.s. (140)
    1794,   #	  West or Central Asian or Middle Eastern, n.o.s. (141)
    1795,   #	  Caribbean, n.o.s. (142)
    1796,   #	  Algonquin
    1797,   #	  West Indian, n.o.s. (143)
    1798,   #	  Lithuanian
    1799,   #	  South African
    1800,   #	  Australian
    1801,   #	  Palestinian
    1802,   #	  Chilean
    1803,   #	  Congolese
    1804,   #	  Nova Scotian
    1805,   #	  Ethiopian
    1806,   #	  Hispanic, n.o.s. (144)
    1807,   #	  Peruvian
    1808,   #	  Yoruba
    1809,   #	  Cambodian (Khmer)
    1810,   #	  Berber
    1811,   #	  Albanian
    1812,   #	  Maltese
    1813,   #	  Macedonian
    1814,   #	  Slovenian
    1815,   #	  Western European, n.o.s. (145)
    1816,   #	  New Brunswicker
    1817,   #	  Gujarati
    1818,   #	  Eritrean
    1819,   #	  African Canadian
    1820,   #	  Israeli
    1821,   #	  Mohawk
    1822,   #	  Czechoslovakian, n.o.s. (146)
    1823,   #	  Bulgarian
    1824,   #	  Albertan
    1825,   #	  Ghanaian
    1826,   #	  Barbadian
    1827,   #	  African American
    1828,   #	  Yugoslavian, n.o.s. (147)
    1829,   #	  Tunisian
    1830,   #	  Slavic, n.o.s. (148)
    1831,   #	  Cuban
    1832,   #	  Bosnian
    1833,   #	  Venezuelan
    1834,   #	  Innu/Montagnais, n.o.s. (149)
    1835,   #	  Latvian
    1836,   #	  Bengali
    1837,   #	  Cameroonian
    1838,   #	  Guatemalan
    1839,   #	  Indonesian
    1840,   #	  Laotian
    1841,   #	  Ilocano
    1842,   #	  Northern Irish
    1843,   #	  Celtic, n.o.s. (150)
    1844,   #	  British Columbian
    1845,   #	  Ecuadorian
    1846,   #	  Franco Ontarian
    1847,   #	  Argentinian
    1848,   #	  Estonian
    1849,   #	  Kurdish
    1850,   #	  Fijian
    1851,   #	  Jatt
    1852,   #	  North American, n.o.s. (151)
    1853,   #	  Coptic
    1854,   #	  Thai
    1855,   #	  Dominican
    1856,   #	  Nepali
    1857,   #	  Kabyle
    1858,   #	  Assyrian
    1859,   #	  Igbo
    1860,   #	  Byelorussian
    1861,   #	  Dene, n.o.s. (152)
    1862,   #	  Blackfoot, n.o.s. (153)
    1863,   #	  Abenaki
    1864,   #	  Moldovan
    1865,   #	  Iroquois (Haudenosaunee), n.o.s. (154)
    1866,   #	  New Zealander
    1867,   #	  Sudanese
    1868,   #	  Breton
    1869,   #	  Pennsylvania Dutch
    1870,   #	  Malaysian
    1871,   #	  Plains Cree
    1872,   #	  North African, n.o.s. (155)
    1873,   #	  Huron (Wendat)
    1874,   #	  Saskatchewanian
    1875,   #	  Buddhist
    1876,   #	  Gaspesian
    1877,   #	  Norman
    1878,   #	  Southern or East African, n.o.s. (156)
    1879,   #	  Ivorian
    1880,   #	  Saulteaux
    1881,   #	  Anishinaabe, n.o.s. (157)
    1882,   #	  Burundian
    1883,   #	  Tigrinya
    1884,   #	  Nicaraguan
    1885,   #	  Mauritian
    1886,   #	  Kenyan
    1887,   #	  Oji-Cree
    1888,   #	  Vincentian
    1889,   #	  Jordanian
    1890,   #	  Manitoban
    1891,   #	  Cape Bretoner
    1892,   #	  Rwandan
    1893,   #	  Grenadian
    1894,   #	  Malayali
    1895,   #	  Chaldean
    1896,   #	  Sinhalese
    1897,   #	  Mayan
    1898,   #	  Honduran
    1899,   #	  Cherokee
    1900,   #	  Qalipu Mi'kmaq
    1901,   #	  Indo-Caribbean
    1902,   #	  Flemish
    1903,   #	  United Empire Loyalist
    1904,   #	  Senegalese
    1905,   #	  Azerbaijani
    1906,   #	  Sicilian
    1907,   #	  Pashtun
    1908,   #	  Malay
    1909,   #	  Goan
    1910,   #	  Bantu, n.o.s. (158)
    1911,   #	  Tibetan
    1912,   #	  Zimbabwean
    1913,   #	  Burmese
    1914,   #	  Mongolian
    1915,   #	  Azorean
    1916,   #	  Atikamekw
    1917,   #	  Bamileke
    1918,   #	  Indo-Guyanese
    1919,   #	  Ugandan
    1920,   #	  Oromo
    1921,   #	  Tanzanian
    1922,   #	  Yemeni
    1923,   #	  Central African
    1924,   #	  Libyan
    1925,   #	  Basque
    1926,   #	  Uruguayan
    1927,   #	  Akan, n.o.s. (159)
    1928,   #	  Central or West African, n.o.s. (160)
    1929,   #	  Igorot
    1930,   #	  Fulani
    1931,   #	  Woodland Cree
    1932,   #	  Guinean
    1933,   #	  St. Lucian
    1934,   #	  Prince Edward Islander
    1935,   #	  Maliseet
    1936,   #	  Beninese
    1937,   #	  Telugu
    1938,   #	  Roma
    1939,   #	  Costa Rican
    1940,   #	  African Nova Scotian
    1941,   #	  Malagasy
    1942,   #	  Kashmiri
    1943,   #	  Singaporean
    1944,   #	  Karen
    1945,   #	  Edo
    1946,   #	  Tajik
    1947,   #	  Amhara
    1948,   #	  Paraguayan
    1949,   #	Total - Religion for the population in private households - 25% sample data (161)
    1950,   #	  Buddhist
    1951,   #	  Christian
    1952,   #	    Christian, n.o.s. (162)
    1953,   #	    Anabaptist
    1954,   #	    Anglican
    1955,   #	    Baptist
    1956,   #	    Catholic
    1957,   #	    Christian Orthodox
    1958,   #	    Jehovah's Witness
    1959,   #	    Latter Day Saints
    1960,   #	    Lutheran
    1961,   #	    Methodist and Wesleyan (Holiness)
    1962,   #	    Pentecostal and other Charismatic
    1963,   #	    Presbyterian
    1964,   #	    Reformed
    1965,   #	    United Church
    1966,   #	    Other Christian and Christian-related traditions
    1967,   #	  Hindu
    1968,   #	  Jewish
    1969,   #	  Muslim
    1970,   #	  Sikh
    1971,   #	  Traditional (North American Indigenous) spirituality
    1972,   #	  Other religions and spiritual traditions
    1973,   #	  No religion and secular perspectives
    1974,   #	Total - Mobility status 1 year ago - 25% sample data (163)
    1975,   #	  Non-movers
    1976,   #	  Movers
    1977,   #	    Non-migrants
    1978,   #	    Migrants
    1979,   #	      Internal migrants
    1980,   #	        Intraprovincial migrants
    1981,   #	        Interprovincial migrants
    1982,   #	      External migrants
    1983,   #	Total - Mobility status 5 years ago - 25% sample data (164)
    1984,   #	  Non-movers
    1985,   #	  Movers
    1986,   #	    Non-migrants
    1987,   #	    Migrants
    1988,   #	      Internal migrants
    1989,   #	        Intraprovincial migrants
    1990,   #	        Interprovincial migrants
    1991,   #	      External migrants
    1992,   #	Total - Secondary (high) school diploma or equivalency certificate for the population aged 15 years and over in private households - 25% sample data (165)
    1993,   #	  No high school diploma or equivalency certificate
    1994,   #	  With high school diploma or equivalency certificate (166)
    1995,   #	Total - Secondary (high) school diploma or equivalency certificate for the population aged 25 to 64 years in private households - 25% sample data (165)
    1996,   #	  No high school diploma or equivalency certificate
    1997,   #	  With high school diploma or equivalency certificate (166)
    1998,   #	Total - Highest certificate, diploma or degree for the population aged 15 years and over in private households - 25% sample data (165)
    1999,   #	  No certificate, diploma or degree
    2000,   #	  High (secondary) school diploma or equivalency certificate (167)
    2001,   #	  Postsecondary certificate, diploma or degree
    2002,   #	    Postsecondary certificate or diploma below bachelor level
    2003,   #	      Apprenticeship or trades certificate or diploma
    2004,   #	        Non-apprenticeship trades certificate or diploma (168)
    2005,   #	        Apprenticeship certificate (169)
    2006,   #	      College, CEGEP or other non-university certificate or diploma (170)
    2007,   #	      University certificate or diploma below bachelor level
    2008,   #	    Bachelor's degree or higher
    2009,   #	      Bachelor's degree
    2010,   #	      University certificate or diploma above bachelor level
    2011,   #	      Degree in medicine, dentistry, veterinary medicine or optometry
    2012,   #	      Master's degree
    2013,   #	      Earned doctorate (171)
    2014,   #	Total - Highest certificate, diploma or degree for the population aged 25 to 64 years in private households - 25% sample data (165)
    2015,   #	  No certificate, diploma or degree
    2016,   #	  High (secondary) school diploma or equivalency certificate (167)
    2017,   #	  Postsecondary certificate, diploma or degree
    2018,   #	    Postsecondary certificate or diploma below bachelor level
    2019,   #	      Apprenticeship or trades certificate or diploma
    2020,   #	        Non-apprenticeship trades certificate or diploma (168)
    2021,   #	        Apprenticeship certificate (169)
    2022,   #	      College, CEGEP or other non-university certificate or diploma (170)
    2023,   #	      University certificate or diploma below bachelor level
    2024,   #	    Bachelor's degree or higher
    2025,   #	      Bachelor's degree
    2026,   #	      University certificate or diploma above bachelor level
    2027,   #	      Degree in medicine, dentistry, veterinary medicine or optometry
    2028,   #	      Master's degree
    2029,   #	      Earned doctorate (171)
    2030,   #	Total - Major field of study - Classification of Instructional Programs (CIP) 2021 for the population aged 15 years and over in private households - 25% sample data (172)
    2031,   #	  No postsecondary certificate, diploma or degree (173)
    2032,   #	  Education
    2033,   #	    13. Education
    2034,   #	  Visual and performing arts, and communications technologies
    2035,   #	    10. Communications technologies/technicians and support services
    2036,   #	    50. Visual and performing arts
    2037,   #	  Humanities
    2038,   #	    16. Indigenous and foreign languages, literatures, and linguistics
    2039,   #	    23. English language and literature/letters
    2040,   #	    24. Liberal arts and sciences, general studies and humanities
    2041,   #	    30A Interdisciplinary humanities (174)
    2042,   #	    38. Philosophy and religious studies
    2043,   #	    39. Theology and religious vocations
    2044,   #	    54. History
    2045,   #	    55. French language and literature/lettersCAN
    2046,   #	  Social and behavioural sciences and law
    2047,   #	    05. Area, ethnic, cultural, gender, and group studies
    2048,   #	    09. Communication, journalism and related programs
    2049,   #	    19. Family and consumer sciences/human sciences
    2050,   #	    22. Legal professions and studies
    2051,   #	    30B Interdisciplinary social and behavioural sciences (175)
    2052,   #	    42. Psychology
    2053,   #	    45. Social sciences
    2054,   #	  Business, management and public administration
    2055,   #	    30.16 Accounting and computer science
    2056,   #	    44. Public administration and social service professions
    2057,   #	    52. Business, management, marketing and related support services
    2058,   #	  Physical and life sciences and technologies
    2059,   #	    26. Biological and biomedical sciences
    2060,   #	    30.01 Biological and physical sciences
    2061,   #	    30C Other interdisciplinary physical and life sciences (176)
    2062,   #	    40. Physical sciences
    2063,   #	    41. Science technologies/technicians
    2064,   #	  Mathematics, computer and information sciences
    2065,   #	    11. Computer and information sciences and support services
    2066,   #	    25. Library science
    2067,   #	    27. Mathematics and statistics
    2068,   #	    30D Interdisciplinary mathematics, computer and information sciences (177)
    2069,   #	  Architecture, engineering, and related trades
    2070,   #	    04. Architecture and related services
    2071,   #	    14. Engineering
    2072,   #	    15. Engineering/engineering-related technologies/technicians
    2073,   #	    30.12 Historic preservation and conservation
    2074,   #	    46. Construction trades
    2075,   #	    47. Mechanic and repair technologies/technicians
    2076,   #	    48. Precision production
    2077,   #	  Agriculture, natural resources and conservation
    2078,   #	    01. Agricultural and veterinary sciences/services/operations and related fields (178)
    2079,   #	    03. Natural resources and conservation
    2080,   #	  Health and related fields
    2081,   #	    30.37 Design for human health
    2082,   #	    31. Parks, recreation, leisure, fitness, and kinesiology
    2083,   #	    51. Health professions and related programs (178)
    2084,   #	    60. Health professions residency/fellowship programs
    2085,   #	    61. Medical residency/fellowship programs
    2086,   #	  Personal, protective and transportation services
    2087,   #	    12. Culinary, entertainment, and personal services
    2088,   #	    28. Military science, leadership and operational art
    2089,   #	    29. Military technologies and applied sciences
    2090,   #	    43. Security and protective services
    2091,   #	    49. Transportation and materials moving
    2092,   #	  Other (179)
    2093,   #	Total - Major field of study - Classification of Instructional Programs (CIP) 2021 for the population aged 25 to 64 years in private households - 25% sample data (172)
    2094,   #	  No postsecondary certificate, diploma or degree (173)
    2095,   #	  Education
    2096,   #	    13. Education
    2097,   #	  Visual and performing arts, and communications technologies
    2098,   #	    10. Communications technologies/technicians and support services
    2099,   #	    50. Visual and performing arts
    2100,   #	  Humanities
    2101,   #	    16. Indigenous and foreign languages, literatures, and linguistics
    2102,   #	    23. English language and literature/letters
    2103,   #	    24. Liberal arts and sciences, general studies and humanities
    2104,   #	    30A Interdisciplinary humanities (174)
    2105,   #	    38. Philosophy and religious studies
    2106,   #	    39. Theology and religious vocations
    2107,   #	    54. History
    2108,   #	    55. French language and literature/lettersCAN
    2109,   #	  Social and behavioural sciences and law
    2110,   #	    05. Area, ethnic, cultural, gender, and group studies
    2111,   #	    09. Communication, journalism and related programs
    2112,   #	    19. Family and consumer sciences/human sciences
    2113,   #	    22. Legal professions and studies
    2114,   #	    30B Interdisciplinary social and behavioural sciences (175)
    2115,   #	    42. Psychology
    2116,   #	    45. Social sciences
    2117,   #	  Business, management and public administration
    2118,   #	    30.16 Accounting and computer science
    2119,   #	    44. Public administration and social service professions
    2120,   #	    52. Business, management, marketing and related support services
    2121,   #	  Physical and life sciences and technologies
    2122,   #	    26. Biological and biomedical sciences
    2123,   #	    30.01 Biological and physical sciences
    2124,   #	    30C Other interdisciplinary physical and life sciences (176)
    2125,   #	    40. Physical sciences
    2126,   #	    41. Science technologies/technicians
    2127,   #	  Mathematics, computer and information sciences
    2128,   #	    11. Computer and information sciences and support services
    2129,   #	    25. Library science
    2130,   #	    27. Mathematics and statistics
    2131,   #	    30D Interdisciplinary mathematics, computer and information sciences (177)
    2132,   #	  Architecture, engineering, and related trades
    2133,   #	    04. Architecture and related services
    2134,   #	    14. Engineering
    2135,   #	    15. Engineering/engineering-related technologies/technicians
    2136,   #	    30.12 Historic preservation and conservation
    2137,   #	    46. Construction trades
    2138,   #	    47. Mechanic and repair technologies/technicians
    2139,   #	    48. Precision production
    2140,   #	  Agriculture, natural resources and conservation
    2141,   #	    01. Agricultural and veterinary sciences/services/operations and related fields (178)
    2142,   #	    03. Natural resources and conservation
    2143,   #	  Health and related fields
    2144,   #	    30.37 Design for human health
    2145,   #	    31. Parks, recreation, leisure, fitness, and kinesiology
    2146,   #	    51. Health professions and related programs (178)
    2147,   #	    60. Health professions residency/fellowship programs
    2148,   #	    61. Medical residency/fellowship programs
    2149,   #	  Personal, protective and transportation services
    2150,   #	    12. Culinary, entertainment, and personal services
    2151,   #	    28. Military science, leadership and operational art
    2152,   #	    29. Military technologies and applied sciences
    2153,   #	    43. Security and protective services
    2154,   #	    49. Transportation and materials moving
    2155,   #	  Other (179)
    2156,   #	Total - Location of study compared with province or territory of residence for the population aged 25 to 64 years in private households - 25% sample data (180)
    2157,   #	  No postsecondary certificate, diploma or degree
    2158,   #	  Postsecondary certificate, diploma or degree (181)
    2159,   #	    Location of study inside Canada
    2160,   #	      Same as province or territory of residence
    2161,   #	      Different than province or territory of residence
    2162,   #	    Location of study outside Canada (182)
    2163,   #	      Americas
    2164,   #	        United States of America
    2165,   #	        Mexico
    2166,   #	        Cuba
    2167,   #	        Haiti
    2168,   #	        Jamaica
    2169,   #	        Brazil
    2170,   #	        Colombia
    2171,   #	        Peru
    2172,   #	        Venezuela (95)
    2173,   #	        Other locations of study in Americas
    2174,   #	      Europe
    2175,   #	        Belgium
    2176,   #	        France
    2177,   #	        Germany
    2178,   #	        Netherlands
    2179,   #	        Switzerland
    2180,   #	        Hungary
    2181,   #	        Moldova (183)
    2182,   #	        Poland
    2183,   #	        Romania
    2184,   #	        Russian Federation
    2185,   #	        Ukraine
    2186,   #	        Ireland (96)
    2187,   #	        United Kingdom (87)
    2188,   #	        Bosnia and Herzegovina
    2189,   #	        Italy
    2190,   #	        Serbia (86)
    2191,   #	        Other locations of study in Europe
    2192,   #	      Africa
    2193,   #	        Nigeria
    2194,   #	        Algeria
    2195,   #	        Morocco
    2196,   #	        Tunisia
    2197,   #	        Egypt
    2198,   #	        South Africa, Republic of
    2199,   #	        Other locations of study in Africa
    2200,   #	      Asia
    2201,   #	        Iran (88)
    2202,   #	        Iraq
    2203,   #	        Israel
    2204,   #	        Lebanon
    2205,   #	        Syria (89)
    2206,   #	        Turkey
    2207,   #	        China (90)
    2208,   #	        Taiwan
    2209,   #	        Hong Kong (91)
    2210,   #	        Japan
    2211,   #	        Korea, South (92)
    2212,   #	        Philippines
    2213,   #	        Viet Nam
    2214,   #	        Bangladesh
    2215,   #	        Sri Lanka
    2216,   #	        India
    2217,   #	        Pakistan
    2218,   #	        Other locations of study in Asia
    2219,   #	      Oceania
    2220,   #	        Australia
    2221,   #	        New Zealand
    2222,   #	        Other locations of study in Oceania
    2223,   #	Total - Population aged 15 years and over by labour force status - 25% sample data (184)
    2224,   #	  In the labour force
    2225,   #	    Employed
    2226,   #	    Unemployed
    2227,   #	  Not in the labour force
    2228,   #	Participation rate
    2229,   #	Employment rate
    2230,   #	Unemployment rate
    2231,   #	Total - Population aged 15 years and over by work activity during the reference year - 25% sample data (185)
    2232,   #	  Did not work (186)
    2233,   #	  Worked
    2234,   #	    Worked full year full time (187)
    2235,   #	    Worked part year and/or part time (188)
    2236,   #	    Average weeks worked in reference year
    2237,   #	Total - Labour force aged 15 years and over by class of worker including job permanency - 25% sample data (189)
    2238,   #	  Class of worker - not applicable (190)
    2239,   #	  All classes of workers (191)
    2240,   #	    Employee
    2241,   #	      Permanent position
    2242,   #	      Temporary position
    2243,   #	        Fixed term (1 year or more)
    2244,   #	        Casual, seasonal or short-term position (less than 1 year)
    2245,   #	    Self-employed (192)
    2246,   #	Total - Labour force aged 15 years and over by occupation - Broad category - National Occupational Classification (NOC) 2021 - 25% sample data (193)
    2247,   #	  Occupation - not applicable (190)
    2248,   #	  All occupations (191)
    2249,   #	    0 Legislative and senior management occupations
    2250,   #	    1 Business, finance and administration occupations
    2251,   #	    2 Natural and applied sciences and related occupations
    2252,   #	    3 Health occupations
    2253,   #	    4 Occupations in education, law and social, community and government services
    2254,   #	    5 Occupations in art, culture, recreation and sport
    2255,   #	    6 Sales and service occupations
    2256,   #	    7 Trades, transport and equipment operators and related occupations
    2257,   #	    8 Natural resources, agriculture and related production occupations
    2258,   #	    9 Occupations in manufacturing and utilities
    2259,   #	Total - Labour force aged 15 years and over by industry - Sectors - North American Industry Classification System (NAICS) 2017 - 25% sample data (194)
    2260,   #	  Industry - not applicable (190)
    2261,   #	  All industries (191)
    2262,   #	    11 Agriculture, forestry, fishing and hunting
    2263,   #	    21 Mining, quarrying, and oil and gas extraction
    2264,   #	    22 Utilities
    2265,   #	    23 Construction
    2266,   #	    31-33 Manufacturing
    2267,   #	    41 Wholesale trade
    2268,   #	    44-45 Retail trade
    2269,   #	    48-49 Transportation and warehousing
    2270,   #	    51 Information and cultural industries
    2271,   #	    52 Finance and insurance
    2272,   #	    53 Real estate and rental and leasing
    2273,   #	    54 Professional, scientific and technical services
    2274,   #	    55 Management of companies and enterprises
    2275,   #	    56 Administrative and support, waste management and remediation services
    2276,   #	    61 Educational services
    2277,   #	    62 Health care and social assistance
    2278,   #	    71 Arts, entertainment and recreation
    2279,   #	    72 Accommodation and food services
    2280,   #	    81 Other services (except public administration)
    2281,   #	    91 Public administration
    2282,   #	Total - All languages used at work for the population in private households aged 15 years and over who worked since January 1, 2020 - 25% sample data (195)
    2283,   #	  English
    2284,   #	  French
    2285,   #	  Non-official language
    2286,   #	    Indigenous (39)
    2287,   #	    Non-Indigenous
    2288,   #	  English and French
    2289,   #	  English and non-official language(s)
    2290,   #	  French and non-official language(s)
    2291,   #	  English, French and non-official language(s)
    2292,   #	  Multiple non-official languages
    2293,   #	Total - Language used most often at work for the population aged 15 years and over who worked since January 1, 2020, in private households, 2021 Census - 25% sample data (196)
    2294,   #	  Single responses
    2295,   #	    Official languages
    2296,   #	      English
    2297,   #	      French
    2298,   #	    Non-official languages
    2299,   #	      Indigenous languages (39)
    2300,   #	        Algonquian languages
    2301,   #	          Blackfoot
    2302,   #	          Cree-Innu languages
    2303,   #	            Atikamekw
    2304,   #	            Cree languages
    2305,   #	              Ililimowin (Moose Cree)
    2306,   #	              Inu Ayimun (Southern East Cree)
    2307,   #	              Iyiyiw-Ayimiwin (Northern East Cree)
    2308,   #	              Nehinawewin (Swampy Cree)
    2309,   #	              Nehiyawewin (Plains Cree)
    2310,   #	              Nihithawiwin (Woods Cree)
    2311,   #	              Cree, n.o.s.
    2312,   #	            Innu (Montagnais)
    2313,   #	            Naskapi
    2314,   #	          Eastern Algonquian languages
    2315,   #	            Mi'kmaq
    2316,   #	            Wolastoqewi (Malecite)
    2317,   #	          Ojibway-Potawatomi languages
    2318,   #	            Anicinabemowin (Algonquin)
    2319,   #	            Oji-Cree
    2320,   #	            Ojibway languages
    2321,   #	              Anishinaabemowin (Chippewa)
    2322,   #	              Daawaamwin (Odawa)
    2323,   #	              Saulteau (Western Ojibway)
    2324,   #	              Ojibway, n.o.s.
    2325,   #	          Algonquian languages, n.i.e.
    2326,   #	        Athabaskan languages
    2327,   #	          Northern Athabaskan languages
    2328,   #	            Dakelh (Carrier)
    2329,   #	            Dane-zaa (Beaver)
    2330,   #	            Dene, n.o.s.
    2331,   #	            Gwich'in
    2332,   #	            Slavey-Hare languages
    2333,   #	              Deh Gah Ghotie Zhatie (South Slavey)
    2334,   #	              Satuotine Yati (North Slavey)
    2335,   #	              Slavey, n.o.s.
    2336,   #	            Tahltan languages
    2337,   #	            Tlicho (Dogrib)
    2338,   #	            Tse'khene (Sekani)
    2339,   #	            Tsilhqot'in (Chilcotin)
    2340,   #	            Tsuu T'ina (Sarsi)
    2341,   #	            Tutchone languages
    2342,   #	              Northern Tutchone
    2343,   #	              Southern Tutchone
    2344,   #	              Tutchone, n.o.s.
    2345,   #	            Wetsuwet'en-Babine
    2346,   #	          Tlingit
    2347,   #	          Athabaskan languages, n.i.e.
    2348,   #	        Haida
    2349,   #	        Inuktut (Inuit) languages
    2350,   #	          Inuinnaqtun (Inuvialuktun)
    2351,   #	            Inuinnaqtun
    2352,   #	            Inuvialuktun
    2353,   #	          Inuktitut
    2354,   #	          Inuktut (Inuit) languages, n.i.e.
    2355,   #	        Iroquoian languages
    2356,   #	          Mohawk
    2357,   #	          Oneida
    2358,   #	          Iroquoian languages, n.i.e.
    2359,   #	        Ktunaxa (Kutenai)
    2360,   #	        Michif
    2361,   #	        Salish languages
    2362,   #	          Halkomelem
    2363,   #	          Lillooet
    2364,   #	          Ntlakapamux (Thompson)
    2365,   #	          Secwepemctsin (Shuswap)
    2366,   #	          Squamish
    2367,   #	          Straits
    2368,   #	          Syilx (Okanagan)
    2369,   #	          Salish languages, n.i.e.
    2370,   #	        Siouan languages
    2371,   #	          Assiniboine
    2372,   #	          Dakota
    2373,   #	          Stoney
    2374,   #	          Siouan languages, n.i.e.
    2375,   #	        Tsimshian languages
    2376,   #	          Gitxsan (Gitksan)
    2377,   #	          Nisga'a
    2378,   #	          Tsimshian
    2379,   #	        Wakashan languages
    2380,   #	          Haisla
    2381,   #	          Heiltsuk
    2382,   #	          Kwak'wala (Kwakiutl)
    2383,   #	          Nuu-chah-nulth (Nootka)
    2384,   #	          Wakashan languages, n.i.e.
    2385,   #	        Indigenous languages, n.i.e.
    2386,   #	        Indigenous languages, n.o.s.
    2387,   #	      Non-Indigenous languages
    2388,   #	        Afro-Asiatic languages
    2389,   #	          Berber languages
    2390,   #	            Kabyle
    2391,   #	            Tamazight
    2392,   #	            Berber languages, n.i.e.
    2393,   #	          Chadic languages
    2394,   #	          Coptic
    2395,   #	          Cushitic languages
    2396,   #	            Bilen
    2397,   #	            Oromo
    2398,   #	            Somali
    2399,   #	            Cushitic languages, n.i.e.
    2400,   #	          Semitic languages
    2401,   #	            Amharic
    2402,   #	            Arabic
    2403,   #	            Aramaic languages
    2404,   #	              Assyrian Neo-Aramaic
    2405,   #	              Chaldean Neo-Aramaic
    2406,   #	              Aramaic, n.o.s.
    2407,   #	            Hebrew
    2408,   #	            Tigrigna
    2409,   #	            Semitic languages, n.i.e.
    2410,   #	        Austro-Asiatic languages
    2411,   #	          Khmer (Cambodian)
    2412,   #	          Vietnamese
    2413,   #	          Austro-Asiatic languages, n.i.e.
    2414,   #	        Austronesian languages
    2415,   #	          Bikol
    2416,   #	          Bisaya, n.o.s.
    2417,   #	          Cebuano
    2418,   #	          Hiligaynon
    2419,   #	          Ilocano
    2420,   #	          Indonesian
    2421,   #	          Kankanaey
    2422,   #	          Malagasy languages
    2423,   #	          Malay
    2424,   #	          Pampangan (Kapampangan, Pampango)
    2425,   #	          Pangasinan
    2426,   #	          Tagalog (Pilipino, Filipino)
    2427,   #	          Austronesian languages, n.i.e.
    2428,   #	        Creole languages
    2429,   #	          Haitian Creole
    2430,   #	          Jamaican English Creole
    2431,   #	          Morisyen
    2432,   #	          Creole, n.o.s.
    2433,   #	          Creole languages, n.i.e.
    2434,   #	        Dravidian languages
    2435,   #	          Kannada
    2436,   #	          Malayalam
    2437,   #	          Tamil
    2438,   #	          Telugu
    2439,   #	          Dravidian languages, n.i.e.
    2440,   #	        Georgian
    2441,   #	        Indo-European languages
    2442,   #	          Albanian
    2443,   #	          Armenian
    2444,   #	          Balto-Slavic languages
    2445,   #	            Baltic languages
    2446,   #	              Latvian
    2447,   #	              Lithuanian
    2448,   #	            Slavic languages
    2449,   #	              Bulgarian
    2450,   #	              Czech
    2451,   #	              Macedonian
    2452,   #	              Polish
    2453,   #	              Russian
    2454,   #	              Serbo-Croatian
    2455,   #	                Bosnian
    2456,   #	                Croatian
    2457,   #	                Serbian
    2458,   #	                Serbo-Croatian, n.i.e.
    2459,   #	              Slovak
    2460,   #	              Slovene (Slovenian)
    2461,   #	              Ukrainian
    2462,   #	              Slavic languages, n.i.e.
    2463,   #	          Celtic languages
    2464,   #	            Scottish Gaelic
    2465,   #	            Celtic languages, n.i.e.
    2466,   #	          Germanic languages
    2467,   #	            Frisian
    2468,   #	            High German languages
    2469,   #	              German
    2470,   #	              Pennsylvania German
    2471,   #	              Swiss German
    2472,   #	              Yiddish
    2473,   #	            Low Saxon-Low Franconian languages
    2474,   #	              Afrikaans
    2475,   #	              Dutch
    2476,   #	              Low German, n.o.s.
    2477,   #	              Low Saxon
    2478,   #	              Plautdietsch
    2479,   #	              Vlaams (Flemish)
    2480,   #	            Scandinavian languages
    2481,   #	              Danish
    2482,   #	              Icelandic
    2483,   #	              Norwegian
    2484,   #	              Swedish
    2485,   #	            Germanic languages, n.i.e.
    2486,   #	          Greek
    2487,   #	          Indo-Iranian languages
    2488,   #	            Indo-Aryan languages
    2489,   #	              Bengali
    2490,   #	              Gujarati
    2491,   #	              Hindi
    2492,   #	              Kacchi
    2493,   #	              Marathi
    2494,   #	              Nepali
    2495,   #	              Punjabi (Panjabi)
    2496,   #	              Sindhi
    2497,   #	              Sinhala (Sinhalese)
    2498,   #	              Urdu
    2499,   #	              Indo-Aryan languages, n.i.e.
    2500,   #	            Iranian languages
    2501,   #	              Kurdish
    2502,   #	              Pashto
    2503,   #	              Persian languages
    2504,   #	                Dari
    2505,   #	                Iranian Persian
    2506,   #	                Persian (Farsi), n.o.s.
    2507,   #	              Iranian languages, n.i.e.
    2508,   #	            Indo-Iranian languages, n.i.e.
    2509,   #	          Italic (Romance) languages
    2510,   #	            Catalan
    2511,   #	            Italian
    2512,   #	            Portuguese
    2513,   #	            Romanian
    2514,   #	            Spanish
    2515,   #	            Italic (Romance) languages, n.i.e.
    2516,   #	          Indo-European languages, n.i.e.
    2517,   #	        Japanese
    2518,   #	        Korean
    2519,   #	        Mongolian
    2520,   #	        Niger-Congo languages
    2521,   #	          Akan (Twi)
    2522,   #	          Edo
    2523,   #	          Fulah (Pular, Pulaar, Fulfulde)
    2524,   #	          Ga
    2525,   #	          Ganda
    2526,   #	          Igbo
    2527,   #	          Kinyarwanda (Rwanda)
    2528,   #	          Lingala
    2529,   #	          Rundi (Kirundi)
    2530,   #	          Shona
    2531,   #	          Swahili
    2532,   #	          Wolof
    2533,   #	          Yoruba
    2534,   #	          Niger-Congo languages, n.i.e.
    2535,   #	        Nilo-Saharan languages
    2536,   #	          Dinka
    2537,   #	          Nilo-Saharan languages, n.i.e.
    2538,   #	        Sign languages
    2539,   #	          American Sign Language
    2540,   #	          Quebec Sign Language
    2541,   #	          Sign languages, n.i.e.
    2542,   #	        Sino-Tibetan languages
    2543,   #	          Chinese languages
    2544,   #	            Hakka
    2545,   #	            Mandarin
    2546,   #	            Min Dong
    2547,   #	            Min Nan (Chaochow, Teochow, Fukien, Taiwanese)
    2548,   #	            Wu (Shanghainese)
    2549,   #	            Yue (Cantonese)
    2550,   #	            Chinese, n.o.s.
    2551,   #	            Chinese languages, n.i.e.
    2552,   #	          Tibeto-Burman languages
    2553,   #	            Burmese
    2554,   #	            Karenic languages
    2555,   #	              S'gaw Karen
    2556,   #	              Karenic languages, n.i.e.
    2557,   #	            Tibetan
    2558,   #	            Tibeto-Burman languages, n.i.e.
    2559,   #	          Sino-Tibetan languages, n.i.e.
    2560,   #	        Tai-Kadai languages
    2561,   #	          Lao
    2562,   #	          Thai
    2563,   #	          Tai-Kadai languages, n.i.e.
    2564,   #	        Turkic languages
    2565,   #	          Azerbaijani
    2566,   #	          Turkish
    2567,   #	          Uyghur
    2568,   #	          Uzbek
    2569,   #	          Turkic languages, n.i.e.
    2570,   #	        Uralic languages
    2571,   #	          Estonian
    2572,   #	          Finnish
    2573,   #	          Hungarian
    2574,   #	        Other languages, n.i.e.
    2575,   #	  Multiple responses
    2576,   #	    English and French
    2577,   #	    English and non-official language(s)
    2578,   #	    French and non-official language(s)
    2579,   #	    English, French and non-official language(s)
    2580,   #	    Multiple non-official languages
    2581,   #	Total - Other language(s) used regularly at work for the population in private households aged 15 years and over who worked since January 1, 2020 - 25% sample data (197)
    2582,   #	  None
    2583,   #	  English
    2584,   #	  French
    2585,   #	  Non-official language
    2586,   #	    Indigenous (39)
    2587,   #	    Non-Indigenous
    2588,   #	  English and French
    2589,   #	  English and non-official language(s)
    2590,   #	  French and non-official language(s)
    2591,   #	  English, French and non-official language(s)
    2592,   #	  Multiple non-official languages
    2593,   #	Total - Place of work status for the employed labour force aged 15 years and over - 25% sample data (198)
    2594,   #	  Worked at home
    2595,   #	  Worked outside Canada
    2596,   #	  No fixed workplace address
    2597,   #	  Usual place of work
    2598,   #	Total - Commuting destination for the employed labour force aged 15 years and over with a usual place of work - 25% sample data (199)
    2599,   #	  Commute within census subdivision (CSD) of residence
    2600,   #	  Commute to a different census subdivision (CSD) within census division (CD) of residence
    2601,   #	  Commute to a different census subdivision (CSD) and census division (CD) within province or territory of residence
    2602,   #	  Commute to a different province or territory
    2603,   #	Total - Main mode of commuting for the employed labour force aged 15 years and over with a usual place of work or no fixed workplace address - 25% sample data (200)
    2604,   #	  Car, truck or van
    2605,   #	    Car, truck or van - as a driver
    2606,   #	    Car, truck or van - as a passenger
    2607,   #	  Public transit
    2608,   #	  Walked
    2609,   #	  Bicycle
    2610,   #	  Other method
    2611,   #	Total - Commuting duration for the employed labour force aged 15 years and over with a usual place of work or no fixed workplace address - 25% sample data (201)
    2612,   #	  Less than 15 minutes
    2613,   #	  15 to 29 minutes
    2614,   #	  30 to 44 minutes
    2615,   #	  45 to 59 minutes
    2616,   #	  60 minutes and over
    2617,   #	Total - Time leaving for work for the employed labour force aged 15 years and over with a usual place of work or no fixed workplace address - 25% sample data (202)
    2618,   #	  Between 5 a.m. and 5:59 a.m.
    2619,   #	  Between 6 a.m. and 6:59 a.m.
    2620,   #	  Between 7 a.m. and 7:59 a.m.
    2621,   #	  Between 8 a.m. and 8:59 a.m.
    2622,   #	  Between 9 a.m. and 11:59 a.m.
    2623,   #	  Between 12 p.m. and 4:59 a.m.
    2624,   #	Total - Eligibility for instruction in the minority official language for the population in private households born in 2003 or later - 100% data (203)
    2625,   #	  Children eligible for instruction in the minority official language
    2626,   #	  Children not eligible for instruction in the minority official language
    2627,   #	Total - Eligibility and instruction in the minority official language, for the population in private households born between 2003 and 2015 (inclusive) - 100% data (204)
    2628,   #	  Children eligible for instruction in the minority official language
    2629,   #	    Eligible children�who have been instructed in the minority official language at the primary or secondary level in Canada
    2630,   #	    Eligible children�who have not been instructed in the minority official language at the primary or secondary level in Canada
    2631,   #	  Children not eligible for instruction in the minority official language
]