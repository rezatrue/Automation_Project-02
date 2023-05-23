import logging
import inspect
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook

class Utils:

    def assretTextCompare(self, expected, actual):
        assert (expected.lower() == actual.lower())
        print("Assert pass")

    def custom_logger(logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("../automation.log", mode='w')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
        pass

    def read_xlsx_test_data(self, file_name, sheet_name):
        test_data = []
        try:
            workbook = load_workbook(filename=file_name)
            sheet = workbook[sheet_name]

            headers = [sheet[get_column_letter(col)].value for col in range(1, sheet.max_column + 1)]

            for row in range(2, sheet.max_row + 1):
                data = {}
                for col, header in enumerate(headers, start=1):
                    data[header] = sheet[get_column_letter(col) + str(row)].value
                test_data.append(data)
        except:
            print("Error loading xlsx data")

        return test_data