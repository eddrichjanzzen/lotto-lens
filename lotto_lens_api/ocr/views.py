import ocrspace
from django.http import JsonResponse

def ocr_endpoint(request):
    api = ocrspace.API()

    if request.method == 'POST' and request.FILES.get('image'):
        # Assuming 'image' is the name of the file input field
        uploaded_image = request.FILES['image']

        # Perform OCR on the uploaded image
        result = api.ocr_file(uploaded_image)

        return JsonResponse(result)
    else:
        return JsonResponse({'error': 'Invalid request'})
