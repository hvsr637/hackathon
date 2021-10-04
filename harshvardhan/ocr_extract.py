import re

voter_id =  ['02/09/1084', 'Date Of Birth Age', 'Address HN H N 19A VRINDAVAN GARDEN SAHIBABAD', 'Code-201005', '04/04/2014', 'Scanned Signature of', 'Date', 'Electoral Registration Officer', 'Assembly Constituency No. & Name', '55 Sahibabad', 'Part No and Name', '506', 'GHAZIABAD PUBLIC SCHOOL', 'VRINDAVAN GARDEN', 'Mere possession of this card is no guarantee that you', 'are elector in the current electoral roll. Please check your', 'name in the current electoral roll before every election.', 'Date of Birth mentioned in this card shall not be treated', 'as a proof of age 1 D.O.B. for any purpose other than', 'registration in electoral roll.', '201310001213']
driving_license =  ['K-0420110066139', 'Mobile No.', 'OD', 'MCWG', 'LMV', '23-09-2011', '23-09-2011', 'Endorsement Date', '12-06-2018', 'UK', 'Endorsement No', 'UK04 /DLD/0001681/2018', 'Present Address', 'H.N. 45 KHA LAMACHAUDKHAS', 'HALDWANI', 'NAINITAL U.K.', 'ALDWANINAINITAL.263139', 'issuing Authority Sign', "Holder's Signature", 'RTO HALDWANINAINITAL']
pan_card = ['BTX TATT', 'INCOME TAX DEPARTMENT', 'GOVT. OF INDIA', 'Permanent Account Number Card', 'CHGPG0505B', 'HTH /Name', 'RASHI GUPTA', "fHaT cut HTH Father's Name", 'PAWAN GUPTA', 'GIEH t arra Date of Birth', '17/06/1999', 'erpto']
passport =  ['SINIW', '3TUT2T54 REPUBLIC OF INDIA', 'P', 'IND', 'omSurname', 'K4931604', 'GUPTA', 'fem Given Name(s)', 'RASHI', 'greret/Nationaiity', 'fer 1 Sex', 'Ontin of Birth', 'INDIAN', 'F', '17106/1999', '/ Place of Birth', 'INDORE M.P.', 'ora aa T RTPE 1 Place of taste', 'BHOPAL', 'Qunto', 'ona fef/Date of Issue', '25/05/2012', '2410512017', 'P<INDGUPTA<<RASHI< AS<RASHI<<<<<<<<<<<<<<<<<<<<<<<<((', 'K4931604<3IND9906172F1705243< K4931604 4931604<3IND990 <3 F 1705243 43<<<<<<<<<<<<<<<8']
abc = ['Shift', 'Aadhaar is valid throughout the country', 'Aadhaar will be helpful in availing Government', 'and Non-Government services in future', 'End', 'Unique Identification Authority of india', 'Address: D/O Sanjay Solanki, Makan N0-4,', 'Ward NO- 21, Datt Mandir Ki Gali,', 'Budhawara, Burhanpur, Burhanpur,', 'Madhya Pradesh, 450331', '6970 7344 4852', '1947', 'help@uidai.gov.in', 'www.uidai.gov.in']
data_list = [' GOVERNMENT OR INDIA Sudeep Kumar Motwani DOB 22 06 1993 MALE 586341165875 ', 'GOVERNMENT', 'OR', 'INDIA', 'Sudeep', 'Kumar', 'Motwani', 'DOB ', '22 06 1993', 'MALE', '586341165875']


gender  = re.findall('Female|Male', data_list[0])
dob = re.findall('\d{2} \d{2} \d{4}', data_list[0])[0].replace(' ', '-')
try:
    doc_number = re.findall( '\d{4}\d{4}\d{4}', data_list[0])[0]
except:
    pass
name_index = data_list.index('INDIA')
name = data_list[name_index + 1] + ' ' + data_list[name_index + 2]