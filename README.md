# Tea Recommend SNS

## Contents
- [tl;dr](#tldr)
- [Sensing](#sensing)
- [Processing](#processing)
- [Analize and Actuation](#analize)
- [System Environment](#sys_env)
- [ER Diagram](#er)
- [System Diagram](#sys_dig)
- [API Endpoint](#endpoint)

## <a id="tldr" href="#tldr">tl;dr</a>
- SNS like Twitter Specialized in 'TEA'
- User have to post an evaluation of tha tea he drunk.
- A user's preference accumulates, and it is used to recommend some tea to the user.
- A user's preference accumulates is also used to an evaluation of a Tea. So this SNS will be also Tea dictionary.

### Source of Idea
##### Tea community in Twitter
Some people tweets tea's photo, their impressions, tea's name and a producting area, when they drink a tea.
This SNS collect user's evaluation of tea with a post.

## <a id="sensing" href="#sensing">Sensing</a>
- Collect each user's evaluation data of tea with a post.

## <a id="processing" href="#processing">Processing</a>
### A Distictive UI
- User can evaluate tea by sliding a barometer of each futures.
<img width="800" alt="スクリーンショット 2019-07-12 17 30 45" src="https://user-images.githubusercontent.com/30229356/61114472-5a312f80-a4cb-11e9-9a2f-072a6c6a8cbc.png">

### Future values
- A range of Each feature values is from -1 to 1.
<img width="859" alt="スクリーンショット 2019-07-12 17 31 01" src="https://user-images.githubusercontent.com/30229356/61114442-4b4a7d00-a4cb-11e9-972b-31ee885a5d0e.png">

## <a id="analize" href="#analize">Analize and Actuation</a>
### Function1
- Calculate user's Preference.
- Mean of user's evaluation which user judged LIKE per category of tea

### Function2
- Calculate Tea(Evaluation of tea)
- Mean of all user's evaluation about the tea

### Function3
- Recommend tea to a user
- Inner producto between user's preference and teas

## <a id="sys_env" href="#sys_env">System Environment</a>
- Python 3.7.2
- Django 2.2.3
- Django Rest Framework 3.9.4
- PostgreSQL 11.3

## <a id="er" href="#er">ER Diagram</a>
![TeaRecommendDB_Django](https://user-images.githubusercontent.com/30229356/61113565-8b106500-a4c9-11e9-8171-3500d9b8eae2.png)

## <a id="sys_dig" href="#sys_dig">System Diagram</a>
<img width="780" alt="スクリーンショット 2019-07-12 17 31 25" src="https://user-images.githubusercontent.com/30229356/61114313-0cb4c280-a4cb-11e9-8f7f-534982de4980.png">

## <a id="endpoint" href="#endpoint">API Endpoint</a>
### Pages and Action of this service
#### Pages
- index : timeline
- profile : profile of user, old posts of user, follow, follower, posts user liked
- setting : core-info of user
- tea : info of tea
- evaluation : evaluations of user
- preference :  preference of user
#### Action 
- upload and delete a post
- like and delike a post
- follow and defollow a user
- upload a evaluation
- upload and update a user profile
- upload and update a user info
- search posts, tea, and users
### API Policy
Not complete REST, but Not completely fitting in UI -> Make a unit which is grouped by some entities 
<br>! Why -> robust to UI changes
#### Units
1. <b>Profile</b> : profile of user, posts of user
1. <b>APIs</b> : uris of all API
1. <b>Post&Evaluation</b> : post and evakuation about a tea
### RESTful API Endpoint

### UnRESTful API 

