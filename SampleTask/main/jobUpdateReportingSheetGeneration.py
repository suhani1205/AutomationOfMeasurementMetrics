import pandas as pd
from SampleTask.Utilities.toRemoveBold import toRemoveBold
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    input_excelTemplate_path = '/Users/nsuhani/PycharmProjects/pythonProject' \
                               '/SampleTask/inputFile/jobScheduleTemplate.xlsx'

    output_excelTemplate_path = '/Users/nsuhani/PycharmProjects/pythonProject' \
                                '/SampleTask/Output/jobUpdateSheetGenerated.xlsx'

    hva_data_path = "/Users/nsuhani/PycharmProjects/pythonProject" \
                    "/SampleTask/inputFile/hvaNewData.txt"
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
    row_list = {}
    for line in file:
        if len(line.strip()) != 0:
            logging.info("INPUT ROW CANNOT BE NULL")
            row_list[jobName] = line.strip()
            row_list[workflows_localOmniflow_omniflowCommandLineParameters_eventName] = row_list[jobName]
            dataFrame = dataFrame.append(row_list, ignore_index=True)

        else:
            row_list[jobName] = "EMPTY"
            row_list[workflows_localOmniflow_omniflowCommandLineParameters_eventName] = row_list[jobName]
            dataFrame = dataFrame.append(row_list, ignore_index=True)

    return dataFrame

# global Variable
jobName = 'jobName'
workflows_localOmniflow_omniflowCommandLineParameters_eventName = 'workflows_localOmniflow_omniflowCommandLineParameters_eventName'

if __name__ == '__main__':
    main()
