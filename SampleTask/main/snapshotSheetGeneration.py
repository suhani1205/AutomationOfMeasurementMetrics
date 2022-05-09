import pandas as pd
from SampleTask.Utilities.toRemoveBold import toRemoveBold
from SampleTask.Utilities.GenerateLegalIdMap import getLegalIdForGivenMarketPlaceId
from SampleTask.Utilities.GenerateRegionIdMap import getRegionIdForGivenMarketPlaceId
import logging


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    input_excelTemplate_path = '../inputFile/snapshotScheduleSheetTemplate.xlsx'
    output_excelTemplate_path = '../Output/snapshotSheetGenerated.xlsx'
    hva_data_path = "/Users/nsuhani/PycharmProjects/pythonProject" \
                    "/SampleTask/inputFile/hvaData.txt"
    populate_excelFile(input_excelTemplate_path, output_excelTemplate_path, hva_data_path)


def populate_excelFile(input_excelTemplate_path, output_excelTemplate_path, hva_data_path):
    excel_template = pd.read_excel(input_excelTemplate_path)
    output_excel_template = read_Text_file(excel_template, hva_data_path)

    # was not able to fill the recurrent data automatically
    # to do so I have used fillna method
    for i in output_excel_template.columns:
        output_excel_template[i].fillna(output_excel_template[i].mode()[0], inplace=True)

    output_excel_template = output_excel_template.iloc[1:]
    output_excel_template.to_excel(output_excelTemplate_path, index=False)
    toRemoveBold(output_excelTemplate_path)


def read_Text_file(dataFrame, path):

    file = open(path)
    for line in file:
        if line == '\n':
            logging.info("INPUT ROW or COLUMN CANNOT BE NULL")

        else:
            words = line.split(",")
            row_list = generate_row_list(words)
            series = pd.Series(row_list)
            dataFrame = dataFrame.append(series, ignore_index=True)

    return dataFrame


def generate_row_list(words):
    row_list = {}

    row_list[jobName] = words[0].strip()

    if words[1].strip() is None or words[1].strip().isdigit() is False:
        row_list[marketplaceId] = "EMPTY"
        row_list[legalId] = "EMPTY"
        row_list[regionId] = "EMPTY"
        logging.info("MARKETPLACE-ID CANNOT BE EMPTY")

    else:
        row_list[marketplaceId] = int(words[1].strip())
        row_list[legalId] = getLegalIdForGivenMarketPlaceId(row_list[marketplaceId])
        row_list[regionId] = getRegionIdForGivenMarketPlaceId(row_list[marketplaceId])

    if len(words[2].strip()) != 0:
        row_list[runtimeParameters_clusterType] = words[2].strip()
    else:
        row_list[runtimeParameters_clusterType] = "EMPTY" #Not getting filled properly

    if len(words[3].strip()) != 0:
        row_list[scheduleStartDate] = words[3].strip()
    else:
        row_list[scheduleStartDate] = "EMPTY"

    if len(words[4].strip()) != 0:
        row_list[scheduleEndDate] = words[4].strip()
    else:
        row_list[scheduleEndDate] = "EMPTY"

    return row_list


# globalVariable
jobName = 'jobName'
marketplaceId = 'marketplaceId'
runtimeParameters_clusterType = 'runtimeParameters_clusterType'
scheduleStartDate = 'scheduleStartDate'
scheduleEndDate = 'scheduleEndDate'
legalId = 'legalId'
regionId = 'regionId'

if __name__ == '__main__':
    main()