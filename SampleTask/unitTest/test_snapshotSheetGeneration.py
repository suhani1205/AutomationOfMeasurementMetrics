import unittest
import pandas as pd
from SampleTask.main.snapshotSheetGeneration import populate_excelFile

class snapshotSheetGenerationTest(unittest.TestCase):

    def test_PopulateExcelFile_WithValidInput_ProducesCorrectOutput(self):

        input_Template_Path = '/Users/nsuhani/PycharmProjects/pythonProject' \
                              '/SampleTask/unitTest/testInputFile/snapshotScheduleSheet_Test.xlsx'

        output_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                      'SampleTask/unitTest/testOutputFile/snapshotTestOutput_validInputs.xlsx'

        hva_Data_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                        'SampleTask/unitTest/testInputFile/hvaTestData'

        populate_excelFile(input_Template_Path, output_Path, hva_Data_Path)

        df_dict = pd.read_excel(output_Path)
        row_data_frame = df_dict.head(1)

        assert row_data_frame['clusterName'].values[0] == 'dummyClusterName'
        assert row_data_frame['jobGroup'].values[0] == 'hvaEventsSnapshot_v1_backfill'
        assert row_data_frame['jobName'].values[0] == 'fresh_online_delivery_purchase_1st'
        assert row_data_frame['marketplaceId'].values[0] == 1
        assert row_data_frame['runtimeParameters_clusterType'].values[0] == 'backfill_small'
        assert row_data_frame['scheduleEndDate'].values[0] == '2021-10-26'
        assert row_data_frame['scheduleStartDate'].values[0] == '2021-09-26'
        assert row_data_frame['runtimeParameters_orderingLevel'].values[0] == 'orderOnRunDate'


    def test_PopulateExcelFile_WithInvalidInputs_generatesException(self):
        input_Template_Path = '/Users/nsuhani/PycharmProjects/pythonProject' \
                              '/SampleTask/unitTest/testInputFile/snapshotScheduleSheet_Test.xlsx'

        output_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                      'SampleTask/unitTest/testOutputFile/snapshotTestOutput_invalidInputs.xlsx'

        hva_Data_Path = '/Users/nsuhani/PycharmProjects/pythonProject/' \
                        'SampleTask/unitTest/testInputFile/hva_test_data_invalid'

        populate_excelFile(input_Template_Path, output_Path, hva_Data_Path)

        df_dict = pd.read_excel(output_Path)
        row_data_frame = df_dict.head(1)

        assert row_data_frame['clusterName'].values[0] == 'dummyClusterName'
        assert row_data_frame['jobGroup'].values[0] == 'hvaEventsSnapshot_v1_backfill'
        assert row_data_frame['jobName'].values[0] == 'alexa_shopping_addtolist_1st'
        assert row_data_frame['marketplaceId'].values[0] == "EMPTY"
        assert row_data_frame['runtimeParameters_clusterType'].values[0] == 'backfill_large'
        assert row_data_frame['scheduleEndDate'].values[0] == '2021-10-26'
        assert row_data_frame['scheduleStartDate'].values[0] == '2021-09-26'
        assert row_data_frame['runtimeParameters_orderingLevel'].values[0] == 'orderOnRunDate'