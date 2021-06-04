from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email =  serializers.CharField(max_length=100)
    test_score1 = serializers.IntegerField()
    test_score2 = serializers.IntegerField()
    test_score3 = serializers.IntegerField()
    

    def create(self, validated_data):
        return Candidate.objects.create(**validated_data)
    
    def update(self, instance, validate_data):
        print(instance.name)
        instance.name = validate_data.get('name',instance.name)
        print(instance.name)
        instance.email = validate_data.get('email',instance.email)
        instance.test_score1 = validate_data.get('test_score1',instance.test_score1)
        instance.test_score2 = validate_data.get('test_score2',instance.test_score2)
        instance.test_score3 = validate_data.get('test_score3',instance.test_score3)
        instance.save()
        return instance