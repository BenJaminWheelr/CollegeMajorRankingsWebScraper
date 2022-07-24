from selenium import webdriver
from time import sleep
import pandas as pd



class MajorRanking():
    # Sets up selenium driver & creates empty data frame
    def __init__(self, website_url):
        edge_driver_path = "/Users/Bighe/Dropbox/VScode/seleniumDriver/msedgedriver.exe"
        self.driver = webdriver.Edge(executable_path=edge_driver_path)
        self.driver.maximize_window()
        self.driver.get(website_url)
        data = {
            'Rank': [],
            'Major': [],
            'Degree Type': [],
            'Early-Career Pay': [],
            'Mid-Career Pay': [],
            'High Meaning': [],
        }
        self.df = pd.DataFrame(data)

    # gets all data for each row in data frame and stores in nested list
    def get_all_data(self):
        self.first = self.driver.find_elements_by_tag_name('tr')
        all_details = [x.text for x in self.first]
        self.the_test = []
        spot = 1
        for i in range(len(all_details)):
            try:
                result = ''.join(all_details[spot]).split()
                self.the_test.append(result)
                spot += 1
            except IndexError:
                break

    # gets list of major ranks from nested list (ignore the incorrect sequence of numbers in output, the website has the incorrect sequence hard coded into html)
    def get_all_ranks(self):
        self.major_rank = [i[0] for i in self.the_test]
        self.major = []

    # gets list of major titles from nested list
    def get_list_of_majors(self):
        for i in self.the_test:
            list_of_majors = []
            list_of_majors.append(i[1])
            if i[2] == "Bachelors":
                result = ''.join(list_of_majors)
                self.major.append(result)
                continue
            else:
                list_of_majors.append(i[2])
            if i[3] == "Bachelors":
                result = ' '.join(list_of_majors)
                self.major.append(result)
                continue
            else:
                list_of_majors.append(i[3])
            if i[4] == "Bachelors":
                result = ' '.join(list_of_majors)
                self.major.append(result)
                continue
            else:
                list_of_majors.append(i[4])
            if i[5] == "Bachelors":
                result = ' '.join(list_of_majors)
                self.major.append(result)
                continue
            else:
                list_of_majors.append(i[5])
            if i[6] == "Bachelors":
                result = ' '.join(list_of_majors)
                self.major.append(result)
                continue
            else:
                list_of_majors.append(i[6])
            result = ' '.join(list_of_majors)
            self.major.append(result)

    # adds the bachelor degree type to every row in data frame
    def get_all_degree_types(self):
        self.bachelor = []
        for i in range(len(self.major_rank)):
            self.bachelor.append('Bachelors')

    # gets early career pay from nested list
    def get_early_career_pay(self):
        self.early_career_pay = []
        for i in self.the_test:
            length_of_list = len(i) - 3
            self.early_career_pay.append(i[length_of_list])

    # gets mid career pay from nested list
    def get_mid_career_pay(self):
        self.mid_career_pay = []
        for i in self.the_test:
            length_of_list = len(i) - 2
            self.mid_career_pay.append(i[length_of_list])

    # gets percentage of alumni who say that their work makes a difference in the world
    def get_meaning_percentages(self):
        self.meaning = []
        for i in self.the_test:
            length_of_list = len(i) - 1
            percentage = i[length_of_list]
            # if percentage == 
            print(percentage)
            print(type(percentage))
            self.meaning.append(percentage)

    # creates data frame for each web page and appends to the empty dataframe
    def create_data_frame(self):
        new_df_data = {
            'Rank': self.major_rank,
            'Major': self.major,
            'Degree Type': self.bachelor,
            'Early-Career Pay': self.early_career_pay,
            'Mid-Career Pay': self.mid_career_pay,
            'High Meaning': self.meaning,
        }

        new_df = pd.DataFrame(data=new_df_data)
        self.df = self.df.append(new_df)

webpage_url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"

#declares selenium driver object
begin = MajorRanking(webpage_url)
def main():
    begin.get_all_data()
    begin.get_all_ranks()
    begin.get_list_of_majors()
    begin.get_all_degree_types()
    begin.get_early_career_pay()
    begin.get_mid_career_pay()
    begin.get_meaning_percentages()
    begin.create_data_frame()
    next_page_button = begin.driver.find_element_by_class_name("pagination__next-btn") #selenium driver locating next page button
    next_page_button.click()
    sleep(1)

number_of_webpages = 34
for i in range(0, number_of_webpages):
    main()
sleep(2)
begin.driver.quit()

#prints data frame with all data
print(begin.df)

path_to_saved_file = None # SET PATH YOU WOULD LIKE TO SAVE DATA FRAME TO 
begin.df.to_csv(path_to_saved_file)

print("GOODBYE")