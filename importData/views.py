from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
import pandas as pd
from .models import Person

class ExcelUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):
        file = request.FILES['file']
        try:
            data = pd.read_excel(file)
            for _, row in data.iterrows():
                name = row['Name']
                email = row['Email']
                location = row['Location']
                Person.objects.create(name=name, email=email, location=location)

            return Response({'message': 'Data uploaded successfully'})
        except Exception as e:
            return Response({'message': f'Error uploading data: {str(e)}'}, status=400)
