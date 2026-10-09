import { useState } from 'react'

import './Catalog.css'
import { ProductCard } from './ProductCard/ProductCard'
import { OrderForm } from './OrderForm/OrderForm'

export function Catalog({ products }) {
  const [selectedProduct, setSelectedProduct] = useState(null)
  const [isOrderFormOpen, setIsOrderFormOpen] = useState(false)

  const handleOrder = (product) => {
    setSelectedProduct(product)
    setIsOrderFormOpen(true)
  }

  return (
    <section className="catalog" id="catalog">
      <div className="container">
        <div className="catalog__header">
          <span className="catalog__label">
            КАТАЛОГ
          </span>

          <h2 className="catalog__title">
            Игровые маршрутизаторы
          </h2>

          <p className="catalog__description">
            Выберите маршрутизатор под свои задачи
            и получите стабильное соединение
            во время игры.
          </p>
        </div>

        <div className="catalog__grid">
          {products.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
              onOrder={handleOrder}
            />
          ))}
        </div>

        {isOrderFormOpen && selectedProduct && (
          <OrderForm
            product={selectedProduct}
            onClose={() => setIsOrderFormOpen(false)}
          />
        )}
      </div>
    </section>
  )
}