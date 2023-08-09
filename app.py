import streamlit as st

def main():
    st.title("Calculadora de Inversión en AMEX Club Token")
    
    # Ingreso del valor actual del token
    token_value = st.number_input("Ingrese el valor actual del AMEX Club Token:", step=0.01)

    # Cantidad de tokens en tu inversión
    token_amount = 61307555617432

    # Calcular el valor actual de la inversión
    investment_value = token_value * token_amount
    investment_value = '{:,.2f}'.format(investment_value)
    # Mostrar el resultado
    token_amount = '{:,.0f}'.format(token_amount)
    st.caption(f'Total de Tokens: {token_amount}')
    st.write("El valor actual de tu inversión en AMEX Club Token es:")
    st.subheader(f'{investment_value} USD')
if __name__ == "__main__":
    main()
