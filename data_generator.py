import pandas as pd
import numpy as np

def generate_churn_data(n=1000):
    np.random.seed(42)
    
    customer_ids = [f'CUST-{i:04d}' for i in range(1, n + 1)]
    age = np.random.randint(18, 80, size=n)
    gender = np.random.choice(['Masculino', 'Feminino'], size=n)
    tenure = np.random.randint(1, 72, size=n) # Meses como cliente
    contract_type = np.random.choice(['Mensal', 'Anual', 'Bienal'], size=n, p=[0.5, 0.3, 0.2])
    monthly_charges = np.random.uniform(50, 200, size=n).round(2)
    total_charges = (monthly_charges * tenure).round(2)
    
    # Lógica para churn (baseada em algumas variáveis)
    # Maior probabilidade para contratos mensais e menor tempo de casa
    churn_prob = np.zeros(n)
    churn_prob += (contract_type == 'Mensal') * 0.3
    churn_prob += (tenure < 12) * 0.2
    churn_prob += (monthly_charges > 150) * 0.1
    churn_prob += np.random.uniform(0, 0.4, size=n)
    
    churn = (churn_prob > 0.6).astype(int)
    churn_status = np.where(churn == 1, 'Sim', 'Não')
    
    data = pd.DataFrame({
        'CustomerID': customer_ids,
        'Idade': age,
        'Genero': gender,
        'Tempo_Meses': tenure,
        'Contrato': contract_type,
        'Mensalidade': monthly_charges,
        'Total_Gasto': total_charges,
        'Churn': churn_status
    })
    
    return data

if __name__ == "__main__":
    df = generate_churn_data()
    df.to_csv('/home/ubuntu/churn_dashboard/churn_data.csv', index=False)
    print("Dados gerados com sucesso!")
