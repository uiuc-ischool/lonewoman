---
title: About
layout: about
permalink: /about.html
credits: false
about-featured-image: assets/img/literary-tropes/LoneWoman_other_version.png
position: bottom
heading: About the Archive
sub-heading: 
padding: 6em
---

This digital archive collects, transcribes, annotates, and maps 481 nineteenth- and twentieth-century documents relevant to the story of the Lone Woman of San Nicolas Island. This Nicoleña was isolated alone on the most remote of the California Channel Islands between 1835–53, an event triggered by a massacre resulting from the international sea otter trade and then by the Spanish policy of *reducción*, or the in-gathering of Native tribes to Catholic Missions. The story of the Lone Woman, widely known in the nineteenth century, is perhaps best remembered today in the version Scott O'Dell fictionalized in his 1960 children's novel, *Island of the Blue Dolphins*. In O'Dell's Newbery-winning book, the Lone Woman is reimagined as the teenaged Karana.

The archive presents both a digital surrogate of each document and an annotated transcription. Each digital surrogate is a collection of images that include the full newspaper page followed by images of the specific article by sections in a click-through gallery. Each transcript text was tagged to encode key people, places, groups, and sailing vessels, and to highlight text that carried cultural tropes such as the Lone Woman figuring as a "girl Robinson Crusoe" and as "the last of her tribe." This encoding enables users to move between documents when key entities are referenced in another article. Articles can be viewed in the browse section as well as organized by publication, location, and date. The website also shows the frequency of select tropes appearing in articles over time in the tropes section. The document groups section reveals what articles contained text directly reprinted from earlier articles, establishing reprint families of original articles and later articles that are direct, truncated, or paraphrased reprints of the original text. The viewer is encouraged to explore the website and consider how information and stories laden with literary tropes and ideological perspectives are transferred across time and space through the global print culture system of the nineteenth and twentieth centuries. The digital archive seeks to facilitate research and teaching on the Lone Woman as both a historical figure and as a mythic representation of the American Indian, a reimagining central to US nation-building.

## Project History

This digital archive project was first completed in **2019** by a collaborative group at the **University of South Carolina**. A second initiative was completed in **2026** by a collaborative group at the **University of Illinois Urbana-Champaign**, transferring the article images and data to a new website platform in order to maintain and update the project's functionality. The project editor, Professor Sara L. Schwebel, led both of these projects.

The original **2019 project** was developed using the Django web framework with a MySQL database back-end. To transform the documents from their TEI-encoded state into a human-readable webpage, XSLT was used. The links generated through the XSLT transformation enable users to view documents in tandem with contextualizing maps and annotations. The georeferencing software MapTiler was used to add digital copies of historic maps of the California region to a Google Maps base engine.

The **2026 website sustaining project** was developed using the [CollectionBuilder](https://collectionbuilder.github.io/) open-source framework's CSV template, developed by the University of Idaho Library. CollectionBuilder relies on the Jekyll static site generator, which uses the Liquid templating language and Markdown files to generate HTML pages. Images from the original website build were transferred from a hard drive to a GitHub repository at the University of Illinois School of Information Science along with the CollectionBuilder template files. The new website build consisted of developing additional Markdown, HTML, and JavaScript files to create the website with interactive pages and informational panels. JSON files were also developed from previous TEI data to store and encode entity, trope, and location information for articles and transcripts. The document group page also includes animated reprint-network maps built with deck.gl arc and scatterplot functions over a MapLibre GL base using CARTO vector tiles. The JavaScript library D3 (Data-Driven Documents) was used for the trope trendline and bar chart visualizations. A large metadata table was produced to organize each image as connected to an article and transcript with associated data on publisher, date, location, tropes, document groups, and source and permissions for use of the article.

## Scope Notes

Documents in the Lone Woman and Last Indians Digital Archive were acquired between June 2013 and June 2015. Published and unpublished bibliographies on the Lone Woman were used as the starting point in searching for additional material. A list of key words appearing in these accounts (e.g., cormorant, lost woman, female Crusoe) was used to query national, state, institutional, and academic databases, including the Library of Congress's Chronicling America, the California Digital Newspaper Collection, the New York Times, and JSTOR. Relevant articles were identified, acquired, and transcribed. All internal references to other accounts of the Lone Woman were pursued. The search was constrained by the state of periodical digitization, including the accuracy of OCR (optical character recognition), at the time. Some twentieth-century accounts acquired could not be published due to copyright restrictions. Although more newspaper articles on the Lone Woman have likely been digitized since the first iteration of the project, no new articles or data have been added, and the 2026 project relies on the same article data as the 2019 construction. Undoubtedly, many more accounts of the Lone Woman were published and remain to be found by future researchers.

## Collection Statistics

The website consists of **481 distinct articles** across **368 unique publications**. However, 13 of these articles exist in different reprint document groups, incorporating text from two original sources. These 13 articles are counted twice, existing in each document group. As a result there are **494 digital surrogates** connected to trope and document group data that can be explored.

## Project Credits

### 2019 Project

**Editor:** Sara L. Schwebel, PhD

**Research and Development Team**

**Digital Collections Manager:** Rachel M. A. Manuszak  
**Lead Programmer:** Tyler Encke  
**Senior Research Consultants:** Susan L. Morris, Duncan Buell, PhD  
**Data Visualization:** Molly Carlson, Sydney Cowart, Aysegul Kramer  
**Design:** Bonnie Harris-Lowe, Aidan Zanders  
**Document Acquisition and Transcription:** Caroline Blount, Sydney Cowart, Hannah Davis, Georgia Froman, Paige Kuester, Carina Leaman, Alexis Michalos, Tyler Muehl  
**Document Encoding:** Paige Kuester, Ainsley McWaters, Tyler Muehl, Rose Steptoe  
**Maps:** Phillip J. Allan, Molly Carlson, Sydney Cowart  
**Programming:** Molly Carlson, Eric D. Gonzalez  
**Research and Writing:** Paige Kuester, Carina Leaman, Elizabeth A. Matthews, Tyler Muehl, Rose Steptoe  
**Scope Notes:** Paige Kuester

### 2026 Project

**Editor:** Sara L. Schwebel, PhD  
**Programming and Site Development:** Owen Monroe and Zoe LeBlanc, PhD

## Funding

Financial support for this project was generously provided by: two University of South Carolina Provost Humanities Grants, the University of South Carolina Department of English, the Center for Digital Humanities at the Magellan Scholar Program at the Channel Islands National Park, the Student Conservation Association/AmeriCorps internship program, the National Society of the Daughters of the American Revolution, a Carnegie-Whitney Grant from the American Library Association, Richard H. Dittman, and the Children's Literature Association.

---

*Banner image credit: detail from Louis Chorlis' 1817 illustration of an Aleut in a kayak off the coast of St. Paul (Alaska) with sea lions on the beach and a large sailing ship in background. Alaska State Library, Louis Chorlis Collection, 139-48.*
