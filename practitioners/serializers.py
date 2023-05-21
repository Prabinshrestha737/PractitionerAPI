from rest_framework import serializers
from .models import Practitioner, Qualification, Communication


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['code', 'period_start', 'period_end', 'issuer']


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = ['language', 'preferred']


class PractitionerSerializer(serializers.ModelSerializer):
    qualifications = QualificationSerializer(many=True)
    communications = CommunicationSerializer(many=True)

    class Meta:
        model = Practitioner
        fields = [
            'id', 'active', 'name',
            'telecom', 'gender', 'birth_date', 'deceased',
            'address', 'photo', 'qualifications', 'communications'
        ]

    def create(self, validated_data):
        qualifications_data = validated_data.pop('qualifications')
        communications_data = validated_data.pop('communications')

        practitioner = Practitioner.objects.create(**validated_data)

        for qualification_data in qualifications_data:
            Qualification.objects.create(
                practitioner=practitioner, **qualification_data
            )

        for communication_data in communications_data:
            Communication.objects.create(
                practitioner=practitioner, **communication_data
            )

        return practitioner
