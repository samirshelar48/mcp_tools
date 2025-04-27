# Field Analysis Report

This document contains an analysis of different data sources and their field structures.

## Table of Contents
- [Court Data (ecourt)](#court-data-ecourt)
- [High Court Data](#high-court-data)
- [FIR Data](#fir-data)
- [Tribunals Data](#tribunals-data)
- [Consumer Court Data](#consumer-court-data)
- [High Court Causelist Data](#high-court-causelist-data)
- [Supreme Court Data](#supreme-court-data)
- [Arrested Persons Data](#arrested-persons-data)
- [Defaulters Data](#defaulters-data)

## Court Data (ecourt)

This dataset contains district court case information.

### Key Fields:
- **source**: Data source identifier ('ecourt')
- **type**: Binary classification (0 or 1)
- **name**: Name of party/person involved
- **address**: Address information (often from court documents)
- **cnr**: Case number record (unique identifier format: KARC010006002020)
- **state_name**: State where the case is registered (e.g., Karnataka)
- **case_type_name**: Type of case (e.g., SC, M.V.C., Crl.Misc., etc.)
- **case_no**: Case number identifier
- **case_year**: Year when the case was filed
- **pet_name**: Petitioner's name
- **res_name**: Respondent's name
- **filing_date**: Date when the case was filed
- **registration_date**: Date when the case was registered
- **first_hearing_date**: Date of the first hearing
- **decision_date**: Date when the decision was made
- **case_status**: Current status of the case (e.g., 'CASE DISPOSED')
- **nature_of_disposal**: How the case was disposed (e.g., 'Contested--ALLOWED')
- **under_acts**: Acts under which the case is filed
- **under_sections**: Sections under the acts
- **police_station**: Police station handling the case
- **fir_no**: FIR number if applicable

## High Court Data

This dataset contains high court case information.

### Key Fields:
- **source**: Data source identifier ('high court')
- **court**: Court type (e.g., 'ecourt high court')
- **name**: Name of party/person involved
- **address**: Address information
- **state_name**: State of the high court (e.g., Assam, Punjab, Karnataka)
- **court_name**: Name of the high court
- **cnr**: Case number record
- **case_no**: Case number identifier
- **case_type**: Type of case (e.g., RSA, WP(C), etc.)
- **case_year**: Year of the case
- **pet_name**: Petitioner's name
- **res_name**: Respondent's name
- **filing_date**: Date when the case was filed
- **registration_date**: Date when the case was registered
- **decision_date**: Date when the decision was made
- **case_status**: Current status of the case
- **bench_type**: Type of bench (Single/Double)
- **judicial_branch**: Branch handling the case
- **dist_name**: District name
- **under_acts**: Acts under which the case is filed
- **under_sections**: Sections under the acts

## FIR Data

This dataset contains information about First Information Reports (FIRs).

### Key Fields:
- **state_name**: State where FIR is registered (e.g., MAHARASHTRA, Delhi)
- **dist_name**: District name
- **fir_no**: FIR number
- **fir_year**: Year of FIR registration
- **date**: Date of FIR filing
- **name**: Name of the person(s) in FIR
- **father_name**: Father's name
- **address**: Address information
- **police_station**: Police station where FIR is registered
- **under_acts**: Acts under which the FIR is filed
- **under_sections**: Sections under the acts
- **source**: Data source identifier ('fir')

## Tribunals Data

This dataset contains information about tribunal cases.

### Key Fields:
- **id**: Unique identifier
- **uniq_case_id**: Unique case identifier
- **name**: Name of party/entity
- **petitioner**: Petitioner's name
- **respondent**: Respondent's name
- **link**: Link to case documents
- **section**: Legal section relevant to the case
- **date**: Case date
- **purpose**: Purpose of hearing
- **lawyer_name**: Lawyer's name
- **cp_no**: Case petition number
- **category**: Case category
- **bench**: Tribunal bench location
- **sub_type**: Sub-type information ('Insolvency and Bankruptcy Code')
- **source**: Data source identifier ('tribunals')

## Consumer Court Data

This dataset contains consumer court case information.

### Key Fields:
- **date**: Case date
- **uniq_case_id**: Unique case identifier
- **extension**: Extension date
- **case_no**: Case number (e.g., CC/395/2014)
- **business_category**: Category of business ('Miscellaneous')
- **court_type**: Type of court/hearing
- **source**: Data source identifier ('consumer court')
- **advocate**: Advocate's name
- **case_category**: Category of case ('civil')
- **name**: Name of complainant/party
- **court_name**: Name of the consumer court
- **case**: Full case details
- **petitioner**: Petitioner's name
- **respondant**: Respondent's name

## High Court Causelist Data

This dataset contains high court causelist information.

### Key Fields:
- **date**: Date of the causelist
- **extension**: Extension date
- **purpose**: Purpose of hearing
- **year**: Year of the case
- **link**: Link to causelist document
- **source**: Data source identifier ('high court causelist')
- **advocate**: Advocate's name
- **respondant**: Respondent's name
- **state_name**: State of the high court
- **sub_type**: Sub-type of causelist
- **court_name**: Name of the high court
- **case**: Full case details
- **case_no**: Case number
- **sr_no**: Serial number
- **petitioner**: Petitioner's name
- **judge_name**: Name of the judge

## Supreme Court Data

This dataset contains supreme court case information.

### Key Fields:
- **id**: Unique identifier
- **uniq_case_id**: Unique case identifier
- **name**: Name of party/person involved
- **status**: Case status ('D' for Disposed)
- **case_no**: Case number with registration date
- **present_last_listed_on**: Date when last listed with judges
- **status_stage**: Detailed status with disposal information and judges
- **category**: Case category (e.g., Service Matters, Criminal Matters)
- **pet_advocate**: Petitioner's advocate
- **res_advocate**: Respondent's advocate
- **disp_type**: Disposal type (e.g., 'Allowed', 'Dismissed')
- **source**: Data source identifier ('supreme court')

## Arrested Persons Data

This dataset contains information about arrested persons.

### Key Fields:
- **name**: Name of arrested person
- **address**: Address of the arrested person
- **age**: Age of the arrested person
- **gender**: Gender with age
- **father_name**: Father's name
- **state_name**: State where arrested
- **dist_name**: District name
- **police_station**: Police station handling the arrest
- **arrest_place**: Place of arrest
- **arrest_datetime**: Date and time of arrest
- **section**: Section under which arrested
- **police_name_and_designation**: Name and designation of police officer
- **court_name**: Court name where presented
- **source**: Data source identifier ('arrested')

## Defaulters Data

This dataset contains information about loan defaulters.

### Key Fields:
- **source**: Data source identifier ('defaulters')
- **sub_type**: Sub-type ('cibil defaulters')
- **name**: Name of defaulter (individual or company)
- **address**: Address of the defaulter
- **outstanding_amount**: Amount outstanding in rupees
- **report_type_name**: Type of default report
- **data_provider_name**: Bank providing the data
- **state_name**: State of the defaulter
- **bank_name**: Name of the bank
- **branch**: Bank branch
- **quarter**: Reporting quarter
- **borrower_name**: Name of the borrower
- **directors_info**: Information about directors (for companies)
