---
title: Panduan GBIF Data
---

Complete Guide · English edition 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0001-02.png)

G E O L I B R E P L U G I N M O D U L E 

### Biodiversity Occurrence Data on Your Map with the GBIF Data Plugin 

A complete guide from installation to a citable result: every filter from area to IUCN Red List, points and density layers, the record popup, licences, GBIF policy and the derived-dataset DOI. 

1,500 bird (Aves) records around Bandung, West Java, fetched with GBIF Data in GeoLibre 

Defani Arman Alfitriansyah 

Plugin v1.1.0 · GeoLibre 3.0.0+ October 2026 · Guide licence CC BY-NC 4.0 

PLUGIN DEVELOPER · FORESTER 

Complete Guide 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0002-03.png)

#### Preface and Acknowledgements 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0002-05.png)

###### Defani Arman Alfitriansyah 

P L U G I N D E V E L O P E R · F O R E S T E R 

GBIF Data is my third plugin for GeoLibre. It grew out of a question I ask almost every week as a forester: which species have been recorded here? I wanted that answer inside my own map, next to my own boundaries and field data, without writing a script every time. 

Much of what I know about where species live comes from people I will never meet: herbarium curators, museum staff, field surveyors, citizen scientists, and the institutions that publish their records. Thank you to GBIF, its participant countries and nodes, and every data publisher and observer behind each point on the map. You made that knowledge open, consistent and free to reach. 

My sincere thanks to Dr. Qiusheng Wu and the GeoLibre project for an open platform and a plugin registry that welcomes independent contributors, and to everyone in the GeoLibre community who tried the plugin and gave feedback. 

I built the plugin to follow GBIF's rules, to credit the people who did the work, and to make citing their data the easy path rather than the forgotten one. I hope this guide does the same for you. 

With gratitude, 

###### Defani Arman Alfitriansyah 

PLUGIN DEVELOPER 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

02 / 55 

Complete Guide 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0003-02.png)

#### A Clarification about GBIF 

Before you start, please read this short statement about who made this plugin and this guide. 

###### I am an individual contributor 

I wrote the plugin and this guide as a private person: a forester and an independent open-source contributor. I am not GBIF staff, I do not speak for the GBIF Secretariat, a GBIF participant country, a GBIF node or any data publisher. 

###### Not affiliated, not endorsed 

GBIF Data is an independent project. It is not affiliated with, endorsed or sponsored by GBIF, nor by GeoLibre, MapLibre, IUCN or Google. The name "GBIF" is used only to say where the data comes from. No GBIF logo is used. 

###### The data belongs to its publishers 

Every record shown by the plugin is fetched live from GBIF's public API and stays the property of the institution that published it, under the licence that institution chose. 

###### No guarantee of data quality 

GBIF and its publishers do not guarantee that records are accurate or complete. Check the records against your purpose; you use them at your own risk. 

###### Official rules come from GBIF 

Where this guide summarises GBIF's data user agreement, terms of use or citation guidelines, the original documents on gbif.org always prevail. This guide is not legal advice. 

In short: the plugin code is mine (MIT License); the data, photos and taxonomy belong to GBIF's publishers and creators and keep their own licences (Chapter 6). 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

03 / 55 

Complete Guide 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0004-03.png)

#### Terms of Reference (TOR) of This Module 

This module is a self-study and training guide. The terms below define its purpose, scope and expected results. 

###### Background 

Biodiversity occurrence data are needed in forestry, conservation and spatial planning, but are often collected by hand from websites. GBIF Data brings GBIF records straight into GeoLibre with licences and citation built in. 

###### Scope 

All features of GBIF Data v1.1.0: installation, live counter, the six filter steps (incl. IUCN Red List and data licence), points and density output, results, popup, attribute table, licensing, GBIF policy and DOI citation. 

###### Objective 

Participants can find, filter, map, interpret and correctly cite GBIF occurrence records inside GeoLibre. 

###### Learning outcomes 

(1) install and open the plugin, (2) build a filtered query, (3) add points or density layers, (4) read a record and its licences, (5) prepare a derived-dataset or download DOI. 

###### Target users 

Foresters, ecologists, conservation and planning staff, lecturers, students and researchers. No programming needed. 

###### Method and duration 

Guided practice with real data from West Java and Java, Indonesia. About 3 to 4 hours, or one training day with exercises. 

###### Prerequisites 

Basic GeoLibre use (layers, map navigation), an internet connection, GeoLibre 3.0.0 or newer with the MapLibre (2D/globe) renderer. 

###### Outputs 

A GBIF layer in a GeoLibre project, a dataset list (CSV) and a correct citation for a report, paper or map. 

|Session|Topic|Chapters|Time|
|---|---|---|---|
|1|GBIF, the plugin, installation and the panel|1–2|30 min|
|2|The six filter steps, IUCN Red List and data licence|3|60 min|
|3|Fetching points and density; reading records and the attribute table|4–5|60 min|
|4|Licences, citation and the derived-dataset DOI|6|45 min|
|5|Practice with the recipes; checklist before publishing|7|45 min|

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

04 / 55 

Complete Guide 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0005-02.png)

#### Contents 

|01|GBIF and the Plugin<br>What GBIF is, what GBIF Data does, who it is for, and how it is built inside GeoLibre.|pp. 6–10|
|---|---|---|
|02|Installation and the Panel<br>Three ways to install, how to open the panel, its parts, and how to read the live counter.|pp. 11–16|
|03|The Six Filter Steps<br>Every control in steps 01 to 06: area, taxon, record type, time, quality including the IUCN Red List and data<br>licence, and more filters.|pp. 17–26|
|04|Fetching Records onto the Map<br>Choosing points, density or both, the Max records limit, the fetch progress, the results card, and three worked<br>examples.|pp. 27–33|
|05|Records, Popups, IUCN and the Layer<br>Reading a single record and its photo, a threatened-species case study for Java, and working with the attribute<br>table.|pp. 34–40|
|06|Licences, Citation and GBIF Policy<br>Four kinds of licence, what you may do with the data, the Cite this data block, two ways to get a DOI, and how<br>the plugin follows GBIF's rules.|pp. 41–46|
|07|Recipes, Troubleshooting and Closing<br>Ready-made settings for common tasks, fixes for common problems, theming, the licence of this guide, and<br>references.|pp. 47–55|

Conventions: button and menu names are in bold; API parameters and attribute columns in `code` ; scientific names in italics; orange numbered discs on screenshots match the numbered lists beside them. Screenshots were taken on 29 October 2026 in GeoLibre on the web; record counts change daily. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

05 / 55 

Chapter 1 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0006-02.png)

# 01 GBIF and the Plugin 

What GBIF is, what GBIF Data does, who it is for, and how it is built inside GeoLibre. 

About GBIF What the plugin does Use cases Architecture From filters to requests 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

06 / 55 

Chapter 1 · GBIF and the Plugin 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0007-03.png)

#### What Is GBIF? 

The Global Biodiversity Information Facility (GBIF) is an international network and data infrastructure, funded by governments, that gives anyone free and open access to data about all types of life on Earth. 

