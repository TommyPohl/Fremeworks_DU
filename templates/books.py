{% extends "base.html" %}

{% block content %}
    <h1>Seznam kníh</h1>
    <ul>
        {% for book in books %}
            <li>
                <strong>{{ book.title }}</strong> – {{ book.author }}<br>
                {% if book.available %}
                    <span style="color: green;">Dostupná</span>
                {% else %}
                    <span style="color: red;">Vypůjčená</span>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
{% endblock %}
