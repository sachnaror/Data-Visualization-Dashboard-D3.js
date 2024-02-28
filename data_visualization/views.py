from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataPoint
from .serializers import DataPointSerializer


# Create your views here.
class Command(BaseCommand):
    help = 'Load data from JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file path')

    def handle(self, *args, **kwargs):
        file_path = kwargs['json_file']
        with open(file_path, 'r') as file:
            data = json.load(file)
            for entry in data:
                DataPoint.objects.create(
                    intensity=entry['intensity'],
                    likelihood=entry['likelihood'],
                    relevance=entry['relevance'],
                    year=entry['year'],
                    country=entry['country'],
                    topics=entry['topics'],
                    region=entry['region'],
                    city=entry['city']
                    # Add other fields as necessary
                )
            self.stdout.write(self.style.SUCCESS(
                f"Successfully loaded data from {file_path}"))


def datapoint_list(request):
    datapoints = DataPoint.objects.all()
    serializer = DataPointSerializer(datapoints, many=True)
    return JsonResponse(serializer.data, safe=False)


class DataPointList(APIView):
    def get(self, request, format=None):
        data_points = DataPoint.objects.all()
        serializer = DataPointSerializer(data_points, many=True)
        return Response(serializer.data)


def get(self, request, format=None):
    queryset = DataPoint.objects.all()

    # Example for filtering by year
    year = request.query_params.get('year')
    if year is not None:
        queryset = queryset.filter(year=year)

    # Implement other filters similarly

    serializer = DataPointSerializer(queryset, many=True)
    return Response(serializer.data)
