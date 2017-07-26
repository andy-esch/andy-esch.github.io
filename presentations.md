---
layout: default
title: Presentations
---

{% assign curr_time = "now" | date: "%Y-%m-%d %H:%M" %}
{% assign past_events = site.data.talks | where_exp:"item", "item.date < curr_time" | sort: 'date' | reverse %}
{% assign future_events = site.data.talks | where_exp:"item", "item.date >= curr_time" | sort: 'date' %}

## [](#conferences)Conferences and Annual Meetings

A sample of talks given at conferences and annual meetings. Materials and recordings are given when available.

### [](#upcoming-confs)Upcoming


<dl class="talk-list">
{% for event in future_events %}
    <dt>{% if event.conf_url != "" %}
          <a href="{{ event.conf_url }}">{{ event.name }}</a>
        {% else %}
	  {{ event.name }}
        {% endif %}
	- {{ event.location }} <span class="talk-date">{{ event.date | date_to_string }}</span>
    </dt>
    <dd><span class="talk-title">{{ event.title }}</span> {% if event.slides_url != "" %} (<a href="{{ event.slides_url }}">slide deck</a>) {% endif %}</dd>
    {% if event.description %}<dd>{{ event.description }}</dd>{% endif %}
{% endfor %}
</dl>

### [](#past-confs)Past

<dl class="talk-list">
{% for event in past_events %}
    <dt>{% if event.conf_url != "" %}
          <a href="{{ event.conf_url }}">{{ event.name }}</a>
        {% else %}
	  {{ event.name }}
        {% endif %}
	- {{ event.location }} <span class="talk-date">{{ event.date | date_to_string }}</span>
    </dt>
    <dd><span class="talk-title">{{ event.title }}</span>
        {% if event.slides_url != "" %}
	    (<a href="{{ event.slides_url }}">slide deck</a>)
        {% endif %}
    </dd>
    {% if event.description %}
        <dd>{{ event.description }}</dd>
    {% endif %}
{% endfor %}
</dl>

## [](#workshops)Workshops and Presentations

{% assign workshops = site.data.workshops | sort: 'date' | reverse %}

I have given more workshops than I can remember, so what is below is a small sample of the ones that live online and are diverse in content.

<dl class="talk-list">
{% for workshop in workshops %}
    {% capture talkLinks %}
      {% if workshop.writeup or workshop.venueListing %}
        {% if workshop.writeup %}
          <a href="{{ workshop.writeup }}">Writeup</a>{% if workshop.venueListing %}, {% endif %}
        {% endif %}
        {% if workshop.venueListing %}
          <a href="{{ workshop.venueListing }}">Event listing</a>
        {% endif %}
      {% endif %}
    {% endcapture %}
    <dt>
      {{ workshop.title }} <span class="talk-date">{{ workshop.date | date_to_string }}</span>
   </dt>
   {% if talkLinks %}
      <dd>{{ talkLinks }}</dd>
   {% endif %}
   {% if workshop.description %}
           <dd>{{ workshop.description }}</dd>
   {% endif %}
   <dd class="workshop-skills venue">
     <span class="workshop-meta-cat">Venue</span>
       {% if workshop.venueListing %}
         <a href="{{ workshop.venueListing }}">{{ workshop.venue }}</a>,
       {% else %}{{ workshop.venue }},
       {% endif %} {{ workshop.location }}
   </dd>
       {% if workshop.skills %}
         <dd class="workshop-skills"><span class="workshop-meta-cat">Skills</span> {{ workshop.skills | join: ', ' }}</dd>
       {% endif %}
{% endfor %}
</dl>

## [](#cartocamp)CartoCamp

I run a meetup called [CartoCamp](https://meetup.com/cartocamp/) that teaches skills tangential to web mapping and spatial data science.

{% include footer.html %}
