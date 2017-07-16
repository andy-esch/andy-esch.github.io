---
layout: default
---

{% assign curr_time = "now" | date: "%Y-%m-%d %H:%M" %}
{% assign past_events = site.data.talks | where_exp:"item", "item.date < curr_time" | sort: 'date' | reverse %}
{% assign future_events = site.data.talks | where_exp:"item", "item.date >= curr_time" | sort: 'date' | reverse %}

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
    <dd><span class="talk-title">{{ event.title }}</span> {% if event.slides_url != "" %} (<a href="{{ event.slides_url }}">slide deck</a>) {% endif %}</dd>
    {% if event.description %}<dd>{{ event.description }}</dd>{% endif %}
{% endfor %}
</dl>

## [](#workshops)Workshops and Presentations

The following are workshops and presentations given, usually educational in nature. This is a placeholder until events are added.

<dl class="talk-list">
        <dt><a href="https://course.tc/catalog/course/ea5f4a23-743b-4e47-9eaf-6104fb45dad1">Mapping for Social Good at TechChange</a></dt>
	<dd>Teach web mapping skills</dd>
	<dt>New York City Data Science Academy</dt>
	<dd>Introduction to using CARTO's Builder and APIs for data science work</dd>
</dl>

## [](#cartocamp)CartoCamp

I run a meetup called [CartoCamp](https://meetup.com/cartocamp/) that teaches skills tangential to web mapping and spatial data science.

{% include footer.html %}
