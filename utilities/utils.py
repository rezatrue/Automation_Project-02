import logging
import inspect
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

    def read_xlsx_file(self, file_name, sheet_name):
        total_data = []
        try:
            workbook = load_workbook(filename=file_name)
            sheet = workbook[sheet_name]

            max_row = sheet.max_row
            max_column = sheet.max_column

            for row_num in range(2, max_row + 1):
                row_data = []
                for col_num in range(1, max_column + 1):
                    cell_value = sheet.cell(row=row_num, column=col_num).value
                    row_data.append(cell_value)
                total_data.append(row_data)
        except:
            print("Error loading xlsx data")
        return total_data