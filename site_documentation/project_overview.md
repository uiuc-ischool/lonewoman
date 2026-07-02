
### Project Overview

This project uses data from the original Lone Woman project website, taken from Project Leader and Editor Professor Sarah Schwebel’s personal hard drive. The hard drive included a series of folders named with article_ids, each of these folders included article image pngs, article transcript text in .txt, tagged TEI in .xml file and .rtf files. These folders with article_id names were added to the collectionbuilder template in the objects/ folder. Professor Schwebel’s hard drive also included two additional spreadsheets with multiple tabs. The first spreadsheet included article metadata, such as article title, publisher, date, location, copyright permissions, and connection to document groups that indicate how text from one article is reprinted across  others. This spreadsheet is saved at _source_data/drschwebel_harddrive_data/article_metadata_recentbackup_5.17.19.xlsx. 
A second spreadsheet included text write-ups that correspond to tags within transcript TEI XML files for specific literary tropes and person, place, group, organization, and ships entities. This second spreadsheet is saved at _source_data/drschwebel_harddrive_data/typeskeys_hyperlinkdata_recentbackup_5.17.19.xlsx. This tagging for tropes and entity and entity description writing were developed by the original project team along with the original collection of article images. The new project build relied on the article folders, metadata spreadsheet, and tropes and entities spreadsheet to build the current website, connecting images, transcripts, tropes and entity tags into interpretable article pages on the website.  

These article folders and two spreadsheets were used to create a complete metadata spreadsheet, that includes article images, transcript texts, tropes, and document groups, along with metadata on article publication, location, and date, all set to CollectionBuilder requirements. This spreadsheet is saved at _data/cb_complete_metadata_images_tropes_reprints_transcripts.csv. Each row of the final spreadsheet is an unique object ID that accounts for an  individual image of an article within one reprint group. Descriptions of entities and specific text spans of tropes were used to build interpretive functions for article transcripts on the website. 

The complete metadata spreadsheet was used to create article pages that would bring article images together in a gallery view, next to transcripts that would highlight tropes and show descriptions of entities. 

The user can browse the articles organized by publication, date, or location. The tropes page shows the frequency of tropes used across the articles and across time. The document group page groups articles into reprint groups, and also includes interactive maps that show how text is reprinted in different articles from publications across the country over time. 

The literary tropes essay page discusses the significance and movement of literary tropes in the press, as reporting and the exchange of information shape the cultural perception of historical events.

The goal of this project is to show the research output of collected articles that influence Scott O'Dell's *Island of the Blue Dolphins*, and to teach users about the use and spread of texts and literary tropes. This website also aims to show and explore the many-to-many relationships of tropes within articles and articles within documents groups. Many tropes exist across the articles and some articles exist in mutliple document groups, showing the complex network of literary ideas within the historical press. 

The files in this folder, site_documentation, describe how the website’s data, pages, and functionality were built so future stewards of the project can understand our process and the site’s inner workings. 


