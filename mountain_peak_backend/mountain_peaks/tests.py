from django.contrib.gis.geos import Point
from django.test import Client, TestCase
from mountain_peaks.models import MountainPeak

# Create your tests here.


class MountainPeaksTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        mont_blanc_coordinates = Point(x=6.865575, y=45.832119)
        cls.mont_blanc = MountainPeak.objects.create(name="Mont Blanc", altitude=4_696, coordinates=mont_blanc_coordinates)
        cls.client = Client()

    def test_list_mountain_peaks(self):
        response = self.client.get("/api/v1/mountains_peaks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # type: ignore

    def test_get_mountain_peak(self):
        response = self.client.get(f"/api/v1/mountains_peaks/{self.mont_blanc.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_list_mountains_in_bbox(self):
        response = self.client.get("/api/v1/mountains_peaks/?in_bbox=6.92,45.87,6.99,45.81")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)  # type: ignore

        response = self.client.get("/api/v1/mountains_peaks/?in_bbox=6.92,45.87,6.99,45.81")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)  # type: ignore

    def test_mountain_peak_view(self):
        response = self.client.post(
            path="/api/v1/mountains_peaks/",
            data={"name": "Everes", "altitude": 8_848, "coordinates": "POINT(86.922622 27.986064)"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(MountainPeak.objects.filter(name="Everes").count(), 1)

        response = self.client.put(
            path=f"/api/v1/mountains_peaks/{self.mont_blanc.pk}/",
            data={"name": "Everest", "altitude": 8_848, "coordinates": "POINT(86.922623 27.986065)"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        updated_everest = MountainPeak.objects.get(pk=self.mont_blanc.pk)
        self.assertEqual(updated_everest.name, "Everest")
        self.assertEqual(updated_everest.longitude, 86.922623)
        self.assertEqual(updated_everest.latitude, 27.986065)

        response = self.client.patch(
            path=f"/api/v1/mountains_peaks/{self.mont_blanc.pk}/",
            data={"altitude": 8_849},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        updated_everest = MountainPeak.objects.get(pk=self.mont_blanc.pk)
        self.assertEqual(updated_everest.altitude, 8_849)

        response = self.client.delete(
            path=f"/api/v1/mountains_peaks/{self.mont_blanc.pk}/",
        )
        self.assertEqual(MountainPeak.objects.filter(name="Everest").count(), 0)
