from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Document, Company
from .serializers import DocumentSerializer
import requests

@api_view(['POST'])
def create_document(request):
    """
    Crea un documento usando la API de ZapSign y guarda la respuesta en la base de datos.
    """
    try:
        data = request.data
        company = Company.objects.get(id=data.get('company_id'))

        payload = {
            "name": data.get("name"),
            "file_url": data.get("file_url"),
            "signers": data.get("signers"),
        }

        # Enviar solicitud a la API de ZapSign
        headers = {
            "Authorization": f"Token {company.api_token}"
        }
        response = requests.post(
            "https://sandbox.api.zapsign.com.br/api/v1/docs/",
            headers=headers,
            json=payload
        )

        if response.status_code == 201:
            # Guardar respuesta en la base de datos
            document_data = response.json()
            document = Document(
                openID=document_data["id"],
                token=document_data["token"],
                name=document_data["name"],
                status=document_data["status"],
                company=company
            )
            document.save()
            return Response(DocumentSerializer(document).data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Error al crear documento en ZapSign"}, status=response.status_code)

    except Company.DoesNotExist:
        return Response({"error": "Compañía no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)