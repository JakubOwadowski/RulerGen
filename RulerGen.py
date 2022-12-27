import random
import json

with open('settings.json') as json_file:
    # Load settings
    settings = json.load(json_file)

    # Generate semi-random birth and death dates for the monarch
    monarch_birth_year = random.randint(settings["monarch-min-birth-year"], settings["monarch-max-birth-year"])
    monarch_birth_month = random.randint(1, 12)
    monarch_birth_day = random.randint(1, 30)
    monarch_death_year = random.randint(settings["monarch-min-death-year"], settings["monarch-max-death-year"])
    if monarch_death_year - monarch_birth_year > settings["monarch-max-age"]:
        monarch_death_year = monarch_birth_year + settings["monarch-max-age"]
    monarch_death_month = random.randint(1, 12)
    monarch_death_day = random.randint(1, 30)

    # Generate semi-random birth and death dates for the queen
    queen_birth_year = random.randint(settings["queen-min-birth-year"], settings["queen-max-birth-year"])
    queen_birth_month = random.randint(1, 12)
    queen_birth_day = random.randint(1, 28)
    queen_death_year = random.randint(settings["queen-min-death-year"], settings["queen-max-death-year"])
    if queen_death_year - queen_birth_year > settings["queen-max-age"]:
        queen_death_year = queen_birth_year + settings["queen-max-age"]
    queen_death_month = random.randint(1, 12)
    queen_death_day = random.randint(1, 28)

    # Generate semi-random birth and death dates for the heir
    heir_birth_year = random.randint(settings["heir-min-birth-year"], settings["heir-max-birth-year"])
    heir_birth_month = random.randint(1, 12)
    heir_birth_day = random.randint(1, 28)
    heir_death_year = random.randint(settings["heir-min-death-year"], settings["heir-max-death-year"])
    if heir_death_year - heir_birth_year > settings["heir-max-age"]:
        heir_death_year = heir_birth_year + settings["heir-max-age"]
    heir_death_month = random.randint(1, 12)
    heir_death_day = random.randint(1, 28)

    # Generate a random value for "claim" that can only change by 5
    claim = random.randint(settings["heir-mid-claim"], settings["heir-max-claim"])\
        if random.random() <= settings["heir-high-claim-threshold"]\
        else random.randint(settings["heir-min-claim"], settings["heir-mid-claim"])
    if claim % settings["heir-claim-step"] != 0:
        claim += settings["heir-claim-step"] - (claim % settings["heir-claim-step"])

    # Generate random values for "adm", "dip", and "mil"
    monarch_adm = random.randint(0, 6)
    monarch_dip = random.randint(0, 6)
    monarch_mil = random.randint(0, 6)
    heir_adm = random.randint(0, 6)
    heir_dip = random.randint(0, 6)
    heir_mil = random.randint(0, 6)
    queen_adm = random.randint(0, 6)
    queen_dip = random.randint(0, 6)
    queen_mil = random.randint(0, 6)

    # Apply the caveat that if one of the stats (adm, dip, mil) is high, it is more likely that the other stats will
    # also be high, and if one of the stats is very low, it is more likely that the other stats will be low as well
    if monarch_adm >= settings["skill-buff-threshold"]:
        monarch_dip += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        monarch_mil += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if monarch_adm <= settings["skill-debuff-threshold"]:
        monarch_dip -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        monarch_mil -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
    if monarch_dip >= settings["skill-buff-threshold"]:
        monarch_adm += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        monarch_mil += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if monarch_dip <= settings["skill-debuff-threshold"]:
        monarch_adm -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        monarch_mil -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
    if monarch_mil >= settings["skill-buff-threshold"]:
        monarch_adm += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        monarch_dip += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if monarch_mil <= settings["skill-debuff-threshold"]:
        monarch_adm -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        monarch_dip -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])

    if heir_adm >= settings["skill-buff-threshold"]:
        heir_dip += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        heir_mil += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if heir_adm <= settings["skill-debuff-threshold"]:
        heir_dip -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        heir_mil -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
    if heir_dip >= settings["skill-buff-threshold"]:
        heir_adm += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        heir_mil += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if heir_dip <= settings["skill-debuff-threshold"]:
        heir_adm -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        heir_mil -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
    if heir_mil >= settings["skill-buff-threshold"]:
        heir_adm += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        heir_dip += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if heir_mil <= settings["skill-debuff-threshold"]:
        heir_adm -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        heir_dip -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])

    if queen_adm >= settings["skill-buff-threshold"]:
        queen_dip += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        queen_mil += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if queen_adm <= settings["skill-debuff-threshold"]:
        queen_dip -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        queen_mil -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
    if queen_dip >= settings["skill-buff-threshold"]:
        queen_adm += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        queen_mil += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if queen_dip <= settings["skill-debuff-threshold"]:
        queen_adm -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        queen_mil -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
    if queen_mil >= settings["skill-buff-threshold"]:
        queen_adm += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
        queen_dip += random.randint(settings["skill-buff-min"], settings["skill-buff-max"])
    if queen_mil <= settings["skill-debuff-threshold"]:
        queen_adm -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])
        queen_dip -= random.randint(settings["skill-debuff-min"], settings["skill-debuff-max"])

    if monarch_adm > 6:
        monarch_adm = 6
    if monarch_dip > 6:
        monarch_dip = 6
    if monarch_mil > 6:
        monarch_mil = 6
    if heir_adm > 6:
        heir_adm = 6
    if heir_dip > 6:
        heir_dip = 6
    if heir_mil > 6:
        heir_mil = 6
    if queen_adm > 6:
        queen_adm = 6
    if queen_dip > 6:
        queen_dip = 6
    if queen_mil > 6:
        queen_mil = 6
    if monarch_adm < 0:
        monarch_adm = 0
    if monarch_dip < 0:
        monarch_dip = 0
    if monarch_mil < 0:
        monarch_mil = 0
    if heir_adm < 0:
        heir_adm = 0
    if heir_dip < 0:
        heir_dip = 0
    if heir_mil < 0:
        heir_mil = 0
    if queen_adm < 0:
        queen_adm = 0
    if queen_dip < 0:
        queen_dip = 0
    if queen_mil < 0:
        queen_mil = 0

    # Print the generated values
    print(settings["date"], end="")
    print(".1.1 = {")
    print("\tmonarch = {")
    print("\t\tname = \"NAME\"")
    print("\t\tdynasty = \"DYNASTY\"")
    print(f"\t\tbirth_date = {monarch_birth_year}.{monarch_birth_month}.{monarch_birth_day}")
    print(f"\t\tdeath_date = {monarch_death_year}.{monarch_death_month}.{monarch_death_day}")
    print(f"\t\tadm = {monarch_adm}")
    print(f"\t\tdip = {monarch_dip}")
    print(f"\t\tmil = {monarch_mil}")
    print("\t}")
    if random.random() <= settings["heir-chance"]:
        print("\their = {")
        print("\t\tname = \"NAME\"")
        print("\t\tmonarch_name = \"MONARCHNAME\"")
        print("\t\tdynasty = \"DYNASTY\"")
        print(f"\t\tbirth_date = {heir_birth_year}.{heir_birth_month}.{heir_birth_day}")
        print(f"\t\tdeath_date = {heir_death_year}.{heir_death_month}.{heir_death_day}")
        if random.random() <= settings["female-heir-chance"]:
            print("\t\tfemale = yes")
        print(f"\t\tclaim = {claim}")
        print(f"\t\tadm = {heir_adm}")
        print(f"\t\tdip = {heir_dip}")
        print(f"\t\tmil = {heir_mil}")
        print("\t}")
    if random.random() <= settings["queen-chance"]:
        print("\tqueen = {")
        print("\t\tname = \"NAME\"")
        print("\t\tdynasty = \"DYNASTY\"")
        print(f"\t\tbirth_date = {queen_birth_year}.{queen_birth_month}.{queen_birth_day}")
        print(f"\t\tdeath_date = {queen_death_year}.{queen_death_month}.{queen_death_day}")
        print("\t\tfemale = yes")
        print(f"\t\tadm = {queen_adm}")
        print(f"\t\tdip = {queen_dip}")
        print(f"\t\tmil = {queen_mil}")
        print("\t}")
    print("}")
    input("Press any key to continue...")
