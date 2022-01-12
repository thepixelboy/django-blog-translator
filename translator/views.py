from django.shortcuts import render


# Create your views here.
def translator_view(request):
    if request.method == "POST":
        origin_text = request.POST["origin_text"]
        translated_text = origin_text.upper()
        return render(
            request,
            "translator.html",
            {"origin_text": origin_text, "translated_text": translated_text},
        )
    else:
        return render(request, "translator.html")
