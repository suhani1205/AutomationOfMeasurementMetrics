import unittest
import pandas as pd
from SampleTask.main.jobUpdateReportingSheetGeneration import populate_excelFile


class jobUpdateReportingSheetGenerationTest(unittest.TestCase):

    def test_PopulateExcelFile_WithValidInput_ProducesCorrectOutput(self):

        input_Template_Path = 'testInputFile/jobUpdateSheetGeneration_Test.xlsx'

        output_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                      'SampleTask/unitTest/testOutputFile/jobUpdateTestOutput_validInputs.xlsx'

        hva_Data_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                        'SampleTask/unitTest/testInputFile/HVA_jobSheet_TestData'

        populate_excelFile(input_Template_Path, output_Path, hva_Data_Path)

        df_dict = pd.read_excel(output_Path)
        row_data_frame = df_dict.head(1)

        assert row_data_frame['jobGroup'].values[0] == 'hvaEventsReporting_v1_backfill'
        assert row_data_frame['jobName'].values[0] == 'alexa_shopping_addtolist_1st'
        assert row_data_frame['workflows_localOmniflow_omniflowCommandLineParameters_eventName'].values[0] == \
               'alexa_shopping_addtolist_1st'
        assert row_data_frame['workflows_localOmniflow_pipelineName'].values[0] == 'dailyProgramHvaReporting'



    def test_PopulateExcelFile_WithValidInput_generatesException(self):

        input_Template_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                              'SampleTask/unitTest/testInputFile/jobUpdateSheetGeneration_Test.xlsx'

        output_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                      'SampleTask/unitTest/testOutputFile/jobUpdateTestOutput_invalidInputs.xlsx'

        hva_Data_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                        'SampleTask/unitTest/testInputFile/HVA_jobSheetTestData_invalid'

        populate_excelFile(input_Template_Path, output_Path, hva_Data_Path)

        df_dict = pd.read_excel(output_Path)

        # for first row in the output excel
        row_data_frame = df_dict.head(1)

        assert row_data_frame['jobGroup'].values[0] == "hvaEventsReporting_v1_backfill"
        assert row_data_frame['jobName'].values[0] == 'EMPTY'
        assert row_data_frame['workflows_localOmniflow_omniflowCommandLineParameters_eventName'].values[0] == \
               "EMPTY"
        assert row_data_frame['workflows_localOmniflow_pipelineName'].values[0] == 'dailyProgramHvaReporting'

        # for second row in the output_excel
        row_data_frame2 = df_dict.head(2)

        assert row_data_frame2['jobGroup'].values[0] == 'hvaEventsReporting_v1_backfill'
        assert row_data_frame2['jobName'].values[0] == 'EMPTY'
        assert row_data_frame2['workflows_localOmniflow_omniflowCommandLineParameters_eventName'].values[0] == \
               'EMPTY'
        assert row_data_frame2['workflows_localOmniflow_pipelineName'].values[0] == 'dailyProgramHvaReporting'