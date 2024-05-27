# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2024.

import sys, csv, re

codes = [{"code":"67029020","system":"multilex"},{"code":"54412020","system":"multilex"},{"code":"67027020","system":"multilex"},{"code":"75277020","system":"multilex"},{"code":"67032020","system":"multilex"},{"code":"54418020","system":"multilex"},{"code":"54413020","system":"multilex"},{"code":"67037020","system":"multilex"},{"code":"75276020","system":"multilex"},{"code":"55600020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('typical-apds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["typical-apds-thioridazine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["typical-apds-thioridazine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["typical-apds-thioridazine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
