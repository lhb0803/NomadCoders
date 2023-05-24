from rest_framework.test import APITestCase
from . import models

class TestAmenities(APITestCase):
    NAME = "Amenity Test"
    DESC = "Amenity Description"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amaenities(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 200, "Status code isn't 200.")
        self.assertIsInstance(data, list, "Data type is not List")
        
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)
        self.assertEqual(data[0]["description"], self.DESC)
    
    def test_create_amenity(self):
        new_amenity_name = "New Amenity"
        new_amenity_description = "New Description"
        response = self.client.post(self.URL, data={"name": new_amenity_name, "description": new_amenity_description})
        data = response.json()

        self.assertEqual(response.status_code, 200, "Status code isn't 200.")
        self.assertEqual(data["name"], new_amenity_name)
        self.assertEqual(data["description"], new_amenity_description)

        wrong_response = self.client.post(self.URL)
        self.assertEqual(wrong_response.status_code, 400, "Status code isn't 400.")
