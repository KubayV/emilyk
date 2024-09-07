# Core Pkgs
import streamlit as st

from PIL import Image
from PIL import ImageOps
import sys


from functions.functions import set_bg_hack

# https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation

# from st_pages import Page, Section, show_pages, add_page_title, hide_pages
#
# show_pages(
#     [
#         Page("dezoomcamp/DE_Zoomcamp.py", "DE Zoomcamp", "💻"),
#
#         # # 2024 Content
#         Section("DE Zoomcamp 2024", "🧙‍♂️"),
#         Page("dezoomcamp/2024_cohort/Course_Overview.py", "Course Overview", "📚", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_1_Introduction_&_Prerequisites.py", "Module 1 Introduction & Prerequisites",
#              "1️⃣", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_2_Workflow_Orchestration.py", "Module 2 Workflow Orchestration", "2️⃣",
#              in_section=True),
#         Page("dezoomcamp/2024_cohort/Workshop_1_Data_Ingestion.py", "Workshop 1 Data Ingestion", "🛠️",
#              in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_3_Data_Warehouse.py", "Module 3 Data Warehouse and BigQuery", "3️⃣",
#              in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_4_Analytics_Engineering.py", "Module 4 Analytics Engineering", "4️⃣",
#              in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_5_Batch_Processing.py", "Module 5 Batch Processing", "5️⃣",
#              in_section=True),
#         Page("dezoomcamp/2024_cohort/Workshop_2_Stream_Processing_with_SQL.py", "Workshop 2 Stream Processing with SQL",
#              "🛠️", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_6_Stream_Processing.py", "Module 6 Stream Processing", "6️⃣",
#              in_section=True),
#         Page("dezoomcamp/2024_cohort/Course_Project.py", "Course Project", "🏆", in_section=True),
#
#         # 2023 Content
#         # Hide 2023 DE Zoomcamp for faster loading
#         # Section("DE Zoomcamp 2023", "👨‍🔧"),
#         # Page("dezoomcamp/2023_cohort/Course_Overview.py", "Course Overview", "📚", in_section=True),
#         # Page("dezoomcamp/2023_cohort/Week_1_Introduction_&_Prerequisites.py", "Week 1 Introduction & Prerequisites", "1️⃣", in_section=True),
#         # Page("dezoomcamp/2023_cohort/Week_2_Workflow_Orchestration.py", "Week 2 Workflow Orchestration", "2️⃣", in_section=True),
#         # Page("dezoomcamp/2023_cohort/Week_3_Data_Warehouse.py", "Week 3 Data Warehouse", "3️⃣", in_section=True),
#         # Page("dezoomcamp/2023_cohort/Week_4_Analytics_Engineering.py", "Week 4 Analytics Engineering", "4️⃣", in_section=True),
#         # Page("dezoomcamp/2023_cohort/Week_5_Batch_Processing.py", "Week 5 Batch Processing", "5️⃣", in_section=True),
#         # Page("dezoomcamp/2023_cohort/Week_6_Stream_Processing.py", "Week 6 Stream Processing", "6️⃣", in_section=True),
#         # Page("dezoomcamp/2023_cohort/Week_7_Project.py", "Week 7 Project", "7️⃣", in_section=True),
#         # Page("dezoomcamp/2023_cohort/Homework_Quizzes.py", "Homework Quizzes", "📝", in_section=True),
#
#         Page("dezoomcamp/Datasets.py", "Datasets", icon="💾", in_section=False),
#         Page("dezoomcamp/Certificate.py", "Certificate", "📜", in_section=False),
#         Page("dezoomcamp/FAQ.py", "FAQ", "❔", in_section=False),
#         Page("dezoomcamp/Contact.py", "Contact", icon="📩", in_section=False),
#         Page("dezoomcamp/Contact_thanks.py", "Thank you", icon="💌"),
#         Page("dezoomcamp/About.py", "About", icon="🖼️", in_section=False)
#     ]
# )
# def main():
set_bg_hack("Style/cool-backgroundBlue.png")

st.title("EmilyK®")
st.divider()

col1, col2 = st.columns(2)
with col1:
    img = Image.open("Images/Emily2022.jpeg")
    img2 = ImageOps.exif_transpose(img)
    st.image(img2)

with col2:
    st.subheader("Emily K is a girl that lives in South West of UK. "
             "This website is designed to keep track of "
             "Emily's activities and her progress. ")
    st.subheader("Please make a selection from the Menu to see her latest "
             "Piano 🎹, Lamda 🎭 or Violin 🎻 videos. You can also view Emily's artwork 🎨")


# if __name__ == '__main__':
#     main()