###### An occurrence record 

Evidence that a species (or other taxon) was found at a place and time: a field observation, a museum or herbarium specimen, a camera-trap image, a sound recording, an eDNA sample. 

###### Open, with obligations 

Each dataset carries CC0 1.0, CC BY 4.0 or CC BYNC 4.0. GBIF asks every user to cite the data, ideally with a DOI. 

###### Public APIs 

###### Who publishes 

Thousands of institutions: museums, herbaria, universities, government agencies, NGOs and citizen-science platforms such as iNaturalist and eBird. 

###### A common standard 

Records are shared in the Darwin Core standard and matched to the GBIF Backbone Taxonomy, so data from very different sources can be searched together. 

GBIF offers web APIs for occurrence search, species, maps and images. The plugin uses these APIs only. 

###### Billions of records 

GBIF indexes billions of occurrence records from tens of thousands of datasets, and the number grows every day. 

GBIF describes its data as free for all but not free of obligations. Chapter 6 explains what that means in practice and how the plugin helps. 

##### 19.6K 

bird records around 

Bandung 

##### 4,003 

threatened-species records 

in Java 

##### 5,737 

tiger records worldwide 

##### 91 

threatened species in Java 

Counts from the examples in this guide, GBIF.org, 29 October 2026. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

07 / 55 

Chapter 1 · GBIF and the Plugin 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0008-03.png)

#### What the Plugin Does and Who It Is For 

GBIF Data connects GeoLibre to GBIF. You choose an area, a taxon and filters, and the records arrive as a normal GeoLibre layer, with licences and citation tools attached. 

|Part|What it does|
|---|---|
|Live counter|Shows how many GBIF records match your filters, while you change them.|
|Six filter steps|Area, Taxon, Record type, Time, Quality (photos, issues, uncertainty, IUCN, licence) and More<br>filters.|
|Points output|Up to 5,000 records as a GeoJSON layer that is saved with the project.|
|Density<br>output|GBIF hexagon tiles summarisingeverymatching record, at any scale.|
|Results card|Records on the map, with photo, species count, the five most recorded taxa.|
|Record popup|Photo, date, recorder, family, place, uncertainty, IUCN badge, dataset and licence.|
|Cite this data|Licence summary, citation text, dataset list (CSV) for a derived-dataset DOI, link to a GBIF.org<br>download.|

###### Typical uses 

Check species records in a concession, protected area or village; map threatened (IUCN CR/EN/VU) species near a planned activity; see the global range of a species; pull herbarium specimens of a genus before a survey; prepare cited data for a report. 

A bird record opened from the map: photo, details, IUCN badge, dataset and licence 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

08 / 55 

Chapter 1 · GBIF and the Plugin 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0009-02.png)

#### Architecture 

The plugin is one self-contained JavaScript module plus a stylesheet. It bundles no libraries: the map engine belongs to GeoLibre and the data to GBIF. 

###### GeoLibre host (MIT) 

Plugin API: `addMapControl` · `registerRightPanel` · `addGeoJsonLayer` · `addTileLayer` · `getViewBounds` · `getLayerFeatures` · `fitBounds` ; the MapLibre GL JS map (BSD-3-Clause). 

###### Panel UI 

Leaf map control, counter, six steps, output, results. 

###### Query builder 

###### Network layer 

One filter object drives the counter, Timeouts, cancel, back-off on HTTP points, tiles and the GBIF.org link. 429, paging. 

###### Feature mapper 

Turns a GBIF record into a feature and keeps ownership fields. 

Popup Record card with photo from GBIF's image cache. 

Citation block Licence counts, citation text, dataset CSV. 

###### GBIF API v1 

`occurrence/search` , `species/suggest` , `species/match` , occurrence image cache. 

GBIF Maps API v2 

`adhoc` density tiles, hexagon bins, EPSG:3857. 

GBIF.org website (opened by you) 

Derived datasets and downloads, which give the DOI you cite. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

09 / 55 

Chapter 1 · GBIF and the Plugin 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0010-03.png)

#### From Filters to API Requests 

Everything you set in the panel becomes parameters of one GBIF request. Because one filter object drives every request, the counter, the points, the density tiles and the GBIF.org link always describe the same set of records. 

|Panel control|GBIF API parameter|
|---|---|
|01 Area: Map view or Layer|`decimalLatitude=south,north`·<br>`decimalLongitude=west,east`|
|01 Area: Country|`country`(ISO 3166-1 alpha-2, e.g. ID)|
|02 Taxon and major groups|`taxonKey`(repeated=OR)|
|03 Record type|`basisOfRecord`(repeated)|
|04 Time|`year=from,to`|
|05 Photos only · Drop issues · Presence<br>only|`mediaType=StillImage`·<br>`hasGeospatialIssue=false`·<br>`occurrenceStatus=PRESENT`|
|05 Coordinate uncertainty|`coordinateUncertaintyInMeters=0,max`|
|05 IUCN Red List · Data licence|`iucnRedListCategory`·<br>`license`(repeated)|
|06 Recorded by · Dataset · Institution ·<br>Keyword|`recordedBy`·<br>`datasetKey`·<br>`institutionCode`·<br>`q`|
|Always added|`hasCoordinate=true`|

```
// example: birds in the map view, records with photos, since 2000
https://api.gbif.org/v1/occurrence/search?
```

```
taxonKey=212&decimalLatitude=-7.26,-6.34&decimalLongitude=107.28,108.02
```

```
  &year=2000,2026&mediaType=StillImage&hasGeospatialIssue=false&hasCoordinate=true&limit=300
```

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

10 / 55 

Chapter 2 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0011-02.png)

# 02 Installation and the Panel 

Three ways to install, how to open the panel, its parts, and how to read the live counter. 

Install from a link Manage Plugins Activate Panel anatomy Live counter 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

11 / 55 

Chapter 2 · Installation and the Panel 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0012-02.png)

#### Installing from the Catalog Link 

The quickest way on GeoLibre for the web: open the plugin's catalog page, plugins.geolibre.app/catalog/geolibre-gbif-data, and click Open in GeoLibre. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0012-05.png)

<!-- Start of picture text -->
1<br>2<br>3<br><!-- End of picture text -->

The install dialog that GeoLibre shows for a registry link 

Check the plugin card: name GBIF Data v1.1.0, author, description, the source repository and the 1 manifest URL on plugins.geolibre.app. 

Read the warning: plugins run with the same privileges as GeoLibre, so only load plugins from 2 sources you trust. 

Click Trust and load. The plugin is installed and activated; a leaf button appears among the map 3 controls. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

12 / 55 

Chapter 2 · Installation and the Panel 

GBIF Data 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0013-02.png)

a GeoLibre plugin · v1.1.0 

#### Installing from Manage Plugins 

In any GeoLibre, including the desktop app, use the built-in plugin manager. Recent GeoLibre releases check the downloaded code against the bundle SHA-256 published in the registry before running it. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0013-06.png)

