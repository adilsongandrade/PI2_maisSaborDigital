import json
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# URL da API Externa do Simples Nacional
#API_SIMPLES_NACIONAL = 'https://simples-nacional-api.vercel.app/api/calcular_aliquota_efetiva'
# PI2_maisSaborDigital/precificacao/views.py

# ...
# URL da API Externa do Simples Nacional (CORRIGIDA)
API_SIMPLES_NACIONAL = 'https://simples-nacional-api.vercel.app/simples-nacional/aliquota-efetiva' # <--- NOVA URL!
# ...

@require_POST
@csrf_exempt 
def calcular_aliquota_proxy(request):
    try:
        data = json.loads(request.body)
        
        receita_bruta_media = data.get('receitaBrutaMedia')
        anexo_da_atividade = data.get('anexoDaAtividadeEmpresarial')
        
        if not receita_bruta_media or not anexo_da_atividade:
            return JsonResponse(
                {'error': 'Parâmetros ausentes.', 'detalhe': 'Valores de receita ou anexo não recebidos.'}, 
                status=400
            )
            
        payload_api = {
            "receitaBrutaMedia": float(receita_bruta_media),
            "anexoDaAtividadeEmpresarial": anexo_da_atividade
        }
        
        # Chamada HTTP POST para a API externa
        response_api = requests.post(
            API_SIMPLES_NACIONAL, 
            json=payload_api, 
            timeout=10
        )
        
        # Tenta ler o JSON da resposta da API externa
        response_json = response_api.json()
        
        # Verifica se a chamada externa foi bem-sucedida (Status 200)
        if response_api.status_code == 200:
            # Verifica se a chave esperada existe (previne o erro 'undefined')
            if 'aliquotaEfetiva' not in response_json:
                 return JsonResponse(
                    {'error': 'Resposta da API Simples Nacional incompleta.', 
                     'detalhe': 'Chave aliquotaEfetiva não encontrada no JSON de resposta.'}, 
                    status=500
                )
            
            # Retorna o JSON completo da API externa para o frontend
            return JsonResponse(response_json)
        else:
            # Retorna o erro da API externa, se não for 200
            return JsonResponse(
                {'error': 'Erro ao consultar API externa do Simples Nacional', 
                 'detalhe': response_api.text}, 
                status=response_api.status_code
            )

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Corpo da requisição inválido (JSON não formatado)'}, status=400)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Erro de conexão com a API externa: {str(e)}'}, status=503)
    except Exception as e:
        return JsonResponse({'error': f'Erro interno no proxy: {str(e)}'}, status=500)