# Yelp Review Sense

<img src="https://github.com/yashraizada/yelp-review-sense/blob/main/images/Header.png?raw=true"/>

## Table of Contents

* [Introduction](#Introduction)
   * [About Yelp](#About-Yelp)
   * [Objective](#Objective)
   * [Dataset](#Dataset)
* [ETL and Data Storage ](#ETL-and-Data-Storage)
* [EDA](#EDA)
* [Pipeline](#Pipeline)
* [Modeling](#Modeling)
* [Conclusion](#Conclusion)

<br/>

## Introduction

### About Yelp

Yelp is a widely recognized online platform dedicated to helping people discover, rate, and review businesses and services in various categories, such as restaurants, hotels, local shops, and other commercial establishments. Users can explore Yelp to find detailed information about businesses, including their location, contact details, hours of operation, photos, and most importantly, user-generated reviews and ratings. These user reviews offer a candid and firsthand perspective on the quality of products and services, helping potential customers gauge the reputation and reliability of a particular business.

### Objective

The primary objective of this project is to provide a user-friendly interface that summarizes the sentiments expressed in Yelp user reviews and presents this information in a clear and concise manner. This web application is designed to cater to both casual users who want a quick impression of a business's reputation and more discerning users who seek in-depth insights.

### Dataset

<img src="https://github.com/yashraizada/yelp-review-sense/blob/main/images/Yelp%20Open%20Dataset.png?raw=true"/>

The dataset used in this project is sourced from the [Yelp Open Dataset](https://www.yelp.com/dataset). For this project, the dataset serves as the foundation for the development of a web application aimed at summarizing and analyzing user comments and reviews, ultimately assisting users in making informed decisions about businesses and services on Yelp.

<img src="https://github.com/yashraizada/yelp-review-sense/blob/main/images/Dataset%20Description.png?raw=true"/>

The dataset consists of 5 JSON files, totaling approximately 4 GB in compressed format and expanding to roughly 10 GB when uncompressed. These files encompass various aspects of Yelp's data, each with distinct characteristics:

* **User Data**: Contains user data including the user's friend mapping and all the metadata associated with the user
    * Approximately 2 million data points
    * Comprising 22 features
    * Storage size of 3.4 GB
    * Data types include int, float, and string

* **Business Data**: Contains business data including location data, attributes, and categories
    * Encompassing around 150,000 data points
    * Containing 14 features
    * Utilizing 120 MB of storage
    * Data types include int, float, string, and struct

* **Reviews Data**: Contains full review text data including the user_id that wrote the review and the business_id the review is written for
    * Extending to nearly 7 million data points
    * With 9 features
    * Consuming 5.4 GB of storage
    * Data types include int, float, and string

* **Check-In Data**: Contains check-ins on a business
    * Covering approximately 130,000 data points
    * With 2 features
    * And 290 MB of storage
    * Data types include string

* **Tip Data**: Contains tips written by a user on a business. Tips are shorter than reviews and tend to convey quick suggestions.
    * Encompassing about 1 million data points
    * Containing 5 features
    * Utilizing 180 MB of storage
    * Data types include int and string


<br/>

## ETL and Data Storage

|      |business_id           |user_id               |review_id             |review_date   |review_stars|review_text         |review_total_interaction|user_yelping_since|user_review_count|user_average_stars|user_fans|user_friends_count|user_total_interactions|user_total_compliments|user_elite_years_count|user_elite_min_year|user_elite_max_year|biz_name                                |biz_city    |biz_state|biz_postal_code|biz_latitude|biz_longitude|biz_stars|biz_review_count|checkin_count|checkin_date_min|checkin_date_max|
|------|----------------------|----------------------|----------------------|--------------|------------|--------------------|------------------------|------------------|-----------------|------------------|---------|------------------|-----------------------|----------------------|----------------------|-------------------|-------------------|----------------------------------------|------------|---------|---------------|------------|-------------|---------|----------------|-------------|----------------|----------------|
|1     |-3e3CP3FFc-rvJj_-_airw|--2vR0DIsmQ6WfcSzKWigw|m3QNG3Ni7--EsiFv3IS3dg|2/19/15 5:08  |4           |Da uns der erste ...|302                     |11/27/12 14:19    |1534             |4.18              |880      |3982              |578739                 |133351                |10                    |20                 |2021               |Penn's Landing                          |Philadelphia|PA       |19106          |39.960022   |-75.13715    |3.5      |80              |594          |7/4/10 1:17     |7/2/10 23:27    |
|2     |goXz8V980-WFIreZRbLVSQ|4Q-nWKm4_t1UgImW3D_sgA|MGuVuTo9XDgXwHHCEC8O_Q|4/8/17 0:41   |1           |My original post ...|0                       |1/16/16 13:43     |8                |2.56              |0        |1                 |7                      |0                     |0                     |0                  |0                  |317 Burger                              |Indianapolis|IN       |46220          |39.87054    |-86.14242    |4        |422             |693          |12/8/13 1:28    |12/8/13 1:23    |
|3     |4dTLWrSe0GN_GrMZ1uAZwA|5N7-UqSgVYMW68Zo1Nxn5A|8sZv6asRsjIif3es493iQQ|12/26/14 20:57|5           |Hooters is the sa...|0                       |10/5/13 2:22      |8                |4.3               |0        |1                 |8                      |1                     |0                     |0                  |0                  |Hooters                                 |Metairie    |LA       |70006          |30.004791   |-90.18974    |3        |94              |603          |7/11/10 16:48   |6/16/10 0:06    |
|4     |9Ldo7ocJHVrEzRXUpN3Weg|6WW9sM9H2pKMr01twTLfYw|WjEfcAKUDOg7ADeI9U5DPA|5/14/15 21:27 |5           |My favorite nail ...|1                       |5/20/13 17:32     |1                |5                 |0        |1                 |1                      |0                     |0                     |0                  |0                  |Tampa Nails                             |Tampa       |FL       |33606          |27.945114   |-82.48182    |2.5      |121             |40           |8/28/14 14:17   |6/7/14 15:20    |
|5     |9dL1rsPANYr-71hdwoY-CA|43aSMIBPuDYFvduQByx4gw|1CMbbUzQkJFER754NEpUBA|9/18/15 3:17  |3           |The food is aweso...|1                       |4/14/10 22:51     |66               |3.81              |6        |225               |89                     |14                    |0                     |0                  |0                  |Desi Tadka Cuisine                      |Oldsmar     |FL       |34677          |28.042406   |-82.67776    |4        |169             |213          |5/24/13 0:57    |5/5/13 18:26    |

## EDA
## Pipeline
## Modeling
## Conclusion