<!-- Start of picture text -->
1<br>3<br>2<br>Settings or Plugins → Manage plugins…, search "GBIF"<br><!-- End of picture text -->

1 

Open Plugins **→** Installed **→** Manage plugins… (or Settings **→** Manage Plugins). 

Type GBIF in the search box. The card shows version, description, author and the categories Data 2 and Ecology. 

3 Click Install. Once installed the card reads Installed and offers a bin icon to remove it. 

Offline or behind a firewall? Download `geolibre-gbif-data-1.1.0.zip` from the GitHub Releases page and use Install from file in the same dialog. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

13 / 55 

Chapter 2 · Installation and the Panel 

GBIF Data 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0014-02.png)

a GeoLibre plugin · v1.1.0 

#### Activating and Opening the Panel 

An installed plugin can be switched on and off from the Plugins menu. When it is active, a leaf button opens the GBIF Data panel on the right. 

Plugins **→** Installed **→** GBIF Data. A tick shows 1 it is active. GeoLibre may ask again after a 

restart. 

Click the leaf button in the map controls (top right of the map). 

2 

The panel opens in the right sidebar. The leaf also appears on the right-hand rail as GBIF 3 DATA, so you can switch back from Style or Comments. 

GBIF Data needs the MapLibre renderer (2D map or globe). It reads clicks from the MapLibre map, which does not exist on the Cesium 3D globe. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0014-12.png)

<!-- Start of picture text -->
Plugins → Installed → GBIF Data ✓<br>3<br>2<br><!-- End of picture text -->

Leaf button and the GBIF DATA rail tab 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

14 / 55 

Chapter 2 · Installation and the Panel 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0015-02.png)

#### Panel Anatomy 

The panel has a fixed header and counter at the top, six folding steps in the middle, and the output and Fetch button at the bottom. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0015-05.png)

<!-- Start of picture text -->
1<br>7<br>2<br>3<br>4<br>5<br>6<br><!-- End of picture text -->

###### 1 Header and Reset 

Panel title, dock and close buttons; Reset clears every filter back to the defaults. 

###### 2 Live counter · 3 The six steps 

Records that match now; steps 01 to 06 each fold open and show a short summary on the right. 

###### 4 Leaf control · 5 Fetch button · 6 Credit · 7 Rail tab 

Opens the panel; runs the query; data credit and disclaimer; switches back to the panel. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

15 / 55 

Chapter 2 · Installation and the Panel 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0016-01.png)

###### GBIF Data 

a GeoLibre plugin · v1.1.0 

#### The Live Counter 

The grey box under the header tells you, before you fetch anything, how many records in GBIF match your filters. It updates about 0.7 seconds after you stop changing a filter and follows the map while the area is Map view. 

###### Rounded numbers 

Large totals are shortened, for example 52.4K or 1.7M. Hover the number to see the exact figure. 

A number: records that match now 

###### One small request 

0 records: the filters are too narrow 

The counter asks GBIF with `limit=0` , so it only returns a count. Requests are debounced, one per change. 

###### When it shows ! 

— : the filters are incomplete (World with no narrowing filter) 

No network, GBIF down, or HTTP 429 (too many requests). The next change tries again. 

###### Use it to plan 

! : GBIF cannot be reached, or asks to slow down 

If the count is far above 5,000, narrow the filters or use the Density output or a GBIF.org download. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

16 / 55 

Chapter 3 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0017-02.png)

# 03 

## The Six Filter Steps 

Every control in steps 01 to 06: area, taxon, record type, time, quality including the IUCN Red List and data licence, and more filters. 

01 Area 02 Taxon 03 Record type 04 Time 05 Quality IUCN Red List Data licence 06 More filters 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

17 / 55 

Chapter 3 · The Six Filter Steps 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0018-02.png)

#### Step 01 · Area 

The area decides where GBIF searches. Four choices are offered as a segmented switch. 

###### Map view (default) 

The bounding box of what you see on the map. The counter follows the map as you pan and zoom. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0018-07.png)

<!-- Start of picture text -->
Map view<br><!-- End of picture text -->

###### Layer 

The bounding box of a vector layer in your project (its extent, not its exact shape). Raster and tile layers cannot be used. 

###### Country 

Records GBIF assigns to that country (ISO 3166-1 code), wherever the map is. With Country or World the map zooms to the new points. 

Country: Indonesia (ID) 

###### World 

No area limit. It needs a narrowing filter (a taxon, dataset, recorder, institution or keyword) so a query is never "all of GBIF". 

Layer: pick a vector layer 

For a concession or village boundary, use Layer and then clip the points to the exact polygon with GeoLibre's processing tools. 

World 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

18 / 55 

Chapter 3 · The Six Filter Steps 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0019-02.png)

#### Step 02 · Taxon: Searching the GBIF Backbone 

Type at least two letters of a scientific name. Suggestions come from the GBIF Backbone Taxonomy with their rank and kingdom. 

1 Type, for example, Pycnonotus aur. 

Use the arrow keys and Enter, or click a 2 suggestion. Pressing Enter without picking asks GBIF for its best match. 

The chosen taxon becomes a token, for 3 example SPE Pycnonotusaurigaster×. Click × to remove it. 

Add more taxa if needed. Everything selected 4 is combined with OR. 

Suggestions with rank and kingdom 

Picking a species includes its subspecies; picking a genus includes all its species. Synonyms are resolved by the GBIF backbone. 

The species token and the Aves group, both selected 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

19 / 55 

Chapter 3 · The Six Filter Steps 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0020-03.png)

#### Step 02 · Taxon: Major Groups 

Twelve one-click buttons select whole kingdoms or classes. They combine with searched taxa using OR: Panthera tigris + Aves means tigers or birds. With nothing selected the search covers all life. 

|Button|Rank|Covers|
|---|---|---|
|Animalia|kingdom|all animals|
|Plantae|kingdom|all plants|
|Fungi|kingdom|fungi, incl. lichens|
|Aves|class|birds|
|Mammalia|class|mammals|
|Reptilia|class|reptiles|
|Amphibia|class|frogs, salamanders, caecilians|
|Actinopterygii|class|ray-finned fishes|
|Insecta|class|insects|
|Arachnida|class|spiders, scorpions, mites|
|Mollusca|phylum|snails, bivalves, squid|
|Chromista|kingdom|brown algae, diatoms and kin|

Step 02 with search box and major groups 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

20 / 55 

Chapter 3 · The Six Filter Steps 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0021-03.png)

#### Step 03 · Record Type (Basis of Record) 

GBIF's basis of record tells you how a record was made. Nothing selected means every type; several selected are combined with OR. 

|Type|Typical source|
|---|---|
|Human<br>observation|field surveys, citizen science<br>(iNaturalist, eBird)|
|Preserved<br>specimen|herbaria, museum collections|
|Machine<br>observation|camera traps, acoustic sensors|
|Material sample|soil, water, eDNA samples|
|Living specimen|botanic gardens, zoos|
|Fossil specimen|palaeontological collections|
|Observation|generic observation, method not stated|
|Material citation|records cited from literature|
|Occurrence|generic occurrence, type unknown|

