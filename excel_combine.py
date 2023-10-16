import os
import argparse
import pandas as pd 
'''
If we combine the data in Aug 2023 folder, the command to run the code should be:
python excel_combine.py Aug 2023
'''
def main(month: str, year: int) -> None:
    if len(month) != 3: raise ValueError('Make sure to use a 3-letter month code')
    elif len(year) != 4: raise ValueError('Have you input the right year format?')
    cwd = os.getcwd()
    relevant_dir = None
    for dir in os.listdir(cwd):
        path = os.path.join(cwd, dir)
        if dir.lower().split(' ') == [month.lower(), year.lower()] and os.path.isdir(path):
            relevant_dir = path
            print(relevant_dir)
            print(os.path.join(cwd, relevant_dir))
            print(os.listdir(relevant_dir))
    if relevant_dir == None:
        raise FileNotFoundError(f"Couldn't find the right folder for {month} {year}. Make sure that you have downloaded the data and that your input was relevant (month_short_code, full_year)")
    i = 0
    for file in os.listdir(relevant_dir):
        filepath = os.path.join(relevant_dir, file)
        if file.split('.')[-1] != 'xlsx': pass
        elif i == 0 :
            df = pd.read_excel(filepath, converters={'Kunden ID (CWID)':str})
            i+=1
        else:
            df = pd.concat([df, pd.read_excel(filepath)])

    try:
        assert(len(df.Berichtszeitraum.value_counts()) == 1)
        df.to_excel(os.path.join(cwd, f"JLL_ER_{month}{year}_a.xlsx"), index=False)        
    except FileExistsError:
        print(f"The excel file for {month} {year} already exists! Make sure to delete it before running this script")
    except AssertionError:
        print(f"Seems that some of the files in this folder are relevant for different time-periods, please check manually in generated file")
        df.to_excel(os.path.join(cwd, f"JLL_ER_{month}{year}_ERROR_CHECK.xlsx"), index=False)        


if __name__ == "__main__":
    #TODO: Make this argparse fucntional for both JLL and Aengevelt
    parser = argparse.ArgumentParser(description="Accumulate the JLL success reports for the given month and year.")
    parser.add_argument("month", metavar="mmm", help="The three-letter code for the month of interest")
    parser.add_argument("year", metavar="YYYY", help="The 4-digit year of interest")
    year = str(parser.parse_args().year)
    month = str(parser.parse_args().month)

    main(str(month), str(year))
