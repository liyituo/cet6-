import json

with open('temp_sikefix/public/lessons-data.js', 'r', encoding='utf-8') as f:
    c = f.read()
start = c.find('[')
end = c.rfind(']') + 1
data = json.loads(c[start:end])

print(f"Total lessons: {len(data)}")
for item in data:
    yr = item.get('year')
    if int(yr) <= 2021:
        print(f"ID: {item.get('id'):25s} | Year: {yr} | Title: {item.get('title')[:35]} | Answer: {item.get('answerCode')}")