Human observation and Preserved specimen selected 

For a herbarium check before a field survey, pick Preserved specimen. For recent presence, pick Human and Machine observation. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

21 / 55 

Chapter 3 · The Six Filter Steps 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0022-02.png)

#### Step 04 · Time 

Limit records by the year they were made. All years is the default. 

###### All years 

No time limit. 

###### Year range: From, To 

Type the years. Leave one end empty for an open range, for example only From 2015. 

All years 

###### Presets 

Last 5 yr, Last 10 yr, Since 2000, This year fill the range in one click. 

###### Step summary 

The header shows the range, for example 2000– 2026, and a removable tag appears above Add to map. 

Year range with the Since 2000 preset 

Old specimens are valuable for history and range change, but many lack precise coordinates. Combine an old range with Coordinate uncertainty carefully. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

22 / 55 

Chapter 3 · The Six Filter Steps 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0023-03.png)

#### Step 05 · Quality: Switches and Uncertainty 

Quality filters remove records that are unlikely to suit spatial work. Two switches are on by default. 

###### Only records with photos (off) 

`mediaType=StillImage` : only records that carry at least one image. 

###### Drop geospatial issues (on) 

Skips records that GBIF flags as badly placed, for example coordinates at the country centroid or swapped latitude and longitude. 

###### Presence records only (on) 

Leaves out recorded absences (a survey that looked and did not find the taxon). 

###### Coordinate uncertainty 

Any, ≤ 100 m, ≤ 1 km or ≤ 10 km. A limit also drops records that do not state their uncertainty: that is how GBIF's range filter works. 

A popup that says Uncertainty 31,337 m usually means the location was deliberately generalised, which iNaturalist does for sensitive species or on the observer's request. Use **≤** 1 km to leave such records out of fine-scale maps. 

Step 05 with photos, ≤ 1 km, IUCN CR/EN/VU and CC BY selected 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

23 / 55 

Chapter 3 · The Six Filter Steps 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0024-02.png)

###### GBIF Data 

#### The IUCN Red List Filter 

The IUCN Red List of Threatened Species assesses the global extinction risk of species. GBIF attaches the global IUCN category to each record through the taxon, and the plugin lets you filter by it in the official IUCN colours. 

||Category|Meaning(IUCN2012,v3.1)||
|---|---|---|---|
|CR|Critically<br>Endangered|extremely high risk of<br>extinction in the wild|None selected|
|EN|Endangered|very high risk of extinction in<br>the wild|CRENandVUselected|
|VU|Vulnerable|high risk of extinction in the<br>wild|,|
|NT|Near Threatened|close to qualifying for a<br>threatened category||
|LC|Least Concern|widespread and abundant||
|DD|Data Deficient|not enough information to<br>assess|The same colours as a badge in the popup|

###### Threatened species 

CR, EN and VU together are the threatened categories. Select all three for a threatened-species map. 

###### Several buttons 

Are combined with OR. A pressed button is filled with its colour; the step summary shows IUCN×3. 

###### Not offered 

EX, EW (extinct) and NE (not evaluated) are not filter buttons. 

The category is the global IUCN assessment. National protection lists (for example Indonesia's protected species regulation) are separate and are not used by this filter; check them for permits and reports. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

24 / 55 

Chapter 3 · The Six Filter Steps 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0025-03.png)

#### Data Licence Filter 

Below the IUCN buttons, Data licence keeps only records published under the licences you pick. Each publisher chooses one of three Creative Commons licences for the whole dataset. 

|Button|Licence|You must|
|---|---|---|
|CC0|CC0 1.0, public<br>domain dedication|nothing legally; GBIF<br>still asks you to cite|
|CC BY|CC BY 4.0, attribution|credit the source;<br>commercial use allowed|
|CC BY-<br>NC|CC BY-NC 4.0,<br>attribution, non-<br>commercial|credit the source and<br>not use it commercially|

CC BY selected: only CC BY 4.0 records 

###### None selected 

Every licence (the default). 

Commercial work 

Select CC0 and CC BY to leave CC BY-NC records out, for example for paid consulting. 

###### After fetching 

The results card still counts records per licence and warns when some are non-commercial (Chapter 6). 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

25 / 55 

Chapter 3 · The Six Filter Steps 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0026-02.png)

#### Step 06 · More Filters, Tags and Reset 

The last step narrows by people, datasets, institutions or text. Every active filter of every step also appears as a removable tag above Add to map. 

|Field|Example|Note|
|---|---|---|
|Recorded|Ani|names as written in the|
|by|Rahmawati, J.<br>Smith|records; comma-separated|
|Dataset key|50c9509d-<br>22c7-…|UUID from a<br>gbif.org/dataset/… page|
|Institution|MZB, LIPI,|as published by the|
|code|NHMUK|institution|
|Keyword|mangrove|GBIF full-text search<br>across the record|

Institution code and keyword filled in 

Tags of active filters; click × on a tag to remove that filter 

Reset in the header clears every filter at once. Folded steps keep a summary on the right, such as 1 selected, 2000–2026 or Photo + IUCN×3 + Precise + Licence, so you can check the query without opening them. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

26 / 55 

Chapter 4 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0027-02.png)

# 04 Fetching Records onto the Map 

Choosing points, density or both, the Max records limit, the fetch progress, the results card, and three worked examples. 

Points · Density · Both Max records Progress and errors Results card Example: birds of Bandung Density Worldwide range 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

27 / 55 

Chapter 4 · Fetching Records onto the Map 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0028-03.png)

#### Output and Max Records 

At the bottom of the panel, Add to map chooses what the Fetch button produces, and Max records limits how many points are downloaded. 

|Output|What you get|Good for|
|---|---|---|
|Points|A GeoJSON layer with up to Max records records (default 500,|inspecting, attribute table, export,|
||maximum 5,000)|analysis|
|Density|A tile layer of GBIF hexagons summarisingeverymatching record|full distribution, very large queries|
|Both|Both layers at once|points on top of their wider context|

Points selected, Max records 1500 

###### Max records 

Drag the slider (50 to 5,000 in steps of 50) or type a number. The Fetch button repeats it: Fetch 1,500 records; with Density it reads Add density layer. 

###### Why 5,000? 

GBIF asks API users to keep requests reasonable and to use a GBIF.org download for large extractions. For more records, see Option B in Chapter 6. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

28 / 55 

Chapter 4 · Fetching Records onto the Map 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0029-02.png)

#### Fetching: Progress, Cancel and Errors 

Records are fetched in pages of up to 300, about 0.2 seconds apart. A progress bar shows the count and the button turns into Cancel. 

###### Progress 

For example 900 / 1,500 records. Nothing is added to the map until the fetch finishes. 

###### Cancel 

Stops at once; the panel reports Cancelled - nothing was added. 

Fetching in progress 

###### HTTP 429 

If GBIF asks to slow down, the plugin waits 3 s, then 8 s, then stops with a message that points to a GBIF.org download. 

After Cancel 

