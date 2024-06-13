
from .models import Customer
from rest_framework import serializers
from .models import Customer
import pandas as pd
from io import BytesIO

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    excel_file = serializers.FileField(max_length=None, use_url=True, write_only=True)
    file_data = serializers.CharField(read_only=True)

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'date_of_birth', 'excel_file', 'file_data')



    def create(self, validated_data):
        excel_file = validated_data.pop('excel_file', None)
        instance = super().create(validated_data)
        
        if excel_file is not None:
            # Read the excel_file into a pandas DataFrame
            excel_data = pd.read_excel(BytesIO(excel_file.read()))
            # Convert the DataFrame to a JSON string and assign it to file_data
            instance.file_data = excel_data.to_json(orient='records')
            instance.save()


        instance = super().create(validated_data)
        
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation