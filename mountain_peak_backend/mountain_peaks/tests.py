from django.contrib.gis.geos import Point, Polygon
from django.test import TestCase
from mountain_peaks.models import MountainPeak

# Create your tests here.


class MountainPeaksTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        mont_blanc_coordinates = Point(x=6.865575, y=45.832119)
        cls.mont_blanc = MountainPeak.objects.create(name="Mont Blanc", altitude=4_696, coordinates=mont_blanc_coordinates)

    def setUp(self):
        ...

    def test_mountain_in_bbox(self):
        poly = Polygon.from_bbox((6.745578979419631, 45.925101678711506, 7.092869, 45.72095))
        self.assertTrue(self.mont_blanc in MountainPeak.objects.in_bbox(bbox=poly))

        poly = Polygon.from_bbox((6.924254, 45.873148, 6.994573, 45.817374))
        self.assertFalse(self.mont_blanc in MountainPeak.objects.in_bbox(bbox=poly))