Counter while GBIF cannot be reached 

###### Network error 

Could not fetch records: Failed to fetch means GBIF could not be reached. Wait a moment and try again. 

###### Timeouts 

30 s per page (10 to 15 s for suggestions and the counter), so the panel never hangs. 

These polite limits are part of GBIF's fair-use rules. Please do not raise them in a fork of the plugin. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

29 / 55 

Chapter 4 · Fetching Records onto the Map 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0030-02.png)

#### The Results Card 

When the fetch finishes, a results card summarises what arrived. This is the card for the first worked example, birds around Bandung. 

###### Stats 

1,500 on map · 1,452 with photo · 164 species · 19.6K in GBIF (all that match). 

###### Most recorded 

The five most frequent taxa, with bars: here Pycnonotus aurigaster (sooty-headed bulbul, 259), Spilopelia chinensis, Psilopogon haemacephalus, Passer montanus and Lonchura leucogastroides. 

###### Notes 

The new layer's name, and how many more records match (here 18,100): raise Max records, narrow the filters, or use a download. 

###### Cite this data 

Licence chips, warnings and citation tools, explained in Chapter 6. 

Results card after fetching 1,500 Aves records 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

30 / 55 

Chapter 4 · Fetching Records onto the Map 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0031-02.png)

#### Example 1 · Birds around Bandung 

Area Map view over Bandung and Purwakarta, West Java · Taxon Aves · default quality · Points, 1,500 records. The layer GBIF – Aves (1,500) appears in the Layers panel like any other vector layer. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0031-05.png)

<!-- Start of picture text -->
1<br>2<br>3<br>4<br><!-- End of picture text -->

###### 1 The layer 

Named after the taxon and count; it is saved with the project, so it is still there when you reopen it. 

###### 2 The points · 3 Most recorded · 4 Stats 

Records cluster where people look: Bandung city, parks and the volcano slopes. Absence of points is not absence of birds. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

31 / 55 

Chapter 4 · Fetching Records onto the Map 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0032-03.png)

#### Density: Every Matching Record 

Density adds GBIF's own hexagon tiles. Unlike points, they summarise every record that matches (here 17.2K birds), not only the ones you fetched, and they redraw at every zoom. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0032-06.png)

###### Colours 

Yellow to red hexagons: more records in a cell means a warmer colour. 

###### Metadata 

The density layer stores its query, GBIF.org search link and access date in the layer metadata. 

Results card for a density layer 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

32 / 55 

Chapter 4 · Fetching Records onto the Map 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0033-02.png)

#### Example 2 · A Species' Worldwide Range 

Area World · Taxon Panthera tigris (tiger) · Output Both · 1,000 records. The density hexagons show all 5,737 matching records across Asia; green points show the 1,000 fetched ones. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0033-05.png)

World searches always need a narrowing filter. When a query matches many thousands of records, use Density for the picture and a GBIF.org download for the data. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

33 / 55 

Chapter 5 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0034-02.png)

# 05 Records, Popups, IUCN and the Layer 

Reading a single record and its photo, a threatened-species case study for Java, and working with the attribute table. 

Record popup Photo credits Case study: threatened species Attribute table Columns 

Layer tools 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

34 / 55 

Chapter 5 · Records, Popups, IUCN and the Layer 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0035-02.png)

#### The Record Popup 

Click any point (with no Identify, selection or editing tool active) to open a record card. It stays inside the map: it slides sideways at the edges and scrolls if it is too tall. 

###### 1 Header 

Basis of record and the name (species or the identified taxon). 

###### 2 Photo 

A resized copy from GBIF's occurrence image cache. Click it for the full-size original. 

###### 3 Photo credit 

© creator · licence, the licence linked to its legal text. 

###### 4 Rows 

Date, Recorded by, Family, Place, coordinate Uncertainty. 

###### 5 IUCN badge 

The category in IUCN colours. 

###### 6 Dataset · Licence 

Dataset linked to its GBIF page (with its own citation) and the record licence. 

Open record on GBIF.org 

The record page with its suggested citation. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0035-19.png)

<!-- Start of picture text -->
1<br>2<br>3<br>4<br>5<br>6<br><!-- End of picture text -->

Popup of a sooty-headed bulbul record 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

35 / 55 

Chapter 5 · Records, Popups, IUCN and the Layer 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0036-02.png)

#### Photos and Their Credits 

Photos belong to their creators and carry their own licence, often stricter than the record's. The popup always shows the creator and licence under the photo. 

Popup in the desktop app; photo © jj, CC BY-NC (via iNaturalist and GBIF) 

###### Reusing a photo 

Check its licence first and credit its creator. Typical values are CC0, CC BY, CC BY-NC, CC BY-SA, CC BY-NC-ND or all rights reserved. 

###### Missing photo 

The image is not yet in GBIF's cache, or the publisher's server is down; the popup then simply hides the photo row. 

###### Display only 

Showing a cached thumbnail does not change the photo's licence. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

36 / 55 

Chapter 5 · Records, Popups, IUCN and the Layer 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0037-03.png)

#### Case Study · Threatened Species of Java 

Area Map view over Java · Taxon all life · Quality IUCN CR, EN, VU · Points, 1,000 of 4,003 matching records, from 91 species in 7 datasets. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0037-06.png)

|Most recorded|IUCN|Records|
|---|---|---|
|Macaca fascicularis(long-tailed<br>macaque)|EN|255|
|Acridotheres javanicus(Javan<br>myna)|VU|113|
|Nisaetus bartelsi(Javan hawk-<br>eagle)|EN|58|
|Coffea arabica(arabica coffee)|EN|57|
|Trachypithecus auratus(Javan<br>langur)|VU|47|

Read with care Wild arabica coffee is globally Endangered, yet most Javan records are cultivated plants. Check the basis of record and the remarks. 

Planning use Overlay a planned activity, then raise Max records or download the full 4,003 records. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

37 / 55 

Chapter 5 · Records, Popups, IUCN and the Layer 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0038-02.png)

#### Reading a Critically Endangered Record 

A click on one of the points shows Globba maculata, a ginger (Zingiberaceae) assessed as Critically Endangered, observed in Central Java. 

###### IUCN CR 

The red badge comes from the global IUCN category that GBIF attaches to the taxon. 

###### Uncertainty 31,331 m 

The location is generalised by about 31 km, as iNaturalist does for sensitive species. Do not use such a point for site-level decisions. 

###### Dataset and licence 

iNaturalist research-grade observations; record and photo CC BY-NC. 

###### What to do next 

Open the record on GBIF.org to see the full data and citation, and contact the publisher if you need precise locations for conservation work. 

Sensitive species are often hidden or blurred on purpose to protect them from collection. The plugin never tries to recover withheld coordinates. 

Popup of a CR record; photo © Galih Alamsyah, CC BY-NC 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

38 / 55 

Chapter 5 · Records, Popups, IUCN and the Layer 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0039-02.png)

#### The Attribute Table and Columns 

