from django.contrib.gis.geos import Point, Polygon
from django.test import Client, TestCase
from mountain_peaks.models import MountainPeak

# Create your tests here.


class MountainPeaksTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        mont_blanc_coordinates = Point(x=6.865575, y=45.832119)
        cls.mont_blanc = MountainPeak.objects.create(name="Mont Blanc", altitude=4_696, coordinates=mont_blanc_coordinates)

    def setUp(self):
        self.client = Client()

    def test_mountain_in_bbox(self):
        response = self.client.get("/api/v1/mountains_peaks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # type: ignore

        response = self.client.get("/api/v1/mountains_peaks/?in_bbox=6.74,45.92,7.09,45.72")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # type: ignore

        response = self.client.get("/api/v1/mountains_peaks/?in_bbox=6.92,45.87,6.99,45.81")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)  # type: ignore
