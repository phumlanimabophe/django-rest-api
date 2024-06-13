from .models import Customer
from rest_framework import serializers
import pandas as pd
from io import BytesIO

# Define a serializer for the Customer model
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    # Define a FileField for the excel_file attribute
    excel_file = serializers.FileField(max_length=None, use_url=True, write_only=True)
    # Define a CharField for the file_data attribute
    file_data = serializers.CharField(read_only=True)

    class Meta:
        # Specify the model to serialize
        model = Customer
        # Specify the fields to include in the serialized representation
        fields = ('first_name', 'last_name', 'date_of_birth', 'excel_file', 'file_data')

    # Override the create method to handle the excel_file attribute
    def create(self, validated_data):
        # Remove the excel_file from the validated data if it exists
        excel_file = validated_data.pop('excel_file', None)
        # Create the instance using the remaining validated data
        instance = super().create(validated_data)
        
        if excel_file is not None:
            # Read the excel_file into a pandas DataFrame
            excel_data = pd.read_excel(BytesIO(excel_file.read()))
            # Convert the DataFrame to a JSON string and assign it to file_data
            instance.file_data = excel_data.to_json(orient='records')

        # Return the created instance
        return instance

    # Override the to_representation method to customize the serialized representation
    def to_representation(self, instance):
        # Get the default serialized representation
        representation = super().to_representation(instance)
        # Return the customized representation
        return representation