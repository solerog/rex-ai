# author: Quantium Rock
# license: MIT

from data_primary import PrimaryData
from data_secondary import SecondaryData
from data_tertiary import TertiaryData
from merge import merge_db_data
from volatility import VolatilityFeatures
from tendency import TendencyFeatures


def updateDB():

    primaryData = PrimaryData()
    secondaryData = SecondaryData()
    tertiaryData = TertiaryData()

    primaryData.deleteFolder("primary", "2022")

    print("\n### PRIMARY DB ###")
    primaryData.checkDB()

    if primaryData.missing_years:
        # user confirmation
        input("\nUpdate database?\n> Press Enter to proceed\n\n>>> ")
        primaryData.updateDB()

    print("\n### SECONDARY DB ###")
    secondaryData.checkDB()
    secondaryData.updateDB()

    print("\n### TERTIARY DB ###")
    tertiaryData.checkDB()
    tertiaryData.updateDB()

    print("\nPrimary, Secondary & Tertiary DB up to date!")
    input("\nDo you wanna merge db's?\n> Press Enter to proceed\n\n>>> ")

    print("\n### MERGE DB DATA ###")
    merge_db_data()

    print("\nDB's merged successfully.")
    input("\nDo you update indicators?\n> Press Enter to proceed\n\n>>> ")

    TendencyFeatures().getTendency()
    VolatilityFeatures().getVolatility()

    print("\nYour DB is up to date. Bye!\n")

# updateDB()

if __name__ == "__main__":
    updateDB()
