from django.shortcuts import render
import random

def home(request):
    template_name = "halaman/index.html"
    context = {
        'title' : 'selamat datang di halaman home',
        'umur' : 21,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"
    context = {
        'title' : 'selamat datang halaman about',
        'umur' : 21,
    }
    return render(request, template_name, context)

def kutipan(request):
    template_name = "kutipan.html"
    quotes = [
        "Doa memberikan kekuatan pada orang yang lemah, membuat orang tidak percaya "
        "menjadi percaya dan memberikan keberanian pada orang yang ketakutan - Aristoteles.",
        "Orang yang berilmu mengetahui orang yang bodoh karena dia pernah bodoh,sedangkan orang "
        "yang bodoh tidak mengetahui orang yang berilmu karena dia tidak pernah berilmu. - Plato",
        "Cobalah dulu, baru cerita. Pahamilah dulu, baru menjawab. Pikirlah dulu, baru berkata. "
        "Dengarlah dulu, baru beri penilaian. Bekerjalah dulu, baru berharap. - Socrates.",
        "Waktu adalah yang paling bijaksana dari semua hal yang ada, " 
        "karena itu menjadikan segalanya terang” - Thales.",
        "Wahai anak muda, jika engkau tidak sanggup menahan lelahnya belajar, "
        "engkau harus menanggung pahitnya kebodohan. - Phytaghoras."
    ]
    quote = random.choice(quotes)
    return render(request, template_name, {'quote': quote})