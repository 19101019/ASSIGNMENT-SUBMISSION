import json

# Data extracted manually and verified from the tables on pages 1 and 2 of the document.
noticee_data = [
    ("MAHESHWARI FINANCIAL SERVICES PVT. LTD.", "AAACM9185B"),
    ("AUTOLITE AGENCIES PVT. LTD.", "AAECA1487G"),
    ("TOOR FINANCE COMPANY LTD.", "AAACT5163G"),
    ("STELLAR CAPITAL SERVICES LTD.", "AAACS3356A"),
    ("PREMLAL ROY", "ACRPR2362R"),
    ("ARIES COMMERCIALS", "AAVFA6230F"),
    ("MOONLIGHT UDYOG", "AAUFM6147N"),
    ("SHRI RAM TRADERS", "ACDFS3492D"),
    ("CHANDRA PRAKASH BALKISANJI LADDHA", "AAGPL9225Q"),
    ("ANSHU KATARUKA", "BFUPK6760D"),
    ("GOPAL BANSAL (HUF)", "AAEHG7205B"),
    ("HETAB S KANGAD (HUF)", "AAEHH5347D"),
    ("VINDYAVASINI AGENCY PVT LTD*", "AADCV8452B"),
    ("MKR TRADING PVT. LTD.", "AAICS3344J"),
    ("FORTUNATE INFRA DEVELOPERS PVT. LTD.", "AABCF4418M"),
    ("LINKUP VINTRADE PVT. LTD.", "AABCL8020H"),
    ("OMKARA DEALER PVT. LTD.", "AABCO2405K"),
    ("OVERALL LOGISTICS PVT. LTD.", "AABCO3506H"),
    ("DACE EXIM PVT. LTD.", "AACCD9817B"),
    ("IMAGINE LOGISTICS PVT. LTD.", "AACCI3971M"),
    ("NATURAL INVESTMENT MANAGEMENT PVT. LTD.", "AACCN7952M"),
    ("DHIRGA MARKETING PRIVATE LTD.", "AADCD9678H"),
    ("ECOSPACE INFOTECH PVT. LTD.", "AADCE0088L"),
    ("E TRICKS ENTERPRISES PVT. LTD.", "AADCE4004G"),
    ("EVERBLINK AGENCY PVT LTD", "AADCE7290C"),
    ("HEADFIRST VINIMAY PVT. LTD.", "AADCH4445A"),
    ("RICHI CONSULTANTS PVT LTD", "AADCR9667C"),
    ("VIGHNAHARTA INFRA DEVELOPERS PVT. LTD.", "AADCV4831G"),
    ("VEENIT BUILDERS PVT LTD*", "AADCV6070D"),
    ("VEEPRA REALESTATE CONSULTANTS PVT. LTD.", "AADCV8456F"),
    ("GOODPOINT COMMODEAL PVT. LTD.", "AAECG5864F"),
    ("KRUSHANA INFRA PROPERTY PVT. LTD.", "AAECK1734G"),
    ("RAJPUTANA DIGITAL MEDIA PVT. LTD.", "AAECR9659R"),
    ("GOLDENSIGHT COMMOTRADE PVT LTD", "AAFCG6723L"),
    ("SURAKSHIT MERCHANTS PVT. LTD.", "AANCS7666N"),
    ("SURABHI DEALMARK PVT. LTD.", "AAQCS6011A"),
    ("SANSHIPT BROKING AND CONSULTANCY PVT LTD.", "AATCS6941G"),
    ("RAM YADAV", "ALCPY3487E"),
    ("NICKY MARMO LTD.", "AAACN3607P"),
    ("OPTIMAL FARMS PVT. LTD.", "AABCO1420E"),
    ("BIJ BUILDCON INDIA PVT. LTD.", "AAECB6648Q"),
    ("SANJEEV GOEL", "AAPPG1345M"),
    ("RAJNI GOEL", "AAPPG1338J"),
    ("SATVINDER KAUR", "AAXPK8350J"),
    ("HARVINDER SINGH", "AAQPS9683R"),
    ("GURUPREET SANGLA", "APZPS2922M"),
    ("AMIT KHANDELWAL", "AJRPK8212G"),
    ("RENU AGARWAL", "AAYPA6162D"),
    ("SEEMA SANGLA", "AFHPJ0275Q"),
    ("ANKIT KHANDELWAL", "BBUPK5756R"),
    ("HARVINDER SINGH (HUF)", "AACHH8750E"),
    ("KULDEEP KAUR", "AIGPS1433B"),
    ("GYAN PRAKASH RAI", "AOPPR4394M"),
    ("K ASHOK KUMAR (HUF)", "AAAHA4378M"),
    ("K ASHOK KUMAR", "AAFPK4721R"),
    ("MANJU RAI", "ACFPR5859M"),
    ("ASHOKKUMAR AASHISH BOHRA", "BMKPB4897F"),
    ("VIMALA BOHRA", "AACPA9761E"),
    ("NISHA SHARMA", "ADFPC4328R"),
    ("SHUBHRA KHANDELWAL", "AQSPR5044F"),
    ("MAYA DEVI KHANDELWAL", "ADZPK9924F"),
    ("NIDHI KHANDELWAL", "ATFPK3499M"),
    ("DROPDI DEVI", "ACDPD4284G"),
    ("RAJEEV GOEL (HUF)", "AAEHR5208M"),
    ("HANS RAJ AGARWAL", "ABBPA8231D"),
    ("ASHOK SNEHA BOHRA", "AUOPB2860R"),
    ("RAHUL GOEL", "AWJPG9626R"),
    ("AAMIR MEMON", "BSFPM3219K"),
    ("MADHUR BUILDCON PVT. LTD.", "AAFCM9969G"),
    ("SURBHI INFRAPROJECT PVT. LTD.", "AAMCS9707M"),
]

# Used a list comprehension to generate the required relations in the specified format
extracted_relations = [
    f"Entity (PAN): {pan} --- Relation: PAN_Of --- Entity Name: {name.replace('*', '').strip()}"
    for name, pan in noticee_data
]

# Print the list of extracted entities and relations
print("--- Extracted Entities and Relations (Formatted Output) ---")
for relation in extracted_relations:
    print(relation)



# Save the extracted relations to a JSON file
with open("extracted_relations.json", "w") as json_file:
    json.dump(extracted_relations, json_file, indent=4) 


print("\nExtracted relations have been saved to 'extracted_relations.json'.")


# link to the Output CSV: https://docs.google.com/spreadsheets/d/1bGIlpltmk_4X9PhGlqr3kISUnuQTkTBoCFa2fGp2OT8/edit?usp=sharing