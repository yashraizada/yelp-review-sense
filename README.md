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

+--------------------+--------------------+--------------------+-------------------+------------+--------------------+------------------------+-------------------+-----------------+------------------+---------+------------------+-----------------------+----------------------+----------------------+-------------------+-------------------+--------------------+----------------+---------+---------------+------------+-------------+---------+----------------+-------------+-------------------+-------------------+
|         business_id|             user_id|           review_id|        review_date|review_stars|         review_text|review_total_interaction| user_yelping_since|user_review_count|user_average_stars|user_fans|user_friends_count|user_total_interactions|user_total_compliments|user_elite_years_count|user_elite_min_year|user_elite_max_year|            biz_name|        biz_city|biz_state|biz_postal_code|biz_latitude|biz_longitude|biz_stars|biz_review_count|checkin_count|   checkin_date_min|   checkin_date_max|
+--------------------+--------------------+--------------------+-------------------+------------+--------------------+------------------------+-------------------+-----------------+------------------+---------+------------------+-----------------------+----------------------+----------------------+-------------------+-------------------+--------------------+----------------+---------+---------------+------------+-------------+---------+----------------+-------------+-------------------+-------------------+
|-3e3CP3FFc-rvJj_-...|--2vR0DIsmQ6WfcSz...|m3QNG3Ni7--EsiFv3...|2015-02-19 05:08:44|         4.0|Da uns der erste ...|                     302|2012-11-27 14:19:33|             1534|              4.18|      880|              3982|                 578739|                133351|                    10|                 20|               2021|      Penn's Landing|    Philadelphia|       PA|          19106|   39.960022|    -75.13715|      3.5|              80|          594|2010-07-04 01:17:32|2010-07-02 23:27:44|
|CJ3t6dw60CdpflWKe...|-tIU61x9-zg1zjlJ3...|Lv83IvJ7Vl6EYj131...|2019-12-03 18:15:14|         1.0|We went there las...|                       0|2010-11-10 19:24:24|               27|              3.74|        0|                 6|                     26|                     0|                     0|                  0|                  0|            Benihana|Plymouth Meeting|       PA|          19462|    40.11639|   -75.279205|      2.5|             240|          296|2010-08-01 22:18:47|2010-07-15 23:12:04|
|NGR_aVWJ-W_KHvBDr...|-CzwjrantVGMmZB8Q...|iwiGJ2m7_s3owJR47...|2016-03-20 13:54:21|         3.0|Remodel is great,...|                      12|2012-01-25 18:13:34|              153|              3.55|       24|                56|                   1061|                   163|                     6|                 20|               2021|Atlantis Toucan C...|            Reno|       NV|          89502|    39.48895|   -119.79372|      4.0|             917|         1840|2010-05-16 18:25:24|2010-05-02 01:16:23|
|SyCXBCUsoCVEUBdru...|018xlOJfE5Yf997kp...|WU86c2wW3WblikSzl...|2020-01-14 20:02:12|         5.0|My family had the...|                       4|2015-03-28 16:42:50|               18|              4.74|        0|                 1|                     25|                     1|                     0|                  0|                  0|Residence Inn by ...|     New Orleans|       LA|          70130|    29.95064|    -90.07007|      4.0|              17|           13|2020-01-18 06:34:27|2019-12-06 14:01:48|
|T4SBFuxY23-6JsKOr...|00xGfvalJOhzGMxbq...|diB1VykEW3lmAuajJ...|2009-11-25 22:04:02|         4.0|Why would you go ...|                       0|2009-11-25 17:00:08|               32|              3.61|        3|                 5|                     65|                     5|                     0|                  0|                  0|The Black Dog Fre...|        Edmonton|       AB|        T6E 2A1|   53.518215|   -113.49924|      4.0|              48|          172|2011-04-20 00:03:25|2011-02-26 02:18:14|
|cVV8GWVIe9BwyCOKw...|2S_TNGTL1gDTDu3T2...|sXJ7Pv5VUfSrrx6tA...|2017-12-02 22:58:01|         5.0|Why has it taken ...|                      28|2011-03-11 07:16:39|              312|               3.8|       63|               466|                   3299|                   526|                     9|                 20|               2021|        Castellino's|    Philadelphia|       PA|          19125|   39.972336|    -75.12904|      5.0|              72|           71|2017-05-23 22:18:53|2017-04-23 18:36:08|
|dXTXpAK6IpeR8PLFY...|1FPPVOH6Nta9QF1zw...|k0_pkW1SzWaN65snu...|2015-10-22 07:17:41|         5.0|This is the best ...|                       0|2015-10-21 20:23:34|               15|              2.88|        0|                 1|                     28|                     0|                     0|                  0|                  0|     Texas Roadhouse|        Meridian|       ID|          83642|   43.619114|  -116.347466|      3.5|             287|          507|2011-03-13 23:40:48|2010-11-18 00:45:32|
|hVi4_rFTj0fsbfxa4...|2FG_8qjI_IAV5pEVk...|gd_DutOaujHobN9HZ...|2015-12-29 19:55:42|         4.0|Great little plac...|                       0|2012-08-30 15:36:49|               20|               4.2|        0|                 1|                     12|                     1|                     0|                  0|                  0|  Costa's Restaurant|  Tarpon Springs|       FL|          34689|   28.154554|    -82.76048|      3.5|             189|          216|2011-01-29 17:08:49|2011-01-29 17:04:07|
|nzn8r9dpFKYKh6LSW...|0VEa2DL9eO1llMk4w...|vO2di5SRG7nO-Y0dC...|2016-02-15 04:55:18|         5.0|What is Kaia Fit?...|                      20|2012-10-29 04:10:02|              155|              4.37|       24|               292|                   1191|                   348|                     3|               2015|               2017|Kaia FIT Sierra -...|          Sparks|       NV|          89436|    39.58022|   -119.72312|      5.0|               9|          561|2015-12-28 15:04:20|2015-12-23 15:17:07|
|sihT-_DtwOdnDDDJb...|1ji4PRst-aiIBNLJv...|5ccwbPyBnnS1UnDME...|2017-04-16 01:32:43|         1.0|Worse beer tour I...|                       0|2013-07-30 18:12:47|               22|              2.87|        1|                 1|                     21|                     0|                     0|                  0|                  0|  Cigar City Brewing|           Tampa|       FL|          33607|   27.958601|   -82.509346|      4.5|             876|         4116|2010-05-07 23:00:24|2010-05-07 22:36:11|
|sjueAFshWHWkKn5a1...|0HK-BPV0H9d02SrGp...|j-a00a0OqRsPdW3u7...|2018-04-22 19:39:23|         4.0|Great food. The c...|                       0|2009-05-16 00:45:41|              240|              3.82|        9|                76|                    308|                    14|                     5|               2015|               2019|     District Tavern|           Tampa|       FL|          33602|   27.948063|    -82.44682|      4.0|             227|          369|2015-12-22 16:34:53|2015-12-21 00:13:15|
|tR9azg_Dx8EfV1CBv...|0lV6XSKZ_Aiwx85iM...|xQHDzJmxur3WFCRJq...|2010-03-06 23:33:36|         1.0|SORELY disappoint...|                      15|2009-05-05 18:53:00|               72|               2.7|        7|                29|                    723|                    81|                     0|                  0|                  0|                 Pho|            Reno|       NV|          89511|   39.465267|    -119.7811|      3.5|             353|          862|2010-03-20 20:19:40|2010-03-05 19:56:44|
|y2f1eQ3UR-5Wi64TJ...|1POiIjXIuQWgP_QQ5...|gIdHWuBcQ7uuCPhVP...|2019-01-11 22:14:54|         5.0|Art in Philadelph...|                       0|2011-08-16 17:44:02|                2|               5.0|        0|                38|                      0|                     0|                     0|                  0|                  0|           HeaD AreA|    Philadelphia|       PA|          19107|    39.94737|    -75.15939|      5.0|              70|          128|2010-12-17 16:03:22|2010-06-30 00:25:59|
|6HTGlttrzCMsuGBHO...|1b5I-t9pU4F3b6x_3...|PBncZ3aqpAMWtGA93...|2017-03-24 10:36:46|         3.0|A decent romantic...|                       1|2017-01-18 10:36:24|                5|               4.0|        0|                 2|                      4|                     1|                     0|                  0|                  0|           Barbareño|   Santa Barbara|       CA|          93101|   34.418045|   -119.70295|      4.5|             405|          340|2014-11-01 04:47:15|2014-11-01 03:10:13|
|AODksDNj5mH953cyh...|0ahBSLAoO5cZIaVAc...|bVoYjFkM6DitWBkPk...|2016-11-05 00:45:18|         5.0|I was so excited ...|                       0|2010-08-06 18:55:47|               11|               5.0|        0|                11|                      7|                     2|                     0|                  0|                  0|    Thai 5 Fast Food|           Tampa|       FL|          33629|    27.91206|    -82.50577|      4.0|             336|          495|2015-04-25 00:27:24|2015-04-23 22:31:02|
|BVndHaLihEYbr76Z0...|1C2lxzUo1Hyye4RFI...|OAhBYw8IQ6wlfw1ow...|2014-10-11 16:22:06|         5.0|Great place for b...|                       0|2013-07-25 01:04:52|                6|              4.17|        0|                 3|                      4|                     0|                     0|                  0|                  0|       Mamas Kitchen|           Tampa|       FL|          33611|   27.884851|   -82.506004|      4.5|             162|          251|2010-08-11 17:49:14|2010-07-27 13:14:21|
|DA5Mecz4auAhTTlFW...|02UfjUYfSFIX3w0KW...|oU913ipyrVlOxwz03...|2020-04-26 01:21:01|         5.0|What can I say, I...|                       3|2013-06-20 18:27:18|               23|              4.78|        0|                 1|                     67|                     5|                     0|                  0|                  0|        La Chaiteria|          Tucson|       AZ|          85745|   32.220398|  -110.988815|      5.0|              65|           33|2020-02-14 20:38:45|2020-02-14 18:33:55|
|EwJqU25RgwkbOPKai...|0wkV8H_VSJTTwM217...|YTNX6IbebPiahO5sh...|2016-07-08 18:01:12|         5.0|One of the most a...|                       2|2015-09-12 16:11:36|               48|              3.85|        0|               141|                     31|                     4|                     2|               2016|               2017|    La Peña Mexicana|  Kennett Square|       PA|          19348|    39.84496|    -75.71877|      4.5|             198|          281|2011-02-18 17:27:20|2010-12-04 21:38:10|
|GST3wg-wej15vHeCv...|0NAmLqDhiAwmfmXwR...|_thaBhVSOPKn66oqn...|2019-03-10 04:04:17|         5.0|Loved the food. D...|                       0|2014-11-18 20:51:20|              248|              4.06|        0|                 2|                    121|                     2|                     0|                  0|                  0|    Acme Feed & Seed|       Nashville|       TN|          37201|   36.162014|    -86.77445|      4.0|            1731|         3375|2014-05-09 14:57:05|2014-05-09 14:52:06|
|HCYs4zgL7kCLdEqKR...|1yLhI547NuKHe-YEO...|euZs9PEJTBg6sl-ic...|2019-10-12 02:50:27|         5.0|I love grabbing l...|                       0|2017-01-12 00:29:34|                3|               5.0|        0|               224|                      1|                     0|                     0|                  0|                  0|     Lona's Lil Eats|        St Louis|       MO|          63104|   38.610146|    -90.22678|      4.5|             640|         1324|2014-09-06 00:25:51|2014-09-02 23:02:17|
+--------------------+--------------------+--------------------+-------------------+------------+--------------------+------------------------+-------------------+-----------------+------------------+---------+------------------+-----------------------+----------------------+----------------------+-------------------+-------------------+--------------------+----------------+---------+---------------+------------+-------------+---------+----------------+-------------+-------------------+-------------------+


## EDA
## Pipeline
## Modeling
## Conclusion
