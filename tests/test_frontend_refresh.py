from pathlib import Path


def test_signup_flow_refreshes_activity_list_after_success():
    app_js = Path("src/static/app.js").read_text()

    assert 'messageDiv.className = "success";' in app_js
    assert 'signupForm.reset();' in app_js
    assert 'await fetchActivities();' in app_js
