from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def result(request):
    #! GET DATA in STIRING QUERY DATA
    fullText = request.GET['fulltext']
    words = fullText.split()
    lenWords = len(words)
    word_dic = {}
    for word in words:
        if word in word_dic:
            # * inc word
            word_dic[word] += 1
        else:
            # * add to dic
            word_dic[word] = 1
    return render(request, 'result.html', {'full': fullText, 'len': lenWords, 'dic': word_dic.items()})
