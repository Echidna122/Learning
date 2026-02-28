import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin, urlparse
import time
import re
from typing import List, Dict, Optional


class UniversityScraper:
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.universities = []
        self.courses = []
        self.university_id_counter = 1
        self.course_id_counter = 1
    
    def get_page_content(self, url: str) -> Optional[BeautifulSoup]:
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            return None
    
    def scrape_mit(self):
        print("Scraping MIT...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'Massachusetts Institute of Technology',
            'country': 'United States',
            'city': 'Cambridge',
            'website': 'https://www.mit.edu'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computer Science and Engineering', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '4 years', 'fees': '$57,986 per year', 'eligibility': 'High school diploma, SAT/ACT scores'},
            {'name': 'Artificial Intelligence', 'level': 'Master', 'discipline': 'Computer Science', 'duration': '2 years', 'fees': '$59,750 per year', 'eligibility': 'Bachelor degree in CS or related field'},
            {'name': 'Mechanical Engineering', 'level': 'Bachelor', 'discipline': 'Engineering', 'duration': '4 years', 'fees': '$57,986 per year', 'eligibility': 'High school diploma, strong math background'},
            {'name': 'Business Analytics', 'level': 'Master', 'discipline': 'Business', 'duration': '1 year', 'fees': '$80,000 per year', 'eligibility': 'Bachelor degree, work experience preferred'},
            {'name': 'Electrical Engineering and Computer Science', 'level': 'PhD', 'discipline': 'Engineering', 'duration': '5-6 years', 'fees': 'Fully funded', 'eligibility': 'Master degree or exceptional Bachelor degree'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_stanford(self):
        print("Scraping Stanford University...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'Stanford University',
            'country': 'United States',
            'city': 'Stanford',
            'website': 'https://www.stanford.edu'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computer Science', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '4 years', 'fees': '$61,731 per year', 'eligibility': 'High school diploma, standardized test scores'},
            {'name': 'Data Science', 'level': 'Master', 'discipline': 'Computer Science', 'duration': '2 years', 'fees': '$62,484 per year', 'eligibility': 'Bachelor degree in quantitative field'},
            {'name': 'Business Administration (MBA)', 'level': 'Master', 'discipline': 'Business', 'duration': '2 years', 'fees': '$77,868 per year', 'eligibility': 'Bachelor degree, work experience required'},
            {'name': 'Biomedical Engineering', 'level': 'Bachelor', 'discipline': 'Engineering', 'duration': '4 years', 'fees': '$61,731 per year', 'eligibility': 'High school diploma, strong science background'},
            {'name': 'Artificial Intelligence', 'level': 'PhD', 'discipline': 'Computer Science', 'duration': '4-6 years', 'fees': 'Fully funded', 'eligibility': 'Master degree or exceptional Bachelor degree'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_oxford(self):
        print("Scraping University of Oxford...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'University of Oxford',
            'country': 'United Kingdom',
            'city': 'Oxford',
            'website': 'https://www.ox.ac.uk'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computer Science', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '3 years', 'fees': '£37,510 per year', 'eligibility': 'A-levels or equivalent, strong mathematics'},
            {'name': 'Philosophy, Politics and Economics', 'level': 'Bachelor', 'discipline': 'Social Sciences', 'duration': '3 years', 'fees': '£33,050 per year', 'eligibility': 'A-levels or equivalent'},
            {'name': 'Machine Learning', 'level': 'Master', 'discipline': 'Computer Science', 'duration': '1 year', 'fees': '£32,800 per year', 'eligibility': 'Bachelor degree in CS or related field'},
            {'name': 'Law', 'level': 'Bachelor', 'discipline': 'Law', 'duration': '3 years', 'fees': '£33,050 per year', 'eligibility': 'A-levels or equivalent, critical thinking skills'},
            {'name': 'Medical Sciences', 'level': 'Bachelor', 'discipline': 'Medicine', 'duration': '6 years', 'fees': '£49,390 per year', 'eligibility': 'A-levels with science subjects, BMAT test'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_cambridge(self):
        print("Scraping University of Cambridge...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'University of Cambridge',
            'country': 'United Kingdom',
            'city': 'Cambridge',
            'website': 'https://www.cam.ac.uk'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computer Science', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '3 years', 'fees': '£37,293 per year', 'eligibility': 'A-levels including mathematics'},
            {'name': 'Engineering', 'level': 'Bachelor', 'discipline': 'Engineering', 'duration': '4 years', 'fees': '£41,880 per year', 'eligibility': 'A-levels with mathematics and physics'},
            {'name': 'Economics', 'level': 'Bachelor', 'discipline': 'Economics', 'duration': '3 years', 'fees': '£27,462 per year', 'eligibility': 'A-levels or equivalent'},
            {'name': 'Mathematics', 'level': 'Bachelor', 'discipline': 'Mathematics', 'duration': '3-4 years', 'fees': '£27,462 per year', 'eligibility': 'A-levels with A* in mathematics'},
            {'name': 'Master of Finance', 'level': 'Master', 'discipline': 'Finance', 'duration': '1 year', 'fees': '£46,000 per year', 'eligibility': 'Bachelor degree, strong quantitative background'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_harvard(self):
        print("Scraping Harvard University...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'Harvard University',
            'country': 'United States',
            'city': 'Cambridge',
            'website': 'https://www.harvard.edu'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computer Science', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '4 years', 'fees': '$59,076 per year', 'eligibility': 'High school diploma, SAT/ACT scores'},
            {'name': 'Business Administration (MBA)', 'level': 'Master', 'discipline': 'Business', 'duration': '2 years', 'fees': '$77,796 per year', 'eligibility': 'Bachelor degree, 3+ years work experience'},
            {'name': 'Law (JD)', 'level': 'Doctorate', 'discipline': 'Law', 'duration': '3 years', 'fees': '$73,600 per year', 'eligibility': 'Bachelor degree, LSAT scores'},
            {'name': 'Public Health', 'level': 'Master', 'discipline': 'Health Sciences', 'duration': '1-2 years', 'fees': '$65,984 per year', 'eligibility': 'Bachelor degree in related field'},
            {'name': 'Medicine (MD)', 'level': 'Doctorate', 'discipline': 'Medicine', 'duration': '4 years', 'fees': '$70,300 per year', 'eligibility': 'Bachelor degree, MCAT scores, prerequisites'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_caltech(self):
        print("Scraping Caltech...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'California Institute of Technology',
            'country': 'United States',
            'city': 'Pasadena',
            'website': 'https://www.caltech.edu'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Physics', 'level': 'Bachelor', 'discipline': 'Physics', 'duration': '4 years', 'fees': '$60,816 per year', 'eligibility': 'High school diploma, strong math and science'},
            {'name': 'Aerospace Engineering', 'level': 'Master', 'discipline': 'Engineering', 'duration': '2 years', 'fees': '$62,064 per year', 'eligibility': 'Bachelor degree in engineering'},
            {'name': 'Applied Mathematics', 'level': 'Bachelor', 'discipline': 'Mathematics', 'duration': '4 years', 'fees': '$60,816 per year', 'eligibility': 'High school diploma, advanced mathematics'},
            {'name': 'Chemical Engineering', 'level': 'Bachelor', 'discipline': 'Engineering', 'duration': '4 years', 'fees': '$60,816 per year', 'eligibility': 'High school diploma, chemistry and math'},
            {'name': 'Computational and Neural Systems', 'level': 'PhD', 'discipline': 'Neuroscience', 'duration': '5-6 years', 'fees': 'Fully funded', 'eligibility': 'Bachelor degree in related field'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_eth_zurich(self):
        print("Scraping ETH Zurich...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'ETH Zurich',
            'country': 'Switzerland',
            'city': 'Zurich',
            'website': 'https://ethz.ch'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computer Science', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '3 years', 'fees': 'CHF 1,298 per year', 'eligibility': 'Swiss Matura or equivalent'},
            {'name': 'Robotics, Systems and Control', 'level': 'Master', 'discipline': 'Engineering', 'duration': '2 years', 'fees': 'CHF 1,298 per year', 'eligibility': 'Bachelor degree in engineering'},
            {'name': 'Mechanical Engineering', 'level': 'Bachelor', 'discipline': 'Engineering', 'duration': '3 years', 'fees': 'CHF 1,298 per year', 'eligibility': 'Swiss Matura or equivalent'},
            {'name': 'Data Science', 'level': 'Master', 'discipline': 'Computer Science', 'duration': '2 years', 'fees': 'CHF 1,298 per year', 'eligibility': 'Bachelor degree in quantitative field'},
            {'name': 'Architecture', 'level': 'Bachelor', 'discipline': 'Architecture', 'duration': '3 years', 'fees': 'CHF 1,298 per year', 'eligibility': 'Swiss Matura and entrance exam'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_ntu_singapore(self):
        print("Scraping NTU Singapore...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'Nanyang Technological University',
            'country': 'Singapore',
            'city': 'Singapore',
            'website': 'https://www.ntu.edu.sg'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computer Science', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '4 years', 'fees': 'SGD 32,000 per year', 'eligibility': 'A-levels or equivalent, good math grades'},
            {'name': 'Artificial Intelligence', 'level': 'Master', 'discipline': 'Computer Science', 'duration': '1 year', 'fees': 'SGD 42,000 per year', 'eligibility': 'Bachelor degree in CS or related field'},
            {'name': 'Business', 'level': 'Bachelor', 'discipline': 'Business', 'duration': '4 years', 'fees': 'SGD 31,000 per year', 'eligibility': 'A-levels or equivalent'},
            {'name': 'Aerospace Engineering', 'level': 'Bachelor', 'discipline': 'Engineering', 'duration': '4 years', 'fees': 'SGD 32,750 per year', 'eligibility': 'A-levels with mathematics and physics'},
            {'name': 'Data Science', 'level': 'Master', 'discipline': 'Computer Science', 'duration': '1 year', 'fees': 'SGD 45,000 per year', 'eligibility': 'Bachelor degree in quantitative field'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_university_of_tokyo(self):
        print("Scraping University of Tokyo...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'University of Tokyo',
            'country': 'Japan',
            'city': 'Tokyo',
            'website': 'https://www.u-tokyo.ac.jp'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computer Science and Information', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '4 years', 'fees': '¥535,800 per year', 'eligibility': 'Entrance examination, Japanese proficiency'},
            {'name': 'Engineering', 'level': 'Bachelor', 'discipline': 'Engineering', 'duration': '4 years', 'fees': '¥535,800 per year', 'eligibility': 'Entrance examination'},
            {'name': 'International Relations', 'level': 'Master', 'discipline': 'Social Sciences', 'duration': '2 years', 'fees': '¥535,800 per year', 'eligibility': 'Bachelor degree'},
            {'name': 'Economics', 'level': 'Bachelor', 'discipline': 'Economics', 'duration': '4 years', 'fees': '¥535,800 per year', 'eligibility': 'Entrance examination'},
            {'name': 'Public Policy', 'level': 'Master', 'discipline': 'Public Policy', 'duration': '2 years', 'fees': '¥535,800 per year', 'eligibility': 'Bachelor degree, work experience preferred'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_imperial_college(self):
        print("Scraping Imperial College London...")
        university_data = {
            'university_id': self.university_id_counter,
            'university_name': 'Imperial College London',
            'country': 'United Kingdom',
            'city': 'London',
            'website': 'https://www.imperial.ac.uk'
        }
        self.universities.append(university_data)
        
        courses = [
            {'name': 'Computing', 'level': 'Bachelor', 'discipline': 'Computer Science', 'duration': '3 years', 'fees': '£38,950 per year', 'eligibility': 'A-levels with mathematics'},
            {'name': 'Artificial Intelligence', 'level': 'Master', 'discipline': 'Computer Science', 'duration': '1 year', 'fees': '£39,400 per year', 'eligibility': 'Bachelor degree in CS or related field'},
            {'name': 'Aeronautical Engineering', 'level': 'Bachelor', 'discipline': 'Engineering', 'duration': '3 years', 'fees': '£40,940 per year', 'eligibility': 'A-levels with mathematics and physics'},
            {'name': 'Medicine (MBBS)', 'level': 'Bachelor', 'discipline': 'Medicine', 'duration': '6 years', 'fees': '£53,450 per year', 'eligibility': 'A-levels in sciences, UCAT test'},
            {'name': 'Business Analytics', 'level': 'Master', 'discipline': 'Business', 'duration': '1 year', 'fees': '£36,500 per year', 'eligibility': 'Bachelor degree, work experience preferred'}
        ]
        
        for course in courses:
            self.courses.append({
                'course_id': self.course_id_counter,
                'university_id': self.university_id_counter,
                'course_name': course['name'],
                'level': course['level'],
                'discipline': course['discipline'],
                'duration': course['duration'],
                'fees': course['fees'],
                'eligibility': course['eligibility']
            })
            self.course_id_counter += 1
        
        self.university_id_counter += 1
        time.sleep(1)
    
    def scrape_all_universities(self):
        print("Starting web scraping process...\n")
        
        self.scrape_mit()
        self.scrape_stanford()
        self.scrape_oxford()
        self.scrape_cambridge()
        self.scrape_harvard()
        self.scrape_caltech()
        self.scrape_eth_zurich()
        self.scrape_ntu_singapore()
        self.scrape_university_of_tokyo()
        self.scrape_imperial_college()
        
        print(f"\n✓ Scraping completed!")
        print(f"  - Total universities: {len(self.universities)}")
        print(f"  - Total courses: {len(self.courses)}")
    
    def clean_data(self):
        print("\nCleaning and validating data...")
        
        universities_df = pd.DataFrame(self.universities)
        universities_df = universities_df.drop_duplicates(subset=['university_name'])
        
        courses_df = pd.DataFrame(self.courses)
        courses_df = courses_df.drop_duplicates()
        
        universities_df = universities_df.fillna('')
        courses_df = courses_df.fillna('Not available')
        
        print("✓ Data cleaned successfully!")
        
        return universities_df, courses_df
    
    def export_to_excel(self, filename: str = 'universities_courses_data.xlsx'):
        print(f"\nExporting data to Excel: {filename}")
        
        universities_df, courses_df = self.clean_data()
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            universities_df.to_excel(
                writer,
                sheet_name='Universities',
                index=False
            )
            
            courses_df.to_excel(
                writer,
                sheet_name='Courses',
                index=False
            )
        
        print(f"✓ Excel file created successfully: {filename}")
        print(f"\nData Summary:")
        print(f"  Sheet 1 (Universities): {len(universities_df)} records")
        print(f"  Sheet 2 (Courses): {len(courses_df)} records")
        print(f"\n✓ Assignment completed successfully!")
        
        return filename


def main():
    print("=" * 60)
    print("UNIVERSITY AND COURSE DATA SCRAPER")
    print("=" * 60)
    
    scraper = UniversityScraper()
    
    scraper.scrape_all_universities()
    
    excel_file = scraper.export_to_excel()
    
    print(f"\n{'=' * 60}")
    print(f"File saved at: {excel_file}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
