{% if latest_FacilityID %}
    <ul>
    {% for FacilityID in latest_FacilityID %}
        <li><a href="/polls/{{ FacilityID }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
