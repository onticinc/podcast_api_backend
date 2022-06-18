<div id="top"></div>


<!-- PROJECT LOGO -->
<br />
<!-- <div align="center">
  <a href="https://github.com/onticinc/podcast_template">
    <img src="https://djontic.com/wp-content/uploads/2022/01/R217-0109_Eggs_Profile_Art_v01.jpg" alt="Logo" width="300" height="300"> -->
  </a>



<!-- [![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url] -->

<!-- ![Contributors][contributors-shield] <br> -->
[Michael Smith](https://github.com/onticinc) <br>
[Patrick Brennan](https://github.com/pambonian)<br>
<hr />

<!-- ABOUT THE PROJECT -->

<hr />


# Built With

<br />

[Python.js](https://www.python.org/)

<br />

[Django.js](https://www.djangoproject.com/)

<br />

[Postgres.js](https://www.postgresql.org/)

<br />

[Crispy_forms.js](https://github.com/django-crispy-forms/django-crispy-forms)

<br />

[Aws3](https://aws.amazon.com/s3/)

<hr />


## Appearance


![Alt text](https://djontic.com/wp-content/uploads/2022/01/Screen-Shot-2022-01-31-at-5.58.53-AM.png)

![Alt text](https://djontic.com/wp-content/uploads/2022/01/Screen-Shot-2022-01-31-at-5.59.05-AM.png)

![Alt text](https://djontic.com/wp-content/uploads/2022/01/Screen-Shot-2022-01-31-at-6.00.41-AM.png)




<p align="right">(<a href="#top">back to top</a>)</p>

<!-- TECHNOLOGIES USED -->

## Technologies Used

<hr />

## Python.js

<br />

##### Python is an interpreted high-level general-purpose programming language. Its design philosophy emphasizes code readability with its use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

<br />

##### Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.

<br />

##### Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0. 

<br />

##### Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). 

<br />

##### Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.

<br />

##### Python consistently ranks as one of the most popular programming languages.

<br />

##### Referenced from:

<br />
https://en.wikipedia.org/wiki/Python_(programming_language)


<hr />

## Postgres

<hr />

##### PostgreSQL (/ˈpoʊstɡrɛs ˌkjuː ˈɛl/, POHST-gres kyoo el), also known as Postgres, is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley. 

<br />

##### In 1996, the project was renamed to PostgreSQL to reflect its support for SQL. After a review in 2007, the development team decided to keep the name PostgreSQL and the alias Postgres.]

<br />

##### PostgreSQL features transactions with Atomicity, Consistency, Isolation, Durability (ACID) properties, automatically updatable views, materialized views, triggers, foreign keys, and stored procedures. It is designed to handle a range of workloads, from single machines to data warehouses or Web services with many concurrent users. It is the default database for macOS Server and is also available for Windows, Linux, FreeBSD, and OpenBSD.

<br />

##### Referenced from:

<br />

https://en.wikipedia.org/wiki/PostgreSQL


<hr />

## Django

<br />

##### Django (/ˈdʒæŋɡoʊ/ JANG-goh; sometimes stylized as django) is a Python-based free and open-source web framework that follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.

<br />

##### Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. 

<br />

##### Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.

<br />

##### Some well-known sites that use Django include Instagram, Mozilla, Disqus, Bitbucket, Nextdoor and Clubhouse.

Referenced from: 
https://en.wikipedia.org/wiki/Django_(web_framework)


<hr />

## Beautiful Soup

<hr /> 

##### Beautiful Soup is a Python package for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

<br />

##### Beautiful Soup was started by Leonard Richardson, who continues to contribute to the project, and is additionally supported by Tidelift, a paid subscription to open-source maintenance.

<br />

##### It is available for Python 2.7 and Python 3

<br />

##### Referenced from: 

<br />

https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser)


<hr />


## Crispy Forms

<hr />

##### jango-crispy-forms provides you with a |crispy filter and {% crispy %} tag that will let you control the rendering behavior of your Django forms in a very elegant and DRY way. Have full control without writing custom form templates. All this without breaking the standard way of doing things in Django, so it plays nice with any other form application.

<br />

##### Referenced from:

<br />

https://django-crispy-forms.readthedocs.io/en/latest/



<p align="right">(<a href="#top">back to top</a>)</p>

<hr />

## General Approach

<hr />

##### We started by making the example Poll app in Django's docs then followed a blog turorial. 

<br />

##### We deployed to Linode after getting the blog working. During that process we realized how hard it was to deploy to Linode. Not wanting to go through that process everytime, we decided to deploy to heroku after making the rss app and front end changes...  

<br />

##### That was a big mistake. Lots of debugging and many tears. (not really... ok maybe a few.)

<br />

##### Heroku does not have a way to store images or other media other than AWS buckets. We set that up and got the images pulling from our buckets.


# Roadblocks




<hr />

##### Figuring out how to scrape a rss feed with Beautiful Soup was tricky. Took a lot of tryal and error with the views to get it to work in the end. 


<p align="right">(<a href="#top">back to top</a>)</p>


