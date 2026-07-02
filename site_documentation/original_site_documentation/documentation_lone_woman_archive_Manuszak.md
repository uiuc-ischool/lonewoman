**NOTE: The most current, most complete version of this document is (and should remain in the event of changes) the version found on [lonewomanusc@gmail.com](mailto:lonewomanusc@gmail.com)’s Google Drive. The version saved in Dropbox in the DocumentProcessing \>\> Documentation folder is static. It is inaccessible for change once the LWLI Dropbox account is closed (2019).**

# What follows below:

* an introduction to the Lone Woman & Last Indians Digital Archive (LWLI) project;  
* a conceptual overview of the processes involved in making the LWLI website;  
* specific instructions on how to recreate those processes to add more content to the LWLI project in the future;  
* an overview of the repositories that house the content contained in, data associated with, and programming that supports the LWLI website; and  
* other information including account log-ins, passwords, and contacts to be used in case any new work on this project is undertaken.

1. # Project overview

This digital archive collects, transcribes, annotates, and maps more than 450 nineteenth- and twentieth-century documents relevant to the story of the Lone Woman of San Nicolas Island. This Nicoleña was isolated on the most remote of the California Channel Islands between 1835-53, an event triggered by a massacre resulting from the international sea otter trade and then by the Spanish policy of *reducción*, or the in-gathering of Native tribes to Catholic Missions. The story of the Lone Woman, widely known in the nineteenth century, is perhaps best remembered today in the version Scott O’Dell fictionalized in his 1960 children’s novel, *Island of the Blue Dolphins*. In O’Dell’s Newbery-winning book, the Lone Woman is reimagined as the teenaged Karana.

The digital archive seeks to facilitate research on the Lone Woman as both a historical figure and as a mythic representation of the American Indian, a reimagining central to US nation-building.

Work on this archive was completed between June 2013 and December 2017\. This process was often part of, associated with, and affected by work on the Channel Island National Park’s *Island of the Blue Dolphins* subject website ([https://www.nps.gov/subjects/islandofthebluedolphins/index.htm](https://www.nps.gov/subjects/islandofthebluedolphins/index.htm)) and *Island of the Blue Dolphins: The Complete Reader’s Edition* (UC Press, 2016), but the three products remain distinct.

# How we found our documents

## Searches/Acquisitions

We started with two bibliographies of about 150 documents combined; one of these bibliographies had been compiled by Steve Schwartz, U.S. Navy archaeologist. The bibliographies contained citations for both published (books, periodicals) and unpublished accounts containing the Lone Woman story.  These documents were acquired through Thomas Cooper Library (including digital resources) and Interlibrary Loan (ILL).  

The digital archive is hand-curated. Each document acquired was carefully evaluated for references to other documents; when found, these documents were acquired if at all possible (i.e., if citations were correct enough to lead us to the document referenced). The goal was to use the growing body of Lone Woman references to acquire all known/possible sources and collect as many documents as possible.  To supplement this process, a systematic search of all open-access and institutionally-available databases (e.g., New York Public Library had more searchable databases than USC) was conducted.  A list of search terms can be found below, with the guidance on how to acquire a new document or cache of documents.

Most documents were acquired digitally, often from institutionally-available databases, sometimes from another institution scanning a physical copy and sharing that scan through ILL. In other cases, ILL acquired microfilm reels (particularly for newspapers and manuscripts) or print items and then digital copies were made at USC. In a very few instances, institutions provided photocopies, and digital copies were made from these.

Once a clean digital copy of an item was obtained, we made it into what is called the Digital Surrogate. Specific instructions for creating that Digital Surrogate can be found below, with guidance on how to add a new document or cache of documents to the website.

## Logging the find (Data entry, citation)

Each Digital Surrogate was assigned a unique identifier, called a Document Key, which was then used to connect the document to both a full Chicago Manual of Style (CMS) citation and to all associated files (e.g., Initial Transcription, TEI). The Document Key is used as an “anchor” across all tabs in the Publications spreadsheet. Instructions on the conventions of assigning Document Keys can be found below, with guidance on how to add a new document or cache of documents to the website.

Once a document was acquired and a Document Key assigned, it was entered into the Publications spreadsheet. The information in this spreadsheet is multifaceted. 

1) It records the discrete information found in each document’s **citation** in a specified format and with specified conventions that can be read by the website’s programming.  
2) It records **permissions** information: whether an item is in the public domain and if not, who owns the copyright (and thus granted republishing permission to the LWLI archive).  
3) It describes if and how the document is **related to** any other document in the archive (e.g., direct reprint, truncated reprint, paraphrase of, response to) .  
4) It includes (for periodicals) a **Source or Scope Note** (researched in a separate stage).  
5) Two separate tabs on the Publications spreadsheet include information on searches not completed for a variety of reasons explained therein.

All documents in the archive are recorded in our documentation and presented on the website using the Chicago Manual of Style, 16th edition (CMS). Two things are true and rely on one another to ensure accurate and consistent citations across the website: 

1. Citations are recorded in our spreadsheets in accordance with the CMS.   
2. The website programming pulls and manipulates the information in that spreadsheet to ensure consistent implementation of grammar and presentation conventions (commas, numerals, and italics).  For this to work, all parts of a citation must be in the *correct column* of the *appropriate tab* on the Publications spreadsheet.

Instructions on how to interact with the spreadsheet and its various tabs (including which tabs contain what information) can be found below, with guidance on how to add a new document or cache of documents to the website.

## Relationships

It became apparent quickly that many documents in the archive are related to one another. Most often, one document reprints, truncates, modifies, or paraphrases another. In many cases, one document references another as a source of information. Occasionally, one document responds to, critiques or argues with the facts of another.

These relationships were evaluated “by hand,” by Sara Schwebel (editor) and Rachel Manuszak (digital collections manager), initially by noting parallels while reading transcriptions aloud and later by explicitly looking for common phrases and unusual word usage while noting publication dates (which were used to determine specific document relationships). Document Groups grew or were refined, and more Document Groups were noted, as new documents were added to the archive.  Throughout the process, we were aware that many more reprints likely existed “in the world” but were not being acquired during our searches given the limits of current newspaper digitization and optical character recognition (OCR) technologies.

We utilize Carto, an open-source cloud computer platform that provides GIS and web mapping tools for display in a web browser, to interpret the document relationship information visually.  Data available on the Publications spreadsheet was input into Carto to map the circulation of the articles in each Document Group over time.This work was completed by undergraduates Sydney Cowart ‘18 (statistics major) and Molly Carlson ‘18 (computer science major), with programming assistance (to display Carto visualizations on the LWLI website) from undergraduate computer science major and Lead Programmer Tyler Encke ‘17. 

Instructions on how to record new document relationships in the Publications spreadsheet (including information necessary for Carto) can be found below, with the guidance on how to add a new document or cache of documents to the website.

## Permissions

Most documents in this archive are published in the United States and are in the public domain. For this material, website programming generates a standard permission statement. For documents published abroad and in the public domain, a different, country-specific permission statement is provided with the document citation (on the Publications spreadsheet) and appears via website programming. Unpublished (manuscript) items and copyrighted materials require special, specific permission statements.  The precise wording of these permission statements is provided with the document citation (on the Publications spreadsheet) and appears via website programming.

Determining which post-1923 U.S. documents are in the public domain is not always an easy or precise process.  We operated under the principle of due diligence--if reasonable efforts to obtain permission failed, records of attempted communication by email/U.S. mail/phone were filed and we uploaded the document. If requested by copyright holders, we will take down documents we mistakenly thought were in the public domain.  Sara met with USC Associate General Counsel George W. Lampl, III on 1/22/14; as well as with USC Digital Librarian Kate Boyd and Thomas Cooper’s Head of Circulation Tucky Taylor. She also consulted with other DH projects before setting this policy.

## Digital Surrogates

Digital Surrogates are in PDF and PNG format. PDFs were acquired from digital copies. These PDFs were then compiled, cropped, and straightened in Adobe Acrobat Pro. All individual pages were saved from that PDF as PNG image files, and the PNG files were renamed per conventions described below. Pagination of Digital Surrogates on the LWLI website is determined by the PNG files generated in this process.

Instructions on how to compile, edit, and transform these files can be found below, with guidance on how to add a new document or cache of documents to the website.

## Transcriptions

Transcriptions in this archive are in TXT format and were processed using Notepad to avoid the macros and reformatting present in Microsoft Word.

Because of the unreliable nature of OCR and the age of the material in this archive, most transcription was done by hand. Each Transcription was then read aloud to another team member who checked for accuracy against the Digital Surrogate. Necessary changes in the Transcription were made at this point.

