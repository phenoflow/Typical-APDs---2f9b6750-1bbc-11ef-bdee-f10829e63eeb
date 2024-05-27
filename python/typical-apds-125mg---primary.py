# K Windfuhr, D While, N Kapur, D M Ashcroft, E Kontopantelis, M J Carr, J Shaw, L Applyby, R T Webb, 2024.

import sys, csv, re

codes = [{"code":"69868020","system":"multilex"},{"code":"58525020","system":"multilex"},{"code":"67036020","system":"multilex"},{"code":"65188020","system":"multilex"},{"code":"67028020","system":"multilex"},{"code":"67235020","system":"multilex"},{"code":"52087020","system":"multilex"},{"code":"55204020","system":"multilex"},{"code":"4128020","system":"multilex"},{"code":"4129020","system":"multilex"},{"code":"4131020","system":"multilex"},{"code":"91364020","system":"multilex"},{"code":"54234020","system":"multilex"},{"code":"55746020","system":"multilex"},{"code":"67038020","system":"multilex"},{"code":"55228020","system":"multilex"},{"code":"61244020","system":"multilex"},{"code":"72226020","system":"multilex"},{"code":"65587020","system":"multilex"},{"code":"67241020","system":"multilex"},{"code":"55346020","system":"multilex"},{"code":"59028020","system":"multilex"},{"code":"68531020","system":"multilex"},{"code":"99755020","system":"multilex"},{"code":"95203020","system":"multilex"},{"code":"53898020","system":"multilex"},{"code":"55530020","system":"multilex"},{"code":"55351020","system":"multilex"},{"code":"66353020","system":"multilex"},{"code":"54411020","system":"multilex"},{"code":"54878020","system":"multilex"},{"code":"57101020","system":"multilex"},{"code":"4123020","system":"multilex"},{"code":"60605020","system":"multilex"},{"code":"66245020","system":"multilex"},{"code":"91404020","system":"multilex"},{"code":"73791020","system":"multilex"},{"code":"91368020","system":"multilex"},{"code":"56445020","system":"multilex"},{"code":"51692020","system":"multilex"},{"code":"55217020","system":"multilex"},{"code":"56506020","system":"multilex"},{"code":"66237020","system":"multilex"},{"code":"63105020","system":"multilex"},{"code":"56177020","system":"multilex"},{"code":"72187020","system":"multilex"},{"code":"56187020","system":"multilex"},{"code":"96911020","system":"multilex"},{"code":"58894020","system":"multilex"},{"code":"56337020","system":"multilex"},{"code":"61238020","system":"multilex"},{"code":"72597020","system":"multilex"},{"code":"51690020","system":"multilex"},{"code":"64330020","system":"multilex"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('typical-apds-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["typical-apds-125mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["typical-apds-125mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["typical-apds-125mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
