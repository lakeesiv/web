
def test_pages(app, client):
    del app
    pages = ["","about","projects","blog","contact"]

    for page in pages:
        print(page)
        res = client.get(f"/{page}")
        assert res.status_code == 200 or 308

def test_project_pages(app, client):
    del app
    pages = ["etoh","flask-website","x-ray-cnn"]

    for page in pages:
        print(page)
        res = client.get(f"projects/{page}")
        assert res.status_code == 200 or 308
