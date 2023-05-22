import  re


fname = input('enter file: ')
if len(fname) < 1: fname = './folder/spss.txt'
hand = open (fname)

atm_number_pattern = r"ATM(\d+)"
atm_numbers = re.findall(atm_number_pattern, hand)

percentage_pattern = r"\d+\.\d{2}"
percentages = re.findall(percentage_pattern, hand)

for atm_number, percentage in zip(atm_numbers, percentages):
        print("ATM Number:", atm_number)
        print("Percentage:", percentage)
        print("---")
        










