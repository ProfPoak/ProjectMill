from utils.storage import save, load

# Save and Load Tests
def test_save_and_load_returns_same_data(tmp_path):
    file = tmp_path / "test_db.json"
    data = {"users": [{"id": 1, "name": "John", "email": "john@doe.com"}]}
    
    save(data, path=file)
    result = load(path=file)
    
    assert result == data

def test_save_and_load_preserves_project_task_relationship(tmp_path):
    file = tmp_path / "test_db.json"
    
    data = {
        "projects": [
            {
                "id": 1,
                "title": "identify John",
                "description": "Contact potential family/acquaintances",
                "due_date": "2026-04-25",
                "tasks": [
                    {
                        "id": 1,
                        "title": "Call",
                        "status": "To Do",
                        "assigned_to": "John"
                    }
                ]
            }
        ]
    }
    
    save(data, path=file)
    result = load(path=file)
    
    # Check the relationship is preserved
    assert len(result["projects"]) == 1
    assert len(result["projects"][0]["tasks"]) == 1
    assert result["projects"][0]["tasks"][0]["title"] == "Call"

# Error Handling Tests
def test_load_missing_file_returns_empty(tmp_path):
    file = tmp_path / "nonexistent.json"
    result = load(path=file)
    assert result == {}

def test_load_empty_file_returns_empty(tmp_path):
    file = tmp_path / "empty.json"
    file.write_text("")
    result = load(path=file)
    assert result == {}

def test_load_malformed_json_returns_empty(tmp_path):
    file = tmp_path / "bad.json"
    file.write_text("this is not json {{{")
    result = load(path=file)
    assert result == {}