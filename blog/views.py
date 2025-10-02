from pathlib import Path
import json
from django.shortcuts import render
from django.conf import settings  

def blog(request):
    file_path = Path(settings.BASE_DIR)  /"blog"/ "data" / "posts.json"
    with open(file_path, encoding="utf-8") as fp:
        data = json.load(fp)
    img = ["1.png","2.jpg","3.webp"]    
    for i in range(3):
        data[i]["img"]= img[i]
    return render(request, 'blog/blog.html', context={"p": data[:3]})
