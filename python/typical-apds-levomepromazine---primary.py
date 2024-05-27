# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2024.

import sys, csv, re

codes = [{"code":"64326020","system":"multilex"},{"code":"64327020","system":"multilex"},{"code":"32615020","system":"multilex"},{"code":"66278020","system":"multilex"},{"code":"72988020","system":"multilex"},{"code":"66279020","system":"multilex"},{"code":"55705020","system":"multilex"},{"code":"66282020","system":"multilex"},{"code":"58296020","system":"multilex"},{"code":"87840020","system":"multilex"},{"code":"72183020","system":"multilex"},{"code":"72991020","system":"multilex"},{"code":"72987020","system":"multilex"},{"code":"97323020","system":"multilex"},{"code":"55706020","system":"multilex"},{"code":"66277020","system":"multilex"},{"code":"66283020","system":"multilex"},{"code":"51749020","system":"multilex"},{"code":"72184020","system":"multilex"},{"code":"51751020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('typical-apds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["typical-apds-levomepromazine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["typical-apds-levomepromazine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["typical-apds-levomepromazine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
