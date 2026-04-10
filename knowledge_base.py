"""
Knowledge base for METU IE Summer Practice Chatbot.
Sources: IE300/IE400 Introductory Sessions (2025-2026) + IE300 Manual + IE400 Manufacturing Manual + IE400 Service Manual
"""

KNOWLEDGE_CHUNKS = [
    # ===================== SP COMMITTEE =====================
    {"id": "committee", "topic": "SP Committee Contact Info",
     "content": "SP Committee: Prof. Dr. Esra Karasakal, Prof. Dr. Cem İyigün, Çiya Aydoğan, Buğra Öztürk, Ömer Turan Şahinaslan, Özgür Ünverdi, Mehmet Sencer Zengin. Web: http://sp-ie.metu.edu.tr. Email: ie-staj@metu.edu.tr. Note: ie-staj is NOT a call center — check the SP website and presentation slides before emailing."},

    # ===================== IE 300 PRESENTATION =====================
    {"id": "ie300_prereq", "topic": "IE 300 Prerequisites courses required",
     "content": "Prerequisites for IE 300: IE 102 + IE 251, IE 265, IE 241, OHS 101 (fall semester courses) + One out of {IE 266, IE 252} (spring semester courses). If any prerequisite is not completed with grade >= DD, IE 300 cannot be conducted. If you are in probation in the Fall semester, you cannot take IE 300 even if you finished your SP."},

    {"id": "ie300_overview", "topic": "IE 300 Course Overview Purpose non-credit satisfactory",
     "content": "IE 300 is a compulsory non-credit course. Grade must be S (satisfactory) for graduation. You gain first professional experience: observing supply chain, manufacturing processes, sustainability, cost accounting, operations research methods, statistical analysis, big data, teamwork, and IE roles."},

    {"id": "ie300_when", "topic": "IE 300 When Duration minimum workdays weeks summer 2025",
     "content": "IE 300 conducted in Summer 2025, June 25 to September 26. Minimum 20 workdays (4 weeks). SP must not overlap with summer school. If in graduation status with all coursework done, you can do both IE 300 and IE 400 in succession."},

    {"id": "ie300_registration", "topic": "IE 300 Registration Report Deadline due date October",
     "content": "After SP, register for IE 300 in Fall 2025-2026. Reports due within first 4 weeks. Due date: October 24, 2025."},

    {"id": "ie300_company_accepted", "topic": "IE 300 Accepted Company Types manufacturing firms",
     "content": "IE 300 must be at a MANUFACTURING firm. Accepted: Automotive, Machine parts, Electronics, Furniture, Textiles, Consumer durables. Batch process also accepted: Steel, Paper mills, Pharmaceutical, Food and beverages."},

    {"id": "ie300_company_rejected", "topic": "IE 300 NOT Accepted Company service continuous process",
     "content": "NOT accepted for IE 300: Continuous process industries (cement, concrete, sugar, flour mill). Service industries NOT accepted (hospitals, hotels, banking, research, transportation, cargo). IE 300 is manufacturing only."},

    {"id": "ie300_face_to_face", "topic": "IE 300 face to face online hybrid remote not allowed",
     "content": "IE 300 must be conducted totally in the factory face-to-face. Online or hybrid NOT allowed for IE 300."},

    {"id": "ie300_evaluate", "topic": "IE 300 Evaluate Company suitability manual",
     "content": "To evaluate a company: Check IE 300 Manual (Documents/Forms > SP Manuals). Check if you can answer manual questions. Check: number of employees, engineers/IEs, production capacity, information system/ERP. SP committee does NOT confirm company suitability in advance — students decide. Discuss with committee if unsure."},

    {"id": "ie300_apply", "topic": "IE 300 Apply Company application form letter protocol sözleşme",
     "content": "Some companies need an SP Application Letter — download 'IE-300 Summer Practice Application Form' (Turkish/English) from Documents/Forms tab. Some need SP Protocol (sözleşme) — download from Documents/Forms. Leave protocol at Undergraduate Secretary Office, pick up signed form in a week."},

    {"id": "ie300_insurance", "topic": "IE 300 SGK Insurance OCW application declaration form",
     "content": "When accepted by company and decision is CERTAIN, apply via OCW (ocw.metu.edu.tr) under 'SGK Insurance Application' 2-3 weeks before SP starts. Upload 'Declaration Form for students with/without family health insurance' from Documents/Forms > Insurance Forms. Get 'Sigortalı İşe Başlama Belgesi' from e-devlet before SP starts."},

    {"id": "ie300_insurance_coverage", "topic": "IE 300 Insurance Coverage law compulsory abroad voluntary",
     "content": "Compulsory insurance: iş kazası ve meslek hastalığı sigortası (Law #5510). METU insures all SP students. Coverage: 20 workdays to 3 months. Also covers SP abroad. If company insures you, no need to apply through METU. Voluntary SP insurance: max 1 month for 1 organization (must have completed 2nd year)."},

    {"id": "ie300_evaluation_form", "topic": "IE 300 Evaluation Form Employer Survey Başarı Belgesi photo",
     "content": "Download 'Evaluation Form and Employer Survey' from Documents/Forms > SP Evaluation Form section. Two pages: 'Başarı Belgesi' + 'İşveren Anketi' (Turkish and English available). Attach your photo to first page. Company fills at end of SP and emails to sp-belge@metu.edu.tr."},

    {"id": "ie300_report_submit", "topic": "IE 300 Report Submission ODTUClass turnitin plagiarism AI",
     "content": "Submit report (PDF, docx converted to pdf) at ODTUClass IE 300 turnitin assignment. Plagiarism check: similarity must be < 20%. Reports checked for AI generation. Write based on IE300 Summer Practice Manual (Documents/Forms > SP Manuals). Answer ALL questions. Provide sufficient explanation — figures/tables only not accepted. Use Grammarly to correct. Can start writing during practice."},

    {"id": "ie300_paid", "topic": "IE 300 Paid Summer Practice payment bank receipt İşsizlik Fonu",
     "content": "If paid during SP: 1) Fill 'Paid SP questionnaire' at OCW. 2) Download/sign 'Paid Summer Practice Information Form (İşsizlik Fonu Katkısı Bilgi Formu)' from Documents/Forms > Insurance Forms. 3) Upload signed form (PDF) + bank receipt at OCW."},

    {"id": "ie300_voluntary", "topic": "IE 300 Voluntary Internship additional experience",
     "content": "Voluntary internships possible for additional experience. University insures if you completed 2nd year. Max 1 month for 1 organization. Same OCW procedure."},

    {"id": "ie300_candidate_eng", "topic": "IE 300 Candidate Engineering stajyer mühendis",
     "content": "Candidate engineering during semesters does NOT count (SP cannot overlap teaching period). If continued during summer for 20 full workdays in a row, can count for IE 300."},

    # ===================== IE 400 PRESENTATION =====================
    {"id": "ie400_prereq", "topic": "IE 400 Prerequisites courses required",
     "content": "Prerequisites for IE 400: IE 300 + IE 252, IE 323, IE 333 + Any two from {IE 304, IE 324, IE 372, IE 368}. If any prerequisite not completed with grade >= DD, IE 400 cannot be conducted."},

    {"id": "ie400_when", "topic": "IE 400 When Duration minimum workdays weeks winter break",
     "content": "IE 400 conducted in Summer 2025, June 25 to September 26. Minimum 20 workdays (4 weeks), can be more if company requests. Can also do IE 400 during winter semester break if 20 workdays available. SP must not overlap with summer school."},

    {"id": "ie400_registration", "topic": "IE 400 Registration Report Deadline due date October",
     "content": "After SP, register for IE 400 in Fall 2025-2026. Reports due within first 4 weeks. Due date: October 24, 2025."},

    {"id": "ie400_company_manufacturing", "topic": "IE 400 Accepted Manufacturing Company Types continuous",
     "content": "IE 400 accepts manufacturing firms: Automotive, Machine parts, Electronics, Furniture, Textiles, Consumer durables, Batch process (Steel, Paper, Pharma, Food). ALSO accepts continuous process (cement, concrete, sugar, flour) unlike IE 300."},

    {"id": "ie400_company_service", "topic": "IE 400 Accepted Service Company Types hospital bank NGO",
     "content": "IE 400 accepts service industries (unlike IE 300): Hospitals, Hotels, Banking, Research organizations (ODTÜ Teknokent), Transportation, Cargo, Public institutions, NGOs."},

    {"id": "ie400_face_to_face", "topic": "IE 400 face to face hybrid online manufacturing service",
     "content": "IE 400 at manufacturing: must be face-to-face. IE 400 at service company: can be face-to-face OR hybrid (face-to-face + online)."},

    {"id": "ie400_conduct_types", "topic": "IE 400 Individual Group Project-based types 6 weeks proposal",
     "content": "IE 400 three modes: 1) Individual: min 20 workdays. 2) Group of two: min 20 workdays, each writes own report, project must be more involved, notify SP committee in first week. 3) Project-based: min 6 weeks (30 workdays), two-page proposal approved by SP Committee before SP starts, different content/format (see IE 400 manual)."},

    {"id": "ie400_apply", "topic": "IE 400 Apply Company application form letter protocol",
     "content": "Download 'IE-400 Summer Practice Application Form' (Turkish/English) from Documents/Forms. Login at sp-ie.metu.edu.tr. Can apply to multiple companies (separate form each). SP Protocol (sözleşme) available if needed — leave at Undergraduate Secretary Office IE 128, pick up in a week."},

    {"id": "ie400_insurance", "topic": "IE 400 SGK Insurance OCW application",
     "content": "Apply via OCW (ocw.metu.edu.tr) under 'SGK Insurance Application' 2 weeks before SP. Upload declaration form from Documents/Forms > Insurance Forms. Get 'Sigortalı İşe Başlama Belgesi' from E-DEVLET. See General Information tab for details."},

    {"id": "ie400_sd_project", "topic": "IE 400 Systems Design Project SD committee opportunity",
     "content": "During IE 400 search for a Systems Design Project. Summer practice is good opportunity for SD projects. Ask engineers about challenging problems. Check identified problem with SD committee (NOT SP committee)."},

    {"id": "ie400_report_structure", "topic": "IE 400 Report two sections Questions Problem Project grading pass",
     "content": "IE 400 report has two sections: 'Questions' and 'Problem/Project' — graded separately. Must get S in BOTH to pass. Report written based on IE 400 manuals: 'IE400 Manufacturing Manual' or 'IE400 Service Manual' (Documents/Forms > SP Manuals)."},

    {"id": "ie400_report_submit", "topic": "IE 400 Report Submission plagiarism turnitin AI check",
     "content": "Submit PDF (docx to pdf) at ODTUClass IE 400 turnitin assignment. Plagiarism similarity < 20%. Checked for AI generation. Answer all required questions with sufficient explanation. Can start writing during practice. Use Grammarly."},

    {"id": "ie400_paid", "topic": "IE 400 Paid Summer Practice payment zip file",
     "content": "If paid during IE 400: Fill 'Paid SP questionnaire' at OCW. Download/sign 'Paid SP Form (İşsizlik Fonu Katkısı Bilgi Formu)' from Documents/Forms. Upload signed form + bank receipt as ZIP file at OCW."},

    # ===================== IE 300 MANUAL — GRADING =====================
    {"id": "ie300_grading", "topic": "IE 300 Grading Evaluation Points Scoring report grade incomplete unsatisfactory repeat",
     "content": "IE 300 grading: Total 200 points from questions. Must score at least 50% in EACH section. Total < 160 or any section < 50% = 'Incomplete' (report returned for revision). Total < 125 = 'Unsatisfactory' (repeat SP at different workplace next semester break). Points breakdown: Introductory Features 10, Analysis of Macro Aspects 20, Management Information System 20, Overview of Production System 35, Production Planning and Control 35, Quality Planning and Control 20, Observation of Professional at Work 15, Analysis of Decision Making Problem 20, Conclusion 15, Style and Organization 10."},

    # ===================== IE 300 MANUAL — SECTIONS =====================
    {"id": "ie300_manual_format", "topic": "IE 300 Report Format Style language English sections structure",
     "content": "IE 300 report must be in English. Sections: Table of Contents, Introduction (scope, difficulties), Main body, Conclusion (experience evaluation), References, Appendix. Main sections numbered in capitals, subtitles lowercase underlined. All pages numbered. Figures/tables numbered. Questions can be answered in given order or reorganized. If a question is not applicable, justify why. Add glossary for technical terms."},

    {"id": "ie300_manual_sec1", "topic": "IE 300 Manual Section 1 Introductory Features firm title shareholders sector products customers stakeholders",
     "content": "IE 300 Manual Section 1 — Introductory Features (10 pts): Q1.1 Full title, founding date, location/address. Q1.2 Main shareholders and shares, joint venture/franchise/holding/multinational. Q1.3 Sector, typical products, domestic/international market share. Q1.4 Customers (end users, retailers, manufacturers, employees) and stakeholders (certifying agencies, unions, government, competitors, etc.). Q1.5 Functions performed by industrial engineers."},

    {"id": "ie300_manual_sec2", "topic": "IE 300 Manual Section 2 Macro Aspects inputs supply chain facilities location factors",
     "content": "IE 300 Manual Section 2 — Analysis of Macro Aspects (20 pts): Q2.1 Identify major inputs, where/how supplied (sources, transportation, volume, frequency, usage rates). Q2.2 Identify major facilities on a rough sketch, show items flowing among them. Q2.3 Location factors: distribution needs, raw material availability, labor, transportation, proximity to suppliers, environment, laws/taxation, cost of land — specify most prevailing factor."},

    {"id": "ie300_manual_sec3", "topic": "IE 300 Manual Section 3 Management Information System MIS decisions strategic tactical operational computers hardware",
     "content": "IE 300 Manual Section 3 — Management Information System (20 pts): Q3.1 Decision makers and subjects at three levels: Strategic (plant expansion, product lines, mergers), Tactical (resource allocation, budgets, layout, personnel), Operational (scheduling, inventory control, shipping). Q3.2 Computer systems: networks, PCs, workstations, mainframes — types, capacities, spread across departments."},

    {"id": "ie300_manual_sec4", "topic": "IE 300 Manual Section 4 Production System Overview material flow process chart layout productivity cost manufacturing",
     "content": "IE 300 Manual Section 4 — Overview of Production System (35 pts): Q4.1 Schematic of material flow (raw materials through finished goods, all conversion points). Q4.2 Type of operations: continuous/repetitive/intermittent (job shop/batch/project). Q4.3 Layout types: process/product/cellular(GT)/fixed-position — discuss with sketches. Q4.4 Materials handling equipment, paths. Q4.5 Productivity measure. Q4.6 Unit manufacturing cost (direct labor + direct material + overhead). Q4.7 Balance sheet/income statement ratio analysis for 2 years."},

    {"id": "ie300_manual_sec5", "topic": "IE 300 Manual Section 5 Production Planning Control demand forecasting resources inventory stocks ordering",
     "content": "IE 300 Manual Section 5 — Production Planning and Control (35 pts): Q5.1 Decisions on product-mix and quantities — who decides, how recorded/transferred, basis for decisions. Q5.2 Scarce resources controlled through planning — how planned and monitored. Q5.3 Four inventory items, requirements/causes, plot inventory vs time graph, inventory management difficulties."},

    {"id": "ie300_manual_sec6", "topic": "IE 300 Manual Section 6 Quality Planning Control quality definition life cycle product service",
     "content": "IE 300 Manual Section 6 — Quality Planning and Control (20 pts): Choose a product, explain how organization defines quality. How are customer requirements translated into specs? Describe quality control at all four life cycle stages: product design, process design, manufacturing/delivery, usage/warranty."},

    {"id": "ie300_manual_sec7", "topic": "IE 300 Manual Section 7 Observation Professional at Work position communication workday",
     "content": "IE 300 Manual Section 7 — Observation of a Professional at Work (15 pts): Identify most appealing position. Observe that professional: tasks/responsibilities, typical workday, % breakup of activities, who they manage/report to, required background/skills."},

    {"id": "ie300_manual_sec8", "topic": "IE 300 Manual Section 8 Decision Making Problem identification formulation objective alternatives constraints",
     "content": "IE 300 Manual Section 8 — Analysis of a Decision Making Problem (20 pts): Identify a decision making problem. Formulate: decision maker (owner), goal/objective, alternative courses of action, limitations/restrictions/requirements."},

    {"id": "ie300_manual_conclusion", "topic": "IE 300 Manual Section 9 Conclusion assessment feedback suggestions IE career",
     "content": "IE 300 Manual Conclusion (15 pts): Assess the SP procedure (scope, method, approach). What would you do with 4 more weeks? What to learn in future IE training? Differences between IE and other engineering disciplines. IE roles in the firm. Top management's attitudes toward IE."},

    # ===================== IE 400 MANUFACTURING MANUAL — GRADING =====================
    {"id": "ie400_mfg_grading", "topic": "IE 400 Manufacturing Grading Points scoring questions problem project incomplete unsatisfactory repeat",
     "content": "IE 400 Manufacturing grading: Questions section 200 points, Problem/Project section 100 points. Must pass BOTH separately. Questions: 125-160 or any section < 50% = 'Incomplete' (revision). < 125 = 'Unsatisfactory' (repeat at different workplace). Problem/Project: 40-65 = 'Incomplete', < 40 = 'Unsatisfactory'. Points for questions: Introductory Features 10, Macro Aspects 20, Production System Overview 35, Production Planning & Control 50, Quality 20, MIS 20, Work Study 20, Conclusion 15, Style 10."},

    {"id": "ie400_mfg_problem_grading", "topic": "IE 400 Manufacturing Problem Project section grading criteria project-type report",
     "content": "IE 400 Problem/Project section (100 pts) evaluated on: problem/project context (IE relevance, significance), technical content, style/organization. Project-type SP report grading: Introduction 5, Literature Review 10, Problem Definition 30, Data Gathering & Analysis 10, Solution Approaches 20, Results 15, Conclusion 10."},

    # ===================== IE 400 MFG MANUAL — SECTIONS =====================
    {"id": "ie400_mfg_format", "topic": "IE 400 Manufacturing Report Format Style English sections appendix glossary",
     "content": "IE 400 Manufacturing report: English, sections numbered in capitals. Sections: TOC, Introduction, Main body (including IE problem or project), Conclusion, References, Appendix. Add glossary for technical terms including company jargon."},

    {"id": "ie400_mfg_sec1", "topic": "IE 400 Manufacturing Section 1 Introductory Features firm ownership sector customers stakeholders IE functions",
     "content": "IE 400 Mfg Section 1 — Introductory Features (10 pts): Q1.1 Full title, founding, location. Q1.2 Ownership type, shareholders. Q1.3 Sector, products/services, market shares, advertising brochures. Q1.4 Customers and stakeholders. Q1.5 IE functions in the organization."},

    {"id": "ie400_mfg_sec2", "topic": "IE 400 Manufacturing Section 2 Macro Aspects black box inputs outputs mission vision location investment technology R&D project management",
     "content": "IE 400 Mfg Section 2 — Macro Aspects (20 pts): Q2.1 Black box diagram (inputs/outputs), exports, imports, standards/certificates. Q2.2 Mission and vision. Q2.3 Location factors. CHOOSE ONE of: Q2.4 Capital investment plans/evaluation methods OR Q2.5 Technology, know-how, R&D, project management."},

    {"id": "ie400_mfg_sec3", "topic": "IE 400 Manufacturing Section 3 Production System process chart capacity utilization MTS MTO ATO layout block plan cost ratio analysis",
     "content": "IE 400 Mfg Section 3 — Production System Overview (35 pts): Q3.1 Process/operations chart. Q3.2 Capacity (designed, effective, rated). Q3.3 Operations type (continuous/repetitive/intermittent, MTS/MTO/ATO). Q3.4 Block plan. Q3.5 Layout types. Q3.6 Detailed department layout. Q3.7 Unit manufacturing cost. Q3.8 Financial ratio analysis."},

    {"id": "ie400_mfg_sec4", "topic": "IE 400 Manufacturing Section 4 Production Planning Control forecasting demand aggregate planning inventory MRP scheduling JIT",
     "content": "IE 400 Mfg Section 4 — Production Planning & Control (50 pts): Must answer at least 3 questions. Q4.1 Forecasting activities, methods, accuracy. Q4.2 Product decisions, scarce resources, allocation plans. Q4.3 Inventory: items, functions, control policies (periodic/continuous review), performance measures, MRP. Q4.4 Detailed scheduling, performance measures. Q4.5 JIT philosophy, reducing slack."},

    {"id": "ie400_mfg_sec5", "topic": "IE 400 Manufacturing Section 5 Quality Planning Control definition life cycle quality assurance preventive organization",
     "content": "IE 400 Mfg Section 5 — Quality (20 pts): Must answer at least 2 questions. Q5.1 Quality definition, customer requirements to specs, quality control at all life cycle stages. Q5.2 Three proactive quality assurance activities, quality organization/responsibility sharing."},

    {"id": "ie400_mfg_sec6", "topic": "IE 400 Manufacturing Section 6 MIS Management Information System decisions computers hardware software ERP",
     "content": "IE 400 Mfg Section 6 — MIS (20 pts): Must answer at least 1. Q6.1 Decision makers at strategic/tactical/operational levels. Q6.2 Computer systems, data types. Q6.3 Software, ERP, application programs."},

    {"id": "ie400_mfg_sec7", "topic": "IE 400 Manufacturing Section 7 Work Study method study work measurement stopwatch time study job evaluation wage",
     "content": "IE 400 Mfg Section 7 — Work Study (20 pts): Must answer at least 1. Q7.1 Apply work measurement (stopwatch/predetermined times/work sampling) to operator, evaluate results, apply method study. Q7.2 Job evaluation, job description, job specification, wage differentiation."},

    {"id": "ie400_mfg_conclusion", "topic": "IE 400 Manufacturing Section 8 Conclusion assessment IE problem feedback career",
     "content": "IE 400 Mfg Conclusion (15 pts): Assess SP procedure. Most difficult part of IE problem study. Plans for 4 more weeks. Future IE training needs. IE vs other engineering. IE roles in firm. Top management attitudes toward IE."},

    {"id": "ie400_mfg_appendixA", "topic": "IE 400 Manufacturing Appendix A IE Problem Definition Formulation identification symptoms causes tools fishbone pareto",
     "content": "IE 400 Appendix A — IE Problem Definition: Identify problem through symptoms (e.g. low utilization, planning deficiencies). Validate with data. Use tools: cause-effect diagrams, Pareto analysis, flowcharts, check sheets, brainstorming, influence diagrams. Formulate: decision maker, objective, performance criteria, alternatives, limitations. Think about modeling approaches."},

    {"id": "ie400_mfg_appendixB", "topic": "IE 400 Manufacturing Appendix B Participated Project report completed in-progress Gantt",
     "content": "IE 400 Appendix B — Participated Project Report: If completed: Introduction, Problem statement, Approach, Summary of Work, Conclusions. If in-progress: Introduction, Problem statement, Approach, Project Schedule (Gantt/network), Work Done To Date, Expected Outcomes."},

    # ===================== IE 400 SERVICE MANUAL — GRADING =====================
    {"id": "ie400_svc_grading", "topic": "IE 400 Service Grading Points scoring questions problem project incomplete unsatisfactory",
     "content": "IE 400 Service grading: Questions 200 pts, Problem/Project 100 pts. Must pass both separately. Questions: 125-160 or section < 50% = Incomplete. < 125 = Unsatisfactory (repeat). Problem/Project: 40-65 = Incomplete. < 40 = Unsatisfactory. Points: Introductory Features 10, Macro Aspects 20, Service System Overview 35, Planning & Control 50, Quality 20, MIS 20, Work Study 20, Conclusion 15, Style 10."},

    {"id": "ie400_svc_problem_grading", "topic": "IE 400 Service Problem Project section project-type report grading 6 weeks",
     "content": "IE 400 Service Problem/Project (100 pts): context, technical content, style. Project-type report (min 6 weeks, proposal approved): Introduction 5, Literature Review 10, Problem Definition 30, Data Gathering 10, Solution Approaches 20, Results 15, Conclusion 10."},

    # ===================== IE 400 SERVICE MANUAL — SECTIONS =====================
    {"id": "ie400_svc_format", "topic": "IE 400 Service Report Format Style Times New Roman font 12 spacing",
     "content": "IE 400 Service report: English, Times New Roman size 12, 1.5 line spacing. Use report cover from SP website. Sections: TOC, Introduction, Main body (with IE problem/project), Conclusion, References, Appendix. Add glossary."},

    {"id": "ie400_svc_sec1", "topic": "IE 400 Service Section 1 Introductory Features firm ownership services customers stakeholders",
     "content": "IE 400 Service Section 1 — Introductory Features (10 pts): Full title, founding, location. Ownership. Sector and services, market shares. Customers and stakeholders. IE functions."},

    {"id": "ie400_svc_sec2", "topic": "IE 400 Service Section 2 Macro Aspects black box resources inputs outputs tangible intangible service package mission vision location labor capital investment technology R&D innovation project management",
     "content": "IE 400 Service Section 2 — Macro Aspects (20 pts): Q2.1 Black box (distinguish resources vs inputs/customers), standards. Q2.2 Service package: supporting facility, facilitating goods, explicit/implicit services, tangible vs intangible components. Q2.3 Mission and vision. Q2.4 Location factors (customers, cost, competitors, demand management). Choose at least one of: Q2.5 (capital vs labor intensive, investment), Q2.6 (technology), Q2.7a+b (innovation, R&D, project management)."},

    {"id": "ie400_svc_sec3", "topic": "IE 400 Service Section 3 Service System Overview service blueprint flowchart front office back office productivity layout process product fixed-position cost ratio",
     "content": "IE 400 Service Section 3 — Service System Overview (35 pts): Q3.1 Service blueprint (flowchart with line of visibility, front/back office). Q3.2 Productivity definition and measurement. Q3.3 Service classification: divergence, customer contact, continuous vs discrete, labor intensity (service factory/shop/mass/professional). Q3.4 Layout types + block plan. Q3.5 Unit service cost. Q3.6 Financial ratio analysis."},

    {"id": "ie400_svc_sec4", "topic": "IE 400 Service Section 4 Planning Control forecasting demand management yield reservation capacity scheduling inventory buffer waiting JIT",
     "content": "IE 400 Service Section 4 — Planning & Control (50 pts, at least 3 questions): Q4.1 Forecasting in service environment. Q4.2a Demand management (promotions, yield management, reservation, complementary services). Q4.2b Operations strategy for capacity control (workforce adjustment, cross-training, customer participation). Q4.3 Inventory: input materials, output, perishable, control policies, buffer capacity vs customer waiting. Q4.4 JIT, reducing slack."},

    {"id": "ie400_svc_sec5", "topic": "IE 400 Service Section 5 Quality service quality reliability responsiveness competence empathy tangibles gap perceived expected customer",
     "content": "IE 400 Service Section 5 — Quality (20 pts): Q5.1 Quality definition: reliability, responsiveness, competence, empathy, tangibles. Gap between perceived and expected service. How customer requirements become specs. Q5.2 Quality control tools (histograms, Pareto, fishbone, control charts), quality assurance, quality organization."},

    {"id": "ie400_svc_sec6", "topic": "IE 400 Service Section 6 MIS decisions computers software ERP",
     "content": "IE 400 Service Section 6 — MIS (20 pts, at least Q6.1 + one more): Q6.1 Decision makers at 3 levels, data usage. Q6.2 Computer systems. Q6.3 Software, ERP."},

    {"id": "ie400_svc_sec7", "topic": "IE 400 Service Section 7 Work Study measurement stopwatch sampling method study job evaluation description specification wage",
     "content": "IE 400 Service Section 7 — Work Study (20 pts, at least 1): Q7.1 Apply TWO work measurement techniques to repetitive tasks, method study. Q7.2 Job evaluation, description, specification, wage differentiation."},

    {"id": "ie400_svc_conclusion", "topic": "IE 400 Service Section 8 Conclusion assessment feedback IE career",
     "content": "IE 400 Service Conclusion (15 pts): Same as manufacturing — assess SP, most difficult part, plans for 4 more weeks, future training, IE vs other engineering, IE roles, management attitudes."},

    # ===================== DOCUMENTS / FORMS ROUTING =====================
    {"id": "docs_app_letters", "topic": "Documents Forms Application Letters download staj başvuru belgesi",
     "content": "Application Letters at sp-ie.metu.edu.tr > Documents/Forms (login required): IE-300 SP Application Form (Turkish/English), IE-400 SP Application Form (Turkish/English), SP Protocol (sözleşme, if company requests)."},

    {"id": "docs_insurance", "topic": "Documents Forms Insurance declaration paid SP form download",
     "content": "Insurance Forms at Documents/Forms: Declaration Form (with family health insurance), Declaration Form (without family health insurance), Paid SP Information Form (İşsizlik Fonu Katkısı Bilgi Formu)."},

    {"id": "docs_eval", "topic": "Documents Forms Evaluation Form Employer Survey download",
     "content": "Evaluation Forms at Documents/Forms: Evaluation Form + Employer Survey (Turkish), Evaluation Form (English)."},

    {"id": "docs_manuals", "topic": "Documents Forms SP Manuals download IE300 IE400 manufacturing service report guide",
     "content": "SP Manuals at Documents/Forms > SP Manuals (login required): IE300 Summer Practice Manual, IE400 Summer Practice Manufacturing Manual, IE400 Summer Practice Service Manual. Read the relevant manual BEFORE starting SP to know what to observe and what questions to answer in the report."},

    {"id": "docs_presentations", "topic": "Documents Forms Introductory Session presentations slides download",
     "content": "Introductory Session presentations at Documents/Forms: IE 300 Introductory Session slides, IE 400 Introductory Session slides. Cover prerequisites, steps, company types, insurance, deadlines."},
]
