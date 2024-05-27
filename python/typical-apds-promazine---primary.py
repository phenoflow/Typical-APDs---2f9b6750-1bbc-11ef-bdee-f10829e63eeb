# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2024.

import sys, csv, re

codes = [{"code":"60250020","system":"multilex"},{"code":"72588020","system":"multilex"},{"code":"55203020","system":"multilex"},{"code":"66356020","system":"multilex"},{"code":"61243020","system":"multilex"},{"code":"68532020","system":"multilex"},{"code":"55202020","system":"multilex"},{"code":"61237020","system":"multilex"},{"code":"91408020","system":"multilex"},{"code":"55710020","system":"multilex"},{"code":"58896020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('typical-apds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["typical-apds-promazine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["typical-apds-promazine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["typical-apds-promazine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