The points layer is an ordinary GeoLibre GeoJSON layer. Open its ⋯ menu → Open attribute table to sort, search, select and export the records. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0039-05.png)

<!-- Start of picture text -->
Attribute table of GBIF – all taxa (1,000)<br><!-- End of picture text -->

|||Attr|ibute table of GBIF–all taxa(1,000|)||
|---|---|---|---|---|---|
|Group|Columns|||||
|Identity|`gbifKey`<br>`gbif`|`Url`<br>`occurr`|`enceID`|||
|Taxon|`scientificNam`|`e`<br>`species`|`taxonRank`<br>`kingdom`…<br>`genus`|`taxonKey`|`speciesKey`|
|Event and|`basisOfRecord`|`eventDate`|`year`<br>`recordedBy`<br>`country`|`countryCode`|`stateProvince`|
|place|`uncertaintyM`|||||
|Status|`iucnRedListCa`|`tegory`<br>`occu`|`rrenceStatus`|||
|Ownership|`datasetName`|`datasetKey`|`datasetUrl`<br>`institutionCode`|`publisher`|`rightsHolder`<br>`license`|
||`licenseLabel`|`accessed`||||
|Photo|`imageCount`<br>`i`|`mage`<br>`image`|`Creator`<br>`imageLicense`|||

Keep the ownership columns whenever you share or export the layer: the GBIF data user agreement requires the identifier of ownership to travel with every record. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

39 / 55 

Chapter 5 · Records, Popups, IUCN and the Layer 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0040-03.png)

#### Working with the Layer 

Because the result is a normal layer, all of GeoLibre's tools apply. The layer's ⋯ menu is the starting point. 

###### Open Style panel 

Colour points by `iucnRedListCategory` , `family` or `basisOfRecord` . 

###### Select by expression 

For example `uncertaintyM /= 1000` or `year /= 2015` . 

###### Select by location 

Keep only records inside a protected area or concession polygon. 

###### Quick analysis 

Counts and charts per column. 

###### Export 

GeoJSON, CSV, GeoPackage and other formats; keep the ownership columns. 

###### Layer order and opacity 

Move the points above a density layer so they stay visible; density defaults to 0.85 opacity. 

Save the project to keep the layers. Before you publish a map made from them, follow Chapter 6. 

The layer ⋯ menu 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

40 / 55 

Chapter 6 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0041-02.png)

# 06 

## Licences, Citation and GBIF Policy 

Four kinds of licence, what you may do with the data, the Cite this data block, two ways to get a DOI, and how the plugin follows GBIF's rules. 

Four licences What you may do Cite this data Derived dataset DOI Download DOI GBIF compliance 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

41 / 55 

Chapter 6 · Licences, Citation and GBIF Policy 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0042-02.png)

#### Four Things, Four Licences 

Four different things meet in this plugin, and each has its own licence. The MIT License covers only the plugin code. 

|What|Licen|ce||Who sets it|
|---|---|---|---|---|
|Plugin code (index.js, style.css, plugin.json,<br>documentation)|MITi|© 2026 Defani A i|rman Alfitriansyah|the author|
|Icons inside the plugin (Material Symbols)|Apac|he-2.0||Google|
|Occurrence records|CC0 1|.0, CC BY 4.0 o|r CC BY-NC 4.0|each dataset's<br>publisher|
|Photos and other media|the cr  t|eator's choice, t|often stricter|each creator or rights<br>holder|
|GBIF Backbone Taxonomy|CC BY|4.0 · doi.org/1|0.15468/39omei|GBIF Secretariat|
|Density tiles|follow<br>summ|the licences o<br>arise|f the records they|GBIF and publishers|
|GeoLibre · MapLibre GL JS · basemaps|MIT ·|BSD-3-Clause|· their own terms|provided by the host|
|You want to…|CC0data|CC BY data|CC BY-NC data|Photos|
|Use it in a study or government report|✓cite|✓cite|✓cite|check licence, credit|
|Publish a map in a paper|✓cite|✓cite|✓cite|check licence|
|Use it in paid consulting work|✓cite|✓cite|ask the publisher|check licence|
|Sell the data or a product built on it|✓cite|✓cite|✗|usually✗|

A guide, not legal advice: the licence texts and the publisher's terms decide. If you are unsure whether a use is commercial, GBIF asks you to act in good faith and contact the publisher. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

42 / 55 

Chapter 6 · Licences, Citation and GBIF Policy 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0043-02.png)

#### The Cite This Data Block 

Search results have no DOI of their own. The Cite this data block in the results card prepares everything you need to get one. 

Licence chips 

Records per licence, e.g. CC BY-NC · 1,353, CC BY · 

147, with a warning when some are non-commercial. 

###### Dataset count 

1,500 records from 4 datasets: the datasets you must credit. 

Copy citation 

Copies a ready citation text (below). The button briefly reads Copied ✓. 

Save dataset list (CSV) 

Cite this data 

Saves `gbif-datasets-DATE.csv` : one `datasetKey,count` 

per line, no header, the format of GBIF's derived-dataset form. 

###### Links 

Register a derived dataset (DOI), Open this search on GBIF.org, GBIF citation guidelines. 

```
// text placed on the clipboard by Copy citation (shortened)
```

```
GBIF.org (29 October 2026) GBIF Occurrence Data, 1,500 records accessed via the GBIF occurrence
search API:
```

```
https://api.gbif.org/v1/occurrence/search?taxonKey=212&decimalLatitude=…
```

```
Source datasets (datasetKey, records, title), 4 in all:
50c9509d-22c7-4a22-a47d-8c48425ef4a7   1353   iNaturalist research-grade observations
```

```
Register these as a derived dataset to get a DOI to cite: https://www.gbif.org/derived-
dataset/register
```

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

43 / 55 

Chapter 6 · Licences, Citation and GBIF Policy 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0044-01.png)

###### GBIF Data 

a GeoLibre plugin · v1.1.0 

#### Option A · Register a Derived Dataset 

A derived dataset cites exactly the records you used. GBIF gives it a DOI that credits every source dataset. 

1 

In Cite this data, click Save dataset list (CSV). You get `datasetKey,count` lines with no header. 

Deposit the data you used somewhere public and persistent, for example Zenodo, an institutional 2 repository or a data paper supplement. GBIF asks for its URL. 

Sign in at GBIF.org and open Derived datasets **→** Register (the Register a derived dataset (DOI) 3 link). 

Give a title and a description of how you prepared the data (area, filters, date of access, any 4 cleaning), add the URL, and upload or paste the dataset list. 

5 GBIF assigns a DOI such as `10.15468/dd.xxxxxx` . Cite that DOI in your report, paper or map. 

Use Option A when you used only what the plugin fetched, for example 1,500 bird records for a site report. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

44 / 55 

Chapter 6 · Licences, Citation and GBIF Policy 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0045-03.png)

#### Option B · A GBIF.org Download, and Citation Formats 

A download is a snapshot of the whole search, any size, with its own DOI. Use it for big or repeatable extractions, or more than 5,000 records. 

1 

Click Open this search on GBIF.org. The same filters open on the GBIF website. 

