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

<br/><br/>

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
## EDA
## Pipeline
## Modeling
## Conclusion
