from rest_framework.test import APITestCase
from . import models
from users.models import User

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


class TestAmenity(APITestCase):
    NAME = "Test Amenity"
    DESC = "Test Description"
    URL = "/api/v1/rooms/amenities/{pk}"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC
        )
    
    def test_amenity_not_found(self):
        wrong_response = self.client.get(self.URL.format(pk=2))
        self.assertEqual(wrong_response.status_code, 404)

    def test_get_amenity(self):
        response = self.client.get(self.URL.format(pk=1))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESC)
    
    def test_put_amenity(self):
        amended_amenity_name = "Amended Name"
        amended_amenity_description = "Amended Description"
        response = self.client.put(self.URL.format(pk=1), data={"name": amended_amenity_name, "description": amended_amenity_description})

        self.assertEqual(response.status_code, 200)

    def test_delete_amenity(self):
        response = self.client.delete(self.URL.format(pk=1))
        self.assertEqual(response.status_code, 204)


class TestRooms(APITestCase):
    URL = "/api/v1/rooms/"

    def setUp(self):
        user = User.objects.create(username="test_user")
        user.set_password("123")
        user.save()

    def test_create_room(self):
        forbidden_response = self.client.post(self.URL)
        self.assertEqual(forbidden_response.status_code, 403)

        self.client.login(username="test_user", password="123")
        wrong_response = self.client.post(self.URL)
        self.assertEqual(wrong_response.status_code, 400)
