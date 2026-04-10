"""
Knowledge base for METU IE Summer Practice Chatbot.
Contains all information scraped from https://sp-ie.metu.edu.tr/en
"""

KNOWLEDGE_CHUNKS = [
    # --- GENERAL INFORMATION ---
    {
        "id": "general_physical",
        "topic": "General Information - Physical Attendance",
        "content": "Summer internships must be done by physically attending the work place. Remote or online internships are not accepted."
    },
    {
        "id": "general_ie400_project",
        "topic": "IE 400 Project Based Internship",
        "content": "For IE 400, project based internships are allowed. Project based internship should be at least 6 weeks (30 workdays). Before the internship, you need to submit a proposal to the SP Committee which covers the content of the internship in detail. If the proposal is approved you can do the project based internship. The proposal should include a brief description of the company, details of the proposed project, and an outline of what will be included in the report. The proposal should be approved (signed) by the company and submitted to the summer practice committee by the first week of the summer practice."
    },
    {
        "id": "general_public_institutions",
        "topic": "Internships in Public Institutions",
        "content": "All public institutions in Turkey (Kamu kurumları) accept internship applications through a centralized system. Students should consult https://kariyerkapisi.cbiko.gov.tr/ for further information about applying to public institutions for summer practice."
    },
    {
        "id": "general_erasmus",
        "topic": "Erasmus Internship",
        "content": "Within the Erasmus program, it is possible to do an internship within the scope of Student Internship mobility. Students may generally prefer an internship in Europe for a minimum of 3 months and a maximum of 12 months. For detailed information, check the Erasmus office website at https://ico.metu.edu.tr/. If the summer internships completed within the scope of this program are made for a short term (3 months), it can only be counted as one of IE300 and IE400 internship, not both."
    },
    # --- SGK INSURANCE ---
    {
        "id": "sgk_overview",
        "topic": "SGK Insurance Application Overview",
        "content": "SGK Insurance Applications are managed via METU OpenCourseWare platform (OCW) at https://ocw.metu.edu.tr/. All 1st, 2nd, 3rd, and 4th year students are registered to the 'IE300/400 Summer Internship' course by default. This OCW course is created only for the practical purpose of collecting insurance application information. It is not a real course. Students still need to register for IE300 or IE400 courses in the Fall semester after the internship is complete."
    },
    {
        "id": "sgk_when_to_apply",
        "topic": "When to Apply for SGK Insurance",
        "content": "The ideal time to apply for SGK insurance using the OCW system is 2-3 weeks before the beginning of the internship. On the Monday morning of each week, insurance applications of students beginning their internships within two weeks will be sent to Rektörlük. Students should leave a safety margin of 1 whole week (Monday to Friday) between their application and the beginning of the SP. Do not apply too early (e.g., 2 months before) because Rektörlük does not process applications that start in more than two weeks, and plans may change. Do not apply too late (e.g., 5 days before) as this leads to delays."
    },
    {
        "id": "sgk_how_to_apply",
        "topic": "How to Apply for SGK Insurance",
        "content": "To apply for SGK insurance: 1) Login to https://ocw.metu.edu.tr/ with your student account. 2) Find the IE 300/400 course under 'My courses'. If you cannot see it, email the SP committee at ie-staj@metu.edu.tr. 3) Click on IE 300/400, find 'Required Information' in the course menu. 4) Click on 'SGK Insurance Application' and fill in the questionnaire with identity and company information, then click 'Submit Questionnaire'. 5) Upload the 'Declaration Form for students with/without family health insurance' which can be found at the Documents/Forms page of the SP website."
    },
    {
        "id": "sgk_document",
        "topic": "SGK Insurance Document",
        "content": "The SGK insurance document will be available on e-devlet (turkiye.gov.tr) typically 2-3 workdays before the beginning of the SP. To access it: login to turkiye.gov.tr, type 'işe giriş' in the search field, select '4A İşe Giriş Çıkış Bildirgesi (Sosyal Güvenlik Kurumu)', find the line for your current SP, and click 'Belge oluştur'. The SP committee does not send the SGK document by email."
    },
    {
        "id": "sgk_emergency",
        "topic": "Emergency SGK Application",
        "content": "If the internship starts soon and there are no Mondays between the current date and the SP beginning date, and the student was unable to apply via OCW on time, they should fill in the emergency excel file from the SP website with internship information and email it to ie-staj@metu.edu.tr with the subject line: 'SGK basvurusu: Name Surname dd.mm.2025'. This emergency solution should only be used with a very valid reason."
    },
    {
        "id": "sgk_mistakes",
        "topic": "SGK Application Mistakes",
        "content": "If you made a mistake in your SGK Insurance Application questionnaire: First check if your application has already been sent to Rektörlük (check Rule 2 in 'When to apply'). If NOT yet sent: enter a new questionnaire with correct information, the most recent version will be used and older ones ignored. If ALREADY sent: contact the SP committee at ie-staj@metu.edu.tr. If your internship is cancelled: contact the SP committee. If your internship is approaching and your SGK document is not ready: Rektörlük issues documents typically 2-3 workdays before. If there are still 2 workdays until your SP, wait. If SP begins next workday and document is not accessible, contact the SP Committee in the morning."
    },
    # --- VOLUNTARY INTERNSHIPS ---
    {
        "id": "voluntary_internship",
        "topic": "Voluntary Internships",
        "content": "Students can do voluntary internships in summer and get SGK insurance. Voluntary internships are not mandatory and not required by the department. The process is between the student and the company, no letter from the committee is needed. SGK insurance is provided for up to one month for one company. Follow the same OCW procedure for a new SGK application, but make sure the second application is submitted only after the SGK document of the first internship is already issued. Rektörlük recommends leaving at least one blank day between two SPs. IMPORTANT: Foreign students are NOT allowed to do voluntary internships in Turkey - a work permit is required."
    },
    # --- PAID SUMMER PRACTICE ---
    {
        "id": "paid_sp",
        "topic": "Paid Summer Practice Instructions",
        "content": "If you did your SP in a private company in Turkey and received payment, you need to do the following after finishing the SP and receiving all payments (this does NOT apply to public institutions or unpaid SPs): 1) Login to ocw.metu.edu.tr. 2) Fill in the 'Paid SP form questionnaire' under IE300/400 course carefully - incomplete submissions are rejected by Rektörlük. 3) Download, print, and sign the Paid Summer Practice Form (İşsizlik Fonu Katkısı Bilgi Formu), upload the scanned signed copy in PDF format. 4) Upload the bank receipt (PDF) showing payment received from the company. If you made a mistake, submit a new form and the latest submission will be taken into account."
    },
    # --- STEPS TO FOLLOW ---
    {
        "id": "steps_before",
        "topic": "Steps Before Summer Practice",
        "content": "Before summer practice: 1) Examine the Summer Practice Website early. 2) Read the Summer Practice Manual from the Documents/Forms tab. 3) Check information about paid/SGK insurance on the website. 4) Find a company - check the department's list of companies, use social connections, or examine earlier SP databases. 5) Some companies need a letter (SP Application Letter from Documents/Forms tab) explaining the internship aim, minimum duration, and METU insurance coverage. 6) Some companies may request an SP protocol (sözleşme/agreement) form - fill it out and leave it at Undergraduate Secretary Office (IE 129), pick up the signed form in a week. 7) Apply for SGK insurance on time via OCW. 8) Start your summer work."
    },
    {
        "id": "steps_during",
        "topic": "Steps During Summer Practice",
        "content": "During summer practice: 1) Attend work with full concentration, observe and participate. 2) Regularly take notes for the final report. 3) Prepare a draft of your report while doing the practice. 4) Have the 'SP Evaluation Form' and 'Employer Survey' filled out and signed by your SP supervisor. 5) Your SP supervisor can send these forms to sp-belge@metu.edu.tr in PDF format (traditional or digital signature). They can also send by post in a closed envelope. 6) If you received payment, fill in the 'Paid SP Questionnaire' on OCW, upload the signed Paid SP Form and bank receipt."
    },
    {
        "id": "steps_after",
        "topic": "Steps After Summer Practice",
        "content": "After summer practice: 1) Prepare your report following the Summer Practice Manual. 2) Register for IE 300 or IE 400 during the registration period. 3) SP reports are collected via ODTUClass with a strict deadline that will be announced. 4) The SP report should be in PDF format. 5) Reports will be checked for plagiarism and whether they are generated by AI tools. 6) Reports will be graded by assigned faculty members. 7) In the last month of the semester, reports requiring corrections will be returned to students. 8) Students have 2-3 weeks to complete requested corrections and return the report via ODTUClass."
    },
    # --- FAQ ---
    {
        "id": "faq_arrange_sp",
        "topic": "FAQ - How to arrange a summer practice",
        "content": "There are two alternatives: apply to organizations personally or wait for summer practice opportunities announced by the department. The second option is more risky and has limited capacity. Certain firms require the department to determine candidates, in which case an announcement is made and students send transcripts, resumes, and fill out the Preference Form. If assigned through the department, the summer practice must be conducted at that company."
    },
    {
        "id": "faq_departments_to_visit",
        "topic": "FAQ - Which departments to visit during SP",
        "content": "It is preferable to take an all-around trip in the organization. However, you can still gather observations through effective communication. You can inquire about overall operations even if stationed at a particular department."
    },
    {
        "id": "faq_topics",
        "topic": "FAQ - Topics during summer practice",
        "content": "Industrial engineering has a broad application area focused on systems run by people for the needs of others. Summer practice is the first lengthy period of observing and inquiring about systems in operation. Try to relate course topics to what you experience. Learn about various ways of getting organizational and technical functions performed. Identify systems behind activities. Use the Summer Practice Manual as a guide."
    },
    {
        "id": "faq_bank_ie400",
        "topic": "FAQ - Bank divisions for IE 400",
        "content": "For IE 400 in a bank, be interested in the systems aspects: organizational, information-related, procedural, and managerial in service provision. Divisions or branches are suitable as long as they consist of integrated operation of people, financial resources, processes, and information with performance expectations, and have ongoing decision making (planning, evaluation) or development (new services) as required functions."
    },
    {
        "id": "faq_paperwork",
        "topic": "FAQ - Required paperwork for SP registration",
        "content": "Four steps are required: 1) Add IE 300 or IE 400 course during registration at the beginning of the semester. 2) Submit SP reports to Students Affair Secretary (Room IE 128) within the first two weeks of the following academic term, also submit soft copy through the website. 3) The company should send filled and signed evaluation form and employer survey to Student Affairs Secretary. 4) Fill out the online questionnaire (will be announced)."
    },
    {
        "id": "faq_ie400_problem",
        "topic": "FAQ - IE 400 problem definition",
        "content": "A sufficient IE problem definition for IE 400 is described in Appendix A of the IE 400 Summer Practice Manual. Students must supply their own description of problem formulation components and justify their points, specific to the practice organization. Problem identification should result from methodical analysis. Alternative courses of action and constraining factors should be supported by problem-specific facts."
    },
    {
        "id": "faq_service_org",
        "topic": "FAQ - Manufacturing questions in service organization",
        "content": "The critical issue is to see the analogies between manufacturing and service. Budget allocation can substitute a production plan, preclassified records can stand as inventory, timetables for professionals can be their schedules, form flow may replace material flow. Highlight the reasons that justify such similarities in your specific case."
    },
    {
        "id": "faq_multiple_students",
        "topic": "FAQ - Multiple students at same organization",
        "content": "Every practitioner will have a separate report. For IE 400, the general outlook at the firm can be common. However, separate examples should be chosen for reporting. The questions part must be different for each practitioner. For problem definition/project: problem definitions must be different in any case. The project part might be the same if the project is complex (valid for at most two students). Students doing project type IE 400 can prepare either a regular report or a project type report."
    },
    {
        "id": "faq_ie400_service_manual",
        "topic": "FAQ - IE 400 service sector manual",
        "content": "Yes, a manual for IE 400 summer practice in the service sector is available. A copy can be obtained from the photocopy office in the department."
    },
    {
        "id": "faq_project_type",
        "topic": "FAQ - Project type IE 400 practice",
        "content": "IE 400 practice may involve a full-time project where students submit a project report instead of defining an IE problem. Minimum duration is 30 workdays (6 weeks). The project may have been initiated earlier, offered by the organization, or identified by the student. Students need to submit a two-page project proposal including a brief company description, project details, and report outline. The proposal must be approved (signed) by the company and submitted to the SP committee by the first week of summer practice. The report should describe all phases including the issue, organizational environment, data collected, tools used, outcomes, and implementation."
    },
    # --- SP COMMITTEE ---
    {
        "id": "sp_committee",
        "topic": "SP Committee Contact Information",
        "content": "SP Committee members: Esra Karasakal (Room 215, Tel: +90 312 210 2278), Cem İyigün (Room 331, Tel: +90 312 210 2282), Çiya Aydoğan (Room 214, Tel: +90 312 210 4792), Mehmet Sencer Zengin (Room 318, Tel: +90 312 210 2269), Özgür Ünverdi (Room 326, Tel: +90 312 210 4687), Buğra Öztürk (Room 325, Tel: +90 312 210 2277), Ömer Turan Şahinaslan (Room 136, Tel: +90 312 210 4796). Fax: +90 312 210 4786. Email: ie-staj@metu.edu.tr"
    },
    # --- IE 300 vs IE 400 ---
    {
        "id": "ie300_vs_ie400",
        "topic": "IE 300 vs IE 400 Requirements",
        "content": "IE 300 is the first summer practice course focused on observing and understanding industrial/manufacturing systems. IE 400 is the second summer practice course with more advanced requirements including problem definition, analysis, and potentially project-based work. IE 400 requires a minimum of 20 workdays for regular internship, or 30 workdays (6 weeks) for project-based internship. Both courses require physical attendance at the workplace, SGK insurance, and submission of reports via ODTUClass."
    },
    {
        "id": "sp_meeting_2025",
        "topic": "SP Meeting 2025",
        "content": "A general meeting on IE 300 and IE 400 summer internship courses and Summer Practice procedures was held on March 14, 2025, at 14:40. IE 300 meeting was in IE03 and IE 400 meeting was in IE04. The meeting slides can be found on the Documents/Forms page of the SP website."
    },
    {
        "id": "sp_contract",
        "topic": "Summer Practice Work Contract",
        "content": "If you need your SP work contract (staj sözleşmesi) to be signed, leave it at the Undergraduate Secretary Office, IE 129 and get it back in one week."
    },
    # --- ADDITIONAL CUSTOM FAQ ---
    {
        "id": "custom_duration",
        "topic": "Summer Practice Duration",
        "content": "IE 300 summer practice is typically 20 workdays (4 weeks). IE 400 summer practice is also typically 20 workdays for regular internship. For project-based IE 400, the minimum duration is 30 workdays (6 weeks). All internships must be completed physically at the workplace."
    },
    {
        "id": "custom_report_format",
        "topic": "Report Format and Submission",
        "content": "SP reports should be prepared in PDF format following the Summer Practice Manual available on the SP website. Reports are submitted via ODTUClass with a strict deadline announced at the beginning of the semester. Reports are checked for plagiarism and AI-generated content. Students may be asked to make corrections, and they have 2-3 weeks to complete corrections."
    },
    {
        "id": "custom_abroad",
        "topic": "Summer Practice Abroad",
        "content": "Students can do their summer practice abroad. The Erasmus program offers Student Internship mobility for internships in Europe (3-12 months). Short-term Erasmus internships (3 months) can only count as one of IE300 or IE400, not both. Students doing SP abroad should still arrange SGK insurance through the OCW system. The SP Application Letter can be used for companies abroad that need documentation."
    },
    {
        "id": "custom_contact",
        "topic": "How to Contact SP Committee",
        "content": "The SP Committee can be reached by email at ie-staj@metu.edu.tr. Before contacting, students should first check the SP website and meeting slides to see if their question is already answered. For SGK-related document submissions, use sp-belge@metu.edu.tr. The Undergraduate Secretary Office is in Room IE 129 (for document drop-off) and Room IE 128 (Students Affair Secretary)."
    },
    # --- DOCUMENTS / FORMS ---
    {
        "id": "forms_presentations",
        "topic": "Internship Presentations and Introductory Sessions",
        "content": "Internship presentation slides are available on the Documents/Forms page of the SP website. There are separate introductory session slides for IE 300 and IE 400."
    },
    {
        "id": "forms_application_letters",
        "topic": "Summer Practice Application Letters",
        "content": "SP Application Letters are available on the Documents/Forms page. There are separate forms for IE 300 and IE 400, each available in both Turkish and English versions: IE-300 SP Application Form (Turkish), IE-300 SP Application Form (English), IE-400 SP Application Form (Turkish), IE-400 SP Application Form (English). Additionally, an SP Protocol (sözleşme) form is available if requested by the company."
    },
    {
        "id": "forms_insurance",
        "topic": "Insurance Forms",
        "content": "Insurance-related forms available on the Documents/Forms page include: Declaration Form for students with family health insurance, Declaration Form for students without family health insurance, and the Paid Summer Practice Information Form (İşsizlik Fonu Katkısı Bilgi Formu). Students must upload the appropriate declaration form to the OCW system as part of the SGK insurance application."
    },
    {
        "id": "forms_evaluation",
        "topic": "SP Evaluation Form and Employer Survey",
        "content": "The SP Evaluation Form and Employer Survey must be filled out and signed by the SP supervisor at the company. Available versions: Evaluation Form and Employer Survey (Turkish version), and Evaluation Form (English version). The supervisor can send these forms to sp-belge@metu.edu.tr in PDF format with traditional or digital signature, or by post in a closed envelope."
    },
    {
        "id": "forms_manuals",
        "topic": "Summer Practice Manuals",
        "content": "Three SP Manuals are available on the Documents/Forms page: IE300 Summer Practice Manual, IE400 Summer Practice Manufacturing Manual, and IE400 Summer Practice Service Manual. Students should read the relevant manual before starting their internship to understand what is expected in the report and what to observe during the practice."
    },
    # --- SP OPPORTUNITIES (CURRENT) ---
    {
        "id": "sp_opportunities_current",
        "topic": "Current Summer Practice Opportunities",
        "content": "Current SP opportunities are listed on the SP Opportunities page (requires login). Some notable opportunities include: MS Spektral Savunma Sanayi (Başkent OSB, paid, production planning, prefers 3rd year students for IE400, may lead to full-time), NACRES Yazılım Teknoloji (for 4th year students), GÜRİŞ (Genç Yetenek long-term program, apply via LinkedIn or ODTÜ KPM), Noksel Çelik Boru (production, quality, maintenance, sales), Koçtaş (IE 400, hybrid, due April 30 2025, apply via kockariyerim.com), İGA İstanbul Airport (apply via Kariyer Kapısı), TEI TUSAŞ Motor Sanayi (Eskişehir, paid, for 4th year students), and many more companies in Ankara, Istanbul, Izmir, Bursa, and other cities. Companies offer positions in areas like production, R&D, project management, assembly, maintenance, and software."
    },
    {
        "id": "sp_opportunities_ankara",
        "topic": "SP Opportunities in Ankara",
        "content": "SP opportunities in Ankara include: TÜMAŞ (Kavaklıdere, project design and consultancy), UDEA Elektronik (Yenimahalle, production), HİDROAN (Sincan, multiple areas including production and R&D), MTM Makina (Kavaklıdere, project design and assembly, paid), MPES Mühendislik (Çankaya, project design and R&D, paid), DURUKAN Şekerleme (Sincan, production and R&D, paid), Koluman Otomotiv Hacettepe Teknokent (Çankaya, R&D, paid), BAŞÖZ Enerji (Temelli, production and maintenance, paid), DEICO (Yenimahalle, assembly and R&D), VERTE (Yenimahalle, production and R&D), Hestaş Madencilik (Çankaya, mining), EUROPOWER Enerji (paid, multiple areas)."
    },
    # --- PREVIOUS SP OPPORTUNITIES ---
    {
        "id": "prev_sp_opportunities",
        "topic": "Previous Summer Practice Opportunities and Companies",
        "content": "Previous years' SP companies include (with IE300/IE400 availability): Wicode (ODTÜ Teknokent, IE400 only), SİLKAR Madencilik (Bilecik, both IE300 and IE400), Tezcanlar Yatırım (Adana, both), Hazine ve Maliye Bakanlığı Bilgi Teknolojileri (Ankara, IE400 only), İnofab Sağlık Teknolojileri (ODTÜ Teknokent, IE400 only), Ekinciler Demir Çelik (Hatay, IE400 only), YÜKSEL Kompozit Teknolojileri (Başkent OSB Sincan, both, aviation/defense), SÖĞÜT Seramik (Bilecik, both), Stackpole International (İzmir, both, automotive), Silverline Endüstri (Merzifon/Amasya, both), Kanca El Aletleri (Kocaeli, IE400 only), Meka Beton Santralleri (Ankara, both), Akdaş Döküm (Sincan/Ankara, both), Şişecam, Eczacıbaşı Bilişim, Forte, and others. Students can check this list for reference when looking for SP companies."
    },
    # --- IE 300 PRESENTATION DETAILS ---
    {
        "id": "ie300_prerequisites",
        "topic": "IE 300 Prerequisites",
        "content": "Prerequisites for IE 300: IE 102 + IE 251, IE 265, IE 241, OHS 101 (fall semester courses) + One out of {IE 266, IE 252} (spring semester courses). If any one of these prerequisite courses is not completed with a grade >= DD, IE 300 summer practice cannot be conducted. If you are in probation in the Fall semester, you cannot take the IE 300 course even if you successfully finished your SP."
    },
    {
        "id": "ie300_overview",
        "topic": "IE 300 Course Overview",
        "content": "IE 300 is a must (compulsory) course which is non-credit. Your grade should be S (satisfactory) for graduation. It is integral and complementary to the IE curriculum. You gain your first experience of professional life. For the first time you get to know a company with all her aspects, get involved in decision problems, and get the chance of observing: the whole supply chain, manufacturing processes, sustainability concerns, cost accounting issues, use of operations research methods, use of statistical analysis and big data, team work, and IE roles and jobs."
    },
    {
        "id": "ie300_when",
        "topic": "IE 300 When to Conduct and Duration",
        "content": "IE 300 summer practice is conducted in Summer 2025. Available time interval is approximately 3 months: June 25 to September 26. If you attend summer school, your summer practice period should not overlap with summer school. Minimum practice is 20 workdays (4 weeks). If you are in graduation status and have completed all your course work, you can conduct both IE 300 and IE 400 in succession in Summer 2025."
    },
    {
        "id": "ie300_registration",
        "topic": "IE 300 Registration and Report Deadline",
        "content": "After summer practice is completed, you must register for IE 300 in the immediate academic term (Fall 2025-2026). Summer practice reports are due within the first 4 weeks of the registered academic term. Due date: October 24, 2025."
    },
    {
        "id": "ie300_company_types",
        "topic": "IE 300 Acceptable Company Types",
        "content": "IE 300 MUST be done at a MANUFACTURING firm. Acceptable types include: Automotive, Machine parts, Electronics, Furniture, Textiles, Consumer durables (refrigerator, washing machine, etc.). Batch process industries are also accepted: Steel, Paper mills, Pharmaceutical, Food and beverages. NOT accepted for IE 300: Continuous process industries (cement, concrete, sugar, flour mill) and service industries (hospitals, hotels, banking, research organizations, transportation, cargo carriers). The summer practice must be conducted totally in the factory (face-to-face). Online or hybrid types are NOT allowed for IE 300."
    },
    {
        "id": "ie300_report_rules",
        "topic": "IE 300 Report Submission Rules",
        "content": "IE 300 report submission: Upload your report at ODTUClass. The report is written based on the IE 300 manual. You should answer ALL questions in the manual. In some questions (e.g. accounting, finance), provide information about the method used at least if not provided with sufficient data. For each question, provide sufficient explanation and analysis — giving only a figure/table is not accepted. Before answering a question, read the explanation in the question and answer accordingly. Submit the soft copy (PDF file, docx converted to pdf) at ODTUClass IE 300 turnitin assignment for plagiarism check — similarity must be less than 20%. Reports are also checked whether they are AI generated. For the questionnaire, you will use METU Survey."
    },
    {
        "id": "ie300_candidate_engineering",
        "topic": "IE 300 Candidate Engineering Programs",
        "content": "Candidate engineering activities during the semesters do not count for IE 300 since SP cannot overlap with the teaching period. If you continue candidate engineering during summer and you work for 20 full workdays in a row, then you can present it for IE 300."
    },
    # --- IE 400 PRESENTATION DETAILS ---
    {
        "id": "ie400_prerequisites",
        "topic": "IE 400 Prerequisites",
        "content": "Prerequisites for IE 400: IE 300 + IE 252, IE 323, IE 333 + Any two courses from the set: {IE 304, IE 324, IE 372, IE 368}. If any one of the prerequisite courses is not completed with a grade >= DD, IE 400 cannot be conducted."
    },
    {
        "id": "ie400_when",
        "topic": "IE 400 When to Conduct and Duration",
        "content": "IE 400 summer practice is conducted in Summer 2025. Available time interval is approximately 3 months: June 25 to September 26. If you attend summer school, your summer practice period should not overlap with summer school. Minimum practice is 20 workdays (4 weeks), but this duration can be more if the company requests it. You can also conduct IE 400 during semester break in winter, if 20 workdays are available in the break. If you are in graduation status and have completed all your course work, you can conduct both IE 300 and IE 400 in succession in Summer 2025."
    },
    {
        "id": "ie400_registration",
        "topic": "IE 400 Registration and Report Deadline",
        "content": "After summer practice is completed, you must register for IE 400 in the immediate following academic term (Fall 2025-2026). Summer practice reports are due within the first 4 weeks of the registered academic term. Due date: October 24, 2025."
    },
    {
        "id": "ie400_company_types",
        "topic": "IE 400 Acceptable Company Types",
        "content": "IE 400 accepts BOTH manufacturing AND service companies. Manufacturing firms: Automotive, Machine parts, Electronics, Furniture, Textiles, Consumer durables, and batch/continuous process industries (Steel, Paper mills, Pharmaceutical, Food, Cement, Concrete, Sugar, Flour mill). Service industries: Hospitals, Hotels, Banking, Research organizations (ODTÜ Teknokent, etc.), Transportation, Cargo carriers, Public institutions, Non-governmental organizations (NGOs). For manufacturing companies: SP must be totally face-to-face. For service companies: SP can be either face-to-face or hybrid (face-to-face + online)."
    },
    {
        "id": "ie400_conduct_types",
        "topic": "IE 400 Summer Practice Types (Individual, Group, Project)",
        "content": "IE 400 summer practice can be conducted in three ways: 1) Individual: at least 20 workdays. 2) Group of two students: at least 20 workdays, each writes their own report, the project/problem should be much more involved, and students must notify the SP committee in the first week of practice. 3) Project-based: at least 6 weeks (30 workdays), a two-page proposal must be approved by the SP Committee before SP starts, content and format is different (see the manual)."
    },
    {
        "id": "ie400_report_rules",
        "topic": "IE 400 Report Submission Rules",
        "content": "IE 400 report consists of two sections: 'Questions' and 'Problem/Project' sections that are graded separately. Grade S (satisfactory) is required in BOTH parts to pass IE 400. The report is written based on IE 400 manuals — there are two types: manufacturing manual and service manual. For each question, provide sufficient explanation and analysis. Submit the soft copy (PDF, docx converted to pdf) at ODTUClass IE 400 turnitin assignment for plagiarism check — similarity must be less than 20%. Reports are also checked whether they are AI generated. For the questionnaire, use METU Survey."
    },
    {
        "id": "ie400_sd_project",
        "topic": "IE 400 Systems Design Project Opportunity",
        "content": "During IE 400 summer practice, you are required to search for a 'Systems Design Project'. Summer practice is a good opportunity to find SD projects. Make your practice effective by looking for interesting problems and asking engineers about potential challenging problems for the SD project. Once you identify an interesting and challenging problem, check it with the SD committee (not the SP committee)."
    },
    {
        "id": "ie400_paid_sp",
        "topic": "IE 400 Paid Summer Practice Procedure",
        "content": "If you receive payment during IE 400 SP: 1) Fill out the 'Paid SP questionnaire' under IE400 course at OCW. 2) Download, print, and sign the Paid SP Form (İşsizlik Fonu Katkısı Bilgi Formu) from the SP website. 3) Scan the signed form in PDF format. 4) Upload the Paid SP Form together with the bank receipt (PDF) showing payment received, under the assignment 'İşsizlik Fonu Katkısı Bilgi Formu' at OCW as a Zip file."
    },
    {
        "id": "insurance_details",
        "topic": "Insurance Coverage Details",
        "content": "The compulsory insurance covers 'iş kazası ve meslek hastalığı sigortası' (work accident and occupational disease insurance) under Law #5510 (Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu). METU provides insurance for all SP students upon application. For compulsory summer practices, insurance is made for a period of 20 workdays to 3 months. For voluntary summer practices, insurance is made for a period of one month at most for only one organization. Insurance is also provided for summer practices abroad. If the company insures you, you do not need to apply through the university."
    },
    {
        "id": "evaluation_form_details",
        "topic": "Evaluation Form and Employer Survey Details",
        "content": "Students must download the 'Evaluation Form and Employer Survey Form' from Documents/Forms tab. The forms are together in two pages: 'Başarı Belgesi' (Evaluation Form) and 'İşveren Anketi' (Employer Survey). Attach a recent photograph to the first page. The company should fill out these forms at the end of summer practice and email them to sp-belge@metu.edu.tr."
    },
    # --- IE 300 REPORT FORMAT AND GRADING (from IE 300 Manual) ---
    {
        "id": "ie300_report_format",
        "topic": "IE 300 Report Format and Style Requirements",
        "content": "IE 300 report must be written in English, printed in ink or typed. Main section headings should be numbered and written in CAPITAL letters. Subtitles should be in lowercase letters and underlined. All pages must have page numbers. Figures, drawings, tables, and pictures must be numbered. Report sections in order: 1) Table of contents with page numbers, 2) Introduction covering scope of SP and main difficulties faced, 3) Main body with detailed explanation of work carried out, 4) Conclusion with evaluation of experience gained and feedback, 5) References for all material referred to, 6) Appendix for data, tables, and diagrams not immediately relevant to main text. Questions may be followed in the given order, or reorganized as long as all questions are answered. If a question is not appropriate, it can be disregarded with a clear justification. Adding a glossary for technical terms is advisable."
    },
    {
        "id": "ie300_grading_criteria",
        "topic": "IE 300 Report Grading Criteria and Point Breakdown",
        "content": "IE 300 report is graded out of 200 points total. Point breakdown: Section 1 Introductory Features (10 pts), Section 2 Analysis of Macro Aspects (20 pts), Section 3 Management Information System (20 pts), Section 4 Overview of Production System (35 pts), Section 5 Production Planning and Control System (35 pts), Section 6 Quality Planning and Control System (20 pts), Section 7 Observation of a Professional at Work (15 pts), Section 8 Analysis of a Decision Making Problem (20 pts), Section 9 Conclusion (15 pts), Style and Organization (10 pts). Grading rules: Total < 160 points OR any section < 50% means 'Incomplete' and report is returned for revision. Total < 125 points means 'Unsatisfactory' and SP must be repeated at a different workplace. Otherwise the grade is 'Satisfactory' (S). Students must also fill out the online questionnaire; failure to do so means the report is considered incomplete."
    },
    # --- IE 300 MANUAL QUESTIONS BY SECTION ---
    {
        "id": "ie300_manual_section1",
        "topic": "IE 300 Manual - Section 1: Introductory Features (10 pts)",
        "content": "Section 1 questions: Q1.1: Full title of the firm, when it was founded, and its full address. Q1.2: Main shareholders and their shares; whether it is a joint venture, franchise, part of a holding company or multinational group. Q1.3: Sector and typical products manufactured; shares in domestic and international markets. Q1.4: Who are the customers (end users, retailers, other manufacturers, employees)? Identify stakeholders including certifying agencies, labor unions, professional societies, government, local community, potential customers, competitors, and employees. Q1.5: List of functions performed by industrial engineers in the practice organization."
    },
    {
        "id": "ie300_manual_section2",
        "topic": "IE 300 Manual - Section 2: Analysis of Macro Aspects (20 pts)",
        "content": "Section 2 questions: Q2.1: Identify major items of input of the production system. Specify where and how they are supplied — sources, means of transportation, volume and frequency of deliveries, usage rates. Q2.2: Identify major facilities of the manufacturing firm on a rough sketch. Show items that flow among them. Q2.3: Specify the most prevailing factor for selecting the current location of the facility. Factors include distribution needs, raw material availability, product characteristics, labor availability, transportation facilities, proximity to suppliers, environmental factors, laws/taxation/incentives, and cost of land/buildings. Support your ideas."
    },
    {
        "id": "ie300_manual_section3",
        "topic": "IE 300 Manual - Section 3: Management Information System (20 pts)",
        "content": "Section 3 questions: Q3.1: Specify decision makers and decision-making subjects at three levels. (a) Strategic level: plant expansion, product lines, mergers, diversification, capital expenditures. (b) Tactical level: resource allocation, budgets, funds flow, plant layout, personnel. (c) Operational level: receiving/shipping, scheduling, inventory control, quality control, worker allocation. Provide one decision-making activity for each level. Q3.2: Identify computer systems in use (networks, PCs, workstations, mainframes — types and capacities) and their spread across functions/departments."
    },
    {
        "id": "ie300_manual_section4",
        "topic": "IE 300 Manual - Section 4: Overview of the Production System (35 pts)",
        "content": "Section 4 questions: Q4.1: Provide a schematic representation of material flow of a particular product from raw materials inventory through finished goods inventory, showing every workstation and stock point. Q4.2: Explain the type of operations (continuous process, repetitive/flow shop, intermittent/job shop/batch shop/project shop) with regards to production volume or product variety, and describe reasons in detail. Q4.3: Discuss the type of layout (process layout, product layout, group technology/cellular layout, fixed-position layout, or combination) with rough sketches. Q4.4: Identify materials handling equipment — where and for what purposes used, and draw the path followed by one piece of equipment. Q4.5: Compute or describe an appropriate productivity measure (labor, capital, energy, material usage). Q4.6: Are unit-manufacturing costs calculated? Explain how (direct material + direct labor + factory overhead) with an example, or describe how expenses are accounted for. Q4.7: Carry out comparative ratio analysis using balance sheets and income statements for the last two years, or itemize balance sheet/income statement titles."
    },
    {
        "id": "ie300_manual_section5",
        "topic": "IE 300 Manual - Section 5: Production Planning and Control (35 pts)",
        "content": "Section 5 questions: Q5.1: State typical decisions on types and quantities of specific products. Who makes these decisions? How are decisions recorded and transferred? What is the basis for these decisions? Q5.2: What resources are controlled as scarce through careful planning? How are their uses planned and monitored? Q5.3: State four different items kept in stocks. What requirements do they serve? Plot inventory on hand vs. time for at least one item. Observe any pattern? How can you explain it? Supply data sources. What difficulties exist in managing inventories?"
    },
    {
        "id": "ie300_manual_section6",
        "topic": "IE 300 Manual - Section 6: Quality Planning and Control (20 pts)",
        "content": "Section 6 question: Q6.1: Choose a product and explain how the organization defines quality of it. How are customer requirements translated into product/service specifications? Describe quality control activities throughout the product life cycle at four stages: (a) product/service design stage, (b) manufacturing/service process design stage, (c) manufacturing/service delivery stage, (d) usage stage covering warranty and repair."
    },
    {
        "id": "ie300_manual_section7",
        "topic": "IE 300 Manual - Section 7: Observation of a Professional at Work (15 pts)",
        "content": "Section 7 question: Q7.1: Identify the most appealing position to you. Observe a professional in that position and narrate: their tasks and responsibilities, a typical workday, percentage breakup of activities, who they manage, who they report to, and the background and skills needed for the position."
    },
    {
        "id": "ie300_manual_section8",
        "topic": "IE 300 Manual - Section 8: Analysis of a Decision Making Problem (20 pts)",
        "content": "Section 8 question: Q8.1: Identify a decision making problem in the organization and formulate it. Specify: Who is the decision maker (owner of the problem)? What is the goal or objective (direction and satisfactory amount of improvement)? What are the alternative courses of action? What are the limitations, restrictions, and requirements of the system?"
    },
    {
        "id": "ie300_manual_section9",
        "topic": "IE 300 Manual - Section 9: Conclusion (15 pts)",
        "content": "Section 9 questions: Q9.1: Answer the following — Is the procedure sufficient in scope, method and approach? If not, identify drawbacks and suggestions; if yes, what did you enjoy most? If you had another four weeks, what would you do and why? What do you expect to learn in future IE training to improve understanding of production systems? Discuss differences between IE and other engineering disciplines in the production environment. If IEs are employed, what areas do they work in? If not, what activities are suitable for IEs? Discuss top management's impression and attitudes towards IE functions. Q9.2: Fill out the online questionnaire by the submission date, otherwise the report is considered incomplete."
    },
    {
        "id": "ie300_evaluate_company",
        "topic": "IE 300 How to Evaluate Company Suitability",
        "content": "Before starting IE 300, students should check the IE 300 Manual and evaluate whether they can answer the report questions at the chosen company without much difficulty. Consider: number of employees, how many engineers and IEs work there, production capacity, information system, ERP usage. The SP Committee does not examine and confirm the suitability of a company in advance — students determine whether the company is appropriate. If unsure, discuss with the SP Committee."
    },
    # --- IE 400 MANUFACTURING MANUAL - FORMAT AND GRADING ---
    {
        "id": "ie400_mfg_report_format",
        "topic": "IE 400 Manufacturing Report Format and Style",
        "content": "IE 400 manufacturing report must be written in English with numbered headings in capitals and subtitles in lowercase underlined. All pages must have page numbers, and figures/tables must be numbered. Report sections: 1) Table of contents with page numbers, 2) Introduction covering scope and difficulties, 3) Main body including IE problem or contributed project sections, 4) Conclusion with evaluation and feedback, 5) References, 6) Appendix, 7) Glossary (advisable, including company-specific jargon). Reports are due within the first two weeks of the following academic term. Questions may be reorganized as long as all are answered. Unanswerable questions may be skipped with clear justification."
    },
    {
        "id": "ie400_mfg_grading",
        "topic": "IE 400 Manufacturing Report Grading Criteria",
        "content": "IE 400 manufacturing report has two separately graded parts — students must pass BOTH. QUESTIONS SECTION (200 pts): Introductory Features 10 pts, Analysis of Macro Aspects 20 pts, Overview of Production System 35 pts, Production Planning and Control 50 pts, Quality Planning and Control 20 pts, Management Information System 20 pts, Work Study 20 pts, Conclusion 15 pts, Style and Organization 10 pts. Rules: must score at least 50% in each section; total 125-160 or any section < 50% means Incomplete (returned for revision); total < 125 means Unsatisfactory (SP repeated). PROBLEM/PROJECT SECTION (100 pts): evaluated on problem/project context and IE relevance, technical content, style. Score 40-65 means Incomplete; score < 40 means Unsatisfactory. PROJECT-TYPE SP (100 pts): Introduction 5 pts, Literature Review 10 pts, Problem Definition 30 pts, Data Gathering and Analysis 10 pts, Solution Approaches 20 pts, Results 15 pts, Conclusion 10 pts."
    },
    {
        "id": "ie400_mfg_minimum_questions",
        "topic": "IE 400 Manufacturing Manual - Minimum Question Requirements",
        "content": "IMPORTANT: For IE 400 manufacturing report, students do NOT have to answer ALL questions in Chapters 4, 5, 6, and 7. Minimum requirements are: at least 3 questions from Chapter 4 (Production Planning and Control), at least 2 questions from Chapter 5 (Quality Planning and Control), at least 1 question from Chapter 6 (Management Information System), and at least 1 question from Chapter 7 (Work Study). All questions in Sections 1, 2, 3, and 8 must be answered."
    },
    # --- IE 400 MANUFACTURING MANUAL QUESTIONS BY SECTION ---
    {
        "id": "ie400_mfg_section1",
        "topic": "IE 400 Mfg Manual - Section 1: Introductory Features (10 pts)",
        "content": "Section 1 questions: Q1.1: Full title, founding date, location with full mailing address. Q1.2: Type of ownership, main shareholders and shares. Is it a partnership, joint venture, franchise, part of a holding company, or multinational? Q1.3: Sector and typical products/services. Include advertising brochures/catalogues in appendix. Domestic and international market shares. Q1.4: Customers (end users, retailers, manufacturers, employees). Identify stakeholders. Q1.5: Functions performed by industrial engineers in the organization."
    },
    {
        "id": "ie400_mfg_section2",
        "topic": "IE 400 Mfg Manual - Section 2: Analysis of Macro Aspects (20 pts)",
        "content": "Section 2 questions: Q2.1: Sketch the production system as a black box showing inputs and outputs. Does the firm export? Import raw materials? What standards and certificates does it hold (ISO, TSE, EN, EC)? Q2.2: State the mission and vision of the organization. Are there differences in missions for different products/services? Q2.3: Most prevailing factor for facility location selection (distribution needs, raw materials, labor, transportation, suppliers, environment, laws/taxation, land cost). Support with observations. Then choose one of Q2.4 or Q2.5: Q2.4: Capital investment plans, evaluation methods/criteria, effects of inflation, example of past evaluation. Q2.5: How the firm obtained know-how/technologies, improvements, licensed trademarks/patents, R&D unit, project management for capital investments or technology adoptions."
    },
    {
        "id": "ie400_mfg_section3",
        "topic": "IE 400 Mfg Manual - Section 3: Overview of Production System (35 pts)",
        "content": "Section 3 questions: Q3.1: Process (operations) chart of a major product/subassembly, routing for a group of products, or service process. Q3.2: How is rated capacity defined and measured? (Rated capacity = Designed capacity x Utilization x Efficiency). Q3.3: Type of operations — continuous, repetitive/flow shop, intermittent (job/batch/project shop). Also classify as MTS (make-to-stock), MTO (make-to-order), or ATO (assemble-to-order). Q3.4: Draw a block plan of the organization or provide blueprint. Q3.5: Discuss layout types (process, product, cellular/GT, fixed-position, or combination). Q3.6: Select a department, indicate its layout type, and discuss how its characteristics fit. Q3.7: Unit-manufacturing costs — how calculated (direct material + direct labor + overhead) with example. Q3.8: Comparative ratio analysis using balance sheets and income statements for last two years, or itemize titles."
    },
    {
        "id": "ie400_mfg_section4",
        "topic": "IE 400 Mfg Manual - Section 4: Production Planning and Control (50 pts, min 3 questions)",
        "content": "Section 4 questions (answer at least 3): Q4.1: Forecasting activities — purposes, methods, data sources, model used, accuracy measurement, computer support. Provide example. Q4.2: Who decides what and how much to produce? How? What resources are scarce? Current limits? Main concerns in allocation (customer satisfaction, cost, time, utilization)? How are plans made and reviewed? Q4.3: Major inventory items by function. Reasons for holding (uncertainty, seasonal, cycle stocks, quantity discounts, pipeline). Inventory control policies (periodic vs continuous review). MRP activity? Performance measures. Q4.4: Detailed scheduling activities. Records (timetables, daily lists, charts)? Provide example. Apply performance measure on schedule implementation. Q4.5: JIT philosophy — organized studies to reduce slack? Example of allowance/slack used to assure uninterrupted operation."
    },
    {
        "id": "ie400_mfg_section5",
        "topic": "IE 400 Mfg Manual - Section 5: Quality Planning and Control (20 pts, min 2 questions)",
        "content": "Section 5 questions (answer at least 2): Q5.1: Choose a product — how does the organization define quality? How are customer requirements translated into specifications? Describe quality control activities throughout the product life cycle: design stage, process design stage, delivery stage, and usage stage. Q5.2: Describe at least three proactive (preventive) quality assurance activities. How is responsibility of quality shared across the organization?"
    },
    {
        "id": "ie400_mfg_section6",
        "topic": "IE 400 Mfg Manual - Section 6: Management Information System (20 pts, min 1 question)",
        "content": "Section 6 questions (answer at least 1): Q6.1: Decision makers and subjects at strategic, tactical, and operational levels. Provide one decision-making activity per level. Q6.2: Computer systems — types, capacities, spread across departments. Types of data recorded/processed in a specific division. Level of decision supported. Q6.3: Software used — ERP, reservation system, stock keeping, accounting (not standard office programs). Level of decision supported, with an example."
    },
    {
        "id": "ie400_mfg_section7",
        "topic": "IE 400 Mfg Manual - Section 7: Work Study (20 pts, min 1 question)",
        "content": "Section 7 questions (answer at least 1): Q7.1: Apply a work measurement technique (stopwatch time study, predetermined time standards, or work sampling) to an operator. Evaluate results. Apply method study for more effective methods. Q7.2: Has there been a Job Evaluation study? If yes, describe the method and implementation. If no, how is wage differentiation determined?"
    },
    {
        "id": "ie400_mfg_section8",
        "topic": "IE 400 Mfg Manual - Section 8: Conclusion (15 pts)",
        "content": "Section 8 questions: Q8.1: Is the procedure sufficient in scope, method and approach? Drawbacks and suggestions? What was most difficult about studying an IE problem? If you had another four weeks, what would you do? Future IE training expectations. Differences between IE and other engineering disciplines. IE roles in the firm. Top management's impression of IE. Q8.2: Fill out the online questionnaire by the submission date — otherwise report is considered incomplete."
    },
    # --- IE 400 APPENDIX A: IE PROBLEM DEFINITION ---
    {
        "id": "ie400_appendix_a",
        "topic": "IE 400 Appendix A - How to Define and Formulate IE Problems",
        "content": "Step 1 — Identification and Definition: Observe symptoms such as deficiencies in planning, low utilization, and inventory problems. Validate symptoms with objective data. Use analysis tools including cause-effect diagrams, Pareto analysis, relations diagram, logic tree, flowcharts, check sheets, rich pictures, brainstorming, run charts, influence diagrams, multivoting, nominal group technique, stratification, affinity diagrams, and precedence diagrams. Step 2 — Formulation: Define the decision maker (owner of the problem), the goal or objective (direction and satisfactory amount of improvement), performance criteria, alternative courses of action, limitations/restrictions/requirements, analysis of interactions with subsystems, and comment on specific modeling approaches."
    },
    # --- IE 400 APPENDIX B: PROJECT REPORTING ---
    {
        "id": "ie400_appendix_b",
        "topic": "IE 400 Appendix B - How to Report on a Participated Project",
        "content": "If the project is COMPLETED, the report must include: 1) Introduction covering products/processes, context, and team composition. 2) Problem statement explaining the issue addressed and its IE relevance. 3) Approach taken including planned stages, modifications, and the student's role. 4) Summary of work done with data gathered, methods, and results. 5) Conclusions and recommendations with outcomes, suggestions, and extensions. If the project is STILL IN PROGRESS, the report must include: 1) Introduction. 2) Problem statement. 3) Approach taken with planned stages and role. 4) Project schedule as an activity network or Gantt chart. 5) Work done to date with data, methods, and results so far. 6) Expectations of outcomes including prospective benefits and evaluation."
    },
    # --- IE 300/400 INTRODUCTORY SESSION EXTRAS ---
    {
        "id": "ie400_evaluate_company",
        "topic": "IE 400 How to Evaluate Company Suitability",
        "content": "Before starting IE 400, students should check the IE 400 Manual from the Documents/Forms tab. There are two types of manuals: manufacturing manual and service manual. Evaluate whether you can answer the questions without much difficulty. Consider: number of employees, how many engineers and IEs work there, production capacity, information system, and ERP usage. The SP Committee does not examine and confirm the suitability of a company in advance — students determine appropriateness themselves. If unsure, discuss with the SP Committee."
    },
    {
        "id": "ie400_apply_company",
        "topic": "IE 400 Applying to Companies",
        "content": "For IE 400, use the SP Application Form and/or SP Protocol from the Documents/Forms tab. You can apply to more than one company; for each company, fill out a separate form. After filling the protocol form, leave it at the Undergraduate Secretary Office (IE 128). Pick up the signed form in a week."
    },
    {
        "id": "email_not_callcenter",
        "topic": "SP Committee Email Policy",
        "content": "The SP Committee email ie-staj@metu.edu.tr is NOT a call center. Students should check the SP presentation slides and website thoroughly before sending an email. Most common questions are already answered in the introductory session slides and on the SP website."
    },
    # --- ANNOUNCEMENTS ---
    {
        "id": "announcement_sp_meeting_2026",
        "topic": "Announcement - SP Meeting Spring 2026",
        "content": "The Internship Information Meeting for Spring 2026 will be held on Friday, April 17, 2026 between 10:30 and 11:40. The IE 300 meeting will take place in Ömer Saatçioğlu Auditorium. Students planning to do their summer practice should attend this meeting for important procedural information. Published: 10/04/2026."
    },
    {
        "id": "announcement_sp_meeting_2025",
        "topic": "Announcement - SP Meeting 2025",
        "content": "A general meeting on IE 300 and IE 400 summer internship courses and the Summer Practice procedures was held on March 14, 2025, at 14:40. IE 300 students met in IE03 and IE 400 students in IE04. Meeting slides can be found under Documents/Forms on the SP website."
    },
    # --- ADDITIONAL CUSTOM FAQ ---
    {
        "id": "custom_ie300_vs_ie400",
        "topic": "Difference Between IE 300 and IE 400",
        "content": "IE 300 is the first summer practice course, typically done after the 2nd or 3rd year, and can only be done at manufacturing companies. IE 400 is the second summer practice course, done in a later year, and accepts both manufacturing and service companies. IE 400 requires a more in-depth report including a problem definition or project component. IE 400 also allows project-based internships of at least 6 weeks (30 workdays) with prior proposal approval from the SP Committee. Both courses require a minimum of 20 workdays (4 weeks) for standard internships."
    },
    {
        "id": "custom_ai_report_warning",
        "topic": "AI-Generated Reports Policy",
        "content": "Summer practice reports will be checked for plagiarism via ODTUClass turnitin assignment (similarity must be less than 20%) and will also be checked whether they are generated by AI tools. AI-generated reports are not accepted. Students must write their own reports based on their own observations and experiences during the summer practice."
    },
    {
        "id": "custom_report_evaluation_process",
        "topic": "Report Evaluation and Correction Process",
        "content": "SP reports are graded by assigned faculty members. In the last month of the semester, reports that require corrections will be returned to students. Students have 2-3 weeks to complete the requested corrections and return the revised report via ODTUClass. If the report scores below the passing threshold, the summer practice must be repeated at a different workplace."
    },
    {
        "id": "custom_report_submission",
        "topic": "Where and How to Submit SP Reports",
        "content": "SP reports are collected via ODTUClass. The deadline will be announced on ODTUClass at the beginning of the semester. This is a strict deadline. Reports must be in PDF format (docx converted to pdf). Students should also fill out the online questionnaire using METU Survey (details will be announced by the SP Committee at the beginning of the semester)."
    },
    {
        "id": "custom_contract_signing",
        "topic": "How to Get SP Contract (Staj Sözleşmesi) Signed",
        "content": "If you need your SP work contract (staj sözleşmesi) to be signed, leave it at the Undergraduate Secretary Office, IE 129. You can pick up the signed form in one week. The SP Protocol (sözleşme) form template is available under Documents/Forms on the SP website."
    },
    {
        "id": "custom_finding_sp_tips",
        "topic": "Tips for Finding a Summer Practice Company",
        "content": "Finding a summer practice location is never easy. Start looking as early as possible. Options include: 1) Check the SP Opportunities page on the SP website for companies that contacted the department. 2) Use your social connections — family, friends, and personal network. 3) Examine the previous summer practice databases of earlier years on the SP website. 4) Apply to organizations personally. 5) Wait for department-announced opportunities (risky, limited capacity). Some companies require the department to determine candidates — in that case, an announcement is made and students send transcripts and resumes. If assigned through the department, the summer practice must be conducted at that company."
    },
    {
        "id": "sgk_no_confirmation",
        "topic": "SGK Application - No Confirmation Notification",
        "content": "After completing the SGK insurance application on OCW, the student will NOT receive any notification or confirmation email. The application is considered complete once the questionnaire is submitted and the declaration form is uploaded. The SGK document will appear on e-devlet (turkiye.gov.tr) typically 2-3 workdays before the SP begins. The SP committee does not send the SGK document by email."
    },
    {
        "id": "forms_download_links",
        "topic": "Direct Download Links for SP Forms",
        "content": "Some SP forms have direct download links: Paid Summer Practice Form (İşsizlik Fonu Katkısı Bilgi Formu) can be downloaded from https://sp-ie.metu.edu.tr/en/system/files/issizlik_fonu_katkisi_bilgi_formu_1.doc. Emergency SGK Application Excel file can be downloaded from https://sp-ie.metu.edu.tr/en/system/files/kzso-sa01-f04_stajyer_ogrenci_bilgi_formu_guncelleme_0.xls. All other documents are available at https://sp-ie.metu.edu.tr/en/forms (METU login may be required for some documents)."
    },
    # --- DETAILED SP OPPORTUNITIES WITH CONTACT INFO ---
    {
        "id": "sp_opp_ms_spektral",
        "topic": "SP Opportunity - MS Spektral Savunma Sanayi",
        "content": "MS Spektral Savunma Sanayi A.Ş. offers a summer practice opportunity. Location: Başkent OSB, Ankara. Area: Production planning candidate engineer. Wage: Yes. Insurance, food, and transportation support provided. Third-year students (for IE 400) preferred. Program lasts one year and may be extended. May lead to full-time position upon mutual agreement. Contact: Tolga Öztürk, phone 0(505)9500813, email insan.kaynaklari@msspektral.com."
    },
    {
        "id": "sp_opp_nacres",
        "topic": "SP Opportunity - NACRES Yazılım Teknoloji",
        "content": "NACRES Yazılım Teknoloji offers a summer practice opportunity for 4th year students. Email: sercansarman@nacres.com.tr. Website: www.nacres.com.tr."
    },
    {
        "id": "sp_opp_guris",
        "topic": "SP Opportunity - GÜRİŞ",
        "content": "GÜRİŞ offers the Genç Yetenek Uzun Dönem Staj Programı (Young Talent Long-Term Internship Program). Application is via LinkedIn or the ODTÜ KPM website."
    },
    {
        "id": "sp_opp_noksel",
        "topic": "SP Opportunity - Noksel Çelik Boru",
        "content": "Noksel Çelik Boru Sanayi AŞ offers summer practice opportunities. Areas: production, quality, maintenance, sales, project management, business development. Contact: Banu Çağlar, phone 03124725959, email bcaglar@noksel.com.tr."
    },
    {
        "id": "sp_opp_koctas",
        "topic": "SP Opportunity - Koçtaş",
        "content": "Koçtaş offers an IE 400 summer practice opportunity. The internship is hybrid (2 days office, 3 days remote). Application via https://www.kockariyerim.com. Due date: April 30, 2025. Students should send a notification email to ie-staj@metu.edu.tr after applying."
    },
    {
        "id": "sp_opp_iga",
        "topic": "SP Opportunity - İGA İstanbul Havalimanı",
        "content": "İGA (İstanbul Airport) offers a summer practice opportunity. Application is through the Kariyer Kapısı system — search for İGA Staj Programı at https://kariyerkapisi.cbiko.gov.tr/."
    },
    {
        "id": "sp_opp_tei",
        "topic": "SP Opportunity - TEI TUSAŞ Motor Sanayi",
        "content": "TEI TUSAŞ Motor Sanayii A.Ş. offers a summer practice opportunity in Eskişehir. Areas: project design, assembly, production, maintenance, R&D. Wage: Yes. For 4th year students. Contact: Alpaslan Demir, phone 02222112100, email insankaynaklari@tei.com.tr."
    },
    {
        "id": "sp_opp_eltas",
        "topic": "SP Opportunity - ELTAŞ Transformatör",
        "content": "ELTAŞ Transformatör San. Tic. AŞ. offers a summer practice opportunity. Location: Aliağa, İzmir. Areas: project design, assembly, production, R&D, quality, testing. Wage: Yes. Contact: Duygu Ünlü, phone 05325559827, email mujdat.bilgic@eltas.com.tr."
    },
    {
        "id": "sp_opp_ankara_group",
        "topic": "SP Opportunities in Ankara - Detailed Contacts",
        "content": "Ankara-based SP opportunities with contact details: TÜMAŞ (Kavaklıdere, project design and consultancy, no wage, contact Betül Durmaz 03124176025). UDEA Elektronik (Yenimahalle, production, no wage, contact Sıla Atay 05393090169, email ik@udea.com.tr). HİDROAN (Sincan, project design/assembly/production/R&D/software, no wage, contact Neşet Dağdelen 5498204886). MTM Makina (Kavaklıdere, project design/assembly/maintenance, paid, contact Bahar Dayığı 05322380010). MPES Mühendislik (Çankaya, project design/production/R&D, paid, contact Zafer Demirtaş 05423991240). DURUKAN Şekerleme (Sincan, production/R&D, paid, contact İK 05344564971). Koluman Otomotiv Hacettepe Teknokent (Çankaya, project design/R&D, paid, contact Aybike Kırım 05496513225). BAŞÖZ Enerji (Temelli, production/maintenance, paid, contact Gamze Doğan 05416955792). DEICO (Yenimahalle, assembly/production/R&D, no wage, for 4th year, contact Berat Akçay 05313051961). VERTE (Yenimahalle, production/R&D, no wage, for 4th year, contact Berat Akçay 05313051961). Hestaş Madencilik (Çankaya, mining, no wage, for 4th year, contact Gözde Söğüt Uçak 05393086837). EUROPOWER Enerji (project design/assembly/production/maintenance/R&D, paid, for 4th year)."
    },
    {
        "id": "sp_opp_other_cities",
        "topic": "SP Opportunities Outside Ankara - Detailed",
        "content": "SP opportunities outside Ankara: EKER Süt (Mustafakemalpaşa/Bursa, production/maintenance/R&D, paid, contact Hatice Özdemir Çakır 02244443537). Emet Bor İşletme Müdürlüğü (production, paid, contact Ömer Temur 5368236356). İMECAR Elektronik (Döşemealtı/Antalya, project design/production/R&D, no wage, contact Buket Aytekin 05317270525). Gönenli Süt (Gönen/Balıkesir, production, no wage, contact Burcu Cöne 5349595126). Anadolu Sigorta (Beykoz/İstanbul, project design/R&D, paid, contact İlayda Yelken Hocaoğlu 08507440423). Ledbim Bilişim (Muratpaşa/Antalya, project design/R&D, no wage, for 4th year). Kütahya Porselen (Kütahya, production, no wage, for 4th year)."
    },
    # --- DETAILED PREVIOUS SP COMPANIES ---
    {
        "id": "prev_sp_ankara",
        "topic": "Previous SP Companies in Ankara Region",
        "content": "Previous SP companies in the Ankara region: Hazine ve Maliye Bakanlığı Bilgi Teknolojileri Genel Müdürlüğü (Dikmen/Çankaya, IE400 only). İnofab Sağlık Teknolojileri A.Ş. (ODTÜ Teknokent Silikon Blok, IE400 only). YÜKSEL Kompozit Teknolojileri A.Ş. (Başkent OSB Sincan, aviation/defense, IE300+IE400). SENKRON Plastik (Ostim Megacenter Yenimahalle, IE300+IE400). TELMEK A.Ş. (Ostim OSB, IE400 only). Meka Beton Santralleri (Malıköy, IE300+IE400). Akdaş Döküm (Sincan, IE300+IE400). ELTEM-TEK (Balgat, IE400 only). Wicode (ODTÜ Teknokent, IE400 only)."
    },
    {
        "id": "prev_sp_other_regions",
        "topic": "Previous SP Companies Outside Ankara",
        "content": "Previous SP companies outside Ankara: SİLKAR Madencilik (Bilecik, IE300+IE400). Tezcanlar Yatırım (Sarıçam/Adana, IE300+IE400). Ekinciler Demir ve Çelik (İskenderun/Hatay, IE400 only). Muğla Su ve Kanalizasyon İdaresi (Menteşe/Muğla, IE400 only). Kula Yağ Sanayi (Balıkesir, IE400 only). SÖĞÜT Seramik (Söğüt/Bilecik, IE300+IE400). İĞREK Makina (Nilüfer/Bursa, IE400 only). Stackpole International (Gaziemir/İzmir, automotive, IE300+IE400). İPEK Mobilya Çinkom (İncesu/Kayseri, IE300+IE400). Nazkaya Ambalaj (IE300+IE400). Silverline Endüstri (Merzifon/Amasya, IE300+IE400). ŞA-RA Enerji (Yüreğir/Adana, IE300+IE400). Kanca El Aletleri (Çayırova/Kocaeli, IE400 only). KAANLAR Gıda (Malkara/Tekirdağ, IE400 only). National companies: Şişecam, Eczacıbaşı Bilişim, Forte, Koç Holding ve Microsoft Türkiye (IE300+IE400). ILGAZ Grup, Ofisus Danışmanlık (IE400 only)."
    },
    # --- DOCUMENTS/FORMS COMPLETE LIST ---
    {
        "id": "forms_complete_list",
        "topic": "Complete List of Available Documents and Forms",
        "content": "All documents available on the Documents/Forms page (https://sp-ie.metu.edu.tr/en/forms): Internship Presentations: IE 300 Introductory Session slides, IE 400 Introductory Session slides. Application Letters: IE-300 SP Application Form (Turkish and English), IE-400 SP Application Form (Turkish and English), SP Protocol/Agreement form (sözleşme). Insurance Forms: Declaration Form for students with family health insurance, Declaration Form for students without family health insurance, Paid Summer Practice Information Form (İşsizlik Fonu Katkısı Bilgi Formu). Evaluation: SP Evaluation Form and Employer Survey (Turkish version), Evaluation Form (English version). Manuals: IE300 Summer Practice Manual, IE400 Summer Practice Manufacturing Manual, IE400 Summer Practice Service Manual. METU login may be required for some documents."
    },
]
