
from rest_framework import serializers
from .models import ClientOneToOne
from .models import SgOneToOne
from .models import matched
class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientOneToOne
        fields = ('field_20','field_22a','field_22c','field_30t','field_52a','field_82a',
        	'field_87a','field_77h','field_30v','field_36','field_32b','field_57a','field_33b',
        	'field_53a','field_56','field_57d','field_58a','field_24d','id')

class SgSerializer(serializers.ModelSerializer):

    class Meta:
        model = SgOneToOne
        fields = ('field_20','field_22a','field_22c','field_30t','field_52a','field_82a',
        	'field_87a','field_77h','field_30v','field_36','field_32b','field_57a','field_33b',
        	'field_53a','field_56','field_57d','field_58a','field_24d','id')

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = matched
        fields= ('client','sg','status')