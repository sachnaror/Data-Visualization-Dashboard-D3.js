import json
import os

from data_visualization.models import DataPoint
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Loads data from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str,
                            help='Path to the JSON file containing the data')

    def handle(self, *args, **options):
        # Path to the JSON file
        json_file_path = options['json_file']

        # Ensure the file exists
        if not os.path.isfile(json_file_path):
            raise CommandError(
                'File "{}" does not exist.'.format(json_file_path))

        # Open and load the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)

            # Iterate over each entry in the JSON data
            for entry in data:
                try:
                    # Create and save a new DataPoint instance
                    DataPoint.objects.create(
                        intensity=entry['intensity'],
                        likelihood=entry['likelihood'],
                        relevance=entry['relevance'],
                        year=entry['year'],
                        country=entry['country'],
                        topics=entry['topics'],
                        region=entry['region'],
                        city=entry['city']
                    )
                except Exception as e:
                    # If an error occurs, print it and skip to the next entry
                    print(f"Error loading entry: {e}")
                    continue

        self.stdout.write(self.style.SUCCESS(
            'Successfully loaded data from "{}"'.format(json_file_path)))
