# 07 — Rúbrica de Evaluación

## Criterios y pesos

| Criterio | Peso | Evidencia requerida |
|---|---|---|
| **Funcionamiento backend / API** | 25% | Endpoints obligatorios funcionando, validaciones correctas, códigos HTTP apropiados |
| **Arquitectura y buenas prácticas** | 20% | Separación por capas, manejo de errores, estructura limpia del código |
| **Frontend e integración** | 20% | Pantallas funcionales, consumo real de la API, diseño responsivo |
| **Git, Gitflow y versionamiento** | 15% | Ramas correctas, commits semánticos, tags SemVer |
| **Documentación e informe técnico** | 10% | Swagger, README, informe con evidencias y capturas |
| **Sustentación y demo** | 10% | Explicación técnica, pruebas en vivo, defensa de decisiones |

**Total: 100%**

---

## Criterios de calidad institucional

Estos son requisitos indispensables — su ausencia puede significar no recibir la entrega:

### README obligatorio
Todo repositorio entregado debe incluir un archivo `README.md` con:
- Descripción del proyecto
- Instrucciones para clonar el repositorio
- Instrucciones para instalar dependencias
- Instrucciones para ejecutar localmente

> ⛔ Sin este documento, la entrega **no será recibida**.

### No datos hardcodeados en el frontend
Cuando la API de la Actividad 1 esté desplegada y operativa, el frontend **debe** consumir sus endpoints reales. No se acepta un frontend que muestre datos quemados en el código.

### Demo en vivo en la sustentación
Cada equipo debe demostrar en vivo al menos este flujo completo:
1. Listar pedidos
2. Crear un pedido nuevo
3. Editar un ítem del pedido
4. Verificar que el `totalAmount` se recalcula correctamente

### Evidencias requeridas en sustentación
- Repositorio en GitHub (mostrar ramas, commits y tags)
- Despliegue en la nube (mostrar URL funcional)
- Documentación Swagger/OpenAPI (abrir en el navegador)
- Ejecución de pruebas en tiempo real
