import os
import shutil


def remove_more_than_spec_generate_master_sd_from_combined(input_file_path, output_dir_path):
    with open(input_file_path, 'r') as combined_sd:
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
                master_RNC_SD_file = os.path.join(output_dir_path, "CFGMML-{}.txt".format(master_RNCID))

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
                    print("print got ADD UCELLSETUP LOGICRNCID={}".format(master_RNCID))
                    master_SD_object_data.write(row_data)
                elif "ADD UINTERFREQNCELL" in row_data and "RNCID={}".format(master_RNCID) in row_data:
                    print("got ADD UINTERFREQNCELL for RNCID={}".format(master_RNCID))
                    master_SD_object_data.write(row_data)
                elif "ADD UINTRAFREQNCELL" in row_data and "RNCID={}".format(master_RNCID) in row_data:
                    print("got ADD UINTRAFREQNCELL for RNCID={}".format(master_RNCID))
                    master_SD_object_data.write(row_data)
                elif "SYSOBJECTID" not in row_data  and "SET " not in row_data and "ADD " not in row_data:
                    master_SD_object_data.write(row_data)
                else:
                    continue


def generate_master_sd_from_combined(input_file_path, output_dir_path, is_zip):
    input_filename = os.path.basename(input_file_path)
    with open(input_file_path, 'r') as combined_sd:
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
                master_RNC_SD_file = os.path.join(output_dir_path, "{}".format(input_filename))

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
                    print("print got ADD UCELLSETUP LOGICRNCID={}".format(master_RNCID))
                    master_SD_object_data.write(row_data)
                elif "ADD UINTERFREQNCELL" in row_data and "RNCID={}".format(master_RNCID) in row_data:
                    print("got ADD UINTERFREQNCELL for RNCID={}".format(master_RNCID))
                    master_SD_object_data.write(row_data)
                elif "ADD UINTRAFREQNCELL" in row_data and "RNCID={}".format(master_RNCID) in row_data:
                    print("got ADD UINTRAFREQNCELL for RNCID={}".format(master_RNCID))
                    master_SD_object_data.write(row_data)
                elif "SYSOBJECTID" not in row_data and "SYSOBJECTID" not in row_data  and "SET NODE:NID=" not in row_data and "ADD EXTNODE:ENID=" not in row_data and "ADD URNCBASIC:RNCID=" not in row_data and "ADD UCELLSETUP" not in row_data and "ADD UINTERFREQNCELL" not in row_data and "ADD UINTRAFREQNCELL" not in row_data:
                    master_SD_object_data.write(row_data)
                else:
                    continue

    if is_zip.upper() == 'YES':
        with ZipFile("{}.zip".format(master_RNC_SD_file), 'w') as ouput_zip:
            ouput_zip.write(master_RNC_SD_file)


if __name__ == "__main__":
    import sys
    from zipfile import ZipFile
    v_input_file_path = None
    v_output_dir_path = None
    is_zip = None
    try:
        with open("splitter_config.ini", 'r') as splitter_config:
            for line in splitter_config.readlines():
                if "input_file_path" in line:
                    line = line.strip()
                    v_input_file_path = line.split("=")[1]
                elif "output_dir_path" in line:
                    line = line.strip()
                    v_output_dir_path = line.split("=")[1]
                elif "is_zip" in line:
                    line = line.strip()
                    is_zip = line.split("=")[1]
                else:
                    continue
    except (FileNotFoundError, FileExistsError):
        print("Please put the splitter_config.ini file at the same directory where exe is present")
        sys.exit()
    if v_input_file_path is None:
        print("Please provide input_file_path=the path for the input file")
        sys.exit()
    if v_output_dir_path is None:
        print("Please provide the output_dir_path=the directory path where the output file be created ")
        sys.exit()

    if is_zip is not None and is_zip.upper() == "YES":
        with ZipFile(v_input_file_path, 'r') as zip_input_ob:
            zip_input_ob.extractall("temp_input")

        for input_file in os.listdir("temp_input"):
            v_input_file_path = os.path.join("temp_input", input_file)
            generate_master_sd_from_combined(v_input_file_path, v_output_dir_path, is_zip=is_zip)
        else:
            shutil.rmtree("temp_input")
    else:
        generate_master_sd_from_combined(v_input_file_path, v_output_dir_path, is_zip='NO')


