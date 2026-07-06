
### Project Overview

This project uses data from the original Lone Woman project website, taken from project editor Professor Sara Schwebel’s personal hard drive, incorporated in the CollectionBuilder static website framework developed by the University of Idaho Library. The hard drive included a series of folders named with article IDs, each of these folders included article images as .png files, article transcripts in .txt files, tagged TEI text in .xml files, and additional .rtf files. These folders were added to the CollectionBuilder CSV template in the objects/ folder.
 
Professor Schwebel’s hard drive also included two additional spreadsheets with multiple tabs. The first spreadsheet includes article metadata, such as title, publisher, date, location, copyright permissions, document notes, and connection to document groups. Document groups are a collection of articles that share a piece of text, reprinted from an original article. The groups include the original article and articles containing reprinted text categorized as direct, truncated, or paraphrased reprints. This first original spreadsheet is saved at _source_data/drschwebel_harddrive_data/article_metadata_recentbackup_5.17.19.xlsx. A second spreadsheet includes keys that connect article transcript text spans to specific literary tropes and keys that connect named entities of person, place, group, organization, and ships to written descriptions. This tagging for tropes and entity descriptions was developed by the original project team using TEI. This second original spreadsheet is saved at _source_data/drschwebel_harddrive_data/typeskeys_hyperlinkdata_recentbackup_5.17.19.xlsx. The new project build relied on the article folders, metadata, and tropes and entity keys to build the current website, connecting images, transcripts, and tropes and entity descriptions into discrete interpretable article pages on the website. 
 
The article folders and two spreadsheets were used to create a complete metadata spreadsheet, that includes article images, transcript texts, tropes, and document groups, along with metadata on article publication, location, and date, all set to CollectionBuilder requirements. Each row of the final metadata spreadsheet is a unique object ID that corresponds to  a compound object that leads an image group or an individual article image within one reprint group. There are 494 compound rows and 3,934 image rows for 4,428 total object ID rows in the final complete metadata spreadsheet. Descriptions for entities and specific text spans of tropes were used to build interpretive functions for article transcripts on the website.
 
This complete metadata spreadsheet was used to create article pages that would bring article images together in a gallery view, next to transcripts that would underline tropes and show descriptions of entities. The spreadsheet accounts for articles as compound objects with associated images. HTML code builds the image gallery for each article, and JavaScript code builds the functionality to underline tropes and describe entities using interactive panels.
Original .xml transcript tags were stored as JSON data to connect transcript texts to tropes and entity data.
 
The website allows the user to browse the articles and contains tabs to explore the articles by publication, location, date, tropes, and document groups. The publishers tab lists articles by publication alphabetically, the location tab lists articles by place of publication including source notes tags for reprint types that show where text originates or spreads, and the timeline tab organizes articles by year of publication. The tropes page does not list articles, but shows the frequency of tropes used in articles across time with sparkline visualizations, along with a graph on total articles published across time and frequency of tropes across all articles. The visualizations were built using the Data Driven Document (D3) JavaScript library. The document groups page lists articles within their document groups by the publication date of the original article. Original documents are listed and can be clicked to reveal reprints, tagged as direct, truncated, or paraphrased. Document introduction notes on this page also describe the text or reprint group for particularly significant texts. Each document group has a corresponding interactive map that shows the spread of text across the documents by publishing location over time. The maps were made using MapLibre GL base map and a deck.gl map overlay. These website pages are all built using the CollectionBuilder Jekyll system of markdown files that use liquid to produce static pages, while HTML and JavaScript files are incorporated to build functionality.
 
The literary tropes essay page discusses the significance and spread of literary tropes in the historical press, as reporting and the exchange of information shaped the cultural perception of historical events. This page contains text that links to mentioned articles and incorporates entity descriptions like the article transcripts.
 
The goal of this project is to show the collected articles that influenced Scott O’Dell’s *Island of the Blue Dolphins*, and to teach users about the use and spread of texts and literary tropes in the United States and beyond from the nineteenth to the twenty-first centuries. The website also aims to show and explore the relationships of tropes across articles and articles within document groups.
 
Documentation included in the project code offers guidance for future stewards of the project to sustain the website and its data while understanding its functionality. Files in the site_documentation folder explain the building of the final metadata spreadsheet, the article and transcript views, and the website pages in more depth, including files used to build the site. The documentation also discusses important elements of the data itself. It is important to note that the data collection contains thirteen articles counted twice as they appear in two document groups, with 481 discrete articles but 494 articles counted and included within the website browse page. There is a many-to-many relationship between articles and document groups and between articles and tropes, as many tropes exist across the articles and some articles exist in multiple document groups, showing the complex network of literary ideas within the historical press. The ERD folder within the code contains diagrams that show relationships for the data associated with the Boston Atlas 1847 document group, the Cambria Freeman 1879 article as existing in two document groups, and the overall architecture of the site’s articles.


---

## Documentation Reading Guide

The files below cover the data model, metadata pipeline, and each major page of the site. They are listed in the recommended reading order.

**`metadata_building_explainer.md`**  
Start here if you want to understand the data. Describes the six-step notebook pipeline that transforms raw article folders and spreadsheets into the CollectionBuilder master CSV (`_data/cb_complete_metadata_images_tropes_reprints_transcripts.csv`). Covers image metadata, article metadata merging, trope and transcript extraction, reprint/document-group merging, CollectionBuilder objectid preparation, and the geographic arc data for maps. Many of the notebooks and spreadsheets produced for these steps are saved in the metadata_notebooks/ folder.

**`data_relationships_erd_explainer.md`**  
Explains the two many-to-many relationships at the heart of the archive: articles↔document groups and articles↔tropes. Lists and explains the 13 articles that belong to more than one document group (the source of the 481 vs. 494 row discrepancy), and documents the `multi_group_articles.csv` analysis notebook. Also covers how objectids are structured across compound_object parent rows and image child rows (494 compound rows + 3,934 image rows = 4,428 total objectids); which articles are vs. are not in reprint groups (362 vs. 119); source note coverage and why non-periodical sources lack source notes; and the five articles with document introductions and their significance to the literary tropes essay. Describes the three sets of ERD diagrams produced to visualize the data architecture.

**`article_page_image_gallery.md`**  
Covers the individual article page image gallery: how digitized scan pages are loaded from the master CSV, how the compound-object/image row structure drives the gallery, and how navigation and zoom work.

**`article_page_transcripts_tropes_entities.md`**  
Covers the transcript, trope highlighting, and entity panel features on article pages. Explains the TEI XML tagging pipeline, how trope spans are highlighted in rendered transcripts, and how the entity panel is populated from `_data/entities.json`.

**`browse_pages_publishers_locations_timeline.md`**  
Describes the Browse, Publishers, Locations, and Timeline pages. Explains how CollectionBuilder’s built-in faceting and map views are configured, and what metadata fields drive each view.

**`document_groups_page.md`**  
Describes the Document Groups page: how articles are organized into reprint networks using metadata, how the interactive arc maps are built with MapLibre GL and deck.gl to show the geographic movement of text over time, and how the `ReprintMap` class and lazy initialization work.

**`tropes_page.md`**  
Covers the Tropes page (`/subjects/`): the D3 v7 sparklines and bar charts showing trope frequency across articles and over time, the shared D3 loader pattern, and the data sources (`article_ids_only.csv` and `tropes.yml`).

**`literary_tropes_essay_page.md`**  
Covers the Literary Tropes essay page: the essay text ported from the original site, how named entities in the prose are linked to the entity panel, and how citations to archival documents open the floating document preview panel (`doc-panel.html`).

