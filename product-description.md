# OpenFEMA Dataset: Disaster Declarations Summaries - V2 | FEMA

The source code outlining how this product gathers, transforms, revises and publishes its datasets is available at [https://github.com/rearc-data/fema-disaster-declarations-summaries](https://github.com/rearc-data/fema-disaster-declarations-summaries).

## Main Overview
FEMA Disaster Declarations Summary is a summarized dataset describing all federally declared disasters. This dataset lists all official FEMA Disaster Declarations, beginning with the first disaster declaration in 1953 and features all three disaster declaration types: major disaster, emergency, and fire management assistance. The dataset includes declared recovery programs and geographic areas (county not available before 1964; Fire Management records are considered partial due to historical nature of the dataset).

Please note the unique structure of the disaster sequencing (due to a numbering system that originated in the 1950's-1970's):

| | |
|-|-|
| 0001-1999 | Major Disaster Declaration |
| 2000-2999 | Fire Management |
| 3000-3999 | Emergency Declaration (Special Emergency) |
| 4000- | Major Disaster Declaration |

This is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The dataset is primarily composed of historical data that was manually entered into NEMIS after it launched in 1998. The financial information is derived from NEMIS and not FEMA's official financial systems.

Due to differences in reporting periods, status of obligations, and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.

#### Data Source
The included datasets are provided in CSV, JSON and JSONA formats. The data contains the following data fields: 

| Name | Title | Type | Description |
|-|-|-|-|
| `femaDeclarationString` | FEMA Declaration String | string | Agency standard method for uniquely identifying Stafford Act declarations - Concatenation of declaration type, disaster number and state code. Ex: DR-4393-NC. |
| `disasterNumber` | Disaster Number | number | Sequentially assigned number used to designate an event or incident declared as a disaster. |
| `state` | State | string | The name or phrase describing the U.S. state, district, or territory. |
| `declarationType` | Declaration Type | string | Two character code that defines if this is a major disaster, fire management, or emergency declaration. |
| `declarationDate` | Declaration Date | date | Date the disaster was declared. |
| `fyDeclared` | FY Declared | number | Fiscal year in which the disaster was declared. |
| `incidentType` | Incident Type | string | Type of incident such as fire or flood. The incident type will affect the types of assistance available. |
| `declarationTitle` | Declaration Title | string | Title for the disaster. |
| `ihProgramDeclared` | IH Program Declared | boolean | Denotes whether the Individuals and Households program was declared for this disaster. |
| `iaProgramDeclared` | IA Program Declared | boolean | Denotes whether the Individual Assistance program was declared for this disaster. |
| `paProgramDeclared` | PA Program Declared | boolean | Denotes whether the Public Assistance program was declared for this disaster. |
| `hmProgramDeclared` | HM Program Declared | boolean | Denotes whether the Hazard Mitigation program was declared for this disaster. |
| `incidentBeginDate` | Incident Begin Date | date | Date the incident itself began. |
| `incidentEndDate` | Incident End Date | date | Date the incident itself ended. |
| `disasterCloseoutDate` | Disaster Closeout Date | date | Date all financial transactions for all programs are completed. |
| `fipsStateCode` | FIPS State Code | string | FIPS two-digit numeric code used to identify the United States, the District of Columbia, US territories, outlying areas of the US and freely associated states. |
| `fipsCountyCode` | FIPS County Code | string | FIPS three-digit numeric code used to identify counties and county equivalents in the United States, the District of Columbia, US territories, outlying areas of the US and freely associated states. |
| `placeCode` | Place Code | string | A unique code system FEMA uses internally to recognize locations that takes the numbers '99' + the 3-digit county FIPS code. There are some declared locations that don't have recognized FIPS county codes in which case we assigned a unique identifier. |
| `designatedArea` | Designated Area | string | The name or phrase describing the U.S. county that was included in the declaration. |
| `declarationRequestNumber` | Declaration Request Number | string | Unique ID assigned to request for a disaster declaration. |
| `lastRefresh` | Last Refresh | date | Date the record was last updated in the API data store. |
| `hash` | Hash | string | MD5 Hash of the fields and values of the record. |
| `id` | ID | string | Unique ID assigned to the record. |

To learn about about the data fields, please visit [the dataset's documentation](https://www.fema.gov/openfema-dataset-disaster-declarations-summaries-v2) on FEMA's website.

## More Information
- Source: [FEMA | OpenFEMA Dataset: Disaster Declarations Summaries - V2](https://www.fema.gov/openfema-dataset-disaster-declarations-summaries-v2)      
- [FEMA | OpenFEMA Homepage](https://www.fema.gov/openfema)    
- [FEMA | OpenFEMA API Terms & Conditions](https://www.fema.gov/openfema-api-terms-conditions)  
- Frequency: Daily
- Format: CSV, JSON, JSONA

## Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub [issue](https://github.com/rearc-data/fema-disaster-declarations-summaries/issues) and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you are looking for specific open datasets currently not available on ADX, please submit a request on our project board [here](https://github.com/orgs/rearc-data/projects/1).
- If you have questions about the source data, please contact FEMA News Desk at FEMA-News-Desk@dhs.gov.
- If you have any other questions or feedback, send us an email at data@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.