## Tropes

After an Initial Transcription was made and its document relationship (if any) determined, the document was sent to Sara to be Troped.  At the beginning of the project, Sara determined which tropes present in the archive as a whole would be marked for visual display (see Trope “Introduction” essay on the LWLI archive).  Sara read each Transcribed document, marking Tropes by using Word’s comment feature.  To attempt to maintain consistency, articles in document groups were first Troped according to their Parent Document and then only Troped again (for added material) if necessary.

## TEI

Text Encoding Initiative (TEI) encoding is perhaps the most important step in the document processing process. It is certainly the most involved, and great care should be taken to all details provided in the “guidance on how to add a new document or cache of documents to the website” section below and to the separate documents Documentation\_Appendix-TEIInstructions and Documentation\_Appendix-TEIConventions. Together, these three documents will allow you to properly implement TEI in the LWLI archive. Read this document first (Documentation\_Manuszak), then Documentation\_Appendix-TEIInstructions will introduce you to the system of TEI, and finally Documentation\_Appendix-TEIConventions provides you with LWLI archive-specific details. TEI is a markup language used to represent a written or printed text in digital space. This includes the form and layout of the text itself, as well as the interpretive layer added to the text via annotations.

Annotations encoded in the text with TEI appear on a LWLI webpage as hyperlinks that, when clicked, bring up annotations or groups of annotations. These provide information on persons, groups, organizations, places, and ships mentioned in a text. Altogether, more than 3,000 people, places, groups, ships were evaluated for inclusion and 1175 annotations were written and are published on the website.

Additionally, TEI markup facilitates the Interpretive Mode of a Transcription’s display, highlighting literary tropes in various colors.

TEI files in this archive are in XML format and were processed using Oxygen XML Editor, version 14.2. Instructions on how to implement TEI, including interpretive standards and conventions as well as download instructions for the Project’s version of Oxygen XML Editor can be found below, with guidance on how to add a new document or cache of documents to the website.

## Uploading (http://calliope.cse.sc.edu/lonewoman/uploader)

Before uploading can begin, the LWLI Dropbox must be restored.  (This involves importing the DocumentProcessing folder and subfolders from the LWLI external Hard Drive into the restored Dropbox).

Uploading content to the LWLI website involves any of four tasks, which you see as options on the Uploader web page (in this order):

1. Force: syncing the website database (which is compiled from, relies on, and mirrors the information in the spreadsheets described below) and any new information or changed information it reflects with the documents being uploaded,  
2. ForcePlus: uploading the PDF, PNG, and XML files (all in the .ZIP folder as described later) that the LWLI website programming uses to produce the final document page,  
3. Restore Databases: restoring the website database in the event of an error while uploading documents, and  
4. Upload All: this has really been superseded by ForcePlus. Creating/replacing the zipped folders used by the LWLI website programming. (This is  a defunct feature, mentioned here so you understand not to use it.)

Instructions on which feature to use and the necessary steps to take before an upload or in order to address an upload error can be found below, with guidance on how to add a new document or cache of documents to the website.

## Final Checks

In earlier workflows, final checks were a kind of quality assurance step taken before documents were uploaded. Rachel proofread all TEI’d documents to check for transcription errors (typos) and TEI errors. In the current process, final checks are best performed after an upload in order to check all of the above as well as the correct display of the Digital Surrogate and Transcription, including population of correct annotations and functioning website features (e.g., citation, document group placement when applicable, document introduction when present).

Instructions on how to perform final checks, including LWLI project conventions that are (and should be) standard across the LWLI website can be found below, with guidance on how to add a new document or cache of documents to the website.

# II. If you want to acquire a new document or cache of documents

## Searches/Acquisitions

1. Familiarize yourself with three tabs on the Publications spreadsheet:  
   1. DatabasesSearched  
      1. This tab details (from left to right) individual databases that have already been searched or were noted for future searches and their websites; the last date on which any searches took place and their status as of that date (complete, in progress, etc.); the person who conducted any searches; notes regarding the database or the search process; and suggestions for streamlining future searches (including possible ways to more easily detect duplicate acquisitions and make searches most efficient for new content).  
   2. SearchesNotCompleted  
      1. This tab details (from left to right) the importance of completing an abandoned search (including an acquisition’s potential relationship to existing documents); a document’s citation information; the details of previous ILL requests for material; any documents already obtained which provided the initial reference; and further notes which might help make future searches more efficient.  
   3. DeadendSearches  
      1. This tab details (from left to right) the importance of completing an abandoned search (including an acquisition’s potential relationship to existing documents); a document’s citation information; the details of previous ILL requests for material; any documents already obtained which provided the initial reference; and further notes which might help make future searches more efficient.  
2. Plan your searches. This process is highly individual, but requires attention to detail however it is performed. Decide whether to make a general search of the databases listed in DatabasesSearched or to complete more targeted requests based on SearchesNotCompleted or DeadendSearches. 

   The guidance below assumes that general searches are performed first, followed by more targeted searches. Finally, it describes how to make requests through ILL (including how to obtain better digital copies when ILL has already obtained an “adequate” copy for the project). The order of searches is not as important as consistency, attention to detail, and taking thorough notes throughout the process.

   As you begin finding new documents through these searches, record new documents on the SearchesNotCompleted tab. This includes the basic citation information, search notes, and and ILL or email communication records. There are columns for each of these things on the SearchesNotCompleted tab. Continue to keep the information on this tab until all information has been gathered and you are ready to assign a Document Key and compile a Digital Surrogate. 

   If you begin searching for items on the DeadendSearches tab, record all new searching and citation information there until all information has been gathered and you are ready to assign a Document Key and compile a Digital Surrogate.

3. At the point in which your search is complete and you’re ready to begin adding a new document or cache of documents to the archive/website, you will transfer all information to the Obtained | InArchive tab. Instructions for that process can be found below, with the guidance for that step.  
4. Begin general searches by first determining the order of databases you will search and organizing them in such order on the spreadsheet. Add two columns--one in which you order the databases and another in which you mark whether new searches are completed. This will help you keep track.

   When you search each database, use the list of search terms found in the Search Terms Appendix (filename: Documentation\_Appendix-SearchTerms).

   Use the tutorials and examples provided by databases to familiarize yourself with features that might make searches more efficient. It is also always appropriate to “fiddle” with search terms, modifying them to ensure the widest net cast. (Examples include using variant spellings, quotation marks, “fuzzy” searching, alternating related words like “female” and “feminine,” etc.) As you become more familiar with the LWLI project and the documents being acquired, you may find a new term or set of terms and return to previous databases to try them. In these cases, update information on the Publications spreadsheet to record your work.

   Before downloading a digital copy of any document found or adding it to the SearchesNotComplete tab, use the Obtained | InArchive tab to ensure you are not duplicating a document already processed and in the LWLI archive.

   Remember to evaluate newly acquired documents for references to other documents (and to evaluate as much as possible whether the referenced documents have already been found, processed, and are in the LWLI archive). Perform targeted searches for any such documents.  
5. Targeted searches are performed by first looking for the publication in previously-mentioned databases or in other online formats. If this fails, research where a print copy of the document can be found via resources like the Library of Congress’ Chronicling America U.S. Newspaper Directory, 1690-Present or WorldCat.org. The goal is to identify an institution likely to have the material (specifically, the correct issue of a publication). Visit any identified institutions’ catalog to confirm holdings. Sometimes a phone call or email is necessary to confirm definitively.

   When found, place an ILL request providing as much information as possible from the records reviewed. Be very specific about what you need. Instructions can be found below on Digital Surrogate conventions; this will make your ILL request efficient and prevent duplicate or additional requests. If available, ILL will provide a digital copy of the requested material. Otherwise, they will attempt to acquire the microfilm or a print copy. Occasionally, they will only be able to acquire a photocopy from the lending institution.  
6. Remember that the searches/acquisitions process is never totally complete. This is due to many things--the ongoing nature of digitization, the expanding nature of digital collections and consortial lending in academic and large public libraries, and the limitations of OCR. 

   For all of these reasons, keep copious notes on the process of your searches and pay special attention to the “Acquisitions Information” column on the Obtained | InArchive spreadsheet if an acquired document is processed and added to the LWLI website.

·       

# III. If you want to add a new document or cache of documents to the archive/website

Once new searches have been completed, follow these steps to process newly acquired documents and add them to the LWLI website.

## Logging the find (Data entry, citation)