2 

Check the filters there, sign in and request a download (simple CSV or Darwin Core Archive). 

###### 3 GBIF e-mails you a link and a citation with a DOI. 

|What you cite|Example reference(adapt to your journal's style)|
|---|---|
|Derived dataset|GBIF.org (2026) Filtered export of GBIF occurrence data. https://doi.org/10.15468/dd.xxxxxx|
|Download|GBIF.org (29 October 2026) GBIF Occurrence Download. https://doi.org/10.15468/dl.xxxxxx|
|A single record|The citation at the bottom of its GBIF.org occurrence page.|
|Taxon<br>matching|GBIF Secretariat. GBIF Backbone Taxonomy. https://doi.org/10.15468/39omei|
|The plugin|Alfitriansyah, D. A. (2026). GBIF Data: a GeoLibre plugin (v1.1.0). https://github.com/Defani/GBIF-<br>Data|

Also: keep the ownership columns, respect each record's and each photo's licence, and credit photo creators when you reuse images. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

45 / 55 

Chapter 6 · Licences, Citation and GBIF Policy 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0046-02.png)

#### How the Plugin Follows GBIF's Rules 

The plugin was reviewed against GBIF's data user agreement, terms of use, citation guidelines and API documentation. The main requirements and how they are met: 

|GBIF requirement|How the plugin meets it|
|---|---|
|Keep the identifier of ownership with every<br>record|Dataset, publisher, institution, licence, GBIF key and access date on<br>every feature|
|Cite the data publishers, with a DOI where<br>possible|Cite this data block: citation text, dataset CSV, links to derived<br>datasets and downloads|
|Comply with each licence; the publisher's<br>licence prevails|Licence in every popup and feature; counts and a non-commercial<br>warning; licence filter|
|Media have their own licences; credit the<br>creator|Photo: © creator · licence under every photo|
|Use the image API for display|Thumbnails from GBIF's occurrence image cache, one per popup,<br>only on click|
|Do not disrupt the API; slow down on HTTP<br>429|Pages≤300,~200 ms apart, 5,000 cap, debounced counter, back-off 3<br>s then 8 s|
|The website is not an API|Only api.gbif.org is called; GBIF.org links are opened by you|
|No guarantee of data quality|Credit line with disclaimer; Drop geospatial issues on by default|
|Respect sensitive data|Only public API results; generalised coordinates are never recovered|
|Do not imply endorsement|Independent-plugin statement in the panel, catalog and docs; no<br>GBIF logo|

One recommendation cannot be met from inside a browser: GBIF suggests apps send a User-Agent header with a contact URL, but browsers do not let page scripts set it. The conservative limits above compensate. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

46 / 55 

Chapter 7 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0047-02.png)

# 07 Recipes, Troubleshooting and Closing 

Ready-made settings for common tasks, fixes for common problems, theming, the licence of this guide, and references. 

Recipes Troubleshooting Light and dark Checklist Guide licence References 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

47 / 55 

Chapter 7 · Recipes, Troubleshooting and Closing 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0048-03.png)

#### Recipes 

Ready-made settings for common forestry, conservation and research tasks. 

|Goal|Settings|
|---|---|
|Threatened species around a planned<br>activity|AreaMap vieworLayer· Quality IUCNCR, EN, VU· Points|
|Threatened mammals in a province|AreaLayer(province boundary) · TaxonMammalia· IUCN<br>CR, EN, VU|
|Herbarium records of a genus before a field<br>survey|Taxon: search the genus · Record typePreserved specimen|
|Recent bird sightings with precise locations|TaxonAves· TimeLast 5 yr· Uncertainty**≤**1 km|
|Everything known for one species,<br>worldwide|AreaWorld· Taxon the species · OutputDensityorBoth|
|Camera-trap records of a project|More filtersDataset key· Record typeMachine observation|
|Data for commercial consulting|Data licenceCC0andCC BYonly|
|Photo-verified records for teaching|QualityOnly records with photos· Record typeHuman<br>observation|
|Mangrove-related records on a coast|AreaMap view· Keywordmangrove|

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

48 / 55 

Chapter 7 · Recipes, Troubleshooting and Closing 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0049-03.png)

#### Troubleshooting 

The most common problems and their fixes. 

|Symptom|Cause and fix|
|---|---|
|No leaf button|Activate the plugin (Plugins→Installed→GBIF Data); switch the renderer<br>to MapLibre (2D or globe).|
|Counter shows —|The filters are incomplete, e.g. World without a taxon, dataset, recorder,<br>institution or keyword.|
|Counter shows !|GBIF is unreachable or asks to slow down. Check the connection; wait a<br>few minutes.|
|"That layer has no vector<br>features…"|Pick a vector layer; tile and raster layers have no extent to read.|
|"GBIF is rate-limiting<br>requests"|Wait, lower Max records, or use a GBIF.org download.|
|Could not fetch records:<br>Failed to fetch|Network interruption during paging. Try again; nothing was added.|
|Popup has no photo|The image is not in GBIF's cache yet, or the publisher's server is<br>unavailable.|
|Density layer hides points|Move the points layer above it in the Layers panel.|
|Copy citation says Copy failed|The webview blocks the clipboard; use Save dataset list (CSV) and the<br>GBIF.org links.|
|Points far from where<br>expected|Check<br>`uncertaintyM` : large values mean generalised locations.|

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

49 / 55 

Chapter 7 · Recipes, Troubleshooting and Closing 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0050-02.png)

#### Light and Dark Mode 

The panel takes every colour from GeoLibre: light or dark mode and the accent chosen in Settings **→** Appearance. It measures the live colours and keeps all text at WCAG AA contrast (4.5:1) for any accent. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0050-05.png)

###### Step numbers 

Sit in an accent-coloured disc; a step with a filter set gets a ring (black in light mode, white in dark mode). 

###### Fixed colours 

Only the official IUCN Red List colours stay the same in every theme. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

50 / 55 

Chapter 7 · Recipes, Troubleshooting and Closing 

GBIF Data a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0051-02.png)

#### Checklist Before You Publish 

Run through this list before a report, paper, poster or web map that uses GBIF-mediated data leaves your desk. 

|✓Filters recorded (area, taxon, time, quality)|✓Access date recorded|
|---|---|
|✓Record licences checked|✓No CC BY-NC data in commercial work|
|✓Photo licences checked, creators credited|✓Ownership columns kept in shared files|
|✓Uncertainty suits the map scale|✓Sensitive species not exposed|
|✓Absence of points not read as absence of<br>species|✓Derived dataset or download DOI obtained|
|✓DOI cited in the text and map credit|✓Backbone Taxonomy cited if used|

A short map credit that works: Occurrence data: GBIF.org and its data publishers, https://doi.org/10.15468/dd.xxxxxx, accessed 29 October 2026. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

51 / 55 

Chapter 7 · Recipes, Troubleshooting and Closing 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0052-02.png)

###### GBIF Data 

#### Licence of This Guide and Image Credits 

