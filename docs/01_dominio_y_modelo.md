# 01 — Dominio y Modelo de Datos

## Relación entre entidades

```
Customer 1 --- N Order 1 --- N OrderItem N --- 1 Product N --- 1 Supplier
```

El agregado principal de la API es **Order**. Desde un pedido se acceden todas las demás entidades relacionadas.

---

## Entidades y campos

### Customer (Cliente)
| Campo | Tipo |
|---|---|
| id | número entero |
| firstName | texto |
| lastName | texto |
| city | texto |
| country | texto |
| phone | texto |

### Order (Pedido)
| Campo | Tipo |
|---|---|
| id | número entero |
| orderDate | fecha/hora |
| orderNumber | texto (ej: ORD-1001) |
| customerId | FK → Customer |
| totalAmount | decimal (calculado) |

### OrderItem (Ítem de pedido)
| Campo | Tipo |
|---|---|
| id | número entero |
| orderId | FK → Order |
| productId | FK → Product |
| unitPrice | decimal |
| quantity | entero |

### Product (Producto)
| Campo | Tipo |
|---|---|
| id | número entero |
| productName | texto |
| supplierId | FK → Supplier |
| unitPrice | decimal |
| package | texto (ej: "Caja x 500g") |
| isDiscontinued | booleano |

### Supplier (Proveedor)
| Campo | Tipo |
|---|---|
| id | número entero |
| companyName | texto |
| contactName | texto |
| contactTitle | texto |
| city | texto |
| country | texto |
| phone | texto |
| fax | texto (puede ser null) |

---

## Cálculo de totalAmount

```
totalAmount = Σ (item.unitPrice × item.quantity)  para todos los items del pedido
```

> ⚠️ Este valor debe recalcularse automáticamente cada vez que se agregue, modifique o elimine un item.
