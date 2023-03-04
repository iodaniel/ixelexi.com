from django.test import TestCase
from django.urls import reverse
from booking.models import Appointment



class BookingTestCase(TestCase):

    def test_create_appointment_hifu_face(self):
        # Creamos una cita de HIFU Face
        appointment = Appointment.objects.create(service='HIFU Face')

        # Verificamos que la cita fue creada exitosamente
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.service, 'HIFU Face')    
 
    def test_create_appointment_time(self):
        # Creamos una cita de HIFU Face
        appointment = Appointment.objects.create(time='11:00 AM')

        # Verificamos que la cita fue creada exitosamente
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.time, '11:00 AM')    

    def test_create_bad_appointment_time(self):
        # Creamos una cita de HIFU Face
        appointment = Appointment.objects.create(time='11:30 AM')

        # Verificamos que la cita fue creada exitosamente
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.time, '11:30 AM')  

def test_create_bad_appointment_time(self):
        # Creamos una cita de HIFU Face
        appointment = Appointment.objects.create(time='11:30 AM')

        # Verificamos que la cita fue creada exitosamente
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.time, '11:30 AM')    
