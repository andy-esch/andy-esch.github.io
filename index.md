---
layout: default
---

## [Projects](projects.html)

<div class="clearfix item-desc">
	<figure>
		<a href="/projects.html#honeymoon-mapping"><img src="/assets/img/honeymoon.png" alt="honeymoon map" width="240" /></a>
		<figcaption>Map of honeymoon journey from Beijing, China to St. Petersburg, Russia</figcaption>
	</figure>
	<div>Projects covering work on coding, math, and maps. Includes projects like a Python package for interacting with CARTO's services, an effort to find the best place to live, and a program to teach the military phonetic alphabet.</div>
</div>

## [Presentations](presentations.html)

<div class="clearfix item-desc">
	<figure>
		<img src="/assets/img/foss4g-seoul-2015.jpg" alt="Andy Eschbacher at FOSS4G Seoul, South Korea Sept 2015" />
		<figcaption>FOSS4G Seoul, South Korea. Image by <a href="http://www.how2map.com/2015/09/">Jody Garnett</a></figcaption>
	</figure>
	<div>Presentations I've given at conferences, annual meetings, workshops at universities or bootcamps, and other educational work.</div>
</div>

## [Blog](blog.html)

<ul class="post-list">
	{% for post in site.posts limit:5 %}
		<li>
			{% assign date_format = "%b %-d, %Y" %}
			<span class="post-meta">
				{{ post.date | date: date_format }}
			</span>
			<h3>
				<a class="post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
			</h3>
		</li>
	{% endfor %}
</ul>

<p class="post-info"><a href="/blog.html">See full listing of blog posts</a></p>

<p class="post-info rss-subscribe">Subscribe <a href="{{ "/feed.xml" | relative_url }}">via RSS</a></p>
