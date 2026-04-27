from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: Nenhuma preparação específica necessária, pois os dados estão no app
    
    # Act: Fazer a requisição GET para /activities
    response = client.get("/activities")
    
    # Assert: Verificar status e estrutura da resposta
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"]["participants"], list)

def test_signup_for_activity():
    # Arrange: Definir email e atividade para teste
    email = "newstudent@mergington.edu"
    activity_name = "Chess Club"
    
    # Act: Fazer a requisição POST para inscrição
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    
    # Assert: Verificar sucesso e adição à lista
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    
    # Verificar se o participante foi adicionado
    response = client.get("/activities")
    data = response.json()
    assert email in data[activity_name]["participants"]

def test_signup_activity_not_found():
    # Arrange: Usar uma atividade inexistente
    email = "test@mergington.edu"
    invalid_activity = "NonExistent"
    
    # Act: Tentar inscrição
    response = client.post(f"/activities/{invalid_activity}/signup?email={email}")
    
    # Assert: Verificar erro 404
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]

# Adicione mais testes AAA para duplicatas, limite de participantes, etc.