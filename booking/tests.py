from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from .models import Appointment

class BookingTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.service = 'Test Service'
        self.day = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')

    def test_booking_submit(self):
        self.client.force_login(self.user)

        # Submit booking with no service selected
        response = self.client.post(reverse('booking'), {'day': self.day})
        self.assertEqual(response.status_code, 302)  # Should redirect to booking page again
        self.assertEqual(response.url, reverse('booking'))

        # Submit booking with no day selected
        response = self.client.post(reverse('booking'), {'service': self.service})
        self.assertEqual(response.status_code, 302)  # Should redirect to booking page again
        self.assertEqual(response.url, reverse('booking'))

        # Submit booking with valid service and day
        response = self.client.post(reverse('booking'), {'service': self.service, 'day': self.day})
        self.assertEqual(response.status_code, 302)  # Should redirect to booking submit page
        self.assertEqual(response.url, reverse('bookingSubmit'))

        # Try to submit booking again with the same service and day
        response = self.client.post(reverse('booking'), {'service': self.service, 'day': self.day})
        self.assertEqual(response.status_code, 302)  # Should redirect to booking submit page
        self.assertEqual(response.url, reverse('bookingSubmit'))

        # Submit booking with valid service, day and time
        time = '10:00 AM'
        response = self.client.post(reverse('bookingSubmit'), {'time': time})
        self.assertEqual(response.status_code, 302)  # Should redirect to index page
        self.assertEqual(response.url, reverse('index'))
        appointment = Appointment.objects.get(user=self.user, service=self.service, day=self.day, time=time)
        self.assertIsNotNone(appointment)

    def test_booking_submit_out_of_range(self):
        self.client.force_login(self.user)

        # Submit booking with valid service but day outside range
        day = (datetime.now() + timedelta(days=22)).strftime('%Y-%m-%d')
        response = self.client.post(reverse('booking'), {'service': self.service, 'day': day})
        self.assertEqual(response.status_code, 302)  # Should redirect to booking page again
        self.assertEqual(response.url, reverse('booking'))
        self.assertFalse(Appointment.objects.filter(user=self.user, service=self.service, day=day).exists())

    def test_booking_submit_full_day(self):
        self.client.force_login(self.user)

        # Book all appointments for the day
        for i in range(11):
            time = '10:00 AM'
            Appointment.objects.create(user=self.user, service=self.service, day=self.day, time=time)

        # Try to book one more appointment for the day
        response = self.client.post(reverse('booking'), {'service': self.service, 'day': self.day})
        self.assertEqual(response.status_code, 302)  # Should redirect to booking page again
        self.assertEqual(response.url, reverse('booking'))
        self.assertFalse(Appointment.objects.filter(user=self.user, service=self.service, day=self.day).exists())
