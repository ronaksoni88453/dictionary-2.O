from turtle import Canvas

from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
root = Tk()
canvas = Canvas(root, width=1920, height=1000)
root.title("Complete Dictionary of SEO")
image = ImageTk.PhotoImage(Image.open("bgimage15.jpg"))
canvas.create_image(0, 0, anchor=NW, image=image)




textin = StringVar()
exlist={
    'algorithms': 'A complex computer program used by search engines to retrieve data and deliver results for a query.',
    'algorithms'.capitalize(): 'A complex computer program used by search engines to retrieve data and deliver results for a query.',
    'algorithms'.upper(): 'A complex computer program used by search engines to retrieve data and deliver results for a query.',
    "alt attribute": 'HTML code that provides information used by search engines and screen readers to understand the contents of an image.',
    "alt attribute".capitalize(): 'HTML code that provides information used by search engines and screen readers to understand the contents of an image.',
    "alt attribute".upper(): 'HTML code that provides information used by search engines and screen readers to understand the contents of an image.',
    "anchor test ".capitalize(): 'he clickable word or words of a link.',
    "anchor test ".upper(): 'he clickable word or words of a link.',
    "anchor test ": 'he clickable word or words of a link.',
    "backlink".upper(): 'A backlink is a link created when one website links to another,Backlinks are also called "inbound links" or "incoming links."',
    "backlink".capitalize(): 'A backlink is a link created when one website links to another,Backlinks are also called "inbound links" or "incoming links."',
    "backlink": 'A backlink is a link created when one website links to another,Backlinks are also called "inbound links" or "incoming links."',
    "black hat seo".capitalize(): 'Risky tactics that go against Google’s Webmaster Guidelines.',
    "black hat seo".upper(): 'Risky tactics that go against Google’s Webmaster Guidelines.',
    "black hat seo": 'Risky tactics that go against Google’s Webmaster Guidelines.',
    'bot': "Crawler, Googlebot",
    'bot'.capitalize(): "Crawler, Googlebot",
    'bot'.upper(): "Crawler, Googlebot",
    "broken link": 'A link that leads to a 404 not found.',
    "broken link".capitalize(): 'A link that leads to a 404 not found.',
    "broken link".upper(): 'A link that leads to a 404 not found.',
    "cache".upper(): 'A technology that temporarily stores web content, such as images, to reduce future page loading times.',
    "cache".capitalize(): 'A technology that temporarily stores web content, such as images, to reduce future page loading times.',
    "cache": 'A technology that temporarily stores web content, such as images, to reduce future page loading times.',
    'click bait': 'Content that is designed to entice people to click, typically by overpromising or being intentionally misleading in headlines.',
    'click bait'.capitalize(): 'Content that is designed to entice people to click, typically by overpromising or being intentionally misleading in headlines.',
    'click bait'.upper(): 'Content that is designed to entice people to click, typically by overpromising or being intentionally misleading in headlines.',
    "click through rate".capitalize(): 'The rate at which users click on an organic search result. This is calculated by dividing the total number of organic clicks by the total number of impressions then multiplying by 100.',
    "click through rate".upper(): 'The rate at which users click on an organic search result. This is calculated by dividing the total number of organic clicks by the total number of impressions then multiplying by 100.',
    "click through rate": 'The rate at which users click on an organic search result. This is calculated by dividing the total number of organic clicks by the total number of impressions then multiplying by 100.',
    'content'.capitalize(): "Words, images, videos, that convey information that is meant to be distributed to and consumed by an audience.",
    'content'.upper(): "Words, images, videos, that convey information that is meant to be distributed to and consumed by an audience.",
    'content': "Words, images, videos, that convey information that is meant to be distributed to and consumed by an audience.",
    'crawler'.upper(): "A program search engines use to crawl the web. Bots visit webpages to collect information and add or update a search engine’s index.",
    'crawler'.capitalize(): "A program search engines use to crawl the web. Bots visit webpages to collect information and add or update a search engine’s index.",
    'crawler': "A program search engines use to crawl the web. Bots visit webpages to collect information and add or update a search engine’s index.",
    "crawling".capitalize(): 'The process of gathering information, using a crawler, from the billions of public webpages to update, add, and organize webpages in a search engine’s index.',
    "crawling".upper(): 'The process of gathering information, using a crawler, from the billions of public webpages to update, add, and organize webpages in a search engine’s index.',
    "crawling": 'The process of gathering information, using a crawler, from the billions of public webpages to update, add, and organize webpages in a search engine’s index.',
    'cloaking': "Showing different content or URLs to people and search engines. A violation of Google’s Webmaster Guidelines.",
    'cloaking'.upper(): "Showing different content or URLs to people and search engines. A violation of Google’s Webmaster Guidelines.",
    'cloaking'.capitalize(): "Showing different content or URLs to people and search engines. A violation of Google’s Webmaster Guidelines.",
    'doorway page'.capitalize(): 'Webpages that are created to rank in search engines for specific keywords only for the purpose of redirecting users who click on that page to a different website.',
    'doorway page'.upper(): 'Webpages that are created to rank in search engines for specific keywords only for the purpose of redirecting users who click on that page to a different website.',
    'doorway page': 'Webpages that are created to rank in search engines for specific keywords only for the purpose of redirecting users who click on that page to a different website.',
    'duplicate content'.capitalize(): 'When a significant amount of content contained on one webpage matches, or is incredibly similar to, content that exists elsewhere on the same website or a completely different website.',
    'duplicate content'.upper(): 'When a significant amount of content contained on one webpage matches, or is incredibly similar to, content that exists elsewhere on the same website or a completely different website.',
    'duplicate content': 'When a significant amount of content contained on one webpage matches, or is incredibly similar to, content that exists elsewhere on the same website or a completely different website.',
    'external link'.upper(): 'External Links are hyperlinks that point at (target) any domain other than the domain the link exists on (source).',
    'external link': 'External Links are hyperlinks that point at (target) any domain other than the domain the link exists on (source).',
    'external link'.capitalize(): 'External Links are hyperlinks that point at (target) any domain other than the domain the link exists on (source).',
    'featured  snippet'.upper(): 'Google sometimes shows a special block above the organic search results. This box contains a summary (in the form of paragraph, list, table, or video), as well as the publication date, page title, link to the webpage from which the answer originated, and URL.',
    'featured  snippet': 'Google sometimes shows a special block above the organic search results. This box contains a summary (in the form of paragraph, list, table, or video), as well as the publication date, page title, link to the webpage from which the answer originated, and URL.',
    'featured  snippet'.capitalize(): 'Google sometimes shows a special block above the organic search results. This box contains a summary (in the form of paragraph, list, table, or video), as well as the publication date, page title, link to the webpage from which the answer originated, and URL.',
    'findability '.upper(): 'How easily the content on a website can be discovered, both internally and externally .',
    'findability ': 'How easily the content on a website can be discovered, both internally and externally .',
    'findability '.capitalize(): 'How easily the content on a website can be discovered, both internally and externally .',
    'google analytics'.upper(): 'A free web analytics program that can be used to track audience behavior, traffic acquisition sources, content performance, and much more.',
    'google analytics': 'A free web analytics program that can be used to track audience behavior, traffic acquisition sources, content performance, and much more.',
    'google analytics'.capitalize(): 'A free web analytics program that can be used to track audience behavior, traffic acquisition sources, content performance, and much more.',
    'googlebot '.upper(): 'The web crawling system Google uses to find and add new websites and webpages to its index.',
    'googlebot ': 'The web crawling system Google uses to find and add new websites and webpages to its index.',
    'googlebot '.capitalize(): 'The web crawling system Google uses to find and add new websites and webpages to its index.',
    'gray hat'.upper(): 'A supposed “gray” area between techniques that adhere to Google’s Webmaster Guidelines, but then add an element that bends the rules a little.',
    'gray hat': 'A supposed “gray” area between techniques that adhere to Google’s Webmaster Guidelines, but then add an element that bends the rules a little.',
    'gray hat'.capitalize(): 'A supposed “gray” area between techniques that adhere to Google’s Webmaster Guidelines, but then add an element that bends the rules a little.',
    'google search console '.upper(): 'Google’s Search Console offers several helpful features, including the ability to monitor sites for indexing errors and site speed. These pages are also used to communicate manual action notifications.',
    'google search console ': 'Google’s Search Console offers several helpful features, including the ability to monitor sites for indexing errors and site speed. These pages are also used to communicate manual action notifications.',
    'google search console '.capitalize(): 'Google’s Search Console offers several helpful features, including the ability to monitor sites for indexing errors and site speed. These pages are also used to communicate manual action notifications.',
    'google trends'.upper(): 'A website where you can explore data visualizations on the latest search trends, stories, and topics.',
    'google trends': 'A website where you can explore data visualizations on the latest search trends, stories, and topics.',
    'google trends'.capitalize(): 'A website where you can explore data visualizations on the latest search trends, stories, and topics.',
    'heading'.upper(): 'Heading tags (H1-H6) separate content into sections, based on importance.',
    'heading': 'Heading tags (H1-H6) separate content into sections, based on importance.',
    'heading'.capitalize(): 'Heading tags (H1-H6) separate content into sections, based on importance.',
    'hidden text'.upper(): 'Any text that can’t be seen by a user that is intended to manipulate search rankings by loading webpages with content-rich keywords and copy.',
    'hidden text': 'Any text that can’t be seen by a user that is intended to manipulate search rankings by loading webpages with content-rich keywords and copy.',
    'hidden text'.capitalize(): 'Any text that can’t be seen by a user that is intended to manipulate search rankings by loading webpages with content-rich keywords and copy.',
    'homepage'.upper(): 'The default, or introductory webpage, of a website.',
    'homepage': 'The default, or introductory webpage, of a website.',
    'homepage'.capitalize(): 'The default, or introductory webpage, of a website.',
    'html'.upper(): 'Stands for Hypertext Markup Language. HTML tags are specific code elements that can be used to improve the effectiveness of SEO for webpages and websites.',
    'html': 'Stands for Hypertext Markup Language. HTML tags are specific code elements that can be used to improve the effectiveness of SEO for webpages and websites.',
    'html'.capitalize(): 'Stands for Hypertext Markup Language. HTML tags are specific code elements that can be used to improve the effectiveness of SEO for webpages and websites.',
    'http'.upper(): 'The Hypertext Transfer Protocol is how data is transferred from a computer server to a web browser.',
    'http': 'The Hypertext Transfer Protocol is how data is transferred from a computer server to a web browser.',
    'http'.capitalize(): 'The Hypertext Transfer Protocol is how data is transferred from a computer server to a web browser.',
    'index'.upper(): 'The database search engines use to store and retrieve information gathered during the crawling process.',
    'index': 'The database search engines use to store and retrieve information gathered during the crawling process.',
    'index'.capitalize(): 'The database search engines use to store and retrieve information gathered during the crawling process.',
    'indexability'.upper(): 'How easily a search engine bot can understand and add a webpage to its index.',
    'indexability': 'How easily a search engine bot can understand and add a webpage to its index.',
    'indexability'.capitalize(): 'How easily a search engine bot can understand and add a webpage to its index.',
    'indexed page'.upper(): ' A webpage that has been discovered by a crawler, has been added to a search engine index, and is eligible to appear in search results for relevant queries.',
    'indexed page': ' A webpage that has been discovered by a crawler, has been added to a search engine index, and is eligible to appear in search results for relevant queries.',
    'indexed page'.capitalize(): ' A webpage that has been discovered by a crawler, has been added to a search engine index, and is eligible to appear in search results for relevant queries.',
    'ipaddress'.upper(): 'An Internet Protocol Address.',
    'ipaddress': 'An Internet Protocol Address.',
    'ipaddress'.capitalize(): 'An Internet Protocol Address.',
    'javascript'.upper(): 'A programming language that makes it possible to dynamically insert content, links, meta data, or other elements, on websites.',
    'javascript': 'A programming language that makes it possible to dynamically insert content, links, meta data, or other elements, on websites.',
    'javascript'.capitalize(): 'A programming language that makes it possible to dynamically insert content, links, meta data, or other elements, on websites.',
    'keyword'.upper(): 'The word, words, or phrase that an SEO professional or marketer targets for the purpose of matching and ranking for what users are searching for.',
    'keyword': 'The word, words, or phrase that an SEO professional or marketer targets for the purpose of matching and ranking for what users are searching for.',
    'keyword'.capitalize(): 'The word, words, or phrase that an SEO professional or marketer targets for the purpose of matching and ranking for what users are searching for.',
    'keyword density'.upper(): 'How often a word or phrase appears within the content of a webpage.',
    'keyword density': 'How often a word or phrase appears within the content of a webpage.',
    'keyword density'.capitalize(): 'How often a word or phrase appears within the content of a webpage.',
    'keyword research'.upper(): 'The process of discovering any relevant topics, subjects, and terms searchers enter into search engines, as well as the volume and competition level of those terms. This practice is made possible by a variety of free and paid tools.',
    'keyword research': 'The process of discovering any relevant topics, subjects, and terms searchers enter into search engines, as well as the volume and competition level of those terms. This practice is made possible by a variety of free and paid tools.',
    'keyword research'.capitalize(): 'The process of discovering any relevant topics, subjects, and terms searchers enter into search engines, as well as the volume and competition level of those terms. This practice is made possible by a variety of free and paid tools.',
    'keyword stuffing'.upper(): 'Adding irrelevant keywords, or repeating keywords beyond what is natural, to a webpage in the hopes of increasing search rankings. This spam tactic is against Google’s Webmaster Guidelines and can result in a manual action.',
    'keyword stuffing': 'Adding irrelevant keywords, or repeating keywords beyond what is natural, to a webpage in the hopes of increasing search rankings. This spam tactic is against Google’s Webmaster Guidelines and can result in a manual action.',
    'keyword stuffing'.capitalize(): 'Adding irrelevant keywords, or repeating keywords beyond what is natural, to a webpage in the hopes of increasing search rankings. This spam tactic is against Google’s Webmaster Guidelines and can result in a manual action.',
    'landing page'.upper(): 'Any webpage that a visitor can navigate to.',
    'landing page': 'Any webpage that a visitor can navigate to.',
    'landing page'.capitalize(): 'Any webpage that a visitor can navigate to.',
    'link'.upper(): 'A connection between two websites built using HTML code. A link enables users to navigate to websites, social networks, and apps.',
    'link': 'A connection between two websites built using HTML code. A link enables users to navigate to websites, social networks, and apps.',
    'link'.capitalize(): 'A connection between two websites built using HTML code. A link enables users to navigate to websites, social networks, and apps.',
    'link bait'.upper(): 'Intentionally provocative content that is meant to grab people’s attention and attract links from other websites.',
    'link bait': 'Intentionally provocative content that is meant to grab people’s attention and attract links from other websites.',
    'link bait'.capitalize(): 'Intentionally provocative content that is meant to grab people’s attention and attract links from other websites.',
    'Link building'.upper(): 'A process designed to get other trusted and relevant websites to link to your website to help improve your organic search rank and visibility.',
    'Link building': 'A process designed to get other trusted and relevant websites to link to your website to help improve your organic search rank and visibility.',
    'Link building'.capitalize(): 'A process designed to get other trusted and relevant websites to link to your website to help improve your organic search rank and visibility.',
    'link farm'.upper(): 'When a group of websites link to each other, usually using automated programs, in the hopes of artificially increasing search rankings.it is also a spam tactic.',
    'link farm': 'When a group of websites link to each other, usually using automated programs, in the hopes of artificially increasing search rankings.it is also a spam tactic.',
    'link farm'.capitalize(): 'When a group of websites link to each other, usually using automated programs, in the hopes of artificially increasing search rankings.it is also a spam tactic.',
    'link profile '.upper(): 'Every type of link that points to a particular website. The quality of a website’s link profile can vary widely, depending on how they were acquired and the anchor text used.',
    'link profile ': 'Every type of link that points to a particular website. The quality of a website’s link profile can vary widely, depending on how they were acquired and the anchor text used.',
    'link profile '.capitalize(): 'Every type of link that points to a particular website. The quality of a website’s link profile can vary widely, depending on how they were acquired and the anchor text used.',
    'meta keywords'.upper(): 'A tag that can be added to the “head section of an HTML document. Adding a bunch of keywords here won’t help you rank – search engine algorithms have ignored this tag for ranking purposes for years due to abuse (in the form of keyword stuffing).',
    'meta keywords': 'A tag that can be added to the “head section of an HTML document. Adding a bunch of keywords here won’t help you rank – search engine algorithms have ignored this tag for ranking purposes for years due to abuse (in the form of keyword stuffing).',
    'meta keywords'.capitalize(): 'A tag that can be added to the “head section of an HTML document. Adding a bunch of keywords here won’t help you rank – search engine algorithms have ignored this tag for ranking purposes for years due to abuse (in the form of keyword stuffing).',
    'meta description': 'A tag that can be added to the “head section of an HTML document. It acts as a description of a webpage’s content.',
    'meta description'.upper(): 'A tag that can be added to the “head section of an HTML document. It acts as a description of a webpage’s content.',
    'meta description'.capitalize(): 'A tag that can be added to the “head section of an HTML document. It acts as a description of a webpage’s content.',
    'meta tags'.upper(): 'Information that appears in the HTML source code of a webpage to describe its contents to search engines. The title tag and meta description are the most commonly used types of meta tags in SEO.',
    'meta tags': 'Information that appears in the HTML source code of a webpage to describe its contents to search engines. The title tag and meta description are the most commonly used types of meta tags in SEO.',
    'meta tags'.capitalize(): 'Information that appears in the HTML source code of a webpage to describe its contents to search engines. The title tag and meta description are the most commonly used types of meta tags in SEO.',
    'niche'.upper(): 'A specific market or area of interest consisting of a small group of highly-passionate people.',
    'niche': 'A specific market or area of interest consisting of a small group of highly-passionate people.',
    'niche'.capitalize(): 'A specific market or area of interest consisting of a small group of highly-passionate people.',
    'no index tag'.upper(): 'A meta tag that tells search engines not to index a specific webpage in its index.',
    'no index tag': 'A meta tag that tells search engines not to index a specific webpage in its index.',
    'no index tag'.capitalize(): 'A meta tag that tells search engines not to index a specific webpage in its index.',
    'no snippet tag'.upper(): 'A meta tag that tells search engines not to show a description with your listing.',
    'no snippet tag': 'A meta tag that tells search engines not to show a description with your listing.',
    'no snippet tag'.capitalize(): 'A meta tag that tells search engines not to show a description with your listing.',
    'negative seo'.upper(): 'A malicious practice where webspam techniques are used to harm the search rankings of another website, usually a competitor.',
    'negative seo': 'A malicious practice where webspam techniques are used to harm the search rankings of another website, usually a competitor.',
    'negative seo'.capitalize(): 'A malicious practice where webspam techniques are used to harm the search rankings of another website, usually a competitor.',
    'off page seo'.upper(): 'Brand awareness activities that take place outside of a website. Like link building, promotion tactics include social media marketing, content marketing.',
    'off page seo': 'Brand awareness activities that take place outside of a website. Like link building, promotion tactics include social media marketing, content marketing.',
    'off page seo'.capitalize(): 'Brand awareness activities that take place outside of a website. Like link building, promotion tactics include social media marketing, content marketing.',
    'on page seo'.upper(): 'These SEO activities all take place within a website.',
    'on page seo': 'These SEO activities all take place within a website.',
    'on page seo'.capitalize(): 'These SEO activities all take place within a website.',
    'organic search'.upper(): 'The natural, or unpaid, listings that appear on a SERP. Organic search results, which are analyzed and ranked by algorithms, are designed to give users the most relevant result based on their query.',
    'organic search': 'The natural, or unpaid, listings that appear on a SERP. Organic search results, which are analyzed and ranked by algorithms, are designed to give users the most relevant result based on their query.',
    'organic search'.capitalize(): 'The natural, or unpaid, listings that appear on a SERP. Organic search results, which are analyzed and ranked by algorithms, are designed to give users the most relevant result based on their query.',
    'orphan page'.upper(): 'Any webpage that is not linked to by any other pages on that website.',
    'orphan page': 'Any webpage that is not linked to by any other pages on that website.',
    'orphan page'.capitalize(): 'Any webpage that is not linked to by any other pages on that website.',
    'page rank'.upper(): 'PageRank is the measure of the importance of a page based on the incoming links from other pages. In simple terms, each link to a page on your site from another site adds to your site’s PageRank.',
    'page rank': 'PageRank is the measure of the importance of a page based on the incoming links from other pages. In simple terms, each link to a page on your site from another site adds to your site’s PageRank.',
    'page rank'.capitalize(): 'PageRank is the measure of the importance of a page based on the incoming links from other pages. In simple terms, each link to a page on your site from another site adds to your site’s PageRank.',
    'personalisation'.upper(): 'When search engines use search history, web browsing history, location, and relationships to create a set of search results tailored to a specific user.',
    'personalisation': 'When search engines use search history, web browsing history, location, and relationships to create a set of search results tailored to a specific user.',
    'personalisation'.capitalize(): 'When search engines use search history, web browsing history, location, and relationships to create a set of search results tailored to a specific user.',
    'php'.upper(): 'Hypertext Preprocessor is a scripting language used to create dynamic content on webpages.',
    'php': 'Hypertext Preprocessor is a scripting language used to create dynamic content on webpages.',
    'php'.capitalize(): 'Hypertext Preprocessor is a scripting language used to create dynamic content on webpages.',
    'piracy'.upper(): 'Search engines aim to reduce the organic search rankings of content that infringes on copyright. Google introduced a filter in 2012 that reduces the visibility of sites reported for numerous DMCA-related takedown requests.',
    'piracy': 'Search engines aim to reduce the organic search rankings of content that infringes on copyright. Google introduced a filter in 2012 that reduces the visibility of sites reported for numerous DMCA-related takedown requests.',
    'piracy'.capitalize(): 'Search engines aim to reduce the organic search rankings of content that infringes on copyright. Google introduced a filter in 2012 that reduces the visibility of sites reported for numerous DMCA-related takedown requests.',
    'query'.upper(): 'The word, words, or phrase that a user enters into a search engine.',
    'query': 'The word, words, or phrase that a user enters into a search engine.',
    'query'.capitalize(): 'The word, words, or phrase that a user enters into a search engine.',
    'rank'.upper(): 'Where a webpage appears within the organic search results for a specific query.',
    'rank': 'Where a webpage appears within the organic search results for a specific query.',
    'rank'.capitalize(): 'Where a webpage appears within the organic search results for a specific query.',
    'redirect'.upper(): 'A technique that sends a user (or search engine) who requested one webpage to a different (but equally relevant) webpage.',
    'redirect': 'A technique that sends a user (or search engine) who requested one webpage to a different (but equally relevant) webpage.',
    'redirect'.capitalize(): 'A technique that sends a user (or search engine) who requested one webpage to a different (but equally relevant) webpage.',
    'responsive website'.upper(): 'A website designed to automatically adapt to a user’s screen size, whether it’s being viewed on a desktop or mobile device.',
    'responsive website': 'A website designed to automatically adapt to a user’s screen size, whether it’s being viewed on a desktop or mobile device.',
    'responsive website'.capitalize(): 'A website designed to automatically adapt to a user’s screen size, whether it’s being viewed on a desktop or mobile device.',
    'search engine'.upper(): 'A computer program that enables users to enter a query in order to retrieve information (e.g., files, websites, webpages) from that program’s index (i.e., a web search engine, such as Google, indexes websites, webpages, and files found on the World Wide Web).',
    'search engine': 'A computer program that enables users to enter a query in order to retrieve information (e.g., files, websites, webpages) from that program’s index (i.e., a web search engine, such as Google, indexes websites, webpages, and files found on the World Wide Web).',
    'search engine'.capitalize(): 'A computer program that enables users to enter a query in order to retrieve information (e.g., files, websites, webpages) from that program’s index (i.e., a web search engine, such as Google, indexes websites, webpages, and files found on the World Wide Web).',
    'search engine optimisation'.upper(): 'The process of optimizing a website – as well as all the content on that website – so it will appear in prominent positions in the organic results of search engines. SEO requires an understanding of how search engines work, what people search for (i.e., keywords and keyphrases).',
    'search engine optimisation': 'The process of optimizing a website – as well as all the content on that website – so it will appear in prominent positions in the organic results of search engines. SEO requires an understanding of how search engines work, what people search for (i.e., keywords and keyphrases).',
    'search engine optimisation'.capitalize(): 'The process of optimizing a website – as well as all the content on that website – so it will appear in prominent positions in the organic results of search engines. SEO requires an understanding of how search engines work, what people search for (i.e., keywords and keyphrases).',
    'site map'.upper(): 'A list of pages on a website.',
    'site map': 'A list of pages on a website.',
    'site map'.capitalize(): 'A list of pages on a website.',
    'subdomain'.upper(): 'A separate section that exists within a main domain. For example: http://jobs.searchenginejournal.com/ is a subdomain that exists within the main domain of https://www.searchenginejournal.com/.',
    'subdomain': 'A separate section that exists within a main domain. For example: http://jobs.searchenginejournal.com/ is a subdomain that exists within the main domain of https://www.searchenginejournal.com/.',
    'subdomain'.capitalize(): 'A separate section that exists within a main domain. For example: http://jobs.searchenginejournal.com/ is a subdomain that exists within the main domain of https://www.searchenginejournal.com/.',
    'search history'.upper(): 'Search engines track every search users conduct (text and voice), every webpage visited, and every ad clicked on.',
    'search history': 'Search engines track every search users conduct (text and voice), every webpage visited, and every ad clicked on.',
    'search history'.capitalize(): 'Search engines track every search users conduct (text and voice), every webpage visited, and every ad clicked on.',
    'title tag'.upper(): 'An HTML meta tag that acts as the title of a webpage.',
    'title tag': 'An HTML meta tag that acts as the title of a webpage.',
    'title tag'.capitalize(): 'An HTML meta tag that acts as the title of a webpage.',
    'top level domain'.upper(): 'The extension of a given web address. These include:.com,.org,.net,.info.etc',
    'top level domain': 'The extension of a given web address. These include:.com,.org,.net,.info.etc',
    'top level domain'.capitalize(): 'The extension of a given web address. These include:.com,.org,.net,.info.etc',
    'traffic'.upper(): 'The people (and sometimes bots) who visit your website.',
    'traffic': 'The people (and sometimes bots) who visit your website.',
    'traffic'.capitalize(): 'The people (and sometimes bots) who visit your website.',
    'universal search'.upper(): 'When search engines pull data from multiple speciality databases to display on the same SERP. Results can include images, videos, news, shopping, and other types of results.',
    'universal search': 'When search engines pull data from multiple speciality databases to display on the same SERP. Results can include images, videos, news, shopping, and other types of results.',
    'universal search'.capitalize(): 'When search engines pull data from multiple speciality databases to display on the same SERP. Results can include images, videos, news, shopping, and other types of results.',
    'url'.upper(): 'The term URL is usually short-hand for the letter-based web address (e.g., www.searchenginejournal.com) entered into a browser to access a webpage.',
    'url': 'The term URL is usually short-hand for the letter-based web address (e.g., www.searchenginejournal.com) entered into a browser to access a webpage.',
    'url'.capitalize(): 'The term URL is usually short-hand for the letter-based web address (e.g., www.searchenginejournal.com) entered into a browser to access a webpage.',
    'user agent'.upper(): 'Web crawling software.',
    'user agent': 'Web crawling software.',
    'user agent'.capitalize(): 'Web crawling software.',
    'user experience'.upper(): 'The overall feeling users are left with after interacting with a brand, its online presence, and its product/services.',
    'user experience': 'The overall feeling users are left with after interacting with a brand, its online presence, and its product/services.',
    'user experience'.capitalize(): 'The overall feeling users are left with after interacting with a brand, its online presence, and its product/services.',
    'vertical search'.upper(): 'A specialized type of search where the focus is only on a specific topic, type of content, or media.',
    'vertical search': 'A specialized type of search where the focus is only on a specific topic, type of content, or media.',
    'vertical search'.capitalize(): 'A specialized type of search where the focus is only on a specific topic, type of content, or media.',
    'visibility'.upper(): 'The positions a website occupies within the organic search results.',
    'visibility': 'The positions a website occupies within the organic search results.',
    'visibility'.capitalize(): 'The positions a website occupies within the organic search results.',
    'webpage'.upper(): 'A document that exists on the World Wide Web and can be viewed by web browsers.',
    'webpage': 'A document that exists on the World Wide Web and can be viewed by web browsers.',
    'webpage'.capitalize(): 'A document that exists on the World Wide Web and can be viewed by web browsers.',
    'website'.upper(): 'A collection of webpages hosted together on the World Wide Web.',
    'website': 'A collection of webpages hosted together on the World Wide Web.',
    'website'.capitalize(): 'A collection of webpages hosted together on the World Wide Web.',
    'white hat'.upper(): 'Tactics that comply with Google’s Webmaster Guidelines.',
    'white hat': 'Tactics that comply with Google’s Webmaster Guidelines.',
    'white hat'.capitalize(): 'Tactics that comply with Google’s Webmaster Guidelines.',
    'word count'.upper(): 'The total number of words that appear within the copy of content.',
    'word count': 'The total number of words that appear within the copy of content.',
    'word count'.capitalize(): 'The total number of words that appear within the copy of content.',
'A'.lower() or 'A'.upper() : '1)algorithms 2)alt attribute 3)anchor  test',
    'A'.upper(): '1)algorithms 2)alt attribute 3)anchor  test',
'B'.lower() or 'B'.upper(): '1)backing 2)blackhat seo  3)bot 4)broken link',
    'B'.upper(): '1)backing 2)blackhat  seo  3)bot 4)broken  link',
'C'.lower() or 'C'.upper(): '1)cache 2)click bait 3)click through rate 4)content 5)crawler 6)crawling 7)cloaking',
    'C'.upper(): '1)cache 2)click bait 3)click through rate 4)content 5)crawler 6)crawling 7)cloaking',
'D'.lower() or 'D'.upper(): '1)doorway page 2)duplicate content ',
    'D'.upper(): '1)doorway page 2)duplicate content ',
'E'.lower() or 'E'.upper(): '1)external  link',
    'E'.upper(): '1)external  link',
'F'.lower() or 'F'.upper(): '1)featured  snippet  2)findability',
    'F'.upper(): '1)featured  snippet  2)findability',
'G'.lower() or 'G'.upper(): '1)google analytics 2)googlebot 3)gray hat',
    'G'.upper(): '1)google analytics 2)googlebot 3)gray hat 4)google search console 4)google trends',
'H'.lower() or 'H'.upper(): '1)heading 2)hidden text 3)homepage 4)html 5)http',
    'H'.upper(): '1)heading 2)hidden text 3)homepage 4)html 5)http',
'I'.lower() or 'I'.upper(): '1)index 2)indexability 3)indexed page 4)ipaddress',
    'I'.upper(): '1)index 2)indexability 3)indexed page 4)ipaddress',
'J'.lower() or 'J'.upper(): '1)javascript',
    'J'.upper(): '1)javascript',
'K'.lower() or 'K'.upper(): '1)keyword 2)keyword density 3)keyword research 4)keyword stuffing',
    'K'.upper(): '1)keyword 2)keyword density 3)keyword research 4)keyword stuffing',
'L'.lower() or 'L'.upper(): '1)landingpage 2)link 3)linkbait 4)link building 5)linkfarm 6)link profile',
    'L'.upper(): '1)landingpage 2)link 3)linkbait 4)link building 5)linkfarm 6)link profile',
'M'.lower() or 'M'.upper(): '1)meta keywords 2)meta description 3)meta tags',
    'M'.upper(): '1)meta keywords 2)meta description 3)meta tags',
'N'.lower() or 'N'.upper(): '1)niche 2)no index tag 3)no snippet tag 4)negative seo',
    'N'.upper(): '1)niche 2)no index tag 3)no snippet tag 4)negative seo',
'O'.lower() or 'O'.upper(): '1)off page seo 2)on page seo 3)organic search 4)orphan page',
    'O'.upper(): '1)off page seo 2)on page seo 3)organic search 4)orphan page',
'P'.lower() or 'P'.upper(): '1)page rank 2)personalisation 3)php 4)piracy',
    'P'.upper(): '1)page rank 2)personalisation 3)php 4)piracy',
'Q'.lower() or 'Q'.upper(): '1)query ',
    'Q'.upper(): '1)query',
'R'.lower() or 'R'.upper(): '1)rank 2)rank 3)redirect 4)responsive website',
    'R'.upper(): '1)rank 2)rank 3)redirect 4)responsive website',
'S'.lower() or 'S'.upper(): '1)search engine 2)search engine optimisation 3)site map 4)subdomain 5)search history',
    'S'.upper(): '1)search engine 2)search engine optimisation 3)site map 4)subdomain 5)search history',
'T'.lower() or 'T'.upper(): '1)title tag 2)top level domain 3)traffic',
    'T'.upper(): '1)title tag 2)top level domain 3)traffic',
'U'.lower() or 'U'.upper(): '1)universal search 2)url 3)user agent 4)user experience (ux)',
    'U'.upper(): '1)universal search 2)url 3)user agent 4)user experience (ux)',
'V'.lower() or 'V'.upper(): '1)vertical search 2)visibility 3)anchor  test',
    'V'.upper(): '1)vertical search 2)visibility 3)anchor  test',
'W'.lower() or 'W'.upper(): '1)webpage 2)website 3)white hat 4)word count ',
    'W'.upper(): '1)webpage 2)website 3)white hat 4)word count',
'X'.lower() or 'X'.upper(): '''As we haven't discovered any words with these letters but as we move forward we will gonna update our data with alot of new words''',
    'X'.upper():'''As we haven't discovered any words with these letters but as we move forward we will gonna update our data with alot of new words''',
'Y'.lower() or 'Y'.upper():'''As we haven't discovered any words with these letters but as we move forward we will gonna update our data with alot of new words''',
    'Y'.upper():'''As we haven't discovered any words with these letters but as we move forward we will gonna update our data with alot of new words''',
'Z'.lower() or 'Z'.upper():'''As we haven't discovered any words with these letters but as we move forward we will gonna update our data with alot of new words''',
    'Z'.upper():'''As we haven't discovered any words with these letters but as we move forward we will gonna update our data with alot of new words''',
}
def A():

    Label(root, text="ALGORITHMS", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="ALT ATTRIBUTE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="ANCHOR  TEST", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def B():
    Label(root, text="BACKLINK", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="BLACK HAT SEO", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="BOT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="BROKEN", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def C():
    Label(root, text="CACHE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="CLICK BAIT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="CLICK THROUGH RATE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="CONTENT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="CRAWLER", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)
    Label(root, text="CRAWLING", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=280)
    Label(root, text="CLOAKING", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=320)
def D():
    Label(root, text="DOORWAY PAGE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="DUPLICATE CONTENT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def E():
    Label(root, text="EXTERNAL LINK", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def F():
    Label(root, text="FEATURED SNIPPET", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="FINDABILITY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def G():
    Label(root, text="GOOGLE ANALYTICS", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="GOOGLEBOT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="GRAY HAT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="GOOGLE SEARCH CONSOLE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="GOOGLE TRENDS", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def H():
    Label(root, text="HEADING", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="HIDDEN TEXT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="HOMEPAGE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="HTML", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="HTTP", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def I():
    Label(root, text="INDEX", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="INDEXABILITY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="INDEXED PAGE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="IPADDRESS", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def J():
    Label(root, text="JAVASCRIPT", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def K():
    Label(root, text="KEYWORD", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="KEYWORD DENSITY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="KEYWORD RESEARCH", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="KEYWORD STUFFING", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def L():
    Label(root, text="LANDING PAGE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="LINK", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="LINK BAIT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="LINK BUILDING", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="LINK FARM", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)
    Label(root, text="LINK PROFILE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def M():
    Label(root, text="META KEYWORDS", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="META DESCRIPTION", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="META TAGS", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def N():
    Label(root, text="NICHE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="NO INDEX TAG", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="NO SNIPPET TAG", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="NEGATIVE SEO", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def O():
    Label(root, text="OFF PAGE SEO", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="ON PAGE SEO", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="ORGANIC SEARCH", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="ORPHAN PAGE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def P():
    Label(root, text="PAGE RANK", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="PERSONALISATION", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="PHP", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="PIRACY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def Q():
    Label(root, text="QUERY", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def R():
    Label(root, text="RANK", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="REDIRECT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="RESPONSIVE WEBSITE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def S():
    Label(root, text="SEARCH ENGINE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="SEARCH ENGINE OPTIMISATION", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="SITE MAP", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="SUBDOMAIN", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="SEARCH HISTORY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def T():
    Label(root, text="TITLE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="TOP LEVEL DOMAIN", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="TRAFFIC", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def U():
    Label(root, text="UNIVERSAL SEARCH", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="URL", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="USER AGENT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="USER EXPERIENCE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def V():
    Label(root, text="VERTICAL SEARCH", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="VISIBILITY", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def W():
    Label(root, text="WEBPAGE", width=20, font="comicansans 12 bold", height=2, bg="pink",).place(x=800,y=80)
    Label(root, text="WEBSITE", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=120)
    Label(root, text="WHITE HAT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800,y=160)
    Label(root, text="WORD COUNT", width=20, font="comicansans 12 bold", height=2, bg="pink").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def X():
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black",).place(x=800,y=80)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def Y():
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black",).place(x=800,y=80)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def Z():
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black", ).place(x=800, y=80)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=120)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=160)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=200)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=240)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=280)
    Label(root, text="", width=20, font="comicansans 12 bold", height=2, bg="black").place(x=800, y=320)
def clk():
    entered = ent.get()
    output.delete(0.0,END)
    try:
        textin = exlist[entered]
    except:
        textin = 'Sorry this Keyword is not available!\n'
    output.insert(0.0,textin)
def ex():
    tkinter.messagebox.showinfo("Program",'Exit')
    exit()
def exitt():
    tkinter.messagebox.showinfo("program",'Exit')
    exit()
def me():
    text='\n XYZ \n OKEY DEXTER \n NICE'
    saveFile = open('text.txt', 'w')
    saveFile.write(text)
    print('This are the entries::', text)
def hel():
    help(tkinter)
def cont():
    tkinter.messagebox.showinfo('__Version 1.0__')
def clr():
    textin.set("")
    output.delete(0.0, END)
menu = Menu(root)
root.config(menu=menu)
subm = Menu(menu)
menu.add_cascade(label="File",menu=subm)
subm.add_command(label="Memo",command=me)
subm.add_command(label="Save")
subm.add_command(label="Save As")
subm.add_command(label="Print")
subm.add_command(label="Exit",command=ex)
subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Tkinter Help",command=hel)
subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Contributors",command=cont)
TITLE=Label(root,text='WELCOME TO COMPLETE SEO DICTIONARY',font=('none 15 bold'),bg ='silver')
TITLE.place(x=100,y=30,)
lab=Label(root,text='Keyword :',font=('none 15 bold'),bg ='silver')
lab.place(x=200,y=100,)
ent=Entry(root,width=22,font=('none 12 bold'),textvar=textin,bg='powder blue')
ent.place(x=310 ,y=100,)
but1=Button(root,padx=2,pady=2,text='Search',command=clk,bg='silver',font=('none 15 bold'))
but1.place(x=325,y=150)
but2=Button(root,padx=2,pady=2,text='Clear',font=('none 15 bold'),bg='silver',command=clr)
but2.place(x=385,y=400)
output=Text(root,width=21,height=8,font=('Time 15 bold'),fg="black",bg='powder blue')
output.place(x=300,y=200)
labb=Label(root,text='Result   :',font=('non 15 bold'),bg='silver')
labb.place(x=200,y=200)
but3=Button(root,padx=2,pady=2,text='Exit',command=exitt,bg='silver',font=('none 15 bold'))
but3.place(x=175,y=400)
but4=Button(root,padx=2,pady=2,text='A',command=A,width=3,height=0,bg='green',font=('none 15 bold'))
but4.place(x=30,y=90)
but5=Button(root,padx=2,pady=2,text='B',command=B,width=3,height=0,bg='green',font=('none 15 bold'))
but5.place(x=30,y=135)
but6=Button(root,padx=2,pady=2,text='C',command=C,width=3,height=0,bg='green',font=('none 15 bold'))
but6.place(x=30,y=180)
but7=Button(root,padx=2,pady=2,text='D',command=D,width=3,height=0,bg='green',font=('none 15 bold'))
but7.place(x=30,y=225)
but8=Button(root,padx=2,pady=2,text='E',command=E,width=3,height=0,bg='green',font=('none 15 bold'))
but8.place(x=30,y=270)
but9=Button(root,padx=2,pady=2,text='F',command=F,width=3,height=0,bg='green',font=('none 15 bold'))
but9.place(x=30,y=315)
but10=Button(root,padx=2,pady=2,text='G',command=G,width=3,height=0,bg='green',font=('none 15 bold'))
but10.place(x=30,y=360)
but11=Button(root,padx=2,pady=2,text='H',command=H,width=3,height=0,bg='green',font=('none 15 bold'))
but11.place(x=30,y=405)
but12=Button(root,padx=2,pady=2,text='I ',command=I,width=3,height=0,bg='green',font=('none 15 bold'))
but12.place(x=30,y=450)
but13=Button(root,padx=2,pady=2,text='J',command=J,width=3,height=0,bg='green',font=('none 15 bold'))
but13.place(x=30,y=495)
but14=Button(root,padx=2,pady=2,text='K',command=K,width=3,height=0,bg='green',font=('none 15 bold'))
but14.place(x=30,y=540)
but15=Button(root,padx=2,pady=2,text='L',command=L,width=3,height=0,bg='green',font=('none 15 bold'))
but15.place(x=30,y=585)
but16=Button(root,padx=2,pady=2,text='M',command=M,width=3,height=0,bg='green',font=('none 15 bold'))
but16.place(x=30,y=630)
but17=Button(root,padx=2,pady=2,text='N',command=N,width=3,height=0,bg='green',font=('none 15 bold'))
but17.place(x=600,y=90)
but18=Button(root,padx=2,pady=2,text='O',command=O,width=3,height=0,bg='green',font=('none 15 bold'))
but18.place(x=600,y=135)
but19=Button(root,padx=2,pady=2,text='P',command=P,width=3,height=0,bg='green',font=('none 15 bold'))
but19.place(x=600,y=180)
but20=Button(root,padx=2,pady=2,text='Q',command=Q,width=3,height=0,bg='green',font=('none 15 bold'))
but20.place(x=600,y=225)
but21=Button(root,padx=2,pady=2,text='R',command=R,width=3,height=0,bg='green',font=('none 15 bold'))
but21.place(x=600,y=270)
but22=Button(root,padx=2,pady=2,text='S',command=S,width=3,height=0,bg='green',font=('none 15 bold'))
but22.place(x=600,y=315)
but23=Button(root,padx=2,pady=2,text='T',command=T,width=3,height=0,bg='green',font=('none 15 bold'))
but23.place(x=600,y=360)
but24=Button(root,padx=2,pady=2,text='U',command=U,width=3,height=0,bg='green',font=('none 15 bold'))
but24.place(x=600,y=405)
but25=Button(root,padx=2,pady=2,text='V',command=V,width=3,height=0,bg='green',font=('none 15 bold'))
but25.place(x=600,y=450)
but26=Button(root,padx=2,pady=2,text='W',command=W,width=3,height=0,bg='green',font=('none 15 bold'))
but26.place(x=600,y=495)
but27=Button(root,padx=2,pady=2,text='X',command=X,width=3,height=0,bg='green',font=('none 15 bold'))
but27.place(x=600,y=540)
but27=Button(root,padx=2,pady=2,text='Y',command=Y,width=3,height=0,bg='green',font=('none 15 bold'))
but27.place(x=600,y=585)
but28=Button(root,padx=2,pady=2,text='Z',command=Z,width=3,height=0,bg='green',font=('none 15 bold'))
but28.place(x=600,y=630)
canvas.pack()
root.mainloop()