All documents on the LWLI website are recorded on the Publications spreadsheet, in the Obtained | InArchive tab. All new acquisitions (including old searches newly completed) should “land” on the Obtained | InArchive website. If the document information began on another tab (SearchesNotCompleted or DeadendSearches), it should be removed from that tab and transferred to the Obtained | InArchive spreadsheet. 

When a new document is listed on the Obtained | InArchive tab, move from left to right, making sure each of two things:

1. Each cell in the document’s citation contains the appropriate information.  
2. Any directions in the column heading above each cell are followed. These instructions (not repeated here) must be followed to the letter to ensure correct output by the website programming that builds the LWLI archive.

Another method for ensuring accurate spreadsheet information is to copy a model of the type of document you are entering. (e.g. if you’re entering a new journal article, use a citation like Altrocchi1944 as a model. If you’re entering a new manuscript, use a citation like Phelps1848 as a model. If you’re entering a chapter or other section of a book, use Benson1997 as a model. And so forth.)  See the “CMS 16th Ed. Citation Format Designation” column of the Obtained | InArchive tab.

### Source Notes

Source notes were written for every periodical (newspaper, popular magazine, academic journal) for which a similar scope/source note was not already included in Chronicling America.  If Chronicling America contained an appropriate Scope Note, the LWLI archive links to it.  LWLI Source Notes attempt to answer the question, “what does it mean that an article about the Lone Woman appeared in this publication” by providing information about the scope of each publication’s news coverage and readership at the time that Lone Woman-related article(s) appear. Thus, Source Notes address population demographics as well as details about the publication itself.  Most Source Notes were researched and written by undergraduate English  & anthropology double major Paige Kuester ‘17 and funded by a Magellan Grant and ALA Carnegie Fellowship.  (Paige received an undergraduate research award from Thomas Cooper Library for her stellar work on this feature of the archive).  

## Relationships

In order to determine relationships between documents, you must first develop a familiarity with the archive. There is no shortcut for this. While it is not necessary to read every document in the archive, it *is* necessary to read and closely evaluate *most* of the documents that appear in Document Groups. Use the Browse by Document Group feature of the LWLI website and review the DocumentRelationships and DocumentGroups tabs of the Publications spreadsheet. Start with the parent document of each Document Group. Read it in its entirety. Then, based on the “Relationship notes” column of the DocumentRelationships tab, read all documents that are not a direct reprint of a parent document in order to become familiar with the phrases, details, etc. that make Document Groups distinct.

Sometimes a new document will make an explicit reference to another publication but not be a member of a Document Group. References may be specific, such as:  “From the *San Francisco Chronicle*.” But this does not guarantee that the reference is correct or that the document reprints fully (or only) the text from the publication named. The new document could mistakenly refer to the *Chronicle* and actually have meant the *Gazette* or *Times*. It may also reprint only a few sentences or paragraphs of one or two documents within an entirely new story. We have noted all of these details for document groups in the “Relationship notes.” It will help you keep track of the precise relationship between documents to record these details. Only a familiarity with existing document groups will help you determine these things.

Once the precise document relationship is ascertained, record this information in the DocumentRelationships tab. This tab records the precise relationships between documents, including information like presence or absence of attribution, misattributions, etc. Find the pertinent document group on the spreadsheet and insert the new document in order by date in that group. Use other documents in the document group to determine the level of information to be provided. It is likely you will duplicate precise wording already present. (e.g. if you find a direct reprint of TheArgus1857, the text to describe that precise relationship is already written).

Lastly, new documents that  you add to the DocumentRelationships tab (described above) must be added to the DocumentGroups page. You will use the relationship recorded in the DocumentRelationships tab to do this. You will also maintain the chronological order within each column. (All direct reprints in column B are in chronological order inside Document Groups. The same is true for columns C and D. In column H, all documents are in chronological order regardless of the specific relationship they have to the parent document.)

The instructions in the column headings should be followed very, very carefully for this tab. Most importantly, remember: both sides should be even. This means that the left side of the spreadsheet should be “even” with the right side--notice that the first line describing a Document Group on the left side is in the same row as the first line describing that Document Group on the right side of the spreadsheet.

