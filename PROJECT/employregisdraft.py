import tkinter as tk
from tkinter import Label, Frame, Text, Button, ttk
from PIL import Image, ImageTk

# Initialize the main window
window = tk.Tk()
window.title('Employee Registration')
window.geometry('782x1020')
window.configure(bg='#f6f4f4')

# Define the GUI design class
class DesignGUI:
    def __init__(self, root):
        self.root = root

    def create_frame(self, x, y, width, height, bg='#c4c0c0'):
        frame = Frame(self.root, width=width, height=height, bg=bg)
        frame.place(x=x, y=y)
        return frame

    def create_heading(self, x, y, text):
        heading = Label(self.root, text=text, fg='black', bg='#f6f4f4', font=('Algerian', 25, 'bold'))
        heading.place(x=x, y=y)
        return heading

    def create_label(self, x, y, text, font=('Segoe UI', 9), bg='#c4c0c0'):
        label = Label(self.root, text=text, bg=bg, font=font)
        label.place(x=x, y=y)
        return label

    def create_textbox(self, x, y, width=25, height=1, bg_color='white'):
        textbox = Text(self.root, width=width, height=height, fg="black", bg=bg_color, font=('Segoe UI', 9))
        textbox.place(x=x, y=y)
        return textbox

    def create_combobox(self, x, y, values, width=22):
        combo = ttk.Combobox(self.root, width=width, values=values, font=('Segoe UI', 9))
        combo.place(x=x, y=y)
        return combo

    def create_button(self, x, y, text, width=10, height=1, command=None, font=('Segoe UI', 10), fg='black', bg='blue'):
        button = Button(self.root, text=text, width=width, height=height, bg=bg, fg=fg, font=font, command=command)
        button.place(x=x, y=y)
        return button

    def create_image(self, image_path, x, y, width, height):
        image = Image.open(image_path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        label = Label(self.root, image=photo, bg='white')
        label.image = photo  # Prevent garbage collection
        label.place(x=x, y=y)
        return label

# Instantiate the GUI design class
gui = DesignGUI(window)

# Header
header = gui.create_heading(40, 18, "SERI'S EMPLOYEE PERSONAL INFORMATION")

# First Frame
personal_frame = gui.create_frame(20, 125, 740, 145)

# Basic Information for first frame
gui.create_label(140, 140, 'First Name')
gui.create_textbox(140, 163, width=26)
gui.create_label(310, 140, 'Middle Name')
gui.create_textbox(310, 163, width=26)
gui.create_label(480, 140, 'Last Name')
gui.create_textbox(480, 163, width=26)
gui.create_label(650, 140, 'Suffix')
gui.create_textbox(650, 163, width=15)

# Combo box Row for first frame (Date of Birth, Gender, Nationality, and Civil Status)
# Date of birth (Day, Month, and Year)
gui.create_label(140, 193, 'Date of Birth')

# Day Combobox
day_combo = ttk.Combobox(window, width=3, values=[str(i) for i in range(1, 32)])
day_combo.place(x=140, y=216)

# Month Combobox
month_combo = ttk.Combobox(window, width=10, values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                                     'September', 'October', 'November', 'December'])
month_combo.place(x=180, y=216)

# Year Combobox
year_combo = ttk.Combobox(window, width=6, values=[str(i) for i in range(2025, 1899, -1)])
year_combo.place(x=262, y=216)

# Gender
gui.create_label(332, 193, 'Gender')
gender_combo = ttk.Combobox(window, width=17, values=['Male', 'Female', 'Other'])
gender_combo.place(x=332, y=216)

