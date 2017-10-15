# Django-Conektatest

Despliegue de catpura de datos de tarjeta con tokenización en ambiente de pruebas - es posible tomar datos de esta fuente (http://generatarjetasdecredito.com/generador-tarjetas-visa.php) -, genera un cliente relacionado al token generado y genera un cargo a la tarjeta capturada. 
Se muestra el estatus de pago, monto y ID de Orden y Cliente generado. 

## Excepciones
La primera validación se realiza sobre el campo de captura de número de tarjeta. Con una función de que busca tarjetas que inicien con el número 4 y sean de 13 o 16 de longitud (https://www.bbva.es/general/finanzas-vistazo/tarjetas/numero-tarjeta-visa-mastercard/index.jsp). En caso de no cumplir con ese criterio, el botón para generación de token ser bloqueado. 
Como siguiente validación se realizan las validaciones a partir de el JS de Conekta.

# Pruebas
Para realizar pruebas acceder a la siguiente URL (https://namestse.herokuapp.com/)
