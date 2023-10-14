import ocrspace
from django.http import JsonResponse
from ocr.utils.process_image import process_image
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def ocr_endpoint(request):
    api = ocrspace.API()

    if request.method == 'POST' and request.FILES.get('image'):
        # Assuming 'image' is the name of the file input field
        uploaded_image = request.FILES['image']
        processed_image = process_image(uploaded_image)

        # Perform OCR on the uploaded image
        result = api.ocr_file(processed_image)

        response = {
            "text": result
        }

        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid request'})