# Nationality
gui.create_label(468, 193, "Nationality")
nationalities_combo = ttk.Combobox(window, width=20, values=[
                 'Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguan', 'Argentine', 'Armenian', 'Australian',
                 'Austrian', 'Azerbaijani', 'Bahamian', 'Bangladeshi', 'Barbadian', 'Barbadian', 'Belarusian', 'Belgian', 'Belizean',
                 'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Botswana', 'Brazilian', 'Bruneian', 'Bulgarian', 'Burundian', 'Cambodian',
                 'Cameroonian', 'Canadian', 'Cape Verdean', 'Caymanian', 'Central African', 'Chilean', 'Chinese', 'Colombian', 'Comorian',
                 'Congolese', 'Costa Rican', 'Croatian', 'Cuban', 'Cypriot', 'Czech', 'Danish', 'Djiboutian', 'Dominican', 'Dutch',
                 'Ecuadorean', 'Egyptian', 'Salvadoran', 'Equatorial Guinean', 'Eritrean', 'Estonian', 'Ethiopian', 'Fijian', 'Filipino',
                 'Finnish', 'Gabonese', 'Gambian', 'Georgian', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan', 'Guinean', 'Guyanese', 'Haitian',
                 'Honduran', 'Hungarian', 'Icelander', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian', 'Jamaican',
                 'Japanese', 'Jordanian', 'Kazakhstani', 'Kenyan', 'Kittitian', 'Kosovar', 'Kuwaiti', 'Kyrgyzstani', 'Laotian', 'Latvian',
                 'Lebanese', 'Lesothan', 'Liberian', 'Libyan', 'Liechtenstein', 'Lithuanian', 'Luxembourgian', 'Macedonian', 'Malagasy',
                 'Malawian', 'Malaysian', 'Maldivian', 'Malian', 'Malta', 'Mauritian', 'Mexican', 'Moldovan', 'Monacan', 'Mongolian',
                 'Montenegrin', 'Moroccan', 'Mozambican', 'Namibian', 'Nauruan', 'Nepali', 'Netherlandish', 'New Zealander', 'Nicaraguan',
                 'Nigerian', 'Nigerien', 'North Korean', 'Northern Mariana Islander', 'Norwegian', 'Omani', 'Pakistani', 'Palauan',
                 'Panamanian', 'Papua New Guinean', 'Paraguayan', 'Peruvian', 'Polish', 'Portuguese', 'Qatari', 'Romanian', 'Russian',
                 'Rwandan', 'Saint Kitts and Nevis', 'Saint Lucian', 'Saint Vincent and Grenadines', 'Samoan', 'San Marinese', 'Sao Tomean',
                 'Saudi', 'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovak', 'Slovenian', 'Solomon Islander',
                 'Somali', 'South African', 'South Korean', 'Spanish', 'Sri Lankan', 'Sudanese', 'Surinamese', 'Swazi', 'Swedish', 'Swiss',
                 'Syrian', 'Taiwanese', 'Tajikistani', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian', 'Tunisian', 'Turkish',
                 'Turkmen', 'Ugandan', 'Ukrainian', 'Uruguayan', 'Venezuelan', 'Vietnamese', 'Yemeni', 'Zambian', 'Zimbabwean'
                 ])
nationalities_combo.place(x=468, y=216)

# Civil Status
gui.create_label(622, 193, 'Civil Status')
status_combo = ttk.Combobox(window, width=17, values=['Single', 'Married', 'Divorced', 'Widowed'])
status_combo.place(x=622, y=216)

# Profile image (placeholder)
profile_image = gui.create_image('C:\\Users\\valde\\Documents\\GitHub\\LAB-3-FILES---VALDEZ\\LAB-3-FILES---VALDEZ\\IMAGES\\Profile.jpg', 22, 77, 100, 100)

# Label for file selection (Placeholder text)
no_file_label = gui.create_label(68, 184, 'No file chosen', font=('Segoe UI', 7), bg='#c4c0c0')

# 'Choose File' button
upload_button = gui.create_button(19, 183, 'Choose File', width=8, height=0, font=('Segoe UI', 7), fg='black', bg='light gray')

# Second Frame
employment_frame = gui.create_frame(20, 290, 740, 150)

