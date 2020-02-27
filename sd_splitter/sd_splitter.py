input_path = r"D:\D_drive_BACKUP\MENTOR\Jira\RAN-15574\3800\SD\CFGMML-RNC3800_RNC3200_RNC3600-10.249.155.161-20200127130605.txt"
# input_path = r"D:\D_drive_BACKUP\MENTOR\Jira\RAN-15574\script_requirement.txt"

with open(input_path, 'r') as combined_sd:
    rows = combined_sd.readlines()
    rowindex = -1
    master_RNCID = None
    master_RNC_postion = None
    master_RNC_SD_file = None
    for row in rows:
        rowindex +=1
        row = row.rstrip("\n")
        if "System BSCID" in row:
            # TODO Note this information
            master_RNCID = row.split(":")[1].strip()
            master_RNC_postion = rowindex
            master_RNC_SD_file = "CFGMML-{}.txt".format(master_RNCID)
            with open(master_RNC_SD_file, 'w') as master_SD_object:
                for index in range(0, master_RNC_postion+1):
                    master_SD_object.write(rows[index])

            break
    # TODO file is created for master RNC, now we will populate data into the SD file
    row_dataindex = -1
    with open(master_RNC_SD_file, 'a') as master_SD_object_data:
        for row_data in rows:
            row_dataindex += 1
            if row_dataindex <= master_RNC_postion:
                continue

            elif "BAM version" in row_data:
                master_SD_object_data.write(row_data)
            # TODO next line is written in general for master
            elif "SYSOBJECTID" in row_data:
                master_SD_object_data.write(row_data)
            elif "SET NODE:NID={}".format(master_RNCID) in row_data:
                master_SD_object_data.write(row_data)
            elif "ADD EXTNODE:ENID=" in row_data:
                master_SD_object_data.write(row_data)
            elif "ADD URNCBASIC:RNCID={}".format(master_RNCID) in row_data:
                master_SD_object_data.write(row_data)
            elif "ADD UCELLSETUP" in row_data and "LOGICRNCID={}".format(master_RNCID) in row_data:
                print("print got LOGICRNCID")
                master_SD_object_data.write(row_data)
            elif "ADD UINTERFREQNCELL" in row_data and "RNCID={}".format(master_RNCID) in row_data:
                print("got RNCID=3800")
                master_SD_object_data.write(row_data)
            elif "ADD UINTRAFREQNCELL" in row_data and "RNCID={}".format(master_RNCID) in row_data:
                print("got RNCID=3800")
                master_SD_object_data.write(row_data)
            elif "SYSOBJECTID" not in row_data and "SYSOBJECTID" not in row_data  and "SET NODE:NID=" not in row_data and "ADD EXTNODE:ENID=" not in row_data and "ADD URNCBASIC:RNCID=" not in row_data and "ADD UCELLSETUP" not in row_data and "ADD UINTERFREQNCELL" not in row_data and "ADD UINTRAFREQNCELL" not in row_data:
                master_SD_object_data.write(row_data)
            else:
                continue



















