import requests

requests.get("http://127.0.0.1:7776")

requests.post("http://127.0.0.1:7776/games", json={
    "name": "spiderman",
    "studio": "sony",
     "total_hours": 20,
    "hours_played": 10,
 })
requests.post("http://127.0.0.1:7776/games", json={
    "name": "spiderman",
    "studio": "sony",
    "total_hours": 20,
    "hours_played": 10,
})

# requests.delete("http://127.0.0.1:7776/games/spiderman")

requests.put("http://127.0.0.1:7776/games/spiderman", json={"hours_played": 5})
# requests.put("http://127.0.0.1:7776/games/spiderman", json={"hours_played": 5})