<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Knihovna</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        header, nav { background-color: #eee; padding: 10px; }
        main { padding: 20px; }
    </style>
</head>
<body>
    {% include "header.html" %}
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
