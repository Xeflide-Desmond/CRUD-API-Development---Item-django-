from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Item
from .serializers import ItemSerializer
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError

class ItemAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        # Creating test users
        self.user1 = User.objects.create_user(username="user1", password="password123")
        self.user2 = User.objects.create_user(username="user2", password="password123")

        # Creating test items
        self.item1 = Item.objects.create(name="Item 1", description="Description 1", last_modified_by=self.user1)
        self.item2 = Item.objects.create(name="Item 2", description="Description 2", last_modified_by=self.user2)

    def tearDown(self):
        Item.objects.all().delete()
        User.objects.all().delete()

    # Create Item
    def test_create_item(self):
        try:
            with transaction.atomic():
                data = {
                    "name": "New Item",
                    "description": "New Description",
                    "last_modified_by": self.user1.id
                }
                response = self.client.post(reverse('item-list-create'), data, format='json')
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(Item.objects.count(), 3)
                self.assertEqual(Item.objects.get(id=3).name, "New Item")
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during item creation!")

    # List Items
    def test_list_items(self):
        try:
            with transaction.atomic():
                response = self.client.get(reverse('item-list-create'))
                items = response.data['results']
                serializer = ItemSerializer(Item.objects.all(), many=True)
                self.assertEqual(items, serializer.data)
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during item listing!")

    # Retrieve Item
    def test_retrieve_item(self):
        try:
            with transaction.atomic():
                response = self.client.get(reverse('item-detail', kwargs={'pk': self.item1.pk}))
                item = Item.objects.get(pk=self.item1.pk)
                serializer = ItemSerializer(item)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data, serializer.data)
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during item retrieval!")

    # Update Item
    def test_update_item(self):
        try:
            with transaction.atomic():
                data = {
                    "name": "Updated Item 1",
                    "description": "Updated Description",
                    "last_modified_by": self.user1.id
                }
                response = self.client.put(reverse('item-detail', kwargs={'pk': self.item1.pk}), data, format='json')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                updated_item = Item.objects.get(pk=self.item1.pk)
                self.assertEqual(updated_item.name, "Updated Item 1")
                self.assertEqual(updated_item.description, "Updated Description")
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during item update!")

    # Delete Item
    def test_delete_item(self):
        try:
            with transaction.atomic():
                response = self.client.delete(reverse('item-detail', kwargs={'pk': self.item1.pk}))
                self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
                self.assertEqual(Item.objects.count(), 1)
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during item deletion!")

    # Test Pagination
    def test_pagination_is_applied(self):
        try:
            with transaction.atomic():
                response = self.client.get(reverse('item-list-create'), {'page': 1})
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertTrue('next' in response.data or 'previous' in response.data)
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during pagination testing!")

    # Test Filtering
    def test_filter_items_by_name(self):
        try:
            with transaction.atomic():
                # Creating additional items to filter
                Item.objects.create(name="Item 3", description="Description 3", last_modified_by=self.user2)
                Item.objects.create(name="Another Item", description="Description 4", last_modified_by=self.user2)

                # Applying the filter
                response = self.client.get(reverse('item-list-create'), {'search': 'Item 1'})
                
                # Assert that only the filtered item is returned
                self.assertEqual(len(response.data['results']), 1)
                self.assertEqual(response.data['results'][0]['name'], "Item 1")
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during item filtering!")

    # Test Validation Error
    def test_create_item_with_duplicate_name(self):
        try:
            with transaction.atomic():
                data = {
                    "name": "Item 1",
                    "description": "Duplicate Description",
                    "last_modified_by": self.user1.id 
                }
                response = self.client.post(reverse('item-list-create'), data, format='json')
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertIn('name', response.data['error'])  
                self.assertEqual(response.data['error']['name'][0].code, 'unique')
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during duplicate name test!")



    # Test Edge Cases
    def test_retrieve_nonexistent_item(self):
        try:
            with transaction.atomic():
                response = self.client.get(reverse('item-detail', kwargs={'pk': 999}))
                self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        except IntegrityError:
            self.fail("Integrity error raised unexpectedly during nonexistent item retrieval!")
