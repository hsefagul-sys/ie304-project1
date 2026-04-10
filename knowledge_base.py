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
]