# Employment Information for second frame
gui.create_label(35, 305, 'Department')
gui.create_textbox(35, 330, width=53)  # Customize width
gui.create_label(368, 305, 'Designation')
gui.create_textbox(368, 330, width=33)  # Customize width

# Qualified Dept. Status Combo box
gui.create_label(580, 305, 'Qualified Dept. Status')
qualified_combo = ttk.Combobox(window, width=24, values=['Qualified', 'Pending', 'Not Qualified'])
qualified_combo.place(x=580, y=330)

gui.create_label(35, 360, 'Employee Status')
gui.create_textbox(35, 385, width=61)  # Customize width

# Paydate (Month, Day, Year)
gui.create_label(415, 360, 'Paydate')

# Month Combobox
month_combo_paydate = ttk.Combobox(window, width=5, values=[str(i) for i in range(1, 13)])
month_combo_paydate.place(x=415, y=385)

# Day Combobox
day_combo_paydate = ttk.Combobox(window, width=4, values=[str(i) for i in range(1, 32)])
day_combo_paydate.place(x=467, y=385)

# Year Combobox
year_combo_paydate = ttk.Combobox(window, width=6, values=[str(i) for i in range(2025, 1899, -1)])
year_combo_paydate.place(x=513, y=385)

gui.create_label(580, 360, 'Employee Number')
gui.create_textbox(580, 385, width=27)  # Customize width

# Third Frame
contact_frame = gui.create_frame(20, 460, 740, 150)

# Contact Information for third frame
gui.create_label(35, 475, 'Contact No.')
gui.create_textbox(35, 500, width=50)  # Customize width
gui.create_label(350, 475, 'Email')
gui.create_textbox(350, 500, width=65)

# Social Media Combobox
gui.create_label(35, 530, 'Other (Social Media)')
socials_combo = ttk.Combobox(window, width=47, values=['Facebook', 'Twitter (X)', 'Instagram'])
socials_combo.place(x=35, y=555)

gui.create_label(350, 530, 'Social Media Account ID/No.')
gui.create_textbox(350, 555, width=65)  # Customize width

# Fourth Frame
address_frame = gui.create_frame(20, 630, 740, 315)

# Address for fourth frame
gui.create_label(35, 645, 'Address Line 1')
gui.create_textbox(35, 670, width=117)  # Customize width
gui.create_label(35, 700, 'Address Line 2')
gui.create_textbox(35, 725, width=100)  # Customize width
gui.create_label(35, 755, 'City/Municipality')
gui.create_textbox(35, 780, width=58)  # Customize width
gui.create_label(400, 755, 'State/Province')
gui.create_textbox(400, 780, width=56)  # Customize width

# Country Combobox
gui.create_label(35, 810, "Country")
countries_combo = ttk.Combobox(window, width=55, values=[
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
    'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia',
    'Comoros', 'Congo (Congo-Brazzaville)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Democratic Republic of the Congo',
    'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea',
    'Estonia', 'Eswatini (fmr. "Swaziland")', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany',
    'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary',
    'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan',
    'Kenya', 'Kiribati', 'Korea (North)', 'Korea (South)', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon',
    'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
    'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia',
    'Montenegro', 'Morocco', 'Mozambique', 'Myanmar (formerly Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
    'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia (formerly Macedonia)', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine State',
    'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
    'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe',
    'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands',
    'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',
    'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
    'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Uruguay', 'Uzbekistan',
    'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'])
countries_combo.place(x=35, y=835)

gui.create_label(400, 810, 'Zip Code')
gui.create_textbox(400, 835, width=56)  # Customize width

gui.create_label(35, 865, 'Picture Path')
gui.create_textbox(35, 890, width=117)  # Customize width

# Buttons
gui.create_button(20, 960, 'Save', width=10, height=1, font=('Segoe UI', 9), fg='white', bg='#2b81d1', command=None)
gui.create_button(120, 960, 'Cancel', width=10, height=1, font=('Segoe UI', 9), fg='black', bg='#f6f4f4', command=None)

# Runs the code
window.mainloop()