This guide follows the same policy as the plugin: each part keeps the licence of its owner. 

###### This guide (text, layout, diagrams) 

© 2026 Defani Arman Alfitriansyah, licensed CC BY-NC 4.0. Share and adapt it for non-commercial purposes with attribution. It is non-commercial because some figures contain CC BY-NC material. 

###### The plugin code 

MIT License, github.com/Defani/GBIF-Data. Material Symbols icon paths: Apache-2.0, Google. 

###### Occurrence data in the screenshots 

GBIF.org and its data publishers, accessed 29 October 2026, mainly iNaturalist research-grade observations (CC BY-NC 4.0) and other datasets under CC BY 4.0 and CC0. Shown for illustration only. 

###### Photos in the screenshots 

© ko25ra_k08 (CC BY-NC), © Galih Alamsyah (CC BY-NC) and © jj (CC BY-NC), via iNaturalist and the GBIF image cache. 

###### Basemaps 

GeoLibre default basemaps; map data © OpenStreetMap contributors (ODbL), tiles © OpenFreeMap / OpenMapTiles. 

###### Software 

GeoLibre (MIT) and MapLibre GL JS (BSD-3-Clause). IUCN category colours follow the IUCN Red List. 

GBIF, IUCN, GeoLibre and other names are used only to identify sources. No endorsement by any of them is implied. 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

52 / 55 

Chapter 7 · Recipes, Troubleshooting and Closing 

GBIF Data 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0053-02.png)

a GeoLibre plugin · v1.1.0 

#### Closing Words 

Thank you for reading to the end. Every point on a GBIF map stands for a person who looked carefully and an institution that chose to share. I hope this guide helps you use their work well, and give them the credit they deserve. 

GBIF Data is an open project. The source code, releases and documentation are on GitHub. If you find a bug or have an idea, please open an issue or send a pull request; every piece of feedback, however small, makes the plugin better for the next forester or researcher. 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0053-07.png)

###### github.com/Defani/GBIF-Data 

Source code, releases, usage, licensing and GBIF-compliance docs · MIT License 

###### Install 

plugins.geolibre.app/catalog/geolibre-gbif-data → Open in GeoLibre, or Manage plugins → search GBIF. 

Report a bug or an idea 

github.com/Defani/GBIF-Data/issues 

Cite this guide 

Alfitriansyah, D. A. (2026). GBIF Data for GeoLibre: Complete Guide (English edition, plugin v1.1.0). CC BY-NC 4.0. 

Happy mapping, 

###### Defani Arman Alfitriansyah 

PLUGIN DEVELOPER · FORESTER 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

53 / 55 

Chapter 7 · Recipes, Troubleshooting and Closing 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0054-02.png)

###### GBIF Data 

#### References (1): GBIF, Standards and IUCN 

Policies, documentation and standards used in the plugin and this guide. 

1. GBIF Secretariat. (2026). GBIF data user agreement. `gbif.org/terms/data-user` 

2. GBIF Secretariat. (2026). Terms of use and data licensing. `gbif.org/terms` 

3. GBIF Secretariat. (2026). Citation guidelines. `gbif.org/citation-guidelines` 

4. GBIF Secretariat. (2026). Derived datasets. `gbif.org/derived-dataset/about` 

5. GBIF Secretariat. (2026). GBIF API reference: occurrence, species, maps (v2) and images. `techdocs.gbif.org/en/openapi` 

6. GBIF Secretariat. (2023). GBIF Backbone Taxonomy. Checklist dataset. `doi.org/10.15468/39omei` 

7. Wieczorek, J., Bloom, D., Guralnick, R., Blum, S., Döring, M., Giovanni, R., Robertson, T., & Vieglais, D. (2012). Darwin Core: an evolving community-developed biodiversity data standard. PLoS ONE, 7(1), e29715. `doi.org/10.1371/journal.pone.0029715` 

8. Chapman, A. D. (2005). Principles of data quality. Copenhagen: Global Biodiversity Information Facility. `doi.org/10.15468/doc.jrgg-a190` 

9. Chapman, A. D., & Grafton, O. (2008). Guide to best practices for generalising sensitive species occurrence data. Copenhagen: GBIF. 

```
doi.org/10.15468/doc-b02j-gt10
```

10. IUCN. (2012). IUCN Red List Categories and Criteria: Version 3.1 (2nd ed.). Gland and Cambridge: IUCN. `iucnredlist.org/resources/categories-and-criteria` 

11. IUCN. (2026). The IUCN Red List of Threatened Species. `iucnredlist.org` 

12. Creative Commons. CC0 1.0, CC BY 4.0 and CC BY-NC 4.0 legal codes. `creativecommons.org/licenses` 

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

54 / 55 

Chapter 7 · Recipes, Troubleshooting and Closing 

GBIF Data 

a GeoLibre plugin · v1.1.0 

![](../assets/panduan/gbif-data/panduan-gbif-data.pdf-0055-03.png)

#### References (2): Software, Data and Literature 

Software, services and datasets behind the screenshots, and further reading on biodiversity data. 

1. Alfitriansyah, D. A. (2026). GBIF Data: a GeoLibre plugin (v1.1.0) [Software]. MIT License. `github.com/Defani/GBIF-Data · plugins.geolibre.app/catalog/geolibre-gbif-data` 

2. Wu, Q., & Open Geospatial Solutions. (2026). GeoLibre: a free and open-source, cloud-native GIS platform [Software]. MIT. `geolibre.app · github.com/opengeos/GeoLibre` 

3. Open Geospatial Solutions. (2026). GeoLibre plugin registry. `plugins.geolibre.app · github.com/opengeos/geolibre-plugins` 

4. MapLibre contributors. MapLibre GL JS [Software]. BSD-3-Clause. `maplibre.org` 

5. Google. Material Symbols. Apache-2.0. `fonts.google.com/icons` 

6. OpenStreetMap contributors. Map data. ODbL-1.0. `openstreetmap.org/copyright` 

7. OpenFreeMap. Vector basemap tiles. 

   - `openfreemap.org` 

8. iNaturalist contributors, iNaturalist. (2026). iNaturalist research-grade observations. Occurrence dataset accessed via GBIF.org, 29 October 2026. `doi.org/10.15468/ab3s5x` 

9. Heberling, J. M., Miller, J. T., Noesgaard, D., Weingart, S. B., & Schigel, D. (2021). Data integration enables global biodiversity synthesis. PNAS, 118(6), e2018093118. `doi.org/10.1073/pnas.2018093118` 

10. Meyer, C., Kreft, H., Guralnick, R., & Jetz, W. (2015). Global priorities for an effective information basis of biodiversity distributions. Nature Communications, 6, 8221. `doi.org/10.1038/ncomms9221` 

11. Hochachka, W. M., et al. (2012). Data-intensive science applied to broad-scale citizen science. Trends in Ecology & Evolution, 27(2), 130-137. 

```
doi.org/10.1016/j.tree.2011.11.006
```

GBIF Data for GeoLibre · Complete Guide · Defani Arman Alfitriansyah 

55 / 55 