When you insert a new line(s) to insert a Document Key, make sure you evaluate the rest of the row. You may have to move cells up on the opposite side of the spreadsheet. (e.g. if you add a new Document Key underneath WeeklyWisconsin1853 in column C, you need to move ***ALL*** information on the right side of the spreadsheet up by one cell. This keeps both sides of the DocumentGroups tab “even.”

Once these steps have been completed, the Carto and Tableau data visualizations will no longer be up-to-date.  If possible, new Carto and Tableau datasets should be made that incorporate data for all new documents.  Then, the Carto map and Tableau data visualizations (around tropes) will be regenerated.  They automatically update to the LWLI website.  Carto is an open-source cloud computer platform that provides GIS and web mapping tools for display in a web browser (meaning, it interprets and presents the document relationship information visually).  Tableau is an open-source cloud computer platform for data visualizations. Data available on the Publications spreadsheet for all Document Groups was input into Carto to map the circulation of the articles in each Document Group over time and into Tableau to generate trope visualizations.

To create new data sets for the LWLI archive:

1. Create Excel spreadsheet for All Publications.  
   1. Each row represents a document in the archive and should contain that Document Key and relevant document information  
   2. The column headings should include (without regards to order):  
      1. Document Key  
      2. Document Type	  
      3. Author 	  
      4. Article Title	  
      5. Publication Title  
         1. Los Angeles Times, Los Angeles Times Sunday Magazine, and Los Angeles Times Magazine are all denoted as Los Angeles Times and Magazine  
      6. Publication Date  
         1. In date format—Month / Day / Year  
         2. If day is unknown, input first of the month  
         3. If day and month are unknown, input January 1st of corresponding year  
      7. Day  
         1. (of publication) If unknown, leave blank  
      8. Month   
         1. (of publication) If unknown, leave blank  
      9. Year	  
      10. Publisher	  
      11. Editor	  
      12. Place of Publication   
          1. i.e. Ithica, New York  
      13. (Excluding National Pubs) Place of Publication  
          1. Same information as Place of Publication, but N/A for national publications  
      14. City   
          1. (of publication), Left blank if a national publication   
      15. State/Province/Region  
          1. (of publication), Left blank if national publication  
      16. Country  
          1. (of publication), Left blank if national publication  
      17. Latitude	  
          1. (of publication), Left blank if national publication  
      18. Longitude  
          1. (of publication), Left blank if national publication  
   3. Unknown information should be left blank (i.e. No publisher/author/title ect.)  
2. Create Excel spreadsheet for Tropes.   
   1. Each row represents an instance of a trope  
   2. Each row should have the trope (i.e. Indians as Savage), the trope category (Universal or Specific to Archive), the document key for the document in which the trope appears, and the corresponding document information with columns as in All Publications spreadsheet  
3. Create Excel spreadsheet for Document Groups  
   1. Each row represents a document in a document group  
   2. Columns should include Document Key, Relationship (Parent, reprint, Paraphrase ect), Document Group Name, Publication Date and Place of Publication  
4. For visualizations, open Tableau Public platform  
   1. Select “Excel” under “Connect” options  
   2. Find & select Trope spreadsheet   
   3. Once spreadsheet opens in Tableau Public, find the Publication Date column, click on the little “Abc” and select “Date” to change data type from string to date  
   4. Data \-\> Add New Data Source \-\> Excel   
   5. Find  & select All Publications spreadsheet  
   6. Again change data type of Publication Date column to date  
   7. Click Sheet 1 to begin creating the visualization   
   8. When choosing dimensions, make sure the proper data source is selected (both should be visible under “Data” in the upper left)  
   9. Save to Tableau Public  
5. For maps, go to Carto.com and log in  
   1. New Map  
   2. Connect Dataset \-\> Data File should be selected  
   3. Browse to select or drag & drop All Publications spreadsheet OR Document Groups spreadsheet, depending on which map   
   4. Connect Dataset  
   5. In Data View change select Publication Date column header \-\> Change Data Type \-\> Date \-\> “Yes”  
   6. Carto automatically geo-references locations  
   7. To only show magazine & newspaper articles, select filters tab and filter by document type   
   8. In Map View, choose appropriate wizard & change parameters as needed  
   9. Publish

It is uncertain whether Carto and Tableau will still be viable in the event any new documents are added to the LWLI archive. The platforms may be defunct or have new functionality. Alternatively, data visualizations like our circulation maps may be much more common and another platform may offer a better solution. Consult with the new computer programmer about options.  Regardless:

* Evaluate all Document Groups to make sure the most up-to-date information has been input into whatever platform you use.  
  * This includes evaluating the DocumentRelationships tab of the Publications spreadsheet. Some very small document groups (in which the relationship was one of response, not reprinted information or prose) were not included on the LWLI archive website or Carto representation but their relationships have been determined and the information preserved on the Document Relationships tab. It is possible a newer, more dynamic platform could visually present this kind of information (which is currently not displayed).  
* Choose a platform that will work with the LWLI website programming as it exists. Test a small document group in coordination with the computer programmer before inputting all Document Group information to ensure you don’t waste a great deal of time and effort on a non-viable solution.  
* Depending on time and resources available if new documents are added to the LWLI archive, the circulation map and data visualizations may simply have to remain static as of December 2017\. Possible scenarios include: A new platform cannot be found, Carto and/or Tableau is defunct, a computer programmer is unable to make new visualizations work with the website programming, or time constraints on new project personnel make this step one of lowest priority. In this case, consider adding a note at the top of the Data Visualizations and Circulation of the Lone Woman’s Story pages indicating that these visualizations do not yet reflect the most current information in the LWLI archive.


## Permissions

See Permissions section above.

## Digital Surrogates

There are three parts to creating a complete Digital Surrogate.

1. Assigning a Document Key and making certain any instance of this Document Key (in the Publications spreadsheet, in filenames, and in TEI) is consistently spelled and is ***exactly the same each and every time it is used, everywhere***. This cannot be emphasized enough.

   The goal of the filename is to identify the document by author, date of publication, and publication title if author information is unknown. Because naming conventions began long before the size of the archive was known, the Document Keys are not always intuitive. In the examples below, real file names are used and can be referenced the LWLI files if that is helpful. When assigning a document key, be sure to check the Publications Google doc to ensure you are not creating a duplicate Document Key; search for the new key you assign (using the Ctrl+F function).

   Some documents already in the archive fail to adhere to the conventions detailed below or may even contain typos or spelling mistakes; even if they do, we leave them be. With almost 500 documents and multiple spreadsheets, changing filenames at this stage risks inserting errors. Inconsistency on the “backend” of data is not as important as making sure presentation of information on the LWLI archive is correct.

   When you name a document, use the conventions found in the Document Key Conventions Appendix (filename: Documentation\_Appendix-DocumentKeyConventions).  
2. Compiling the complete PDF.

   Adobe Acrobat Pro was/should be used to create and edit digital surrogates for this archive. In Pro, use the Tools menu on the right side of the window to complete the following steps.  
   1. Combine all pages of the acquired digital copy, make sure they are in order, and save as DocumentKey\_DigSur (e.g. Hardacre1950\_DigSur, Meade1964\_July24\_DigSur, EveningBulletin1856\_3(42)\_DigSur.) Identifying front matter should be included as appropriate to the format.  
      1. For books, this includes the title page, copyright page, the first page of the chapter, and all pertinent pages identifying the placement of the section or paragraph(s) to be included in the archive.  
      2. For newspapers, magazines, etc., this includes the front page of the issue, the first page of the section in which the article appears, the entire page(s) on which the article appears, and smaller “chunks” of the text that will make easily readable sections when presented on the LWLI website. What constitutes a “readable chunk” of the Digital Surrogate depends on the quality of the material when digitized. Review other documents of the same type on the LWLI website.  
      3. For academic journals, etc., this includes the title page of the issue, the first page of the section in which the article appears, and the entire page(s) on which the article appears.  
   2. Crop pages to remove any scanning markers (excess space, borders attached by the program that saved the scan, etc.).  
      1. Be careful not to over-crop. We want the document to be “clean” and the margins appropriate to the format, not removed entirely. Consult other documents with the same CMS 16th Ed. Citation Format Designation (found on the Publications spreadsheet) for reference.  
   3. Run OCR to straighten the pages and recognize text. While the resulting text will likely not be very useful, the “optical” part of optical character recognition means the OCR function of Adobe Acrobat Pro is an excellent way to straighten an image.   
   4. You may have to repeat steps 2 and 3 more than once if OCR’s straightening up of the pages creates white space on the sides or in the corners of the document.

   

3. Transforming the finalized PDF into PNGs.

   Select File \>\> Save As \>\> Image \>\> PNG. In the same folder in which the DIgital Surrogate is saved, you will now have one PNG image file for each page of the Digital Surrogate pdf.  
   1. Examples:  
      Robinson2004-Adrift\_DigSur\_Page\_1  
      Robinson2004-Adrift\_DigSur\_Page\_2  
      Robinson2004-Adrift\_DigSur\_Page\_3  
      Robinson2004-Adrift\_DigSur\_Page\_4  
      Robinson2004-Adrift\_DigSur\_Page\_5  
      Robinson2004-Adrift\_DigSur\_Page\_6  
   2. Sort the DocumentKey folder by name, select the PNG files, right-click on the first PNG file, and select “Rename.”  
   3. Remove any text in the filename after DocumentKey\_DigSur and press “Enter.” The files will automatically be renamed in succession. This is the only filename format for PNGs which the website programming can read.  
      1. Examples:  
         Robinson2004-Adrift\_DigSur (1)  
         Robinson2004-Adrift\_DigSur (2)  
         Robinson2004-Adrift\_DigSur (3)  
         Robinson2004-Adrift\_DigSur (4)  
         Robinson2004-Adrift\_DigSur (5)  
         Robinson2004-Adrift\_DigSur (6)  
         

## Transcriptions

Notepad was/should be used to create and edit Transcriptions for this archive. The program is simple, but that works in our favor and helps avoid unnecessary insertion of errors into the text. The macros in fancier programs like Microsoft Word (the features that perform normally useful functions like autocorrect) make it much more difficult to create a true transcription and to be confident that the what is encoded reflects the text of the Digital Surrogate.

If a document is a new, unique document that is not in relationship to another document in the archive:

1. Create a TXT file and save it as DocumentKey\_InitTransc. “InitTransc” stands for “Initial transcription,” a legacy from the earliest workflows.   
2. Bring up both the Initial Transcription and the Digital Surrogate. Some people have used two computer screens to do this, while others have used the “split screen” feature.  
3. If the typeface in the Digital Surrogate is “clean” enough (the typeface is clear and, in most cases, originated on a computer), select the text in the Digital Surrogate and copy it. Paste it into the Initial Transcription.

   In most cases, the document will not be “clean” enough. In these instances, transcribe by hand the entire text of the document in the Digital Surrogate.  
   1. Separate each title and subtitle from the preceding and following text with a blank line (hard return).  
   2. Separate each section heading (if there are any) from the preceding and following text with a blank line (hard return).  
   3. Separate each paragraph from the preceding and following text with a blank line (hard return).  
   4. Ignore any photo captions and do not indicate the presence of photos. Photos may be included in the Digital Surrogate, but they are not indicated in the transcription.  
   5. Do not maintain hyphens when it is clear they are only present due to column widths in newspapers journals. However, remember that antiquated spelling sometimes hyphenates words we no longer hyphenate, like “to-day.” Use the document as a guide; if a word is repeated, use the instance of the word that does not continue across lines. If you are ever unsure, check with Sara.  
   6. Do not indicate any layout conventions, such as columns or reading instructions those found in newspapers (“Continued on page 10,” “Continued from page E5”.). Simply continue the transcription of the document text without interruption.  
   7. DO include presentation conventions, like use of italics or bold text, and punctuation like m-dashes and ampersands. In order to do this, a few special characters are used in the Transcription.  
      1. Bolded text:  
         \<hi rend="bold"\>text\</hi\>  
      2. Italicized text:  
         \<emph\>italic text\</emph\>  
      3. M-dash:  
         &\#8212;  
      4. Ampersand:  
         \&amp;  
      5. Superscript:  
         \<hi rend="superscript" \>Number\</hi\>  
4. Proofread for your own typos and be sure to review the layout of the document. Did you separate each paragraph? Did you note every instance of bolded or italicized text? If you included any photo captions or reading instructions by mistake, remove them. Check that all subtitles have been transcribed.  
   1. If the document contains typographical errors, correct them in the least intrusive way possible. It is very important not to over-correct and to ***be correct*** in the use of any editorial corrections like the following. If you are unsure, consult with Sara before inserting any such changes.  
      1. If a letter is missing, insert the letter inside square brackets.  
         1. Cruso\[e\]  
      2. If the word is incorrect and therefore unintelligible to those unfamiliar with the archive, insert the correct word inside square brackets immediately after the typo. If the word is definitely misspelled (not just an antiquated spelling or British spelling) but is still readable, use \[sic\]  
         1. other \[otter\] hunters  
         2. arroused \[sic\]  
      3. If a word is necessary to clarify meaning, insert the clarifying word inside square brackets immediately before or after the word it is clarifying, as appropriate.  
         1. In the \[eighteen-\] fifties.  
      4. Do not correct antiquated spellings. Dictionaries online and in print should provide clarity for antiquated spellings, including words with hyphens or a lack of expected/seemingly extraneous spaces.  
   2. As a rule, we do not correct the variations of place names. For instance, both the spellings “San Nicolas” and “San Nicholas” are considered correct.  
   3. Sometimes, documents will be inaccurate, inconsistent, and will disagree with one another. For instance, some documents claim Charles Hubbard captained the *Peor es Nada*, while others name Isaac Sparks as captain. We do not correct for historical accuracy (the hoovering annotations take care of this). Sometimes “channel islands” are capitalized and sometimes the phrase is not. Sometimes, a document uses both forms. We rely on the document’s internal consistency to determine how we encode each document and rely on the content of the annotations which come up to clarify if the document is not correct or confusing. Always make the correction that interferes least with the readability of the document.  
      1. One exception to this is instances where it is entirely clear the author ***means*** one thing and the wrong word has been used. This standard is more confusing than the following examples. Before implementing this rule in a new document, consult with the editor to ensure clarity and consistency.  
         1. Capt. John \[sic\] Nidever of Santa Barbara  
            (The person being spoken about here is ***definitely*** George Nidever. This is a rather egregious typo that confuses users, so we inserted the “\[sic\]” in the transcript so that users would not be confused when George Nidever’s one-liner appeared if this annotation was clicked on.)  
         2. –*Forest \[sic\] and Stream*   
            (The document being referenced is ***definitely*** *Field and Stream*, which is encoded and referenced by the TEI.)  
         3. *San Francisco Call* \[sic\]  
            (The document being referenced is ***definitely*** the *San Francisco Chronicle*, which is encoded and referenced by the TEI.)  
5. Read the Transcription aloud against the Digital Surrogate (with a partner) to check transcription accuracy. Correct any errors so that the Transcription reflects exactly the content of the Digital Surrogate .

If a document has been determined to be a reprint:

1. See TEI instructions below. Because TEI and final checks have already been performed, it makes much more sense to work from the completed TEI document rather than duplicating steps by creating another Initial Transcription, which increases the chances of inserting an inconsistency or error.

Early in the project, there was an additional step after Initial Transcriptions were completed. “Flagging” the transcription was done so that new project personnel could become familiar with the TEI concepts of persons, groups, organizations, places, and ships. As everyone became more comfortable with TEI, it became clear that learning to recognize these words/phrases within a text should go hand-in-hand with encoding them. Now, flagging is not a distinct task but is an optional exercise new project personnel may choose to complete separately with the first few documents they transcribe and encode. If that choice is made, any documents created from the exercise should not be retained in the LWLI files.

## Tropes

After an Initial Transcription was made and its document relationship (if any) determined, the document was sent to Sara to be Troped.  At the beginning of the project, Sara determined which tropes present in the archive as a whole would be marked for visual display (see Trope “Introduction” essay on the LWLI archive).  Sara read each Transcribed document, marking Tropes by using Word’s comment feature.  To attempt to maintain consistency, articles in document groups were first Troped according to their Parent Document and then only Troped again (for added material) if necessary.

Microsoft Word was/should be used to create and edit Trope Documents for this archive. The text of the Initial Transcription is copied and pasted into Microsoft Word and then saved as an RTF file, DocumentKey\_Tropes.  This RTF file is used as guide when adding tropes in the document’s TEI. This is done using the “span” feature, which is explained in Documentation\_Appendix-TEIInstructions.

## TEI

There are two parts to implementing TEI in the LWLI archive.

1. The “brass tacks” of implementing TEI. This encompasses the program used, the templates that have been made, and the methods for forming good TEI documents. It also includes structural conventions. (e.g. why we encode “the Lone Woman” but don’t include any articles before “Channel Islands” when we encode that phrase.)  
2. The universal rules and conventions we use which are interpretive in nature. (e.g. we have a standard list of persons included in the 1853 “hunting party” on San Nicolas Island.)

To encode new documents for the LWLI archive, use the TEI Appendices (filenames: Documentation\_Appendix-TEI and Documentation\_Appendix-TEIConventions).

## Uploading

Uploading content to the LWLI website involves any of four tasks. All of them can be access from the website Uploader, [http://calliope.cse.sc.edu/lonewoman/uploader](http://calliope.cse.sc.edu/lonewoman/uploader). This webpage is not accessible from other webpages on the LWLI website; you must go directly to the URL above.

The LWLI archive file structure is explained later in this document. Any instructions here about moving a file or folder will be clear once you have read that guidance.

1. Force

   Upload the PDF, PNG, and XML files that the LWLI website programming uses to produce a final document page

   This function involves uploading an individual document (with its accompanying files) or a small set of new documents.   
   1. Make any new ZIP folders necessary for uploading.  
      1. In the DocumentKey folder, select every file present there (Digital Surrogate PDF and PNG, Initial Transcription, Tropes, TEI, and any additional files).  
      2. Right click on the TEI file and select “Compressed (zipped) folder.”  
      3. When the zipped folder appears, remove “\_TEI” from the filename.  
      4. Move (Do ***not*** copy, but move) the ZIP folder (which you just created and renamed) into the 1-Successful-Calliope folder, where all other ZIP folders are contained.  
         1. If you are replacing an older ZIP folder, you will be given the option of replacing the old folder, or keeping both files. ***Replace*** the old folder. There should only be one ZIP folder per document.  
   2. On the LWLI Uploader, click “Choose Files” (beside the Document Package label) and select the necessary ZIP file/s.  
   3. Enter “ScottOdell” for the LWLI website passcode.  
   4. Select “Force.” This is used to "force" the sync tool to sync the database with the spreadsheet after a single file upload.  
   5. Press the “Submit” button. Do not close the webpage until you see the notification that your action has been successful.  
   6. At the bottom left of your screen, you will see a progress bar and an indication that the site is working with the Calliope server.   
   7. When the function has successfully run, you will see a notification which reads “The documents have been submitted to the archive,” followed by a list of links to each document successfully uploaded. 

      ***Read through this list carefully and make sure you review each link, no matter how many documents you have uploaded***.  
      1. In the event of an error when uploading one document, you will see an error message rather than a link. Error messages are specific and have been tailored to all known errors (including if necessary files like th PNG images have not been generated, or if an error in the TEI prevents the LWLI website from generating a transcription, etc.). 

         If you see a new error, carefully review each new DocumentKey folder, file-by-file, and check the TEI very carefully. The error message should provide a clue about where in the TEI it encountered an error. Once you’ve addressed that error, try to upload that document again. If that doesn’t work, work with the new computer programmer to figure out what went wrong. It may be a “class of” issue that would apply to many documents, in which case a new error message should be generated. It might also be a simple, document-specific fix which can be implemented quickly. 

         Be resourceful and thorough, cooperate with the new computer programmer, and remember that everything takes a bit longer than you thought it would. Leave yourself time to address any uploading errors.  
2. ForcePlus

   Sync the website database (which is compiled from, relies on, and mirrors the information in the spreadsheets described below) and any new information or changed information it reflects with the documents being uploaded.

   This function relies on the content provided in DocumentProcessing \>\> 7-UploadToSite \>\> 7a-FinalCopies\_FullFolders \>\> 7a1-Zipped folder in Dropbox and the metadata provided in the Google Drive spreadsheets. It makes and places in the correct folder the necessary ZIP files (described in the step above), uploads all documents, empties the LWLI website database, and finally updates the LWLI website database from all spreadsheets (Publications and Types & Keys). 

   Once the LWLI archive has moved off Dropbox, this feature will still work to force an update of the LWLI website database with any new information on the LWLI spreadsheets. But rather than change the documents in Dropbox, it will use the last copy of the LWLI file structure saved on Calliope.

   The important distinction between the “Force” and “ForcePlus” features is that the ForcePlus empties the LWLI website database. This was a “guaranteed” way to implement changes quickly on the site when the encoding was changed on large numbers of documents and when important content changes were made to one-liners on the Types & Keys website.   
   If any new documents are added to the LWLI archive, the LWLI Dropbox account will have to be restored if it’s been reverted to a basic account, the file structure will have to be replaced (copied back to Dropbox from the LWLI external hard drive), the complete DocumentKey folder placed in the 7a1-Zipped folder described below, and a ForcePlus run. If a document is removed due to copyright complaint, follow those same steps but ***remove the DocumentKey folder entirely from the 7a1-Zipped folder***. Place it in DocumentProcessing \>\> 2-PermissionsNeededOrDenied \>\> 2-RemovedFromArchive and then run a ForcePlus.  
   1. Enter “ScottOdell” for the LWLI website passcode.  
   2. Select “ForcePlus.”  
   3. Press the “Submit” button. Do not close the webpage until you see the notification that your action has been successful.  
   4. At the bottom left of your screen, you will see an indication that the site is working with the Calliope server. \*You will not see a progress bar because this is such a large task.  
   5. When the function has successfully run, you will see a notification that reads “The documents have been submitted to the archive,” followed by a list of links to each document successfully uploaded. 

      ***Read through this list carefully and make sure you review each link, no matter how many documents you have uploaded***.  
      1. In the event of an error when uploading one document, you will see an error message rather than a link. Error messages are specific and have been tailored to all known errors (including if necessary files like the PNG images have not been generated, or if an error in the TEI prevents the LWLI website from generating a transcription, etc.). 

         If you see a new error, carefully review each new DocumentKey folder, file-by-file, and check the TEI very carefully. Also, work with the new computer programmer to figure out what went wrong. It may be a “class of” issue that would apply to many documents, in which case a new error message should be generated. It might also be a simple, document-specific fix which could be implemented quickly. 

         Be resourceful and thorough, cooperate with the new computer programmer, and remember that everything takes a bit longer than you thought it would. Leave yourself time to address any uploading errors.  
3. Restore Databases

   In the event of an error while uploading documents or updating the LWLI website database, this function restores the previous database and set of documents included on the LWLI website.  
   1. Enter “ScottOdell” for the LWLI website passcode.  
   2. Select “Restore Databases.”  
   3. Press the “Submit” button. Do not close the webpage until you see the notification that your action has been successful.  
   4. When the function has successfully run, you will see a notification that reads “The documents have been submitted to the archive. Successfully restored the backup\!”  
4. Upload All

   This function is similar to the ForcePlus function, but does not change the content of the LWLI website database. This function used to rely the DocumentProcessing \>\> 7-UploadToSite \>\> 7a-FinalCopies\_FullFolders \>\> 7a1-Zipped folder in Dropbox. It made and placed in the correct folder the necessary ZIP files (described in the step above) and then uploaded all documents.

   Once the LWLI archive has moved off Dropbox, this feature will be defunct. The Upload All feature will work, by using the last copy of the LWLI file structure saved on Calliope. But the same task is accomplished by the ForcePlus function, which also updates the LWLI website database.

Once the “Submit” button has been pressed and the function you chose has completed, you *should* see a notification that informs you the action is complete; document-specific error messages will be generated if relevant. Remember to review all lists, to ensure you don’t miss any such error messages. 

If you don’t understand an error message or a “Page Not Found” error comes up, take screenshots to send to the project editor and the computer programmer. Make sure each full document folder (like AlbanyEveningJournal1853 or Carl1952) has all of the associated documents. If you have accidentally left out the image files, for instance, the upload will not work.

## Final Checks

Once any new documents have been uploaded and appear on the LWLI website, a Document Check should be performed.

If a document is a “one-off” document (not part of a Document Group)

1. Click on the link for that document after it has been uploaded or use the document’s “permanent link.” (Note: if you upload new documents, the numeration of each document will change because the documents are uploaded in alphabetical order. Therefore, [http://calliope.cse.sc.edu/lonewoman/home/044](http://calliope.cse.sc.edu/lonewoman/home/044) might lead to different documents after uploading new batches. However, [http://calliope.cse.sc.edu/lonewoman/home/Hardacre1880\_SM](http://calliope.cse.sc.edu/lonewoman/home/Hardacre1880_SM) will always direct you to Hardacre1880\_SM.)  
2. Page through the Digital Surrogate, ensuring it flows naturally through the text and can be read.  
3. Check that the zoom in, zoom out, and zoom restore buttons function properly.  
4. Click “Expand Document” and page through the enlarged Digital Surrogate, ensuring it flows naturally through the text and can be read.  
5. Click “Interpretive Mode,” select each trope you find listed there.   
   1. Scroll through the transcription and ensure each trope present on the tropes list appears in the transcription.

If a document does not contain tropes, the “Interpretive Mode” button should not appear.

6. Check the document citation, ensuring it conforms to CMS 16th Ed. and matches information present on the Publications spreadsheet.  
7. Check that the Source Note appears and is for the correct publication. (A Source Note will only appear for periodical publications.)  
8. Check the Permission Statement, ensuring it conforms to the one on the Publications spreadsheet if a special Permission Statement is provided there. Otherwise, the “standard” LWLI archive permission statement should appear.  
9. Email the citation to yourself, ensuring it matches the document citation on the document page (meaning that it conforms to CMS 16th Ed. and matches information present on the Publications spreadsheet).  
10. Click on each link in the transcription. You are ensuring that  
    1. all links produce a one-liner and not an error message,  
    2. all one-liners display properly (name, write-up, map to the right location, “other documents that mention” link functions properly).  
    3. one-liners do not contradict an individual text's internal narrative, and  
    4. the "universal" rules (described in the TEI Conventions Appendix) have been imposed consistently across the archive.

If a document is part of a Document Group, repeat the same steps above with two changes.

1. Open this document in conjunction with its Document group. 

   This seems like a daunting task, but remember--all “old” documents have been through final checks. Use the DocumentRelationships tab of the Publications spreadsheet to find a document similar to yours or which is the “parent” of yours. If you are checking a new direct reprint of TheBostonAtlas1847, open that document page. If you are checking a truncated reprint of TheDailyHerald1853, it is possibly the same text as the EveningStar1853. The goal is not to re-check every document in a document group, but to use documents that were already checked as a standard for the new documents you have uploaded.  
2. Check that the Related Documents tab reflects the newly uploaded documents and matches the new information on the DocumentGroups tab of the Publications spreadsheet.

If you encounter an error, think critically about the source of the information that is awry. If the error originates from the Publications spreadsheet or the Types & Keys spreadsheet, fixing it there and re-uploading the document should correct any issues. If the error originates in the TEI encoding, fixing it there and re-uploading the document should correct any issues. If you cannot figure out why an error appears and fix it, coordinate with the current computer programmer.

# IV. File structure | How it works/How we did it

Until December 2017, the entire file structure of the LWLI archive lived on Dropbox. Now, all files live on Dr. Duncan Buell’s Calliope server at USC. Two of the four Uploading tasks described above rely on both the Calliope server and the [lonewomanusc@gmail.com](mailto:lonewomanusc@gmail.com) Dropbox account. As of December 2017, the LWLI archive files have been backed up on the Calliope server, on Sara Schwebel’s desktop, on Sara Schwebel’s LWLI external hard drive, and on Rachel Manuszak’s desktop; the [lonewomanusc@gmail.com](mailto:lonewomanusc@gmail.com) Dropbox has been reverted to a basic account--much too small to hold the LWLI archive files. 

If uploading of new content takes place, the simplest process is to renew the [lonewomanusc@gmail.com](mailto:lonewomanusc@gmail.com) Dropbox subscription and rely on the LWLI website programming as it already exists. (The LWLI archive files will not reappear in Dropbox. The basic account does not have enough space for that. The DocumentProcessing folder and subfolders will have to be re-loaded onto Dropbox from the LWLI external hard drive.) If for some reason this is not possible, consult with the new computer programmer, Duncan Buell, and Sara Schwebel to find a new solution. In such a case, the website programming would have to be rewritten based on the new repository/ies used.

Wherever it is housed, the LWLI archive file structure is as follows. A description of each folders’ contents is included.

* DocumentProcessing  
  *Contains all of the LWLI archive content. The website programming depends on the file structure as it exists. Do not change it except in coordination with a new computer programmer. Document Key folders (like Hardacre1880\_SM or Warner1894) were moved through the appropriate folders once document processing steps were complete. This allows all collaborators on the LWLI archive to see in real time the status of each document.*  
  * 1-AcquireDigitalSurrogate  
    *Contains DocumentKey folders for documents that need a better digital surrogate or for which the Digital Surrogate (or pieces of it) are still being acquired.*  
    * Clippings\&Unidentified  
      *Contains clippings from Stoneapple Farm (Dorsa O’Dell’s residence, where IBD was written) and other clipped newspaper articles, the publication of which we were unable to identify or confirm to complete acquisitions.*  
    * ForeignLanguages  
      *Contains documents published in a language other than English. These should be processed according to special instructions described previously in this document and, ideally, should be transcribed and checked by someone with knowledge of the document language.*  
    * NeedBetterCopy\&NeedForRelationships  
      *Contains documents that need a better Digital Surrogate or for which the digital surrogate (or pieces of it) are still being acquired. Includes documents for which the Document Relationship has been established, but which will require a better or complete Digital Surrogate.*  
  * 2-PermissionsNeededOrDenied  
    *Contains DocumentKey folders for post-copyright documents, which remain here until permissions have been acquired, denied, or the search has been abandoned.*  
    * 2-HarringtonPDFs  
      *Contains PDFs from the Smithsonian Institution acquired by Rachel Manuszak during search for Lone Woman-related pieces of John Peabody Harrington’s ethnological notes. Because his notes are in numerous languages (including indigenous California languages) and were very difficult to read, these sections were requested based on the Smithsonian’s collection guide and were not further evaluated. Work on making these notes available (including transcriptions) is being done by the Channel Islands National Park and will likely not be included on the LWLI website.*  
    * 2-PermissionsDenied  
      *Contained DocumentKey folders for documents for which permissions have been specifically denied by the copyright holder. We cannot feature these documents in the LWLI archive unless copyright situations change.*  
    * 2-RemovedFromArchive  
      *Contains DocumentKey folders for documents Sara and/or Rachel deemed inappropriate for the LWLI archive. Reasons included content (*e.g. *mentions of people associated with the Lone Woman but no reference to* her*), format (encyclopedias, etc.), and date of publication (permissions would have been needed but were deemed impossible to get).*  
  * 3-CompleteInitialTranscription  
    *Contains DocumentKey folders for documents which need to be transcribed and checked.*  
    * 3c-ReadAloud  
      *Contains DocumentKey folders for documents that have been transcribed and need to be read aloud between two people, confirming the Initial Transcription is accurate when compared to the Digital Surrogate.*  
  * 4-AddTropes  
    *Contains DocumentKey folders for documents that need to be “trope’d” by Sara.*  
  * 5-CompleteTEI  
    *Contains DocumentKey folders for “one-off” documents (not part of a Document Group) that need to be “TEI’d” per instructions in the TEI Appendices (filenames: Documentation\_Appendix-TEI and Documentation\_Appendix-TEIConventions).*  
    * 5-Reprints  
      *Contains Document Key folders for documents determined to be part of a Document Group and which need to be “TEI’d” per instructions in the TEI Appendices (filenames: Documentation\_Appendix-TEI and Documentation\_Appendix-TEIConventions).*  
  * 6-CompleteFinalChecks  
    *Defunct step. Used to contain DocumentKey folders for documents that needed to be reviewed for well-formed TEI and consistency with LWLI archive conventions. This step is now completed in Document Reviews after documents have been uploaded to the LWLI archive.*  
  * 7-UploadToSite  
    *Contains DocumentKey folders for documents which are complete and need to be uploaded to the LWLI archive and reviewed. The name and file structure of* **this** *folder cannot be altered because the website programming depends on it.*  
    * 7a-FinalCopies\_FullFolders  
      *Defunct step. At one point, the LWLI Uploader did not have the ForcePlus or Upload All functions and each document had to be ZIP’ed individually and was then moved into the 7a1-Zipped folder.*  
      * 7a1-Zipped  
        *Contains DocumentKey folders for documents which are complete and have been uploaded to the LWLI archive and reviewed.*  
    * 7b-ZippedFolderCopies  
      *Defunct step. At one point, the LWLI archive was moved from the USC Center for Digital HUmanities’ server, Tundra to its current server, Calliope. Each DocumentKey ZIP folder had to be re-uploaded to the Calliope folder and was then moved to the 1-Successful-Calliope folder.*  
      * 1-Successful-Calliope  
        *Contains DocumentKey ZIP folders for documents which are complete and have been uploaded to the LWLI archive and reviewed.*  
  * Documentation  
    *Contains documentation for the LWLI archive, including this document and all appendices.*  
    * TEITemplates  
      *Contains TEI Templates used during the TEI process described in the TEI Appendices (filenames: Documentation\_Appendix-TEI and Documentation\_Appendix-TEIConventions).*  
* LWLI-Backups  
  *Contains backups of the LWLI archive spreadsheets and website programming.*  
  * DigitalArchiveBackups  
    *Contains backups of the LWLI archive website programming.*  
  * GoogleDrive-SpreadsheetBackups  
    *Contains backups of the LWLI archive spreadsheets.*  
* NotCalliope  
  *Contains all additional* Island of the Blue Dolphins*/Lone Woman material belonging to Sara Schwebel but not directly associated with nor hosted on the LWLI archive website. Descriptions are not included here because folder and file names were coordinated with Sara solely for her recognition and use.*  
  * CINP-AdditionalImages  
  * CINP-ImagesWithPermissions  
    * IBD-RussianIllustrationsPermissionsGranted  
    * Juana Maria baptism papers  
    * Michael Ward sketches of LW  
    * RAC documents from Russian State Archives  
    * Il'mena sketch Lizzie Chapin  
  * CINP-VoiceOvers  
    * FINAL MP3s  
    * FINAL WAVs  
  * Collation  
    * 1-WorkingDocs  
    * 2-FinalizedDocs  
  * CriticalEditionResearch  
    * MaterialsFromElizabethHall  
    * MaterialsFromHoughtonLibrary  
      * IBD Production Cards (Houghton Lib.)  
    * MaterialsFromPhiladelphiaFreeLibrary  
    * MaterialsFromStoneappleFarm  
    * MaterialsFromUniversal  
      * Dittman documents  
      * IBD Film photos  
      * IBD movie still scans  
  * DEFUNCT-CDHCoding  
  * IBD-BookCovers  
    * BookCoverScans-SarasOffice  
    * Elizabeth Hall collection  
  * IBD-DellLitCriticism\&Reviews  
  * CI Symposium Marla Daily  
  * Discovery Day

# V. Google Drive | How it works/How we did it

The LWLI archive metadata (generally, “information about information;” for the LWLI archive, information about each document contained in the Publications spreadsheet), annotations (Types & Keys spreadsheet), and documentation (everything else including this document) have always lived on the [lonewomanusc@gmail.com](mailto:lonewomanusc@gmail.com)’s Google Drive. 

What follows below is a description of each folder on that Google Drive and the spreadsheets it contains. Each spreadsheet has multiple versions. One version is the shared, master copy like the “Publications” spreadsheet. Changes should be made to the appropriate shared, master spreadsheet because this is the spreadsheet from which the website programming pulls. Backup copies will not have version histories because they reflect the spreadsheet at a single point in time. They are truly static.

Other copies are static, backup copies saved at a particular time and date, for security. These are files like the “Publications | 2015-02-06” spreadsheet. New backups can be made by right-clicking on the document in Google Drive and selecting “Make a copy.” When this “Copy of…” document appears, right-click on it and select “Rename.” Follow the labelling conventions of previous backups for consistency. (i.e., DocumentTitle | YYYY-MM-DD)

Even though every Google Drive file has a version history (which can be accessed through selecting File \>\> Version history \>\> See version history), the backup files are almost five years old and contain all the important data. That leaves a lot of room for human error when using version histories to correct a “spreadsheet SNAFU.” This kind of thing happens if the frozen rows at the top of a spreadsheet tab (which contain the column heading and website programming information) are “unfrozen” and then a column of the spreadsheet tab is reorganized (most often alphabetically). Version histories help correct errors like this. Backup copies build redundancy into that system and help ensure all important work and major changes to the LWLI archive spreadsheets are preserved. 

Specific instructions and guidance for interacting with these spreadsheets is provided at the appropriate places in this document and its appendices. What follows is a descriptive overview rather than a repetition of information previously given.

* Documentation folder  
  * CitationGuides (Spreadsheets/Standardization) folder  
    * CitationFormatChecks spreadsheet  
      *Provides models for CMS 16th Ed. citations for Document Types (recorded on the Publications spreadsheet) present in the LWLI archive*  
    * ProofreadingRules spreadsheet  
      *Provides guidance on proofreading and interacting with the Types & Keys spreadsheet.*  
  * ProcessDocumentation (HowToAddMoreDocuments) folder  
    * Documentation\_Appendix-DocumentKeyConventions spreadsheet  
      *Provides guidance on how to assign new Document Keys when adding new documents to the LWLI archive*  
    * Documentation\_Appendix-SearchTerms spreadsheet  
      *Provides a list of search terms when looking for new documents to add to the LWLI archive*  
    * Documentation\_Appendix-TEIConventions spreadsheet  
      *Describes the conventions used when implementing TEI encoding throughout the LWLI archive. These include “universal rules,” a basic timeline, and other guidance.*  
    * Documentation\_Appendix-TEIInstructions spreadsheet  
      *Describes, from beginning to end, how to create a new TEI document when adding new documents to the LWLI archive.*  
    * Documentation\_Manuszak spreadsheet  
      *Describes the entire LWLI archive process. This is both an overview of what has been done and a set of instructions to follow if adding new documents to the LWLI archive. This document was written by the first LWLI project manager, Rachel Manuszak, with editing and clarifications by Sara Schwebel. This is where new LWLI personnel should start.*  
  * ProgrammingDocumentation (Backend/Database/Website) folder  
    * DOCUMENTATION for Lone Woman Archive\_Tyler Encke May 2017 spreadsheet  
      *Lead Programmer’s notes and instructions, including guidance on website programming, as of May 2017\.  This is where a new LWLI programmer should start.*  
* LWTeamHours spreadsheet  
  *Each tab records one undergraduate’s work on the LWLI archive, including the date, hours worked, total time, tasks accomplished, and notes.  This was used largely before students began working on Magellan grants and is not up-to-date or complete.*  
* NeedToKnow spreadsheet  
  *This was an interactive spreadsheet before current documentation was created. It might be useful for review if you are new to TEI, but all of the conventions contained here are either reflected in or have been updated in the documentation you are reading right now and the accompanying appendices.*  
* Publications spreadsheet  
  *Each tab records information about documents in the LWLI archive or documents and searches either currently being processed or which have been abandoned. The name of these tabs cannot be altered because the website programming depends on it.*  
  * Obtained | InArchive  
    *Describes documents in the LWLI archive. Permission have been secured, a Document Key has been assigned, and they are either in-process (when you are adding new documents to the LWLI archive) or have been uploaded to the LWLI archive.*

    *Lines 2 and 3 cannot be altered because the website programming depends on this information to generate document citations.*  
  * Source Notes  
    *Describes periodical publications featured in the LWLI archive. Paige Kuester ‘17 completed this work.*

    *Line 2 cannot be altered because the website programming depends on this information to generate periodical source notes on the Browse by Publication webpage.*  
  * DocumentRelationships  
    *Describes the relationships between documents featured in the LWLI archive, including details about extent of reprinting/truncation/paraphrasing of “parent” documents. This tab does not work purely as a spreadsheet because it is organized spatially (moving from top to bottom, then left to right to indicate Document Groups) and cannot be reorganized without distorting the information.*  
  * DocumentGroups  
    *Describes the relationships between documents featured in the LWLI archive in a list format, indicating the Document Groups that appear on the Browse by Document Group webpage. This tab does not work purely as a spreadsheet because it is organized spatially (moving from top to bottom, then left to right to indicate Document Groups) and cannot be reorganized without distorting the information.*

    *Line 2 cannot be altered because the website programming depends on the information to generate the Browse by Document Groups web page, Document Group information on each document page, and the Circulation of the Lone Woman’s Story data visualization.*  
  * Obtained | PermissionsNeeded  
    *Describes the state of permissions for documents not in the public domain. This tab has been used exclusively to generate “permission to-do” lists for Sara.*  
  * PermissionsDenied  
    *Describes documents for which permissions have been specifically denied by the copyright holder. We cannot feature these documents in the LWLI archive unless copyright situations change.*  
  * Obtained | DroppedFromArchive  
    *Describes documents Sara and/or Rachel deemed inappropriate for the LWLI archive. Reasons included content (*e.g. *mentions of people associated with the Lone Woman but no reference to* her*), format (encyclopedias, etc.), and date of publication (permissions would have been needed but were deemed impossible to get).*  
  * Obtained | AcademicReprintsDroppedFromArchive  
    *Describes documents that reprint the text of a document in the LWLI archive in an academic edition.* e.g. *numerous reprintings exist of Alfred Kroeber and Robert Heizer’s works, but when these are in post-copyright academic publications, gaining permission to include these documents is tricky. Furthermore, because these reprintings appear after the 1960 publication of Scott O’Dell’s* Island of the Blue Dolphins*, we are, generally speaking, less interested in them.*  
  * Obtained | ReviewsDroppedFromArchive  
    *Describes documents (almost exclusively found in newspapers) that review either Scott O’Dell’s* Island of the Blue Dolphins *or the 1964 Universal Pictures film adaptation.  Securing copyright proved too onerous and expensive.*  
  * Databases Searched  
    *Describes the databases searched to find documents included in the LWLI archive, including the last date on which a particular database was searched and any further notes deemed pertinent.  New searches could be useful as additional newspapers are being digitized constantly.*  
  * SearchesNotCompleted  
    *Describes document searches not completed. In the context of the LWLI archive, “incomplete” means “unacquired” or “unconfirmed.” If document references were confirmed positively not to exist or to have been mistaken/misprinted, they have been deleted. Often, items were unable to be “completed” because time for new searches ran out but new references to the Lone Woman or to reprinted documents were found.*  
  * DeadendSearches  
    *Describes document searches that most likely cannot be “completed.”Often, the notes indicate that an item is based on what is most likely a mistaken/misprinted reference (but this could not be definitively confirmed). Sometimes they were not completed because no holding institution would lend it.*  
* Types\&Keys spreadsheet  
  *Describes every person (alive, dead, historical, and fictional), place, group of persons, organization (formal institutions and legally recognized groups of people like American Indian tribes), and ship for which context is provided in Transcriptions in the LWLI archive. This includes the person who wrote the original “one-liner,” the necessary TEI encoding, the name and body of the one-liner, and pertinent sources and notes.*

  *Line 2 cannot be altered because the website programming depends on the information to generate the hyperlinked annotations in each Transcription.*  
  * Persons  
  * Places  
  * Groups  
  * Orgs  
  * Ships


  *Describes the tropes apparent in each document in the LWLI archive and which Sara analyzes and explains on the Literary Tropes Introduction webpage.*

  * Tropes

# VI. Calliope | A few useful tools

In addition to the LWLI Uploader, there are a few very useful tools provided by the website programming.

* [http://calliope.cse.sc.edu/lonewoman/zip](http://calliope.cse.sc.edu/lonewoman/zip)  
  This web page allows you to download a ZIP’ed folder of all of the TEI files that are on the server with the modifications made by the sync tool.  
* [http://calliope.cse.sc.edu/lonewoman/keys](http://calliope.cse.sc.edu/lonewoman/keys)  
  This web page lists all keys found in the LWLI archive, followed by a list of all of the documents in which each key appears.  
* [http://calliope.cse.sc.edu/lonewoman/files](http://calliope.cse.sc.edu/lonewoman/files)  
  This web page lists all documents in the LWLI archive, followed by a list of all the keys that appear in each document.

# VII. Other information

## Passwords

### LWLI Uploader

calliope.cse.sc.edu/lonewoman/uploader  
ScottOdell

### Dropbox

[lonewomanusc@gmail.com](mailto:lonewomanusc@gmail.com)  
nidever1878

### Gmail

[lonewomanusc@gmail.com](mailto:lonewomanusc@gmail.com)  
z1x2c3v4Z\!X@C\#V$

[lonewomanserver@gmail.com](mailto:lonewomanserver@gmail.com)  
@v3Dq7W8Jy^Dc3IVUpM@hSC%^  
(This email address ONLY functions in connection with the Contact the Editor and Email Citation functions.)

### Carto

lonewoman  
dittman1878

### Tableau Public (As opposed to the Tableau software)

[lonewoman507@gmail.com](mailto:lonewoman507@gmail.com)  
s@nN1ch0las

### Tableau- and Carto-associated Gmail

[lonewoman507@gmail.com](mailto:lonewoman507@gmail.com)  
l0n3W0m@n 

## Contact information

### Sara Schwebel

[sara.schwebel@gmail.com](mailto:sara.schwebel@gmail.com)  
401-527-5154

### Rachel Manuszak

[rmanuszak@gmail.com](mailto:rmanuszak@gmail.com)  
912-659-4905  
\[Note: Moved internationally in 2017 and should be contacted by email unless Sara has updated information.\]

### Tyler Encke

[tylerencke@gmail.com](mailto:tylerencke@gmail.com)   
757-536-0817

### Sydney Cowart

[sydneycowart28@gmail.com](mailto:sydneycowart28@gmail.com)   
843-847-1834  
