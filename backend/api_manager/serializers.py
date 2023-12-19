from rest_framework import serializers
from .models import Order, Customer, Contact, Location, Pickup, Delivery, Driver

# CREATE SERIALIZERS FOR EACH MODEL THAT WILL BE USED AS AN BACKEND API

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['location_id', 'location_name', 'street_address', 'city', 'state', 'zip_code', 'country_code', 'onsite_instructions', 'location_details']

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    location = LocationSerializer()
    
    class Meta:
        model = Customer
        fields = ['created', 'customer_id', 'customer_name', 'location']
        
class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ['driver_id','driver_name','driver_email','driver_paperwork','driver_created','dba','driver_start_date','driver_inactive','driver_inactive_date','vehicle_type','vehicle_make','vehicle_model','vehicle_year','vehicle_color']
        
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    customer = CustomerSerializer()
    
    class Meta:
        model = Contact
        fields = ['created', 'customer', 'contact_id', 'first_name', 'last_name', 'work_number', 'mobile_number', 'email']

class PickupSerializer(serializers.HyperlinkedModelSerializer):
    contact = ContactSerializer()
    location = LocationSerializer()
    
    class Meta:
        model = Pickup
        fields = ['pickup_id', 'contact', 'location', 'pu_arrival_time', 'pu_depart_time']

class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    contact = ContactSerializer()
    location = LocationSerializer()
    
    class Meta:
        model = Delivery
        fields = ['delivery_id', 'contact', 'location', 'del_arrival_time', 'del_depart_time']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    pickup = PickupSerializer()
    delivery = DeliverySerializer()
    customer = CustomerSerializer()
    driver = DriverSerializer()
    
    class Meta:
        model = Order
        fields = ['customer', 'driver', 'pickup', 'delivery', 'time_placed', 'order_id', 'order_type', 'order_complete', 'time_open', 'time_to_complete']
