import xlrd

# for rx in range(self.sheet.nrows):  # for checking purpose only
#     print(self.sheet.row(rx))

class FetchData:
    def __init__(self):
        self.SpecificWorkbook = xlrd.open_workbook("specific_list.xlsx")  # Open workbook (file)
        self.SpecificSheet = self.SpecificWorkbook.sheet_by_index(0)   # Sheet selected from workbook of file
        self.FullDataWorkbook = xlrd.open_workbook("full_list.xlsx")  # Open workbook (file)
        self.FullDataSheet = self.FullDataWorkbook.sheet_by_index(0)   # Sheet selected from workbook of file
        self.roll_headings = ["crn", "roll", "roll no", "roll_no", "roll no.", "roll_no.", "roll number", "roll_number"]
        self.phone_headings = ["phone","phone_no.","phone no.","phone_no","phone no", "phone_number", "phone number", "phone_num", "phone num", "mobile", "mobile_no", "mobile_no.", "mobile no", "mobile no.", "mobile number", "mobile number"]
        self.name_headings = ["name", "names"]
        self.FullDataSheet_Headings = list()  # lists defined
        self.s_list = [[], []]  # list which will contain names and roll no. of specific_list.xlsx
        self.s_refer = {'name':self.s_list[0], 'crn':self.s_list[1]}
        self.f_list = [[], [], [], []]  # list which will contain data of full_list.xlsx
        self.f_refer = {'name':self.f_list[0], 'crn':self.f_list[1], 'branch':self.f_list[2], 'phone':self.f_list[3]}

    def ForData_FetchContent(self):
        # fetching Names
        for _ in range(self.SpecificSheet.nrows):   # run loop for (no. of rows in sheet) times
            data = self.SpecificSheet.cell_value(_, 0)   # get data of particular row ( _ = row no.)
            if str(data).lower() not in self.name_headings:  # check if the data selected is not heading "names"
                self.s_refer['name'].append(data)  # Insert data in the list
        print(self.s_refer['name'])  # Print all fetched names in the list

        # fetching CRN
        for _ in range(self.SpecificSheet.nrows):   # run loop for (no. of rows in sheet) times
            data = self.SpecificSheet.cell_value(_, 1)   # get data of particular row ( _ = row no.)
            if str(data).lower() not in self.roll_headings:  # check if the data selected is not heading "roll_no"
                self.s_refer['crn'].append(data)  # Insert data in the list
        print(self.s_refer['crn'])  # Print all fetched rollno. in the list

        print(self.s_list) # print whole sheet

    def FetchContent(self):
        for _ in range(self.FullDataSheet.ncols):
            self.FullDataSheet_Headings.append(str(self.FullDataSheet.cell_value(0, _)).lower())
        headings_check = self.FullDataSheet_Headings[0]  # For a instance, assigned first column heading
        for i in range(self.FullDataSheet.ncols):  # Read data column wise
            for j in range(self.FullDataSheet.nrows):  # Read data row wise
                data = self.FullDataSheet.cell_value(j, i)  # Data fetched according to rows and columns
                if headings_check in self.FullDataSheet_Headings:
                    # for assigning headings to a variable for checking which column data is fetching at the moment
                    if str(data).lower() in self.name_headings:
                        headings_check = 'name'
                    elif str(data).lower() in self.roll_headings:
                        headings_check = 'crn'
                    elif str(data).lower() == "branch":
                        headings_check = 'branch'
                    elif str(data).lower() in self.phone_headings:
                        headings_check = 'phone'
                    # Now assigning fetched data to respective lists
                    else:
                        if headings_check in self.name_headings:
                            self.f_refer['name'].append(data)  # Fetching the list to which data has to be inserted
                        elif headings_check in self.roll_headings:
                            self.f_refer['crn'].append(data)
                        elif headings_check == "branch":
                            self.f_refer['branch'].append(data)
                        elif headings_check in self.phone_headings:
                            self.f_refer['phone'].append(data)

        print(self.f_list)  # All fetched data/
        print("\n")
        # ====== or =========
        print(str(self.f_list[0])+"\n"+str(self.f_list[1])+"\n"+str(self.f_list[2])+"\n"+str(self.f_list[3]))  # All fetched data
        # print(self.FullDataSheet.cell_value(j, i))

    def Match_data(self):
        pass

    def __del__(self):
        self.SpecificWorkbook.release_resources()
        self.FullDataWorkbook.release_resources()


if __name__ == "__main__":
    obj = FetchData()  # class object created
    obj.ForData_FetchContent()  # calling first function
    obj.FetchContent()  # calling second function
    obj.Match_data()