---
layout: default
---

{% assign curr_time = "now" | date: "%Y-%m-%d %H:%M" %}
{% assign past_events = site.data.talks | where_exp:"item", "item.date < curr_time" | sort: 'date' | reverse %}
{% assign future_events = site.data.talks | where_exp:"item", "item.date >= curr_time" | sort: 'date' | reverse %}

## Conferences and Annual Meetings 

Talks given at conferences and annual meetings. Materials and recordings are given when available.

### Upcoming


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

### Past 

<dl class="talk-list">
{% for event in past_events %}
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

## Workshops and Presentations

The following are workshops and presentations given, usually educational in nature.

<dl class="talk-list">
	<dt>New York City Data Science Academy</dt>
	<dd>Introduction to using CARTO's Builder and APIs for data science work</dd>
</dl>

## CartoCamp

I run a meetup called [CartoCamp](https://meetup.com/cartocamp/) that teaches skills tangential to web mapping and spatial data science.

{% include footer.html %}