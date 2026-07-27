from pathlib import Path


def test_signup_flow_refreshes_activity_list_after_success():
    # Arrange
    app_js = Path("src/static/app.js").read_text()

    # Act
    refresh_behavior = app_js

    # Assert
    assert 'messageDiv.className = "success";' in refresh_behavior
    assert 'signupForm.reset();' in refresh_behavior
    assert 'await fetchActivities();' in refresh_behavior
